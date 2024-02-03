import ship_class
import ocean_class
import numpy as np
import time
import pandas as pd


# 模拟次数
num_simulations = 2

# 存储每次模拟的结果
results = []

my_ship = ship_class.Ship()


for _ in range(num_simulations):
    # 记录一次模拟的开始时间
    start_time = time.time()
    move_time = 0
    while True:
        my_ship.move(0.1)
        move_time += 0.1
        # print(move_time)
        if move_time > 86400:
            # 记录结束时间
            results.append(my_ship.get_position())
            end_time = time.time()
            print("船的位置：", my_ship.get_position(),"\t运行时间：",end_time - start_time)
            # print(time)
            break

# 创建一个DataFrame对象
df = pd.DataFrame(results, columns=['Column1', 'Column2', 'Column3'])
# 将DataFrame写入Excel文件
df.to_excel('output.xlsx', index=False)
print(results)