from sorts import *
import random

class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __lt__(self,other):
        return self.author < other.author

    def __le__(self,other):
        return self.author <= other.author

    def __gt__(self,other):
        return self.author > other.author

    def __ge__(self,other):
        return self.author >= other.author

    def __eq__(self,other):
        return self.author == other.author

    def __str__(self):
        return self.title + " by " + self.author

if __name__ == '__main__':
    book1 = Book("mrt","mrt")
    book2 = Book("grt","grt")
    print(dir(book1))
    print(book1==book2)
    print (book1>book2)

    library = []
    author_names = ['Jill Stein', 'Harambe', 'George R.R. Martin', 'Rick Astley']
    titles = ['Communist Manifesto', 'War and Peace', 'Nineteen Eighty-Four', 'Moby Dick']
    for time in range(10):
        book = Book(random.choice(titles),random.choice(author_names))
        library.append(book)

    for book in library:
        print(str(book))
    library = merge_sort(library)
    print()
    print('Sorting...')
    for book in library:
        print(str(book))
