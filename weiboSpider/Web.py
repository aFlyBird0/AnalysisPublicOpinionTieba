import requests
from lxml import etree


class Web():
    def __int__(self):
        self.url = None
        self.response = None
        self.html_text = None
        self.html_content = None
        self.tree = None

    def set_url(self, u):
        self.url = u

    def get_url(self):
        return self.url

    def get_response(self):
        self.response = requests.get(self.url)

    def get_html_text(self):
        self.html_text = self.response.text

    def get_etree(self):
        self.tree = etree.HTML(self.html_text)

    def get_html_content(self):
        self.html_content = self.response.content


if __name__ == '__main__':
    w = Web()

    w.set_url("https://s.weibo.com/weibo?q=杭州电子科技大学&Refer=g&page=1")
    print(w.url)
