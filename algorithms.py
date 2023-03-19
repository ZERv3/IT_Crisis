import math

def Velocity(mass, voltage = 80):
    # Единица измерения - светововой год / день
    return 2*(voltage/80)*(200/mass)

def Gen(gen_old, k):
    # Новая популяция
    return gen_old*(k+1)

def Koef(temperature, oxygen):
    # Коеффициент
    return math.sin(-(math.pi / 2) + (math.pi/40)*(temperature + oxygen*0.5))

def Energy(temperature):
    s = 0
    for i in range(temperature):
        s += i
    return s

# Каждый день популяция травы увеличивается в 2 раза
# До тех пор пока не будет достаточно для выгрузки на точку + 8
# Если достаточно то энергия тратится только на реактор (80%)

def statistics(dist, SH_value):
    SH_cur = 8
    dist_cur = 0
    stats = []
    while dist_cur < dist:
        flag = 0
        if SH_cur < (SH_value + 8):
            flag = 1
            SH_cur *= 2
        vel = Velocity(mass = 192 + SH_cur)
        dist_cur += vel
        
        line = ""
        if flag == 0:
            line = "Engine: 80% SH_generation: 0%"
        else:
            line = "Engine: 80% SH_generation: 20%"

        stats.append([SH_cur, round(vel*1000)/1000, line])
    
    return stats
