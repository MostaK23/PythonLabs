from edition import Edition


class Article(Edition):

    def __init__(self, title: str, author_last_name: str, magazine_title: str, magazine_number: int, publish_year: int):
        super().__init__(title, author_last_name)
        self.magazine_title = magazine_title
        self.magazine_number = magazine_number
        self.publish_year = publish_year

    def print_info(self):
        super().print_info()
        print("Название журнала:", self.magazine_title)
        print("Номер журнала:", self.magazine_number)
        print("Год издания:", self.publish_year)
