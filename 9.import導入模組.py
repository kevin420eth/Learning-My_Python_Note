######################import導入使用方式######################


######################導入整個模組######################

'''
import 模組名稱
'''
#範例:
import random
n = random.randint(0,100)
print(n)

######################導入模組內的某一個函數######################

#說明:在使用該函數時,可以不用在打出模組名稱作為前綴詞

'''
from 模組名稱 import 函數名稱
'''

#範例:
from random import randint
x = randint(1,5000)
print(x)

######################導入模組內的多個函數######################

'''
from 模組名稱 import 函數1名稱, 函數2名稱, 函數3名稱, ...
'''

######################導入模組內所有函數######################

#說明:與直接導入整個模組不同的是,此方法可以不用在把模組名稱前綴詞寫出來,可以直接呼叫函數

'''
from 模組名稱 import *
'''