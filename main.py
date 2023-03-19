import algorithms

Fuel = 0
Oxygen = 0

data = [(1,504,31)]

days = []    
for target in data:
    stat = algorithms.statistics(target[2], target[1])
    for i in stat:
        days.append(i)

with open('output.txt', 'w') as f:
    for i in range(len(days)):
        line = f"Day {i+1}:\n \tSH: {days[i][0]} units;\n \tVelocity: {days[i][1]} ly/d;\n \tPower: {days[i][2]}\n"
        f.write(line+"\n")
        if days[i][-1] == 0:
            Fuel += 80
        else:
            Fuel += 100
            Oxygen += 38*days[i][0]

    f.write(f"\nFuel: {'{:,}'.format(Fuel)} units ({'{:,}'.format(Fuel*20)}₵)\nOxygen: {'{:,}'.format(Oxygen)} units ({'{:,}'.format(Oxygen*7)}₵)\nTotal: {'{:,}'.format(Fuel*20 + Oxygen)}₵")
