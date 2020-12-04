import requests
import re


class MyCrawler:
    def __init__(self, filename):
        self.filename = filename
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'
        }

    def download(self, url):
        r = requests.get(url, headers=self.headers)
        return r.text

    def extract(self, content, pattern):
        result = re.findall(pattern, content)
        return result

    def save(self, items):
        with open(self.filename, "w", encoding="utf-8") as f:
            for item in items:
                # f.write(item[0] + " " + item[1] + " " + item[2] +
                #         " " + item[3] + " " + item[4] + " " + item[5] + "\n")
                f.write(" ".join(item) + "\n")

    def crawl(self, url, pattern, headers=None):
        if headers:
            self.headers.update(headers)
        content = self.download(url)
        info = self.extract(content, pattern)
        self.save(info)


# 爬爬b站排行版
# url = "https://www.bilibili.com/v/popular/rank/douga?spm_id_from=333.851.b_62696c695f7265706f72745f646f756761.39"
# b_crawler = MyCrawler("bilibili.txt")
# pattern = '<a\shref="//([^"]*?)"\starget="_blank"\sclass="title">(.*?)</a>.*?</i>[\s]+(.*?)[\s]+.*</i>[\s]+(\d+)[\s]+</span>.*</i>[\s]+(.*?)[\s]+</span>.*<div class="pts"><div>(\d+)</div>'
# b_crawler.crawl(url, pattern)


# 一招制敌： 放全部request header
# copy as curl, and use tools to convert code to python code
# 没登陆基本不需要cookies
# url = "https://www.douban.com/search?q=%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C"


# 说明豆瓣只验证user agent
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'
# }


# response = requests.get('https://www.douban.com/search?q=%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C',
#                         headers=headers)
# print(len(response.text))
# print("神经网络与深度学习" in response.text)
# print(response.text)
# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://www.douban.com/search?q=^%^E7^%^A5^%^9E^%^E7^%^BB^%^8F^%^E7^%^BD^%^91^%^E7^%^BB^%^9C', headers=headers, cookies=cookies)
