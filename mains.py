class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books Present in Library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookname):
        if bookname in self.books:
            print(f"You Have been issued {bookname}. Please keep it safe and return it within 30 days")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry, This Book is either not available or has already been issued to someone else. Plese wait until the book is Available")
            return False

    def returnBook(self,bookname):
        self.books.append(bookname)
        print("This for retruning this book! Hope you enjoyed reading it! Have a great day ahead!")

class Student:

    def requestBook(self):
        self.book= input("Enter The name of the book you want to borrow:-->> ")
        return self.book 

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return:-->> ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "PythonNotes"])
    student = Student()
    # centralLibrary.displayAvailableBooks()

    while(True):
        welcomeMsg = '''===== Welcome to the Central Library =====
        Please Choose an Option:
        1 . List all the Books
        2.  Request a book
        3.  Add/Return a book
        4.  Exit the Library
        
        '''
        print(welcomeMsg)

        a = int(input("Enter a choice: "))
        if a == 1 :
            centralLibrary.displayAvailableBooks()

        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())

        elif a == 3:
            centralLibrary.returnBook(student.returnBook())

        elif a == 4:
            print("Thanks for choosing central library! Have a great day ahead")
            exit()
        else:
            print("Invalid Choice")




