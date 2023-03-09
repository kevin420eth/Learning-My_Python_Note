######################request模組使用方式######################

#說明:requests模組可以讓你對HTTP發送請求,並得到一個包括內容,編碼,狀態的回傳物件

import requests

######################傳送GET請求######################

'''
requests.get("網址",params=引數,headers=表頭)
'''

#範例:
response = requests.get("https://www.google.com/")
content = response.text #網頁原始碼
time_taken = response.elapsed #請求所花時間
status_code = response.status_code #狀態碼
encoding = response.encoding #請求網頁的編碼
header = response.headers #請求網頁的表頭

######################傳送POST請求######################
