class Edition:

    def __init__(self, title: str, author_last_name: str):
        self.title = title
        self.author_last_name = author_last_name

    def print_info(self):
        print("Название:", self.title)
        print("Автор:", self.author_last_name)
