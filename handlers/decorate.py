class decorator:

    @staticmethod
    def italic(string: str):
        return "<i>" + string + "</i>"

    @staticmethod
    def href(string: str, link: str):
        return f"<a href='{link}'>" + string + "</a>"

    @staticmethod
    def decorate(link, news, publisher, title):

        tag = "ГоловніНовини"
        if title == "economics":
            tag = "Економіка"
        elif title == "politics":
            tag = "Політика"

        string = f"#{tag}\n\n{decorator.italic(publisher)}: {decorator.href(news, link)}\n\n" \
                 f"{decorator.href('Ukraine Post', 'https://t.me/ukraine_post_main')}"
        return string
