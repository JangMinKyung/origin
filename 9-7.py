in_file = open('chicken.txt', 'r')
sale = 0
day = 0
for line in in_file:
    chicken = line.split()
    sale += int(chicken[1])
    day += 1
print(sale / day)
print("m")