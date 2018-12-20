import happybase
import json
import pandas as pd
import pprint
import ast
import re
import util
import numpy as np
from math import sqrt
import sqlalchemy
import numpy as np
import hashlib
import time
import datetime
from sqlalchemy import create_engine

### 推薦關鍵字數量
KeywordNum = 13
### hbase抓searchlog
hostname = '10.190.254.117'
table_name = 'IKM_SEARCH_LOG'
column_family = 'info'
row_key = 'row_test'

conn = happybase.Connection(hostname)

store_file = {}
json_output = []

table = conn.table(table_name)
for key, data in table.scan(row_start='00d75178ac834462a015cfa7ec49a932'): 
    store_file['Key'] = key.decode("utf-8")
    try:
        store_file['USER_ID'] = data[b'0:USER_ID'].decode("utf-8")
    except:
        store_file['USER_ID'] = "NaNA"

    try:
        convert_SEARCH_COST_TIME = util.convert_search_cost_time(data[b'0:SEARCH_COST_TIME'])
        store_file['SEARCH_COST_TIME'] = convert_SEARCH_COST_TIME
        # store_file['SEARCH_COST_TIME'] = data[b'0:SEARCH_COST_TIME']
    except:
        store_file['SEARCH_COST_TIME'] = "NaN"

    try:
        convert_SEARCH_COUNT = util.convert_search_count(data[b'0:SEARCH_COUNT'])
        store_file['SEARCH_COUNT'] = convert_SEARCH_COUNT
        # store_file['SEARCH_COUNT'] = data[b'0:SEARCH_COUNT']
    except:
        store_file['SEARCH_COUNT'] = "NaN"

    try:
        store_file['SEARCH_KEYWORD'] = data[b'0:SEARCH_KEYWORD'].decode("utf-8")
    except:
        store_file['SEARCH_KEYWORD'] = "NaN"

    try:
        convert_SEARCH_DATE = util.convert_date(data[b'0:SEARCH_DATE'])
        store_file['SEARCH_DATE'] = convert_SEARCH_DATE
    except:
        store_file['SEARCH_DATE'] = "NaN"
    
    try:
        convert_SYSUPDATE_DATE = util.convert_date(data[b'0:SYSUPDATE_DATE'])
        store_file['SYSUPDATE_DATE'] = convert_SYSUPDATE_DATE
    except:
        store_file['SYSUPDATE_DATE'] = "NaN"

    try:
        store_file['SEARCH_ACTION'] = data[b'0:SEARCH_ACTION'].decode("utf-8")
    except:
        store_file['SEARCH_ACTION'] = "NaN"
    json_output.append(store_file.copy())
# pprint.pprint(json_output)


###  Nosql抓hr_sel
def get_nosql(get_tbname,search_category):
    # 寫進database
    DB_USER='ikmap'
    DB_PASS='ikmap'
    DB_HOST='10.190.254.13'
    DB_PORT=1433
    DATABASE='IKM'
    # 1. 用sqlalchemy构建数据库链接engine
    connect_info = 'mssql+pymssql://{}:{}@{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DATABASE)  #1
    engine = create_engine(connect_info)


    if search_category is None:
        sql_cmd = "SELECT * FROM {}".format(get_tbname)
    else:
        sql_cmd = """
            SELECT * 
            FROM {} 
            WHERE category LIKE '%%{}%%';
            """.format(get_tbname,search_category)

    df = pd.read_sql(sql=sql_cmd, con=engine)
    return df

def to_mysql(df,get_tbname,mode):
    #寫進sqlserverdatabase
    DB_USER='cost_driver_admin'
    DB_PASS='1234'
    DB_HOST='10.190.254.109'
    DB_PORT=13306
    DATABASE='cost_driver'
    # 1. 用sqlalchemy構建數據庫链接engine
    connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)  #1
    engine = create_engine(connect_info)

    #寫進SQL
    df.to_sql(name='{}'.format(get_tbname),
        con=engine, 
        if_exists=mode,
        index=True,
        )

def to_mssql(df,get_tbname,mode):
    #寫進sqlserverdatabase
    DB_USER='ikmap'
    DB_PASS='ikmap'
    DB_HOST='10.190.254.13'
    DB_PORT=1433
    DATABASE='IKM'
    # 1. 用sqlalchemy构建数据库链接engine
    connect_info = 'mssql+pymssql://{}:{}@{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DATABASE)  #1
    engine = create_engine(connect_info)

    #寫進SQL
    df.to_sql(name='{}'.format(get_tbname), 
        con=engine, 
        if_exists=mode,
        index=False,
        dtype={col_name: sqlalchemy.types.NVARCHAR(length=255) for col_name in df}
        )

