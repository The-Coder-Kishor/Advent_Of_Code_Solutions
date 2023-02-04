coordinates = open("input.txt", "r").read().splitlines()
map_2d = []
for i in range(1000):
    new = []
    for j in range(1000):
        new.append(0)
    map_2d.append(new)

for i in coordinates:
    a, b = i.split("->")
    a, b = a.strip(" "), b.strip(" ")
    x1, y1 = a.split(",")
    x2, y2 = b.split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    while (str(x1)+","+str(y1)) != (str(x2)+","+str(y2)):
        if x1 != x2 and y1 == y2:
            map_2d[x1][y1] += 1
            while x1 != x2:
                if x1 > x2:
                    x1 = int(x1) - 1
                    
                elif x1 < x2:
                    x1 = int(x1) + 1

                map_2d[x1][y1] += 1

        elif x1 == x2 and y1 != y2:
            map_2d[x1][y1] += 1
            while y1 != y2:
                if y1 > y2:
                    y1 = int(y1) - 1
                    
                elif y1 < y2:
                    y1 = int(y1) + 1

                map_2d[x1][y1] += 1

        elif x1 == y1 and x2 == y2:
            map_2d[x1][y1] += 1
            while x1 != x2:
                if x1 > x2:
                    x1, y1 = int(x1) - 1, int(y1) - 1

                elif x1 < x2:
                    x1, y1 = int(x1) + 1, int(y1) + 1

                map_2d[x1][y1] += 1

        elif x1 == y2 and x2 == y1:
            map_2d[x1][y1] += 1
            while x1 != x2:
                if x1 > x2:
                    x1, y1 = int(x1) - 1, int(y1) + 1

                elif x1 < x2:
                    x1, y1 = int(x1) + 1, int(y1) - 1

                map_2d[x1][y1] += 1

        else:
            map_2d[x1][y1] += 1
            while x1 != x2:
                if x1 > x2 and y1 > y2:
                    x1, y1 = int(x1) - 1, int(y1) - 1
            
                elif x1 < x2 and y1 < y2:
                    x1, y1 = int(x1) + 1, int(y1) + 1

                elif x1 > x2 and y1 < y2:
                    x1, y1 = int(x1) - 1, int(y1) + 1

                elif x1 < x2 and y1 > y2:
                    x1, y1 = int(x1) + 1, int(y1) - 1

                map_2d[x1][y1] += 1
            
        break

sum = 0
for i in map_2d:
    for j in i:
        if(j >= 2):
            sum += 1

print(sum)
