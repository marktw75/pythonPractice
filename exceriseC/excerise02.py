# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:48:55 2024
國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間，
文字為"Hello welcome to Cathay 60th year anniversary"，
請寫一個程式計算每個字母(大小寫視為同個字母)出現次數

預期結果
輸出：
0 1
6 1
A 4  => this should be 5
C 2
E 5
H 3
....(繼續印下去)

@author: marktsai
"""

helloString = "Hello welcome to Cathay 60th year anniversary"

# 排除空格並轉小寫
filteredString = []
for char in helloString:
    if char.isalnum():
        filteredString.append(char.lower())

# 用dict存數量
filteredStringCount = {}

for char in filteredString:
    if char in filteredStringCount:
        filteredStringCount[char] +=1
    else:
        filteredStringCount[char] =1

# 依字母排序並用大寫印出
sortedCharCount = sorted(filteredStringCount.items())

for char, count in sortedCharCount:
    print(char.upper(), count)
