import algorithms

data = [(1,504,31)]

days = []    
for target in data:
    stat = algorithms.statistics(target[2], target[1])
    for i in stat:
        days.append(i)

with open('output.txt', 'w') as f:
    for i in range(len(days)):
        line = f"Day {i+1}:\n \tSH: {days[i][0]};\n \tVelocity: {days[i][1]};\n \tPower: {days[i][2]}\n"
        f.write(line+"\n")

