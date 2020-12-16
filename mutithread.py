import concurrent.futures
import requests
from douban_crawler import DoubanCrawler

# URLS = ['http://www.foxnews.com/',
#         'http://www.cnn.com/',
#         'http://europe.wsj.com/',
#         'http://www.bbc.co.uk/',
#         'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents

urls = [
    f"https://book.douban.com/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD?start={start_id}&type=T" for start_id in range(0, 200, 20)]
douban_crawler = DoubanCrawler("multithread.txt")


def load_url(url):
    global douban_crawler
    return douban_crawler.download(url)


# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url): url for url in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
