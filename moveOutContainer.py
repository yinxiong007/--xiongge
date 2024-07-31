# -- coding: utf-8 --
# @Time : 2023/6/19 18:15
# @Author : Eagle Yin
import requests
import json
import xlrd
# 容器移出接口
moveOutContainers_url = 'http://192.168.29.128:9000/ess-api/container/moveOut'
# 查询库位信息的接口
queryPosition_url = 'http://192.168.29.128:9003/ess-api/monitor/location/query'
# 查询容器
queryContainers_url = 'http://192.168.29.128:9000/container/query'
# 查询所有位置的接口
queryLocation_url = 'http://192.168.29.128:9000/model/queryModelByType?modelType=location'
# 请求头
headers = {'Content-Type': 'application/json', 'accept': 'application/json'}

# 查询所有占用库位
'''def getlocationCodes():
    locationCode = []
    loc = []
    # b = {"page":1,"size":20,"isEmpty":False,"isShelfStorage":True}
    # r = json.dumps(b)
    response = requests.get(queryLocation_url,headers=headers)
    data = response.json().get('data')
    locations = data.get('location')
    for a in locations:
        locationTypeCode = a.get('locationTypeCode')
        containerCode = a.get('containerCode')
        if  locationTypeCode == 'LT_SHELF_STORAGE' and containerCode != '':
            code = a.get('code')
            containerCode = a.get('containerCode')
            # 创建库位对象（也可以使用字典）
            new_loction = {'code': code, 'containerCode': containerCode}
            # 将容器添加到库位列表中
            locationCode.append(new_loction)

    return locationCode

# 批量移出容器
def moveOut(c):
    for i in range(len(c)):
        _data = {
                "containerMoveOuts": [
                    {
                        "containerCode": c[i]["containerCode"],
                        "positionCode": c[i]["code"]
                    }
                ]
            }
        data = json.dumps(_data)
        print(data)
        response = requests.post(url=moveOutContainers_url, headers=headers, data=data)
        print(response.json())


if __name__ == '__main__':
    c = getlocationCodes()
    print(c)
    moveOut(c)'''



# 查询所有占用库位
def getlocationCodes(b):
    locationCode = []
    for i in range(len(b)):
        d = b[i]
        r = json.dumps(d)
        response = requests.post(queryPosition_url, headers=headers, data=r)
        print(response.json())
        locations = response.json().get('data').get('locations')
        # print(locations)
        for a in locations:
            code = a.get('code')
            containerCode = a.get('containerCode')
            # 创建库位对象（也可以使用字典）
            new_loction = {'code': code, 'containerCode': containerCode}
            # 将容器添加到库位列表中
            locationCode.append(new_loction)
    return locationCode

# 批量移出容器
def moveOut(c):
    for i in range(len(c)):
        _data = {
                "containerMoveOuts": [
                    {
                        "containerCode": c[i]["containerCode"],
                        "positionCode": c[i]["code"]
                    }
                ]
            }
        data = json.dumps(_data)
        response = requests.post(url=moveOutContainers_url, headers=headers, data=data)
        print(response.json())

# 翻页列表
def page(i):
    pageList = []
    for page in range(i):
        b = {"page":page+1,"size":10,"isEmpty":False,"isShelfStorage":True}
        pageList.append(b)
    return pageList


if __name__ == '__main__':
    b = page(2)
    print(b)
    c = getlocationCodes(b)
    print(c)
    moveOut(c)