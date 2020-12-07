import requests
import re
from douban_crawler import DoubanCrawler
from lxml import html
import time
import random
import urllib


db_crawler = DoubanCrawler("douban.txt")

tag_list_url = "https://book.douban.com/tag/"
tag_content = db_crawler.download(tag_list_url)

# print(tag_content)

tag_xpath = "//td/a/text()"
tag_tree = html.fromstring(tag_content)
tags = tag_tree.xpath(tag_xpath)
# encode chinese character
# print(urllib.parse.quote(tags[0]))

for tag in tags:
    tag = urllib.parse.quote(tag)

    page_id = 1

    while 1:
        start_id = 20 * (page_id - 1)
        url = "https://book.douban.com/tag/{}?start={}&type=T".format(tag,
                                                                      (page_id - 1) * 20)

        content = db_crawler.download(url)

        print(len(content))
        print(page_id, start_id)

        xpath = "//li[@class='subject-item']"
        tree = html.fromstring(content)

        # retrieve last page link by accessing -1 index
        # page_links = tree.xpath("//div[@class='paginator']/a/@href")
        # print(page_links[-1])

        # or accessing last element in xpath directly using last() function
        if page_id == 1:
            page_links = tree.xpath(
                "//div[@class='paginator']/a[last()]/@href")

            if page_links:
                # -> relative path
                print(page_links[0])
                last_page = int(re.findall("start=(\d+)", page_links[0])[0])
                print("Last ID: ", last_page)

        # dir(book_names[0]) -> find attributes
        book_infos = tree.xpath(xpath)
        print(book_infos)
        if not book_infos:
            break

        # book_list = list(map(lambda x: x.text.strip(), tree.xpath(xpath)))
        for info in book_infos:
            book_name = info.xpath(".//h2/a")[0].text.strip()
            book_url = info.xpath(".//h2/a")[0].attrib['href']
            book_pub_name = "N/A"
            booK_pub_temp = info.xpath(".//div[@class='pub']")
            if booK_pub_temp:
                book_pub_name = booK_pub_temp[0].text.strip()
            book_intro = "N/A"
            book_intro_temp = info.xpath(".//div[@class='info']/p")
            if book_intro_temp:
                book_intro = book_intro_temp[0].text.strip()
            # print(book_name, book_pub_name, "\n", book_intro, "\n", book_url)
            print(book_name)
            print("--------------------------------")
        page_id += 1

        # to simulate the time of human reading
        sleep_time = random.randint(1, 5)
        time.sleep(sleep_time)
        if start_id == last_page:
            break
    break
