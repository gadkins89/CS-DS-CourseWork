'''
13.10 LAB: Book information (overriding member methods)
Given a Book base class, define a derived class called Encyclopedia with a constructor that
initializes the attributes of the Book class as well as new attributes of the following types:

string to store the edition
int to store the number of pages
Within the derived Encyclopedia class, define a print_info() method that overrides the Book
class' print_info() method by printing the title, author, publisher, publication date, edition,
and number of pages.
'''


#Starter Code

class Book:
    def __init__(self, title, author, publisher, publication_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
   
    def print_info(self):
        print('Book Information:')
        print(f'   Book Title: {self.title}')
        print(f'   Author: {self.author}')
        print(f'   Publisher: {self.publisher}')
        print(f'   Publication Date: {self.publication_date}')


class Encyclopedia(Book):
    def __init__(self, title, author, publisher, publication_date, edition, num_volumes):
        super().__init__(title, author, publisher, publication_date)
        self.edition = edition
        self.num_volumes = num_volumes
    # TODO: Define constructor with attributes:
    #       title, author, publisher, publication_date, edition, num_volumes

    
    def print_info(self):
        print('Book Information:')
        print(f'   Book Title: {self.title}')
        print(f'   Author: {self.author}')
        print(f'   Publisher: {self.publisher}')
        print(f'   Publication Date: {self.publication_date}')
        print(f'   Edition: {self.edition}')
        print(f'   Number of Volumes: {self.num_volumes}')
    # TODO: Define a print_info() method that overrides the print_info()
    #       in the Book class

if __name__ == "__main__":
    title = input("Enter a book title: \n")
    author = input("Enter the author's name: \n")
    publisher = input("Enter the publisher: \n")
    publication_date = input("Enter the publication date: \n")
    
    e_title = input("Enter an encyclopedia title: \n")
    e_author = input("Enter the author's name: \n")
    e_publisher = input("Enter the publisher: \n")
    e_publication_date = input("Enter the publication date: \n")
    edition = input("Enter the edition: \n")
    num_pages = int(input("Enter the number of pages: \n"))
    
    my_book = Book(title, author, publisher, publication_date)
    my_book.print_info()
    
    my_encyclopedia = Encyclopedia(e_title, e_author, e_publisher, e_publication_date, edition, num_pages)
    my_encyclopedia.print_info()