# (i)

#soln
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

book1 = Book("Python Programming", "Anitah", 300)
book1.display_info()


# (ii)

#soln

class EBook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def display_info(self):
        super().display_info()
        print(f"Format: {self.format}")
ebook1 = EBook("Advanced Python", "Anitah", 300)
ebook1.display_info()



#(iii)

# soln

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_title_author(self):
        return f"Title: {self.title}, Author: {self.author}"


book2 = Book("Data Science", "Anitah Sisi", 400)

# Get the title and author
print(book2.get_title_author())









# (iV)

# (a)

# Class: A Class is like an object constructor, or a "blueprint" for creating objects.

# (b)   

#  Object: An instance of a class that contains data and methods defined by the class.
