from book import Book
from electronic_edition import ElectronicEdition
from article import Article


book = Book("Отцы и дети", "Тургенев", 1861, "Русский вестник")
el_edition = ElectronicEdition("Здоровье", "Жариков", "http:\\health.zhar", "Как правильно жить")
article = Article("Анекдоты", "Кулибяко", "Ералаш", "322", 2018)

editions = (book, el_edition, article)

find_name = str(input("Введите имя автора: "))

for edition in editions:
    if edition.author_last_name == find_name:
        edition.print_info()