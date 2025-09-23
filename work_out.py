science_books = {
    "A Brief History of Time": {"author": "Stephen Hawking", "quantity": 3},
    "Cosmos": {"author": "Carl Sagan", "quantity": 2},
    "The Selfish Gene": {"author": "Richard Dawkins", "quantity": 4},
    "The Innovators": {"author": "Walter Isaacson", "quantity": 3},
    "Astrophysics for People in a Hurry": {"author": "Neil deGrasse Tyson", "quantity": 5},
    "The Gene: An Intimate History": {"author": "Siddhartha Mukherjee", "quantity": 3},
    "The Structure of Scientific Revolutions": {"author": "Thomas Kuhn", "quantity": 2},
    "Thinking, Fast and Slow": {"author": "Daniel Kahneman", "quantity": 4},
    "Homo Deus": {"author": "Yuval Noah Harari", "quantity": 3},
    "Sapiens: A Brief History of Humankind": {"author": "Yuval Noah Harari", "quantity": 5}
}

mystery_books = {
    "The Da Vinci Code": {"author": "Dan Brown", "quantity": 4},
    "Gone Girl": {"author": "Gillian Flynn", "quantity": 3},
    "The Girl with the Dragon Tattoo": {"author": "Stieg Larsson", "quantity": 5},
    "Sherlock Holmes: The Complete Novels and Stories": {"author": "Arthur Conan Doyle", "quantity": 3},
    "The Silent Patient": {"author": "Alex Michaelides", "quantity": 4},
    "In the Woods": {"author": "Tana French", "quantity": 3},
    "Big Little Lies": {"author": "Liane Moriarty", "quantity": 2},
    "Before I Go to Sleep": {"author": "S.J. Watson", "quantity": 3},
    "The Woman in Cabin 10": {"author": "Ruth Ware", "quantity": 4},
    "The Reversal": {"author": "Michael Connelly", "quantity": 2}
}

fiction_books = {
    "The Alchemist": {"author": "Paulo Coelho", "quantity": 3},
    "1984": {"author": "George Orwell", "quantity": 5},
    "To Kill a Mockingbird": {"author": "Harper Lee", "quantity": 4},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "quantity": 2},
    "The Catcher in the Rye": {"author": "J.D. Salinger", "quantity": 3},
    "Brave New World": {"author": "Aldous Huxley", "quantity": 4},
    "Lord of the Flies": {"author": "William Golding", "quantity": 3},
    "Animal Farm": {"author": "George Orwell", "quantity": 5},
    "Pride and Prejudice": {"author": "Jane Austen", "quantity": 3},
    "The Old Man and the Sea": {"author": "Ernest Hemingway", "quantity": 0}
}
category=["fiction","science","mystery"]

def view_books(book_category):

    for i in book_category:

        print(f"BOOK TITLE : {i} -- AUTHOR :{book_category[i]["author"]} -- QUANTITY :{book_category[i]["quantity"]}")

#VIEW BOOKS IN CART




def view_borrowed_books(ph_num):
    file=open("borrowed_books.txt","r")

    contents=file.read()
    phone=""
    book_name=""
    books_cart=[]

    for i in contents:


        if i.isdigit():

            phone+=i
            if len(phone)==10:

                if phone==ph_num:

                    for j in range(contents.index(phone),len(contents)):

                        if contents[j]!="=":
                        
                            if not contents[j].isdigit():
                                if contents[j]!="\n":

                                    book_name+=contents[j]
                                else:
                                    books_cart.append(book_name)
                                    book_name=""
                        else:
                            break

                    break
                else:
                    phone=""
    
    file.close()
    book_number=1
    print("These are the Books You have Borrowed : \n")
    for i in books_cart:
        if i !="":
            print(f"{book_number}){i}")
            book_number+=1
    return books_cart
view_borrowed_books("7907191810")
books_cart=view_borrowed_books

def return_book(books_cart): 
    
    #book_name=input("Enter the name of the book : ")
    print("\nHere are the categories\nFiction\nScience\nMystery\n")
    while(True):
        category_return=input("Which category book do you want to return : ")
        if category_return.lower() in category:
            break
        else:
            print("\nInvalid Category! Please select valid category")

    if category_return.lower()=="fiction":
        category_return=fiction_books
    elif category_return.lower()=="science":
        category_return=science_books

    elif category_return.lower()=="mystery":
        category_return=mystery_books
    view_books(category_return)
    while(True):
        while(True):
            book_name=input("Enter the name of the book you want to return : ")
            if book_name.lower() not in books_cart:
                print("\nInvalid Book! You have not borrowed this book\n")
            else:
                break
        book_found=False
    
        for i in category_return.copy():

            if book_name.lower()==i.lower():
                category_return[i]["quantity"]+=1
                print(f"\n'{book_name}' has been returned")
                book_found=True
                break
        
        if book_found==False:
            print("\nInvalid Book name!")
        else:
            break
return_book(books_cart)

#     file_1=open("user_details.txt","r")
#     contents=file_1.read()

#     user_entries=contents.split("============================================================================")
#     print(user_entries)

