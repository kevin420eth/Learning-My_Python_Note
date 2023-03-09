######################BeautifulSoup使用方式######################

'''
物件名稱 = BeautifulSoup(抓取下來的網頁內容,'解析器')

備註:
解析器有3種可用
- lxml (官方推薦,解析速度最快)
- html.parser (Python內建)
- html5lib
'''

from bs4 import BeautifulSoup
with open("111.txt") as f:
    content = f.read()


#解析抓取下來的網頁原始碼並把她轉換成BeautifulSouop物件
soup = BeautifulSoup(content,'html.parser')

'''
soup.find("標籤")
'''
