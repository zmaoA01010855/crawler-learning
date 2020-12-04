from crawler import MyCrawler
import re


class DoubanCrawler(MyCrawler):
    def extract(self, content, pattern_main, pattern_star):
        result = re.findall(pattern_main, content)
        for index in range(len(result)):
            if 'allstar' in result[index][4]:
                items = re.findall(pattern_star, result[index][4])
            else:
                items = [['0', '0', '0']]
            result[index] = list(result[index])
            del result[index][4]
            result[index].extend(items[0])
        return result

    def crawl(self, url, pattern_main, pattern_star, headers=None):
        if headers:
            self.headers.update(headers)
        content = self.download(url)
        info = self.extract(content, pattern_main, pattern_star)
        self.save(info)
