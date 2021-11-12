from edition import Edition


class Book(Edition):

    def __init__(self, title: str, author_last_name: str, publish_year: int, edition_name: str):
        super().__init__(title, author_last_name)
        self.edition_name = edition_name
        self.publish_year = publish_year

    def print_info(self):
        super().print_info()
        print("Год публикации:", self.publish_year)
        print("Издательство:", self.edition_name)