def to_logtable(df):
    last_date = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())

        
    log_content = df[['UPDATE_DATE','KEY','LOCNAM','LOCACOD','SEARCH_KEYWORD','TIMES']].to_json(orient='values',force_ascii=False)
    
    log_df = pd.DataFrame(data={'updatedate': [last_date], 'updatelog': [log_content]})
    to_mysql(log_df,get_tbname='LOG_ikm_loc_search_keyword1',mode='replace')

def sim_distance(prefs,person1,person2):
  # Get the list of shared_items
  si={}
  for item in prefs[person1]: 
    if item in prefs[person2]: si[item]=1

  # if they have no ratings in common, return 0
  if len(si)==0: return 0

  # Add up the squares of all the differences
  sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) 
                      for item in prefs[person1] if item in prefs[person2]])

  return 1/(1+sum_of_squares)

# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
  # Get the list of mutually rated items
  si={}
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)

  # Sums of all the preferences
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])

  # Sums of the squares
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])   

  # Sum of the products
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r

def sim_adjcos(prefs,p1,p2):

    si={}
    for item in prefs[p1]: 
      if item in prefs[p2]: si[item]=1
    # if they are no ratings in common, return 0
    if len(si)==0: return 0

    prefs = transformPrefs(prefs)
    si = {}
    for (key, ratings) in prefs.items():
        si[key] = (float(sum(ratings.values())) / len(ratings.values()))
    num = 0 # 分子
    dem1 = 0 # 分母的第一部分
    dem2 = 0
    for (user, ratings) in prefs.items():
        if p1 in ratings and p2 in ratings:
            avg = si[user]
            num += (ratings[p1] - avg) * (ratings[p2] - avg)
            dem1 += (ratings[p1] - avg) ** 2
            dem2 += (ratings[p2] - avg) ** 2
    return num / ((sqrt(dem1) * sqrt(dem2))+0.000000000000001)


def topMatches(prefs,person,n=5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other) 
                  for other in prefs if other!=person]
  scores.sort()
  scores.reverse()
  return scores[0:n]

def getRecommendations(prefs,person,similarity=sim_pearson):
  totals={} #与指定人(person)的相似度 x 对person未看过电影的评分（加权值）。所有人的总和
  simSums={}  #所有人的相似度（是对该电影有过评价且对person来说未看过的人）
  for other in prefs:
    # don't compare me to myself
    if other==person: continue #肯定不和自己比较
    sim=similarity(prefs,person,other) #返回的是与此人的相似度

    # ignore scores of zero or lower
    if sim<=0: continue
    for item in prefs[other]:

      # only score movies I haven't seen yet
      if item not in prefs[person] or prefs[person][item]==0:
        # Similarity * Score
        totals.setdefault(item,0) #该方法是Dictionary方法，若键key不存在于此Dictionary中，将会添加该键到Dictionary中，并设默认值（0）
        totals[item]+=prefs[other][item]*sim
        # Sum of similarities
        simSums.setdefault(item,0)
        simSums[item]+=sim

  # Create the normalized list
  rankings=[(total/simSums[item],item) for item,total in totals.items()]

  # Return the sorted list
  rankings.sort()
  rankings.reverse()
  return rankings

def transformPrefs(prefs):
  result={}
  for person in prefs:
    for item in prefs[person]:
      result.setdefault(item,{})

      # Flip item and person
      result[item][person]=prefs[person][item]
  return result

### MD5
def hash(data):
    m = hashlib.md5()
    # 先將資料編碼，再更新 MD5 雜湊值
    m.update(data.encode("utf-8"))
    h = m.hexdigest()
    return h
#欄位排序(ikm searchlog)
df_search = pd.DataFrame(list(json_output)) 
col=['Key','SEARCH_COST_TIME','SEARCH_COUNT','USER_ID','SEARCH_KEYWORD','SEARCH_DATE','SYSUPDATE_DATE','SEARCH_ACTION']
df2 = df_search[col]
df2.info()
### 與HR資料串起來
HR =  get_nosql(get_tbname='ikm_hr',search_category=None)
HR.rename(columns={ 'EMPID': "USER_ID" }, inplace=True)
df = df2.join(HR.set_index('USER_ID'), on='USER_ID')
## 從HR_sel檔將'user_id'的資料串起來
# HR = pd.read_csv(r'C:\Users\ur07154\Desktop\Python程式\iKM\hr_sel.csv')
# df = df.join(HR.set_index('USER_ID'), on='USER_ID')
# df.to_excel(r'C:\Users\ur07154\Desktop\CFNewData.xlsx')
# print(df.head())


# 1. 直接對df1推薦df2項目
df1 = 'LOCNAM'
# df1 = 'USER_ID'
# df1 = 'USER_ID'
df2 = 'SEARCH_KEYWORD'
#CF輸入自動化
#讀取欄位
cols = [df1,df2]
df = df[cols]
## 2. 對特定df3內的df1推薦df2
# df1 = 'USER_ID'
# df2 = 'SEARCH_KEYWORD'
# df3 = 'BU'
# cols = [df1,df2,df3]
# df = df[cols]
# df = df.loc[df['BU'] == '資訊中心']

