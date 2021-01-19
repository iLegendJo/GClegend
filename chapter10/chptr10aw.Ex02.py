class Book():
    def __init__(self,book_title,author_name,publisher_name):
        self.book_title = book_title
        self.author_name = author_name
        self.publisher_name = publisher_name

    #**********************************************************************************
    # defining Accessor method or Getter Methods
    def get_book_title(self):   # accessor method
        '''Returns the instance variable _book_title. '''
        return self.book_title

    def get_author_name(self): # accessor method
        '''Returns the instance variable _author_name. '''
        return self.author_name

    def get_pub_name(self):   # accessor method
        '''Returns the instance variable _first_name. '''
        return self.publisher_name

    def __str__(self):
        # return the state of the book object
        return "Title: " + self.book_title + " Author: " + self.author_name + " Publisher: " + self.publisher_name
    # ******************************************************************************

    def set_book_title(self,book_title): # mutator method
        '''Assign a value to the instance variable _book_title. '''
        self.book_title = book_title

    def set_author_name(self,author_name):
        '''Assign a value to the instance variable _author_name'''
        self.author_name = author_name

    def set_publisher_name(self,publisher_name):
        '''Assign a value to the instance variable _publisher_name'''
        self.publisher_name = publisher_name


def main():



    #print(Book.__doc__) # prints the docstring for the class
    book1 = Book("Green Eggs and Ham", "Dr. Seuss","Penguin Random House LLC" )
    print(book1)


if __name__ == "__main__":
    main()