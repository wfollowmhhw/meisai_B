import math
import random
import ocean_class
import position
import tools

g = position.my_position.get_g()
w = 7.292 * math.pow(10,-5)
class Limit:
    def __init__(self,v):
        self.change_v = v

limit = Limit(0.1)

class Ship:
    def __init__(self, x=0, y=0, z=100, surface_area=50 , mass = 102857 , volume = 100):
        self.x = x  # 经线方向 指向赤道
        self.y = y  # 纬线方向 北极点看是逆时针
        self.z = z
        # self.v_x = v_x
        # self.v_y = v_y
        # self.v_z = v_z
        v_r = random.uniform(0, 10)
        v_sita = random.uniform(0, 2 * math.pi)
        v_fi = random.uniform(0, math.pi)
        self.v_x = v_r * math.sin(v_fi) * math.cos(v_sita)
        self.v_y = v_r * math.sin(v_fi) * math.sin(v_sita)
        self.v_z = v_r * math.cos(v_fi)
        self.a_x = 0
        self.a_y = 0
        self.a_z = 0
        self.surface_area = surface_area
        self.mass = mass
        self.volume = volume

    def move(self, time):
        # 根据速度和时间移动船的位置
        ocean_class.my_ocean_current.reset_depth_v(self.z,1)
        # print(ocean_class.my_ocean_current.v_x)
        self.x += self.v_x * time
        self.y += self.v_y * time
        self.z += self.v_z * time
        # print(self.z)
        # print(self.v_z)
        # 1/2 * Cd * density * A
        temp_co1 = 0.5 * ocean_class.my_ocean.Cd * position.my_position.getDensity(self.z) * self.surface_area
        # 速度更新
        v_x = self.v_x
        v_y = self.v_y
        v_z = self.v_z
        # 加速度更新
        self.a_x = ((temp_co1 * math.pow(v_x - ocean_class.my_ocean_current.v_x,2)
                     * tools.check(ocean_class.my_ocean_current.v_x - v_x))
                     - 2 * self.mass * v_y * w * math.cos(position.my_position.latitude)
                     + 2 * self.mass * v_z * w * math.sin(position.my_position.latitude)) / self.mass
        self.a_y = ((temp_co1 * math.pow(v_y - ocean_class.my_ocean_current.v_y,2)
                     * tools.check(ocean_class.my_ocean_current.v_y - v_y))
                     + 2 * self.mass * v_x * w * math.cos(position.my_position.latitude)) / self.mass
        self.a_z = (- position.my_position.getDensity(self.z) * g * self.volume + self.mass * g
                     + temp_co1 * math.pow(v_z - ocean_class.my_ocean_current.v_z,2)
                     * tools.check(ocean_class.my_ocean_current.v_z - v_z)
                     - 2 * self.mass * v_x * w * math.sin(position.my_position.latitude)) / self.mass
        self.v_x += self.a_x * time
        self.v_y += self.a_y * time
        self.v_z += self.a_z * time

    def get_position(self):
        # 返回船的当前位置
        return self.x, self.y, self.z

    def get_v(self):
        # 返回船当前的速度
        return self.v_x , self.v_y , self.v_z

    def get_a(self):
        return self.a_x , self.a_y , self.a_z

    def set_v(self, v_x, v_y, v_z):
        # 设置船的速度
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z

    def check_stop(self):
        if abs(self.v_x) < 0.00001 and abs(self.v_y) < 0.00001 and abs(self.v_z) < 0.00001 and abs(self.a_x) < 0.00001 and abs(self.a_y) < 0.00001 and abs(self.a_z) < 0.00001:
            return 1
        else:
            return 0

    def check_go_to_surface(self):
        if self.z < 0:
            return 1
        else:
            return 0

    def change_on_surface(self):
        v_z = self.v_z
        self.v_z = - v_z
        z = abs(self.z)
        self.z = z

    def check_go_to_ground(self):
        if self.z > ocean_class.my_ocean.depth:
            return 1
        else:
            return 0


    def change_on_ground(self):
        v_z = self.v_z
        self.v_z = - ocean_class.my_ocean.rock_e * v_z
        delta_v_x = tools.check(self.v_x) * ocean_class.my_ocean.rock_miu * (1 + ocean_class.my_ocean.rock_e) * v_z
        delta_v_y = tools.check(self.v_y) * ocean_class.my_ocean.rock_miu * (1 + ocean_class.my_ocean.rock_e) * v_z
        if self.v_x > delta_v_x:
            self.v_x -= tools.check(self.v_x) * ocean_class.my_ocean.rock_miu * (1 + ocean_class.my_ocean.rock_e) * v_z
        else:
            self.v_x = 0

        if self.v_y > delta_v_y:
            self.v_y -= tools.check(self.v_y) * ocean_class.my_ocean.rock_miu * (1 + ocean_class.my_ocean.rock_e) * v_z
        else:
            self.v_y = 0

    def check_go_to_trench(self):
        if self.z > ocean_class.my_ocean.trench_depth:
            return -1
        elif abs(self.y) > (ocean_class.my_ocean.trench_depth - self.z) / math.tan(ocean_class.my_ocean.trench_slope):
            return 1
        else:
            return 0

    def change_on_trench(self , beta = ocean_class.my_ocean.trench_slope):
        v_x = self.v_x
        v_y = self.v_y
        v_z = self.v_z
        delta_v_x = (ocean_class.my_ocean.rock_miu * (1 + ocean_class.my_ocean.rock_e)
                     * (v_z * math.cos(beta) + v_y * math.sin(beta)))
        if abs(v_x) > abs(delta_v_x):
            self.v_x -= delta_v_x
        else:
            self.v_x = 0
        a = (v_z * math.sin(beta) - ocean_class.my_ocean.rock_miu * (1 + ocean_class.my_ocean.rock_e)
             * (v_z * math.cos(beta) + v_y * math.sin(beta)))
        b = - ocean_class.my_ocean.rock_e * (v_z * math.cos(beta) + v_y * math.sin(beta))
        a = max(a,0)
        self.v_y = b * math.sin(beta) - a * math.cos(beta)
        self.v_z = b * math.cos(beta) + a * math.sin(beta)

    def change_trench_final(self):
        self.v_x = 0
        self.v_y = 0
        self.v_z = 0
        self.a_x = 0
        self.a_y = 0
        self.a_z = 0



