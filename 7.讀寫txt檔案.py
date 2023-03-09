######################讀取txt檔案方法######################

#機器步驟:
#1.開啟檔案
#2.讀取檔案
#3.關閉檔案

'''
變數名稱 = open("路徑/檔案名稱",mode="模式",encoding="編碼")
檔案內容 = 物件名稱.read()

備註:
1.如果在同一個資料夾底下則不需要指名路徑
2.檔案名稱必須有副檔名
3.沒有輸入模式引數的話則預設為r
4.如是非英文內容的話可能要指定特定編碼才能讀取
5.模式種類:
- r: read,只讀模式,不能對其更改,而且檔案必須存在不然會開啟失敗
- w: write,覆寫模式,可以更改檔案內容,開啟時若檔案不存在則會自動新建一個新檔案
- a: append,附加模式,不能更改檔案已存在的內容,但可以在檔案末端新增新的內容
- b: 二進位模式
- r+: 可讀可寫
- w+: 可讀可寫
- a+: 可讀可寫
'''

######################一次讀取全部內容read()######################

#範例:
lyrics = open("test.txt","r")
content = lyrics.read()
print(content)
lyrics.close()

######################逐行讀取函數readlines()######################

#說明:把內容逐行的放到一個list裡面
#範例:
lyrics = open("test.txt","r")
content = lyrics.readlines()
print(content)
lyrics.close

######################精簡寫法######################

#說明:不需要在自己用close()關閉檔案

'''
with open("路徑/檔案名稱",mode="模式",encoding="編碼") as 變數名稱:
    怎樣怎樣
'''
#範例:
with open("test.txt") as lyrics:
    content = lyrics.read()
    print(content)

######################覆寫檔案######################

#說明:以新的內容取代原本檔案已有的內容

'''
f = open("test.txt","w")
f.write("想要覆寫入的內容")
f.close()
'''

#範例:把新的字串寫入檔案並取代原有內容
f = open("test.txt","w")
f.write("I love you")
f.close()

######################寫入list資料######################

#說明:因為write()的引數必須為字串string,所以如果要寫入list的話要用writelines()
#備註:writelines並不會自動為list中的每個變數自動換行,需自行加入\n

f = open("test.txt","w")
buy_list = ["Apple\n","Banana\n","Orange","Umbrella"]
f.writelines(buy_list)
f.close()

######################精簡寫法######################
with open("test.txt","w") as f:
    f.write("I\n")
    f.write("Love\n")
    f.write("You\n")
    f.write("My Baby\n")

######################附加檔案######################
f = open("test.txt","a")
f.write("Do\n")
f.write("You\n")
f.write("Love\n")
f.write("Me?\n")
f.close()