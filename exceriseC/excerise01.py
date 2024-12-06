# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:47:20 2024
國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]，
但是老師在輸入成績的時候看反了，把五位學生的成績改成了[35, 46, 57, 91, 29]，
請用一個函數來將學生的成績修正。

預期結果
輸入: [35, 46, 57, 91, 29]
輸出: [53, 64, 75, 19, 92]

@author: marktsai
"""
def reverseChr(x):
    return int(str(x)[::-1])


listTeacherInput = [35, 46, 57, 91, 29]
listfix = []

for i in listTeacherInput:
    listfix.append(reverseChr(i))
    
print("輸入: ", listTeacherInput)
print("輸出: ", listfix)