## 3. 以各部門為單位，將所有USER合併為新的欄位'COSTNAM_USER'(增加資料量減少冷啟動問題)
# df1 = 'COSTNAM'
# df2 = 'search_keyword'
# cols = [df1,df2]
# df = df[cols]

## 
df = df.dropna()
# df = df.loc[df['search_keyword']=='304']

L1=df[df1]
L2=df[df2] 
##依照df1做排序
LIST_df1  = (list(set(L1)))
LIST_df1 = sorted(LIST_df1)
##依照df2做排序
LIST_df2  = (list(set(L2)))
LIST_df2 = sorted(LIST_df2)
#
# LIST_df3  = (list(set(L3)))
# LIST_df3 = sorted(LIST_df1)
# for costnam in LIST_df3
#     df.loc[df['COSTNAM']== costnam ,'User2Costnam'] = '0'
#For迴圈自動生成字典
dict_DOC = dict()
for user in LIST_df1:
    dict_DOC_New = {user:df.loc[df[df1] == user, df2].value_counts().to_dict()}
    dict_DOC = dict(dict_DOC, **dict_DOC_New)
USERID = dict_DOC
# print (USERID)
# print ('')

### 將字典轉成Dataframe型態(網狀row關鍵字、column廠區)
# df_UserID = pd.DataFrame.from_dict(USERID)
# # df_UserID = pd.DataFrame.from_dict(USERID, orient='index')
# print (df_UserID)
# df_UserID.to_excel(r"C:\Users\ur07154\Desktop\Python程式\CollaborativeFilttering\字典轉DF\Search_keyword_locnam.xlsx")

### 

# df_CS = USERID['常熟華新一廠']
# df_CS = pd.DataFrame(list(df_CS.items()))
# # print (len(df_CS))
# df_CS['locnam']='常熟華新一廠'
# df_CS['LOCACOD_V']='CS'

### 將字典轉成Dataframe型態(長資料三個欄位廠區、關鍵字、次數)
loc_df = pd.DataFrame()
loc_list = list(USERID.keys())
for ii in loc_list:
    df_new = USERID[ii]
    df_new = pd.DataFrame(list(df_new.items()))
    df_new['LOCNAM']=ii
    loc_df = loc_df.append([df_new])

### 更改欄位名稱
loc_df.rename(columns={ loc_df.columns[0]: "SEARCH_KEYWORD" }, inplace=True)
loc_df.rename(columns={ loc_df.columns[1]: "TIMES" }, inplace=True)

### 將未滿13個關鍵字的廠區補滿(用所有廠區次數最高的關鍵字)

for jj in list(USERID.keys()):
    if len(loc_df.loc[loc_df['LOCNAM']==jj]) < KeywordNum:
        lost = loc_df.loc[loc_df['LOCNAM']==jj]
        dd = loc_df.sort_values(by = "TIMES",ascending=False).head(KeywordNum-len(loc_df.loc[loc_df['LOCNAM']==jj]))
        dd["LOCNAM"] = jj
        dd['TIMES'] = int(1)
        loc_df = loc_df.append(dd)

# print (loc_df.loc[loc_df["LOCNAM"]=='常熟華新一廠'])

df_topKeywordNum = pd.DataFrame()
for kk in loc_list:
    df_topKeywordNum_new = loc_df.loc[loc_df['LOCNAM']==kk].sort_values(by = "TIMES",ascending=False).head(KeywordNum)
    df_topKeywordNum = df_topKeywordNum.append(df_topKeywordNum_new)
loc_df = df_topKeywordNum

loc_df['KEY'] = loc_df['LOCNAM']+loc_df["SEARCH_KEYWORD"]
loc_df["KEY"] = loc_df['KEY'].apply(lambda x: hash(x))
loc_df["UPDATE_DATE"]= datetime.date.today().strftime('%Y-%m-%d')

cols_HR2 = ['LOCNAM','LOCACOD']
HR2 = HR[cols_HR2]
HR2.drop_duplicates('LOCNAM',keep='first', inplace=True)
loc_df = loc_df.join(HR2.set_index('LOCNAM'), on='LOCNAM')
loc_df = loc_df[['KEY','LOCNAM','LOCACOD','SEARCH_KEYWORD','TIMES','UPDATE_DATE']]
print (loc_df)

# loc_df.to_excel(r"C:\Users\ur07154\Desktop\Python程式\CollaborativeFilttering\字典轉DF\自動化測試.xlsx",index=False)
to_mssql(loc_df,get_tbname='ikm_loc_search_keyword',mode = 'replace')
to_mssql(loc_df,get_tbname='ikm_loc_search_keyword_log',mode = 'append')