######################if條件判斷式使用方式######################

'''
if 判斷式:
    就怎樣怎樣
'''
#範例:先請使用者輸入a的值,如果a>0的話就印出a的值
a = int(input("請輸入a的值: "))
if a>0:
    print("黑人問號")

'''
if 判斷式:
    怎樣怎樣
else:
    不然就怎樣怎樣
'''
#範例:
b = int(input("請輸入b的值: "))
if b>10:
    print("b is bigger than 10")
else:
    print("b is small or equivalent than 10")

'''
if 判斷式:
    怎樣怎樣
elif 判斷式:
    不然就怎樣怎樣
elif 判斷式:
    不然就怎樣怎樣
    .
    .
    .
else:
    不然就怎樣怎樣
'''
#範例:
c = int(input("請輸入c的值: "))
if c>100:
    print("c比100大")
elif c>50:
    print("c比50大但不超過100")
elif c>30:
    print("c比30大但不超過50")
else:
    print("c小於或等於30")

######################略過pass######################

#即便符合條件也不一定要怎樣怎樣,可以選擇略過,不執行任何東西
#範例:
d = int(input("請輸入d的值: "))
if d>0:
    pass
else:
    print("給我小心一點")