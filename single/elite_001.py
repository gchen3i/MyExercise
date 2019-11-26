from builtins import print

score = int(input("please input a score:"))
degree = "SABCDE"
num =0
if score > 100 or score < 0:
    print("error, please input correct score")
else:
    num = score//10
    if num < 6:
        num = 5
    print(degree[10-num])
    print("score is {0},degree is {1}".format(score,degree[10-num]))
    print()
    
import pandas as pd
