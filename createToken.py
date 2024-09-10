# -- coding: utf-8 --
# @Time : 2024/8/5 10:56
# @Author : Eagle Yin
import hashlib
import time


def build_token(device_code, timestamp):
    # 拼接字符串，其中"F5vEkyHwqJY0dZxn"是密钥
    concatenated_string = device_code + str(timestamp) + "F5vEkyHwqJY0dZxn"
    # 使用hashlib库的md5()函数生成MD5对象
    md5_object = hashlib.md5(concatenated_string.encode('utf-8'))
    # 生成十六进制表示的哈希值
    token = md5_object.hexdigest()
    return token


if __name__ == "__main__":
    # 获取当前时间戳
    timestamp = int(time.time() * 1000)  # 转换为毫秒
    device_code = "wwsSafe"
    token = build_token(device_code, timestamp)
    print(timestamp)
    print(token)