# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 06:08:08 2024

@author: marktsai
"""

import random

pwd = random.sample(range(0,10),4)  # 不重覆的list
A=0
B=0
count=0

while A!=4:
    userInputNum = input("請輸入 4 個數字: ")
    while len(userInputNum) !=4 or len(set(userInputNum)) != 4:
        userInputNum = input("請輸入 4 個數字，且數字勿重複: ")
        
    count += 1
    
    userInputList = list(map(int,list(userInputNum)))
    A=0
    B=0
    for i in range(len(userInputList)):
        if userInputList[i] in pwd:
            if i == pwd.index( userInputList[i] ):
                A += 1
            else:
                B += 1
    
    print("{}: {}A{}B".format(userInputNum, A, B))

print("猜對了，密碼是", "".join(map(str,pwd)), "猜題次數: {}次".format(count))
