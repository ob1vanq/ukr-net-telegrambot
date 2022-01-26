from typing import Union

import requests
from bs4 import BeautifulSoup


class parser:

    politics = "https://www.ukr.net/news/politics.html"
    economics = "https://www.ukr.net/news/economics.html"
    main = "https://www.ukr.net/news/main.html"

    @staticmethod
    def __get_selection(selection):

        time = selection.find_all("time", class_="im-tm")[0]
        news = selection.find_all("a", class_="im-tl_a")[0]
        publisher = selection.find_all("div", class_="im-pr")[0]
        link = news.get("href")
        id = news.get("data-count").split(",")[0] + time.text.replace(":", "")

        return dict(id=id, publisher=publisher.text, news=news.text, link=link)

    @staticmethod
    def update(url: Union[str, None] = None):

        if url is None:
            url = parser.main

        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, "lxml")
        news = dict()

        for selection in soup.find_all("section", class_="im"):
            data = parser.__get_selection(selection)
            news.update({data["id"]: data})

        return news

