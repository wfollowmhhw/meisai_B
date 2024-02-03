import ship_class
import pandas as pd
from tqdm import tqdm

nums = 3

# 存储每次模拟的结果
results1_rock = []
results1_sand = []

for i in tqdm(range(nums), desc="Processing1", unit="iteration"):
    # 记录一次模拟的开始时间
    my_ship1 = ship_class.Ship(0,0,100,50,102857,100)
    # start_time = time.time()
    move_time = 0
    check = 1
    while True:
        my_ship1.move(0.1)
        move_time += 0.1
        # print(move_time)
        # print(my_ship1.get_position())
        if my_ship1.check_go_to_surface():
            my_ship1.change_on_surface()
            move_time += 0.1
        if my_ship1.check_go_to_ground():
            if check:
                position_data = my_ship1.get_position()
                results1_sand.append([*position_data,"stop",move_time])
                check = 0
            my_ship1.change_on_ground()
            my_ship1.move(0.1)
            move_time += 0.1
        if my_ship1.check_stop():
            position_data = my_ship1.get_position()
            results1_rock.append([*position_data , "stop",move_time])
            break
        if move_time > 86400:
            # 记录结束时间
            position_data = my_ship1.get_position()
            results1_rock.append([*position_data, "move", move_time])
            # end_time = time.time()
            # print("船的位置：", my_ship2.get_position(),"\t运行时间：",end_time - start_time)
            # print(time)
            break
    if check:
        results1_sand.append(['Na','Na','Na', "stop",move_time])
            
# 创建一个DataFrame对象
df = pd.DataFrame(results1_rock, columns=['x座标', 'y座标', 'z座标','停止原因','停止时间'])
# 将DataFrame写入Excel文件
df.to_excel('not_to_ground_rock.xlsx', index=False)
# print(results1)

# 创建一个DataFrame对象
df = pd.DataFrame(results1_sand, columns=['x座标', 'y座标', 'z座标','停止原因','停止时间'])
# 将DataFrame写入Excel文件
df.to_excel('not_to_ground_sand.xlsx', index=False)
# print(results1)
            



results2_rock = []
results2_sand = []

for i in tqdm(range(nums), desc="Processing2", unit="iteration"):
    my_ship2 = ship_class.Ship(0, 0, 100, 50, 104174, 100)
    # 记录一次模拟的开始时间
    # start_time = time.time()
    move_time = 0
    check = 1
    while True:
        my_ship2.move(0.1)
        move_time += 0.1
        # print(move_time)
        # print(my_ship2.get_position())
        # print(my_ship2.get_a())
        # print(my_ship2.get_v())
        if my_ship2.check_go_to_surface():
            my_ship2.change_on_surface()
            move_time += 0.1
        if my_ship2.check_go_to_ground():
            if check:
                position_data = my_ship2.get_position()
                results2_sand.append([*position_data,"stop",move_time])
                check = 0
            my_ship2.change_on_ground()
            my_ship2.move(0.1)
            move_time += 0.1
        # print(move_time)
        if my_ship2.check_stop():
            position_data = my_ship2.get_position()
            results2_rock.append([*position_data , "stop",move_time])
            break
        if move_time > 86400:
            # 记录结束时间
            position_data = my_ship2.get_position()
            results2_rock.append([*position_data, "move",move_time])
            # end_time = time.time()
            # print("船的位置：", my_ship2.get_position(),"\t运行时间：",end_time - start_time)
            # print(time)
            break
    if check:
        results2_sand.append(['Na','Na','Na', "stop",move_time])

# 创建一个DataFrame对象
df = pd.DataFrame(results2_rock, columns=['x座标', 'y座标', 'z座标','停止原因','停止时间'])
# 将DataFrame写入Excel文件
df.to_excel('to_ground_rock.xlsx', index=False)
# print(results1)

# 创建一个DataFrame对象
df = pd.DataFrame(results2_sand, columns=['x座标', 'y座标', 'z座标','停止原因','停止时间'])
# 将DataFrame写入Excel文件
df.to_excel('to_ground_sand.xlsx', index=False)
# print(results1)




results3_rock = []
results3_sand = []

