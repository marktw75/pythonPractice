# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:49:58 2024
QA部門今天舉辦團康活動，有n個人圍成一圈，順序排號。
從第一個人開始報數（從1到3報數），凡報到3的人退出圈子。
請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?

預期結果
輸入：n值(0-100)
輸出：第幾順位

@author: marktsai
"""

n = int( input("請輸入人數(0-100)：") )
people = list(range(1,n+1))

count = 0
while len(people) > 1:
    for person in list(people):
        count +=1
        
        if count == 3:
            people.remove(person)
            count = 0

print("第 {} 順位".format(people[0]))
