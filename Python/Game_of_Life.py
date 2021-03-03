from random import *
import time
import os

def load_world():
    w = []
    a = []
    for x in range(16):
        for y in range(64):
            a.append(sample((1,0), 1))
        w.append(a)
        a = []
    return w

def game(w):
    a = load_world()
    acc = 0
    for i in range(16):
        for j in range(64):

            if i == j == 0 :
                acc = w[i][j+1][0] + w[i+1][j][0] + w[i+1][j+1][0]
                if (acc == 2 or acc == 3) and w[i][j][0] == 1:
                    a[i][j][0] = 1
                elif acc == 3 and w[i][j][0] == 0:
                    a[i][j][0] = 1
                else:
                    a[i][j][0] = 0
                acc = 0

            elif i == 0 and 0 < j < 63:
                acc = w[i][j-1][0] + w[i+1][j-1][0] + w[i][j+1][0] + w[i+1][j][0] + w[i+1][j+1][0]
                if (acc == 2 or acc == 3) and w[i][j][0] == 1:
                    a[i][j][0] = 1
                elif acc == 3 and w[i][j][0] == 0:
                    a[i][j][0] = 1
                else:
                    a[i][j][0] = 0
                acc = 0

            elif 0 < i < 15 and j == 0:
                acc = w[i][j+1][0] + w[i+1][j][0] + w[i+1][j+1][0] + w[i-1][j][0] + w[i-1][j+1][0]
                if (acc == 2 or acc == 3) and w[i][j][0] == 1:
                    a[i][j][0] = 1
                elif acc == 3 and w[i][j][0] == 0:
                    a[i][j][0] = 1
                else:
                    a[i][j][0] = 0
                acc = 0

            elif i == 15 and j == 0:
                acc = w[i-1][j][0] + w[i-1][j+1][0] + w[i][j+1][0]
                if (acc == 2 or acc == 3) and w[i][j][0] == 1:
                    a[i][j][0] = 1
                elif acc == 3 and w[i][j][0] == 0:
                    a[i][j][0] = 1
                else:
                    a[i][j][0] = 0
                acc = 0
                
            elif i == 15 and 0 < j < 63:
                acc = w[i-1][j-1][0] + w[i-1][j][0] + w[i-1][j+1][0] + w[i][j-1][0] + w[i][j+1][0]
                if (acc == 2 or acc == 3) and w[i][j][0] == 1:
                    a[i][j][0] = 1
                elif acc == 3 and w[i][j][0] == 0:
                    a[i][j][0] = 1
                else:
                    a[i][j][0] = 0
                acc = 0
            
            elif i == 15 and j == 63:
                acc = w[i][j-1][0] + w[i-1][j-1][0] + w[i-1][j][0]
                if (acc == 2 or acc == 3) and w[i][j][0] == 1:
                    a[i][j][0] = 1
                elif acc == 3 and w[i][j][0] == 0:
                    a[i][j][0] = 1
                else:
                    a[i][j][0] = 0
                acc = 0

            elif 0 < i < 15 and j == 63:
                acc = w[i-1][j-1][0] + w[i-1][j][0] + w[i][j-1][0] + w[i+1][j-1][0] + w[i+1][j][0]
                if (acc == 2 or acc == 3) and w[i][j][0] == 1:
                    a[i][j][0] = 1
                elif acc == 3 and w[i][j][0] == 0:
                    a[i][j][0] = 1
                else:
                    a[i][j][0] = 0
                acc = 0
            
            elif i == 0 and j == 63:
                acc = w[i][j-1][0] + w[i+1][j-1][0] + w[i+1][j][0]
                if (acc == 2 or acc == 3) and w[i][j][0] == 1:
                    a[i][j][0] = 1
                elif acc == 3 and w[i][j][0] == 0:
                    a[i][j][0] = 1
                else:
                    a[i][j][0] = 0
                acc = 0

            else:
                acc = w[i-1][j-1][0] + w[i-1][j][0] + w[i-1][j+1][0] + w[i][j-1][0] + w[i][j+1][0] + w[i+1][j-1][0] + w[i+1][j][0] + w[i+1][j+1][0]
                if (acc == 2 or acc == 3) and w[i][j][0] == 1:
                    a[i][j][0] = 1
                elif acc == 3 and w[i][j][0] == 0:
                    a[i][j][0] = 1
                else:
                    a[i][j][0] = 0
                acc = 0
    return a

def convert(w):
    for x in range(16):
        for y in range(64):
            if world[x][y][0] == 1:
                print("x", end="")
            else:
                print(" ", end="")
        print("\n")

world = game(load_world())
while True:    
    convert(world)
    world = game(world)
    time.sleep(0.3)
    os.system("cls")
