######################split()字串分割函數使用方式######################

#說明:把字串以指定的符號進行分割,並把分割後的每一項資料儲存在一個新的list裡面

'''
split("指定的符號或字元",切割次數)

備註:
1.如果沒指定符號,則會以預設的空白作為分隔符號
2.如果不指定切割次數,則會切到沒得切為止
'''

#範例1:
string1 = "1 2 3"
string1 = string1.split()
print(string1)

#範例2:
string2 = "www.google.com"
string2 = string2.split(".")
print(string2)

#範例3
string3 = "林俊傑,是一個,他媽的,渣男"
string3 = string3.split(",",2)
print(string3)