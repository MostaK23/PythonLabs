from edition import Edition


class ElectronicEdition(Edition):

    def __init__(self, title: str, author_last_name: str, link: str, annotation: str):
        super().__init__(title, author_last_name)
        self.link = link
        self.annotation = annotation

    def print_info(self):
        super().print_info()
        print("Ссылка:", self.link)
        print("Аннотация:", self.annotation)
