# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 06:30:37 2024

@author: marktsai
"""

import random

pwd = random.randint(1, 100)
maxN = 100
minN = 1

while True:
    guess = int( input("請輸入 " +str(minN)+ "~" +str(maxN) + "間的數字: " ) )
    if guess > maxN or guess < minN:
        print("猜測數字超過範圍", end="")
        continue
    if guess == pwd:
        print("答對了,密碼為", pwd)
        break
    if guess < pwd:
        minN = guess +1
    elif guess > pwd:
        maxN = guess -1
