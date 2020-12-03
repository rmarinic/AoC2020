def repeatMap(mapa,originalnaMapa):
    for i in range(len(mapa)):
        mapa[i] = mapa[i] + originalnaMapa[i]

def tobogganSlide(right, down, mapa):
    x = 0
    counter = 0
    originalnaMapa = mapa

    for i in range(down, len(mapa), down):     
        x = x + right
        if(x >= len(mapa[i]) - 1):
           repeatMap(mapa,originalnaMapa)

        if(mapa[i][x] is '#'):
            counter = counter + 1

            
    return counter
    

mapa = [line.strip() for line in open("input_day3.txt", "r")]

ans = tobogganSlide(1,1,mapa) * tobogganSlide(3,1,mapa)* tobogganSlide(5,1,mapa)* tobogganSlide(7,1,mapa) * tobogganSlide(1,2,mapa)

print(ans)

