import math

class Position:
    def __init__(self,latitude = math.pi / 4,longitude = 0):
        self.latitude = latitude
        self.longitude = longitude


    def getDensity(self,depth):
        miu = 0.928 - 0.079 * math.cos(0.053 * self.latitude)
        alpha = 27.91 - 2.06 * math.exp(-math.pow((0.0161 * abs(self.latitude)), 5))
        beta = 0.00637 + 0.00828 * math.exp(-math.pow(0.017 * abs(self.latitude), 4.66))
        v = 0.964 - 0.091 * math.exp(-math.pow(0.016 * abs(self.latitude), 5))
        # print(depth)
        density = 1000 + alpha * (miu + 0.5 * (1 - miu) * (1 + math.tanh(0.00988 * depth - 1.01613))) + beta * math.pow(depth, v)
        return density

    def get_g(self):
        g_eq = 6.67408 * 10 * 5.9722 / math.pow(6.365 ,2)
        g = g_eq - math.pow(7.292*math.pow(10,-5),2)*6.365*math.pow(10,6)*math.pow(math.cos(self.latitude),2)
        return g

my_position = Position()


# print(my_position.getDensity(0))