for i in tqdm(range(nums), desc="Processing3", unit="iteration"):
    my_ship3 = ship_class.Ship(0, 0, 100, 50, 102857, 100)
    # 记录一次模拟的开始时间
    # start_time = time.time()
    move_time = 0
    check = 1
    while True:
        my_ship3.move(0.1)
        move_time += 0.1
        # print(move_time)
        # print(my_ship2.get_position())
        # print(my_ship2.get_a())
        # print(my_ship2.get_v())
        if my_ship3.check_go_to_surface():
            my_ship3.change_on_surface()
            move_time += 0.1
        if my_ship3.check_go_to_trench() == -1:
            my_ship3.change_trench_final()
        elif my_ship3.check_go_to_trench() == 1:
            if check:
                position_data = my_ship3.get_position()
                results3_sand.append([*position_data,"stop",move_time])
                # print(my_ship2.get_position())
                check = 0
            my_ship3.change_on_trench()
            my_ship3.move(0.1)
            move_time += 0.1
        # print(move_time)
        if my_ship3.check_stop():
            position_data = my_ship3.get_position()
            results3_rock.append([*position_data , "stop" , move_time])
            # print(my_ship2.get_position())
            break
        if move_time > 86400:
            # 记录结束时间
            position_data = my_ship3.get_position()
            results3_rock.append([*position_data, "move" , move_time])
            # print(my_ship2.get_position())
            # end_time = time.time()
            # print("船的位置：", my_ship2.get_position(),"\t运行时间：",end_time - start_time)
            # print(time)
            break
    if check:
        results3_sand.append(['Na','Na','Na', "stop" , move_time])

# 创建一个DataFrame对象
df = pd.DataFrame(results3_rock, columns=['x座标', 'y座标', 'z座标','停止原因','停止时间'])
# 将DataFrame写入Excel文件
df.to_excel('to_trench_rock.xlsx', index=False)
# print(results1)

# 创建一个DataFrame对象
df = pd.DataFrame(results3_sand, columns=['x座标', 'y座标', 'z座标','停止原因','停止时间'])
# 将DataFrame写入Excel文件
df.to_excel('to_trench_sand.xlsx', index=False)
# print(results1)



results4_rock = []
results4_sand = []

for i in tqdm(range(nums), desc="Processing4", unit="iteration"):
    my_ship4 = ship_class.Ship(0, 0, 100, 50, 104174, 100)
    # 记录一次模拟的开始时间
    # start_time = time.time()
    move_time = 0
    check = 1
    while True:
        my_ship4.move(0.1)
        move_time += 0.1
        # print(move_time)
        # print(my_ship2.get_position())
        # print(my_ship2.get_a())
        # print(my_ship2.get_v())
        if my_ship4.check_go_to_surface():
            my_ship4.change_on_surface()
            move_time += 0.1
        if my_ship4.check_go_to_trench() == -1:
            my_ship4.change_trench_final()
        elif my_ship4.check_go_to_trench() == 1:
            if check:
                position_data = my_ship4.get_position()
                results4_sand.append([*position_data,"stop", move_time])
                # print(my_ship2.get_position())
                check = 0
            my_ship4.change_on_trench()
            my_ship4.move(0.1)
            move_time += 0.1
        # print(move_time)
        if my_ship4.check_stop():
            position_data = my_ship4.get_position()
            results4_rock.append([*position_data , "stop" , move_time])
            # print(my_ship2.get_position())
            break
        if move_time > 86400:
            # 记录结束时间
            position_data = my_ship4.get_position()
            results4_rock.append([*position_data, "move" , move_time])
            # print(my_ship2.get_position())
            # end_time = time.time()
            # print("船的位置：", my_ship2.get_position(),"\t运行时间：",end_time - start_time)
            # print(time)
            break
    if check:
        results4_sand.append(['Na','Na','Na', "stop" , move_time])

# 创建一个DataFrame对象
df = pd.DataFrame(results4_rock, columns=['x座标', 'y座标', 'z座标','停止原因','停止时间'])
# 将DataFrame写入Excel文件
df.to_excel('to_trench_rock_heavy.xlsx', index=False)
# print(results1)

# 创建一个DataFrame对象
df = pd.DataFrame(results4_sand, columns=['x座标', 'y座标', 'z座标','停止原因','停止时间'])
# 将DataFrame写入Excel文件
df.to_excel('to_trench_sand_heavy.xlsx', index=False)
# print(results1)