from BookController import BookController
from BookService import BookService
from BookEntity import Book

if __name__ == "__main__":
    # bookController = BookController()
    # print(bookController)
    # bookService = BookService()

    # book = Book(
    #     bookId=99, 
    #     bookName="테스트 도서!!"
    # )

    # print(book.bookId)
    # print(book.bookName)
    # book.setAuthor("테스트 저자")
    # print(book.author)

    # print(book)

    BookController.addBookRequest()