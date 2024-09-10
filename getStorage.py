# -- coding: utf-8 --
# @Time : 2024/8/3 17:21
# @Author : Eagle Yin

import requests
import json
import pandas as pd

ess_ip = '10.79.48.14'
locationTypeCode = ["LT_SHELF_STORAGE", "LT_SHELF_STORAGE_RIGHT", "LT_SHELF_STORAGE_3",
                    "LT_SHELF_STORAGE_RIGHT_3", "LT_SHELF_STORAGE_5", "LT_SHELF_STORAGE_RIGHT_5",
                    "LT_MINI_KIVA_SHELF_STORAGE", "LT_MINI_KIVA_SHELF_STORAGE_RIGHT",
                    "LT_MINI_KIVA_SHELF_STORAGE_3", "LT_MINI_KIVA_SHELF_STORAGE_RIGHT_3",
                    "LT_MINI_KIVA_SHELF_STORAGE_5", "LT_MINI_KIVA_SHELF_STORAGE_RIGHT_5"]

column_names = ["1-1", "1-2", "3-1", "3-2", "5-1", "5-2", "1-1缓存位", "1-2缓存位", "3-1缓存位", "3-2缓存位", "5-1缓存位",
                "5-2缓存位"]


def get_total_locations(url, payload, label):
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload).json()
    return response["data"]["total"], label


def calculate_ratio(type_code):
    url = f"http://{ess_ip}:9003/adapter-api/monitor/location/query"

    payload_A = json.dumps({
        "page": 1, "size": 20, "locationTypeCode": type_code, "isShelfStorage": True
    })
    payload_B = json.dumps({
        "page": 1, "size": 20, "locationTypeCode": type_code, "isEmpty": False, "isShelfStorage": True
    })

    total_A_details = get_total_locations(url, payload_A, "库位总数")
    total_B_details = get_total_locations(url, payload_B, "占用库位数")

    if total_A_details[0] > 0:
        ratio = total_B_details[0] / total_A_details[0]
    else:
        ratio = None

    return total_A_details, total_B_details, ratio


ratios = {}
data = []

for type_code, column_name in zip(locationTypeCode, column_names):
    total_A, total_B, ratio = calculate_ratio(type_code)
    ratios[column_name] = ratio
    data.append([column_name, total_A[0], total_B[0], ratio])

preferred_order = ["1-1", "1-2", "3-1", "3-2", "5-1", "5-2", "1-1缓存位", "1-2缓存位", "3-1缓存位", "3-2缓存位", "5-1缓存位",
                   "5-2缓存位"]

def avg():
    # 计算各仓库容平均值
    avg1 = (data[0][2]+data[1][2])/(data[0][1]+data[1][1])
    data[0].append(avg1)
    avg2 = (data[2][2]+data[3][2])/(data[2][1]+data[3][1])
    data[2].append(avg2)
    avg3 = (data[4][2]+data[5][2])/(data[4][1]+data[5][1])
    data[4].append(avg3)
    return data

data_new = avg()
df = pd.DataFrame(data_new, columns=["库区", "库位总数", "占用库位数", "库容","平均值"])
df['库容'] = df['库容'].apply(lambda x: '{:.2%}'.format(x) if x else None)
df['平均值'] = df['平均值'].apply(lambda x: '{:.2%}'.format(x) if pd.notna(x)  else None)
df.to_excel('D:\project\--xiongge\Result\storage.xlsx', index=False)