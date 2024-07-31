# -- coding: utf-8 --
# @Time : 2024/6/17 14:07
# @Author : Eagle Yin
'''tasks = [
    {'id': 1, 'name': '任务1', 'status': '进行中'},
    {'id': 2, 'name': '任务2', 'status': '完成'},
    {'id': 3, 'name': '任务3', 'status': '进行中'},
    {'id': 4, 'name': '任务4', 'status': '完成'},
]

completed_tasks = [task for task in tasks if task['status'] == '完成']

print(completed_tasks)


def filter_completed_orders(orders):
    # 假设每个订单都有一个'status'字段表示订单状态，'COMPLETED'表示已完成
    return [order for order in orders if order['status'] == 'COMPLETED']


def paginate_orders(orders, page, per_page):
    # 先过滤出已完成的订单
    completed_orders = filter_completed_orders(orders)
    print(completed_orders)

    # 计算总页数
    total_pages = (len(completed_orders) + per_page - 1) // per_page
    print(total_pages)

    # 检查请求的页码是否有效
    if page < 1 or page > total_pages:
        return None, None  # 或者抛出一个错误

    # 计算偏移量
    offset = (page - 1) * per_page
    # print(offset)

    # 获取当前页的数据
    page_data = completed_orders[offset:offset + per_page]
    print(page_data)
    return page_data, total_pages


# 示例订单列表（包含已完成和未完成的订单）
orders = [
    {'id': 1, 'name': 'Order 1', 'status': 'COMPLETED'},
    {'id': 2, 'name': 'Order 2', 'status': 'COMPLETED'},
    {'id': 3, 'name': 'Order 3', 'status': 'COMPLETED'},
    {'id': 4, 'name': 'Order 4', 'status': 'COMPLETED'},
    {'id': 5, 'name': 'Order 5', 'status': 'COMPLETED'},
    {'id': 6, 'name': 'Order 6', 'status': 'COMPLETED'},
    {'id': 7, 'name': 'Order 7', 'status': 'COMPLETED'},
    {'id': 8, 'name': 'Order 8', 'status': 'PENDING'},
    {'id': 9, 'name': 'Order 9', 'status': 'PENDING'},
    {'id': 10, 'name': 'Order 10', 'status': 'PENDING'},
    {'id': 11, 'name': 'Order 11', 'status': 'PENDING'},
    {'id': 12, 'name': 'Order 12', 'status': 'PENDING'},
    {'id': 13, 'name': 'Order 13', 'status': 'PENDING'}
]

# 查询第2页，每页20条已完成的任务
page = 2
per_page = 5

page_data, total_pages = paginate_orders(orders, page, per_page)

# 输出结果
for order in page_data:
    print(order)
print(f"Total pages: {total_pages}")'''


import subprocess
exe_path = 'D:\work\test\mock_conveyor\testpy'
subprocess.run(exe_path)




