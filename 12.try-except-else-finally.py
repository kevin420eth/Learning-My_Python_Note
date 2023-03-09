######################try excepy else finally使用方式######################
'''
try:
    欲執行的程式碼
except 錯誤1:
    如果發生錯誤1,要怎樣怎樣
.
.
.
except 錯誤n:
    如果發生錯誤n,要怎樣怎樣
else:
    如果都沒有發生錯誤,要怎樣怎樣
finally:
    不管有沒有錯誤發生,都要怎樣怎樣

備註:
1.錯誤型別不一定要有,如果沒有指定錯誤型別,則如果發生任何錯誤都會執行except
2.else與finally不一定要有
'''

#範例1:

try:
    x = int(input("Please Enter a number: "))
    x = x+10
    print(x)
except:
    print("Something is wrong!")
else:
    print("Good!")
finally:
    print("Try Again!")

#範例2
while True:
    try:
        y = int(input("Please Enter a non-zero number: "))
        10/y
    except ZeroDivisionError:
        print("0 can't be a divisor!")
    except ValueError:
        print(f"Enter a fucking number not a letter dumb ass!")
    else:
        print(f"10/y = {10/y}")
    finally:
        again = input("Wanna try again (Y/N)? ").upper()
        if again == "N":
            print("Bye Bye!")
            break