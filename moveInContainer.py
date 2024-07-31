# -- coding: utf-8 --
# @Time : 2023/5/31 9:53
# @Author : Eagle Yin
import requests
import json
import xlrd
# 容器移入
moveInContainers_url = 'http://192.168.29.128:9000/ess-api/container/moveIn'
# 查询库位信息的接口
queryPosition_url = 'http://192.168.29.128:9003/ess-api/monitor/location/query'
# 查询容器
queryContainers_url = 'http://192.168.29.128:9000/container/query'
# 查询所有容器的接口
queryLocation_url = 'http://192.168.29.128:9000/model/queryModelByType?modelType=location'
# 查询所有位置的接口
queryContainer_url = 'http://192.168.29.128:9000/model/queryModelByType?modelType=container'
# 请求头
headers = {'Content-Type': 'application/json', 'accept': 'application/json'}

# 查询空闲库位
def getPositionWithLayer(num):
    positionCode = []
    response = requests.get(queryLocation_url, headers=headers)
    result = response.json()
    locations = result.get('data').get('location')
    for location in locations:
        locationTypeCode = location.get('locationTypeCode')
        if locationTypeCode == 'LT_SHELF_STORAGE' or locationTypeCode == 'HIGH_SHELF_STORAGE':
            code = location.get('code')
            # print(int(code[-2:]))
            if num[0] <= int(code[-2:]) <= num[1]:
                print(num[1])
                positionCode.append(code)
            else:
                continue
        else:
            continue
    return positionCode

# 查询空闲容器
def getContainer():
    containerCode = []
    response = requests.get(queryContainer_url, headers=headers)
    result = response.json()
    containers = result.get('data').get('container')
    for container in containers:
        containerTypeCode = container.get('containerTypeCode')
        isInside = container.get('isInside')
        if containerTypeCode == 'CT_KUBOT_STANDARD' and isInside == False:
            code = container.get('code')
            containerCode.append(code)
        else:
            continue
    return containerCode


def moveIn(container,positionCode):
    data = []
    for containerCode, positionCode in zip(container, positionCode):
        data.append({'containerCode': containerCode, 'positionCode': positionCode})
    for i in range(len(data)):
        a = {
            "containerMoveIns": [
                {
                    "containerCode": data[i]["containerCode"],
                    "positionCode": data[i]["positionCode"]
                }
            ]
        }
        r = json.dumps(a)
        r1 = requests.post(moveInContainers_url, headers=headers, data=r)
        print(r1.json())

if __name__ == '__main__':
    # 禁用/释放的层数或者货架范围，调用的方法不同，上面方法都有注解
    num = [1,2]
    # positionCode = getPositionWithStorge(num)
    positionCode = getPositionWithLayer(num)
    container = getContainer()
    moveIn(container, positionCode)

