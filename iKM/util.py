
import pandas as pd
import ast
import re
import struct
import jieba


def pandas_convert_date(dfi):
    convert=[]
    for date in dfi:
        try:
            k = int(date,16)
            result_ms=pd.to_datetime(k,unit='ms')
            a = str(result_ms)
            convert.append(a)
        except:
            convert.append("NaN")
    org = list(dfi)
    dfi.replace(org,convert,inplace=True)


def convert_date(table_data):
    bytes_to_hex = table_data.replace(b'\x80',b'\x00').hex()
    hex_to_int = int(bytes_to_hex,16)
    result_ms=pd.to_datetime(hex_to_int,unit='ms')
    string_datetime = str(result_ms)
    return string_datetime

def convert_row_num(table_data):
    bytes_to_hex = table_data.replace(b'\x80',b'\x00').hex()
    hex_to_int = int(bytes_to_hex,16)
    return hex_to_int

def convert_page(table_data):
    bytes_to_hex = table_data.replace(b'\x80',b'\x00').hex()
    hex_to_int = int(bytes_to_hex,16)
    return hex_to_int

def convert_search_cost_time(table_data):
    bytes_to_hex = table_data.replace(b'\x80',b'\x00').hex()
    hex_to_int = int(bytes_to_hex,16)
    return hex_to_int

def convert_search_count(table_data):
    bytes_to_hex = table_data.replace(b'\x80',b'\x00').hex()
    hex_to_int = int(bytes_to_hex,16)
    return hex_to_int

def convert_solr_score(table_data):
    #unpack出來的類型是tuple
    data_unpack = struct.unpack(">1f",table_data)
    #提取tuple裡的值並取絕對值
    abs_score = abs(data_unpack[0])
    return abs_score

#LDA
def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()
