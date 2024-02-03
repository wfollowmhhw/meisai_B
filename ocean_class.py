import math
import position

w = 7.292 * math.pow(10,-5)

class OceanCurrent:
    def __init__(self, v_x_surface=0.5, v_y_surface=0.5, v_z_surface=0 , wind_v = 10 , v_x_deep = 0.01 , v_y_deep = 0.01):
        self.v_x_surface = v_x_surface
        self.v_y_surface = v_y_surface
        self.v_z_surface = v_z_surface
        self.V_surface_0 = math.sqrt(math.pow(v_x_surface,2) + math.pow(v_y_surface,2))
        self.V_surface_sita = math.atan(v_y_surface / v_x_surface)
        self.V_drifting_0 = math.sqrt(math.pow(v_x_surface - v_x_deep,2) + math.pow(v_y_surface - v_y_deep,2))
        self.V_drifting_sita = math.atan((v_y_surface - v_y_deep) / (v_x_surface - v_x_deep))
        self.wind_force = ( 0.75 + 0.067 * wind_v ) * 1.2 * math.pow(wind_v,2) * 0.001
        self.v_x_deep = v_x_deep
        self.v_y_deep = v_y_deep
        self.v_x = 0
        self.v_y = 0
        self.v_z = 0

    def reset_depth_v(self,depth,option):
        if option == 0: # drifting 纯漂流状态分析
            a = (position.my_position.getDensity(depth) * w * math.sin(position.my_position.latitude)
                 * math.sqrt(2)) * self.V_surface_0 / self.wind_force
            # print(a)
            u = self.V_surface_0 * math.exp(- a * depth) * math.cos(math.pi/4 - a * depth)
            v = self.V_surface_0 * math.exp(- a * depth) * math.sin(math.pi/4 - a * depth)
            self.v_x = u * math.sin(math.pi/4 - self.V_surface_sita) + v * math.cos(math.pi/4 - self.V_surface_sita)
            self.v_y = u * math.cos(math.pi/4 - self.V_surface_sita) + v * math.sin(math.pi/4 - self.V_surface_sita)
            # print(self.v_x,self.v_y)
        elif option == 1: # 考虑深水不变的洋流与浅层受风力影响的洋流共同作用
            a = (position.my_position.getDensity(depth) * w * math.sin(position.my_position.latitude)
                 * math.sqrt(2)) * self.V_drifting_0 / self.wind_force
            u = self.V_drifting_0 * math.exp(- a * depth) * math.cos(math.pi / 4 - a * depth)
            v = self.V_drifting_0 * math.exp(- a * depth) * math.sin(math.pi / 4 - a * depth)
            self.v_x = (u * math.sin(math.pi / 4 - self.V_drifting_sita)
                        + v * math.cos(math.pi / 4 - self.V_drifting_sita) + self.v_x_deep)
            self.v_y = (u * math.cos(math.pi / 4 - self.V_drifting_sita)
                        + v * math.sin(math.pi / 4 - self.V_drifting_sita) + self.v_y_deep)





    def set_v(self, v_x, v_y, v_z):
        # 设置洋流的速度
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z

class Ocean:
    def __init__(self):
        self.Cd = 0.2
        self.depth = 570
        self.trench_depth = 3000
        self.rock_e = 0.62
        self.rock_miu = 0.2
        self.trench_slope = math.pi / 4

    def get_Viscosity(self,temperature):
        viscosity = 2.414 * math.pow(10,-5) * math.pow(10, 247.8 / (temperature - 140))
        return viscosity

    def get_Cd(self):
        return self.Cd


my_ocean = Ocean()
my_ocean_current = OceanCurrent()

# print(my_ocean.get_Cd(273))