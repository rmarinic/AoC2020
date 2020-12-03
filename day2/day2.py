puzzle = [line.strip() for line in open("input_day2_1.txt", "r")]

counter = 0

for line in puzzle:
    flag = False
    brojac = 0
    x = line.find('-')
    y = line.find(' ')
    low = int(line[0:x]) - 1
    high = int(line[x+1:y]) - 1
    slovo = line[y+1:line.find(':')]
    tekst = line[line.find(':')+2:len(line)]

    if tekst[low] is slovo:
        flag = True

    if tekst[high] is slovo:
        if flag:
            flag = False
        else:
            flag = True

    if flag:
        counter = counter + 1

print(counter)
    
