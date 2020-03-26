from selenium import webdriver
import time
import json
from json import JSONEncoder

start_url = "https://www.news.gov.hk/eng/categories/covid19/index.html"

# 爬取的url,title,img,comment,source 通过字典的形式存储在列表里，需要的时候遍历提取就好
unlist = []
unimg = []
prolist = []
urllist = []


class TouTiao():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = start_url

    def load_data(self):
        self.driver.get(start_url)
        time.sleep(5)
        print("reading website")
        for element in self.driver.find_elements_by_class_name("news-item"):
            print(element.text)
            unlist.append(element.text)
            
        images = self.driver.find_elements_by_tag_name("img")
        for image in images:
            print(image.get_attribute("src"))
            unimg.append(image.get_attribute("src"))

        


    def close_browser(self):
        self.driver.quit()

    def main(self):
        self.load_data()
        self.close_browser()


class Info():
    def __init__(self):
        self.date = ""
        self.title = ""
        self.summary = ""
        self.img = ""
        self.url = ""

    def myprint(self):
        print(self.date)
        print(self.title)
        print(self.summary)
        print(self.img)

    def __jsonencode__(self):
        return {"date": self.date, "title": self.title, "summary": self.summarym, "img": self.img}


class myEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def processlis(infos):
    for text in unlist:
        info = Info()
        met = 0
        s = ""
        for i in range(len(text)):
            if text[i] == "\n":
                if met == 0:  # processs titel
                    info.title = s
                    s = ""
                    met += 1
                elif met == 1:
                    info.date = s
                    s = ""
                    met += 1
                else:
                    info.summary = s
                    break
            else:
                s += text[i]

        infos.append(info)


def processimg(infos):
    realimg = []

    for s in unimg:
        if s.find("2020") != -1:
            realimg.append(s)
    i = 0
    for info in infos:
        info.img = realimg[i]
        i += 1


def getsjson():
    toutiao = TouTiao()
    toutiao.main()
    infos = []
    processlis(infos)
    processimg(infos)

    for info in infos:
        info.myprint()
    myJSONData = json.dumps(infos, indent=4, cls=myEncoder)
    return myJSONData
