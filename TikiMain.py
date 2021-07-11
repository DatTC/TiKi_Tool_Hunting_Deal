
from bs4.element import PreformattedString
from TikiTarget import TikiTarget 
from TikiItem import TikiItem
from TikiHelper import *
from bs4 import BeautifulSoup
import requests


TARGET_FILE = "target_list.txt"

targets = getTargetFromFile(TARGET_FILE)

# for target in targets:
#     print(target.info())

target = targets[0]

searchLink = target.getSearchLink(1)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
respond = requests.get(searchLink, headers=headers)
# print(respond.content.decode())
# print(respond.text.encode("utf-8"))

bsoup = BeautifulSoup(respond.text, "html.parser")

#find all <a> class = product-item
listElement = bsoup.findAll("a",{"class":"product-item"})
i = 0
print(len(listElement))
bestItem = None
for e in listElement:
    print(str(i)+": ")
    if (e.get_text().find("Đã hết hàng") >=0 or e.get_text().find("Ngừng kinh doanh") >=0):
        print("==================HẾT SẢN PHẨM==================")
        continue
    newItem = TikiItem()
    newItem.title = e.find("div",{"class":"name"}).get_text()
    newItem.url = "https://tiki.vn"+e.get("href")
    span_price = e.find("div",{"class":"price-discount__price"})
    newItem.price = convertToNum(span_price.contents[0].strip())
    if newItem.isValidItem(target.patterns):
        print (newItem.info())
        if (bestItem == None):
            bestItem = newItem
        else:
            if(newItem.price < bestItem.price):
                bestItem = newItem

    i+=1
    # span_name = e.find("div",{"class":"name"})
    # print(span_name.get_text())
    # span_price = e.find("div",{"class":"price-discount__price"})
    # print(convertToNum(span_price.contents[0].strip()))
    # print("https://tiki.vn"+e.get("href"))

if (bestItem != None):
    print("BEST ITEM IS: ",bestItem.info())

# t = "trương công đạt"
# print(t.text.encode("utf-8"))
# <div class="price-discount__price">3.850.000 ₫</div>