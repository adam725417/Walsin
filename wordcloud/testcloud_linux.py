import re
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import time 
import datetime
import csv
import pandas as pd
from bs4 import BeautifulSoup
import sqlalchemy
from sqlalchemy import create_engine
import happybase
import json
import pprint

def get_mysql(get_tbname,column):
    DB_USER='bdcsd_admin'
    DB_PASS='W@lsinData2018'
    DB_HOST='10.190.254.109'
    DB_PORT=13306
    DATABASE='BDCSD'
    # 1. 用sqlalchemy構建數據庫链接engine
    connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)  #1
    engine = create_engine(connect_info)

    sql_cmd = "SELECT {} FROM {}".format(column,get_tbname)
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


def get_mssql(get_tbname,column):
    # 寫進database
    DB_USER='bigdata'
    DB_PASS='bigdata'
    DB_HOST='10.190.254.13'
    DB_PORT=1433
    DATABASE='BIDATA'
    # 1. 用sqlalchemy构建数据库链接engine
    connect_info = 'mssql+pymssql://{}:{}@{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DATABASE)  #1
    engine = create_engine(connect_info)

    sql_cmd = "SELECT {} FROM {}".format(column,get_tbname)

    df = pd.read_sql(sql=sql_cmd, con=engine)
    return df

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

def get_searchlog(hostname):
    
    local_time = time.strftime("%m_%d", time.localtime())

    table_name = 'IKM_SEARCH_LOG'
    column_family = 'info'
    row_key = 'row_test'

    if hostname == '10.190.254.117':
        conn = happybase.Connection(hostname)

        store_file = {}
        json_output = []

        table = conn.table(table_name)
        for key, data in table.scan(row_start='001277b9ba354f3d8d14724534835b69'):
            

            try:
                store_file['SEARCH_KEYWORD'] = data[b'0:SEARCH_KEYWORD'].decode("utf-8")
            except:
                store_file['SEARCH_KEYWORD'] = "NaN"

            
            json_output.append(store_file.copy())
        # pprint.pprint(json_output)
        df = pd.DataFrame(list(json_output))
        return df



    
if __name__ == '__main__':
    #DB相關
#     get_tbname='ikm_wordcloud_list'#table名稱
#     column='list'#
    try:
        hostname = '10.190.254.117'
    

        #網頁帳密
        web_userid = "iju_cheng@walsin.com"
        web_password = "walsin123"
        #網頁檔案名稱
        web_filename = "test1003"

        chrome_options = webdriver.ChromeOptions()
        #開啟無頭模式，想打開模擬瀏覽器就隱藏掉
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(chrome_options=chrome_options)

        #登入網頁
        driver.get("https://wordart.com/login?next=/my-artwork")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys('{}'.format(web_userid))#帳號
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys('{}'.format(web_password))#密碼
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Forgot password?'])[1]/following::button[1]").click()
        #選擇My artwork 的name
        driver.find_element_by_link_text('{}'.format(web_filename)).click()
        time.sleep(50)
        #選擇第二個視窗
        driver.switch_to_window(driver.window_handles[1])
        # for handle in driver.window_handles:
        #     driver.switch_to.window(handle)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Words table will be cleared without the ability to restore'])[1]/following::button[1]").click()
        #進入import頁面
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Words'])[1]/following::button[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='paste text from Excel'])[1]/following::textarea[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='paste text from Excel'])[1]/following::textarea[1]").clear()
        #從DB匯入文字
        ###############################################################################################################
        df = get_searchlog(hostname)

        total_text=[]
        total_str = ""
        df = get_searchlog(hostname)

        top_keyword = df['SEARCH_KEYWORD'].value_counts()
        top_keyword = top_keyword[0:60]
        top_keyword = top_keyword.rename_axis('keyword').reset_index(name='counts')
        top_keyword['sep'] = ";"
        top_keyword['merge'] = top_keyword['keyword'].map(str)+top_keyword['sep']+top_keyword['counts'].map(str)
        top_keyword_str = top_keyword['merge'].to_string(index=False)

        L = top_keyword_str.split('\n')
        df1 = pd.DataFrame({'keyword': L})

        df1['sep'] = ";;;"
        df1['str'] = "Noto Sans CJK TC Black;"

        df1['final_str']=df1['keyword']+df1['sep']+df1['str']
        for i in df1['final_str']:
            total_text.append(i.strip())
            total_text.append("\n")
        final_str = total_str.join(total_text)
        ###############################################################################################################
        #輸入文字
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='paste text from Excel'])[1]/following::textarea[1]").send_keys("{}".format(final_str))
        time.sleep(2)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Stemming'])[1]/following::div[1]").click()
        #勾選CSV format
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CSV format'])[1]/following::button[1]").click()
        time.sleep(2)
        #進入words option
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Down'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='None'])[2]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Pattern'])[2]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Pattern'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Open links in new window'])[1]/following::button[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='C'])[3]/following::button[1]").click()
        time.sleep(6)
        driver.find_element_by_css_selector("svg.icons-icon").click()
        print("complete")
        time.sleep(60)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Your word art has been successfully saved'])[1]/following::button[1]").click()
        driver.quit()
    except BaseException:
        log_df = pd.DataFrame(columns=['date','errormsg'])
        log_df['date'] = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
        log_df['errormsg'] = 'got error'
        to_mssql(log_df,get_tbname='cloud_log',mode='append')
    else:
        print("complete")