#     contents_list=list(contents.split("\n"))

    

#return_book()
# def return_book():

#     #book_name=input("Enter the name of the book : ")
#     print("\nHere are the categories\nFiction\nScience\nMystery\n")
#     while(True):
#         category_return=input("Which category book do you want to return : ")
#         if category_return.lower() in category:
#             break
#         else:
#             print("\nInvalid Category! Please select valid category")

#     if category_return.lower()=="fiction":
#         category_return=fiction_books
#     elif category_return.lower()=="science":
#         category_return=fiction_books

#     elif category_return.lower()=="mystery":
#         category_return=fiction_books
    
#     while(True):

#         book_name=input("Enter the name of the book : ")
#         book_found=False
    
#         for i in category_return.copy():

#             if book_name.lower()==i.lower():
#                 category_return[i]["quantity"]+=1
#                 print(f"'{book_name}' has been returned")
#                 book_found=True
#                 break
        
#         if book_found==False:
#             print("Invalid Book name!")
#         else:
#             break


# return_book()



# cart=[]

# def borrow_book(book_category):
#     condition=True
#     while (condition==True):

#         book_name=input("Enter the name of the Book : ")
#         for i in book_category.copy():

#             if i.lower()==book_name.lower():
#                 if book_category[i]["quantity"] > 0 :
#                     book_category[i]["quantity"]-=1
#                     cart.append(i)
#                     condition=False
#                     break
        
#         if condition==False:
#             break
#         else:
#             print("Enter a valid book name!")

# borrow_book(fiction_books)

# print(cart)
# print(fiction_books)



# def view_books(book_category):

#     for i in book_category:

#         print(f"BOOK TITLE : {i}: AUTHOR :{fiction_books[i]["author"]}: QUANTITY :{fiction_books[i]["quantity"]}")

# view_books(fiction_books)




# def remove_book(book_category):
#     condition=True
#     while (condition==True):

#         book_name=input("Enter the name of the Book : ")
#         for i in book_category.copy():

#             if i.lower()==book_name.lower():
#                 book_category.pop(i)
#                 print(f"The book '{book_name}' has been removed")
#                 condition=False
#                 break
        
#         if condition==False:
#             break
#         else:
#             print("Enter a valid book name!")
            




# for i in fiction_books:

#     print(i)


# remove_book(fiction_books)

# def add_book(book_category):

#     book_name=input("Enter the name of the book : ")
#     author=input("Enter the name of the author : ")
#     quantity=int(input("Enter the quantity : "))

#     for i in book_category.copy():

#         if book_name.lower()==i.lower():
#             book_category[i]["quantity"]+=quantity
#             print("Book already exist . Quantity updated")
#             break

#     else:
    
#         book_category[book_name]={"author":author,"quantity":quantity}
#         print(f"The book {book_name} has been added")

#     print(book_category)


# add_book(fiction_books)



# while(True):
#     borrow_date=input("Enter the date of borrow :(yy/mm/dd) : ")
#     borrow_date_list=borrow_date.split("/")
#     if "/" not in borrow_date:
#         print("Invalid date")

#     elif int(borrow_date_list[0]) != 25:

#         print("Invalid Year")

#     elif int(borrow_date_list[1]) < 9 or int(borrow_date_list[1]) > 12 :

#         print("Invalid Month" )

#     elif int(borrow_date_list[2]) < 1 or int(borrow_date_list[2]) > 31 :




# print(borrow_date_list)

# from datetime import datetime,timedelta

# today=datetime.today().date()
# return_date=today+timedelta(days=4)

# print(today)

# any_day=datetime.date(2025,7,9)

# print(any_day)

# today=datetime.date.today()

# print(today)
# print(today.year)
# print(today.day)
# print(today.month)

# time_delta=datetime.timedelta(days=6)

# print(today+time_delta)

# user_name=input("Enter name : ")
# ph_num=int(input("Enter phone number : "))


# def check_for_fine(ph_num):

#     file_1=open("user_details.txt","r")
#     contents=file_1.read()
#     new=""
#     date=""
#     if str(ph_num) in contents:

#         ch=contents.index(str(ph_num))
#         for i in range(ch,len(contents)):

#             if contents[i]=="=":

#                 break

#             else:
#                 new+=contents[i]
            
#     if "Return" in new:

#         ind=new.index("Return")

#         for i in range(ind,len(new)):

#             if new[i].isdigit():

#                 date+=new[i]
#     date=datetime.strptime(date, "%Y%m%d")
#     print(date.date())

#     if date.date()<datetime.today().date():

#         print("You have to pay fine")

#     else:
#         print("you dont have to pay fine")

#     #year=[i for in ]

# check_for_fine(ph_num)






# def check_user(ph_num):

#     file_1=open("phone_numbers.txt","r")

#     phone=""

#     contents=file_1.read()
#     print(contents)

#     for i in contents:


#         if i.isdigit():

#             phone+=i
#             if len(phone)==10:

#                 if phone==ph_num:

#                     print("user has borrowed book")
#                     break
#                 else:
#                     phone=""
                    
                

# check_user("6282363119")

