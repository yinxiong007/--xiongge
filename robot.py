# -*- coding:utf-8 -*-
# Time: 2024/5/20 13:52
# Author:七月
import requests
import json

# 服务器url和端口
host_data = '172.20.110.135:9000'


def create_kubot():
    # 机器人数量
    robot_num = 1
    # 背篓数量
    tray_num = 2
    # 从几号机器人开始
    n = 94
    # 机器人类型"RT_KUBOT_RIGHT"RT_KUBOT"
    robotTypeCode = "RT_KUBOT_RIGHT"

    header = {"Content-Type": "application/json"}
    updateModelNotSafe_url = "http://{}/model/updateModelNotSafe".format(host_data)
    trayNormal = {}

    for i in range(tray_num):
        trayNormal[i] = "true"
    trayNormal[64] = "true"

    for j in range(n, n + robot_num):
        data = ({
            "id": "0",
            "code": "",
            "updated": "0",
            "robot": {
                "id": "0",
                "code": "kubot-%s" % j,
                "robotTypeCode": robotTypeCode,
                "trayNormal": trayNormal,
                "state": "UNAVAILABLE",
                "mode": "AUTO",
                "paused": "false",
                "zone": "5",
                "energyLevel": 0,
                "hardwareState": "ROBOT_READY_TO_INIT",
                "isCharging": "false",
                "robot2mapTheta": "0",
                "fork2robotTheta": "0",
                "lockedStatePointCode": [],
                "trayNumToState": {},
                "unfinishedTransportTaskCode": {},
                "assignedTransportTaskCode": [],
                "trayLoadingContainerCode": {},
                "jsonOfLastCommandWhichToOperatingContainer": "",
                "belongLocationCode": "",
                "needHumanTellForkState": "false"
            }
        })

        # 执行请求
        response = requests.post(url=updateModelNotSafe_url, headers=header, data=json.dumps(data))
        # 按照json格式打印请求体
        print(json.dumps(data, indent=4, separators=(', ', ': '), ensure_ascii=False))
        # 打印路径
        print("请求路径为：", response.url)
        # 打印返回信息
        print("添加容器请求返回为：", response.text)
        print()


def create_kiva():
    # 机器人数量
    robot_num = 1
    # 背篓数量
    tray_num = 0
    # 从几号机器人开始
    n = 393

    robotTypeCode = "RT_KUBOT_MINI_KIVA"

    header = {"Content-Type": "application/json"}
    updateModelNotSafe_url = "http://{}/model/updateModelNotSafe".format(host_data)
    trayNormal = {}

    for i in range(tray_num):
        trayNormal[i] = "true"
    trayNormal[64] = "true"

    for j in range(n, n + robot_num):
        data = ({
            "id": "0",
            "code": "",
            "updated": "0",
            "robot": {
                "id": "0",
                "code": "kubot-%s" % j,
                "robotTypeCode": robotTypeCode,
                "trayNormal": trayNormal,
                "state": "IDLE",
                "mode": "AUTO",
                "paused": "false",
                "zone": "5",
                "energyLevel": 85,
                "hardwareState": "ROBOT_IDLE",
                "isCharging": "false",
                "precisePosition": {
                    "x": "648257",
                    "y": "59881",
                    "z": "0"
                },
                "robot2mapTheta": "270",
                "fork2robotTheta": "0",
                "lockedStatePointCode": ["POINT:648727:59881@5#270"],
                "trayNumToState": {},
                "unfinishedTransportTaskCode": {},
                "assignedTransportTaskCode": [],
                "trayLoadingContainerCode": {},
                "jsonOfLastCommandWhichToOperatingContainer": "",
                "belongLocationCode": "",
                "needHumanTellForkState": "false"
            }
        })

        # 执行请求
        response = requests.post(url=updateModelNotSafe_url, headers=header, data=json.dumps(data))
        # 按照json格式打印请求体
        print(json.dumps(data, indent=4, separators=(', ', ': '), ensure_ascii=False))
        # 打印路径
        print("请求路径为：", response.url)
        # 打印返回信息
        print("添加容器请求返回为：", response.text)
        print()


# create_kubot()
create_kiva()