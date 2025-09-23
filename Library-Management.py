from datetime import datetime,timedelta


print("\n📚 Welcome to the Library — A gateway to imagination, knowledge, and endless possibilities! 📚")
print("================================================================================================\n")

# ALL AVAILABLE BOOKS
# ============================
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
    "The Old Man and the Sea": {"author": "Ernest Hemingway", "quantity": 4}
}
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

category=["fiction","science","mystery"]
choice_options=["yes","no"]

# FUNCTIONS
#===========

# Remove a book
# =============

def remove_book(book_category):
    condition = True
    while condition:
        book_name = input("Enter the name of the Book : ")
        for i in book_category.copy():
            if i.lower() == book_name.lower():
                book_category.pop(i)
                print(f"The book '{book_name}' has been removed")
                condition = False
                break
        if condition:
            print("Enter a valid book name!")

# Add a book
# ==========

def add_book(book_category):

    book_name=input("Enter the name of the book : ")
    author=input("Enter the name of the author : ")
    quantity=int(input("Enter the quantity : "))

    for i in book_category.copy():

        if book_name.lower()==i.lower():
            book_category[i]["quantity"]+=quantity
            print(f"'{book_name}' already exist . Quantity updated")
            break

    else:
    
        book_category[book_name]={"author":author,"quantity":quantity}
        print(f"The book {book_name} has been added")


# BORROW BOOK
#============

cart=[]

def borrow_book(book_category):
    view_books(book_category)
    #file_1=open("C:\Users\HP\OneDrive\Desktop\Python_Works\MINI_PROJECT\user_details.txt","a")
    condition=True
    while (condition==True):

        book_name=input("Enter the name of the Book : ")
        for i in book_category.copy():

            if i.lower()==book_name.lower():

                if i.lower() in cart:

                    print("\nYou have already borrowed this book and can't borrow more than one copy!")
                    print("Please select another book!\n")
                    break
                else:
                    if book_category[i]["quantity"] > 0 :
                        book_category[i]["quantity"]-=1
                        cart_value=i.lower()
                        file_1=open("user_details.txt","a")
                        file_1.write(cart_value)
                        file_1.write("\n")
                        file_1.close()
                        cart.append(cart_value)
                        file=open("borrowed_books.txt","a")
                        file.write(f"{cart_value}\n")
                        file.close()
                        #file_1.write(cart)
                        condition=False
                        break
        
        if condition==False:
            break
        else:
            print("Enter a valid book name!")


# View BOOK DETAILS
#==================

def view_books(book_category):

    for i in book_category:

        print(f"BOOK TITLE : {i} -- AUTHOR :{book_category[i]["author"]} -- QUANTITY :{book_category[i]["quantity"]}")

#VIEW BOOKS IN CART
#===================

def view_cart_books(cart):

    print("\nHere is the List of Books you have Borrowed\n")
    book_number=1

    for i in cart:
        print(f"{book_number}) {i}")
        book_number+=1

    print("\n")

# ADD USER DETAILS
#============================================

def add_user_details():
    user_name=input("Enter your name : ")
    phone_number=int(input("Enter your phone number :"))
    #e_mail=input("Enter your email : ")
    address=input("Enter your area of residence : ")
    borrow_date=datetime.today().date()

    file_1=open("user_details.txt","a")
    file_1.write(f"User_Name : {user_name}\n")
    file_1.write(f"Phone_Number : {str(phone_number)}\n")
    #file_1.write(f"E-Mail : {e_mail}\n")
    file_1.write(f"Place of residence : {address}\n")
    file_1.write(f"Borrow Date : {borrow_date}\n\n")
    file_1.write("Books Borrowed:\n")
    file_1.close()


# CHECK FOR FINE
# ==================

def check_for_fine(ph_num):

    file_1=open("user_details.txt","r")
    contents=file_1.read()
    new=""
    date=""
    if str(ph_num) in contents:

        ch=contents.index(str(ph_num))
        for i in range(ch,len(contents)):

            if contents[i]=="=":

                break

            else:
                new+=contents[i]
    # else:

    #     print("\nYou have Not Borrowed any books from the library.\nYour name and phone number is not registered in our log\n")
    #     exit()
                
    if "Return" in new:

        ind=new.index("Return")

        for i in range(ind,len(new)):

            if new[i].isdigit():

                date+=new[i]
    date=datetime.strptime(date, "%Y%m%d")

    if date.date()<datetime.today().date():

        print("\nYou have to pay fine of 100₹\n")

    else:
        print("\nyou dont have to pay fine\n")


# RETURN BOOK
# ================

def return_book():

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

        book_name=input("Enter the name of the book you want to return : ")
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

# CHECK FOR USER
#==================

def check_user(ph_num):

    file_1=open("phone_numbers.txt","r")

    phone=""

    contents=file_1.read()
    flag=False

    for i in contents:


        if i.isdigit():

            phone+=i
            if len(phone)==10:

                if phone==ph_num:

                    print("user has borrowed book")
                    flag=True
                    break
                else:
                    phone=""
    if flag==False:
        print("\nThis user has not registered in the library Log!\n")
        exit()
    file_1.close()
    
# VIEW BORROWED BOOKS
#=====================

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

                


#=============================================================================================================================================

# ADMIN SIDE
#===============================

while(True):
    admin_or_user=input("Are you an Admin or Customer : ")
    if admin_or_user.lower() == "admin" or admin_or_user.lower()=="customer":
        break
    else:

        print("Please enter a valid input (admin/customer)") 

number_of_try=3

if admin_or_user.lower()=="admin" :

    Admin_id=input("Please enter your Admin ID : ")

    while(True):

        if Admin_id.lower() != "admin@123" :

            print(f"\nPlease enter a valid Admin ID !!! , {number_of_try-1} more tries\n")
            number_of_try-=1
            #Admin_id=input("Please enter your Admin ID : ")
            
            if number_of_try==0:
                
                print("\nYou have been Logged Out. Please try again later\n")
                exit()

            else:

                Admin_id=input("Please enter your Admin ID : ")

        else:
            break

    print("\nYou have successfully logged in as ADMIN")
    print("===========================================\n")

    ch_while_loop="yes"

    while(ch_while_loop=="yes"):
        #choice_admin=input("\nDo you want to add or remove book from the Library (add/remove) : ")
        print("Here are the categories : \n Fiction \n Science \n Mystery")

        category_choice=input(f"In which category do you want to perform updation :")

        if category_choice.lower() not in category:
            print("\nThis category is not available. Please select one from the Given List\n")
            continue

        choice_admin=input("\nDo you want to add or remove book from the Library (add/remove) : ")






        print("\nHere is the current list of books")
        print("====================================\n")
                    

        if category_choice.lower()== "fiction" :

            for i in fiction_books:

                print(f"Name : {i} Author : {fiction_books[i]["author"]} Quantity : {fiction_books[i]["quantity"]}")

        #book_choice=input(f"\nWhich book do you want to {choice_admin} :")
                    
            if choice_admin.lower()=="remove" :

                remove_book(fiction_books)
                ch_while_loop=input("Do you want to continue (yes/no): ")

            elif choice_admin.lower()=="add" :

                add_book(fiction_books)
                ch_while_loop=input("Do you want to continue (yes/no): ")

        elif category_choice.lower()== "science" :
                    
            for i in science_books:

                print(f"Name : {i} Author : {science_books[i]["author"]} Quantity : {science_books[i]["quantity"]}")

        #book_choice=input(f"Which book do you want to {choice_admin} :")
                    
            if choice_admin.lower()=="remove" :
                        
                remove_book(science_books)
                ch_while_loop=input("Do you want to continue (yes/no): ")

            elif choice_admin.lower()=="add":

                add_book(science_books)
                ch_while_loop=input("Do you want to continue (yes/no): ")

        elif category_choice.lower()== "mystery" :

            for i in mystery_books:

                print(f"Name : {i} Author : {mystery_books[i]["author"]} Quantity : {mystery_books[i]["quantity"]}")

        #book_choice=input(f"Which book do you want to {choice_admin} :")

            if choice_admin.lower()=="remove" :
                        
                remove_book(mystery_books)
                ch_while_loop=input("Do you want to continue (yes/no): ")

            elif choice_admin.lower()=="add":

                add_book(mystery_books)
                ch_while_loop=input("Do you want to continue (yes/no): ")

#==========================================================================================================================================
# CUSTOMER SIDE
#===============
else :

    print("\nYou have logged in as customer\n")

    while(True):

        borrow_return_choice=input("\nAre you here to borrow or return a book : ")
        if borrow_return_choice.lower() == "borrow" or borrow_return_choice.lower()=="return":
            break
        else:
            print("Please enter a valid choice (borrow/return)")

    if borrow_return_choice.lower()=="borrow":

        user_name=input("Enter your name : ")
        while(True):
            phone_number=int(input("Enter your phone number :"))
            if len(str(phone_number))!=10:
                print("Invalid Phone number! Should have 10 digits")
            else:
                break
        #e_mail=input("Enter your email : ")
        address=input("Enter your area of residence : ")
        borrow_date=datetime.today().date()

        file_1=open("user_details.txt","a")
        file=open("borrowed_books.txt","a")
        file.write(f"{str(phone_number)}\n")
        file.close()
        file_1.write(f"User_Name : {user_name}\n")
        file_1.write(f"Phone_Number : {str(phone_number)}\n")
        #file_1.write(f"E-Mail : {e_mail}\n")
        file_1.write(f"Place of residence : {address}\n")
        file_1.write(f"Borrow Date : {borrow_date}\n\n")
        file_1.write("Books Borrowed:\n")
        file_1.close()
        file_2=open("phone_numbers.txt","a")
        file_2.write(f"User_Name : {user_name}\n")
        file_2.write(f"Phone_Number : {str(phone_number)}\n")
        file_2.close()

        print("\nYou can borrow a Maximum of 3 BOOKS")

        print("\nHere is a list of categories currently available\nFiction\nScience\nMystery\n")

        while(True):

            category_choice_customer=input("Which category would you like to browse in : ")

            if category_choice_customer.lower() not in category:

                print("\nInvalid category! Please select a category from the given list\n")

            else:

                print(f"Here is list of available books in the '{category_choice_customer}' category\n")
                if category_choice_customer.lower()=="fiction":
                    category_choice_customer=fiction_books
                    #view_books(fiction_books)

                elif category_choice_customer.lower()=="science":
                    category_choice_customer=science_books
                    #view_books(science_books)

                elif category_choice_customer.lower()=="mystery":
                    category_choice_customer=mystery_books
                    #view_books(mystery_books)

                #book_choice_customer=input("Which book do you want to borrow : ")

                break

        i=0
        while(True):
            #book_choice_customer=input("Which book do you want to borrow : ")

            borrow_book(category_choice_customer)
            i+=1
            while(True):
                borrow_continue_choice=input("\nDo you want borrow any more books (yes/no): ")
                if borrow_continue_choice.lower() not in choice_options:
                    print("\nInvalid Input (yes/no)\n")
                else:
                    # file_1=open("user_details.txt","a")
                    # file_1.write(cart)
                    # file_1.close()
                    break
            if borrow_continue_choice.lower() == "no" :
                #print(f"\n{view_cart_books(cart)}")
                view_cart_books(cart)
                while(True):
                    number_of_days=int(input("How many days you want to borrow these books :(maximum of 21 days): "))
                    if number_of_days >0 and number_of_days <= 21 :
                        break
                    else:
                        print("\nInvalid Input!You can only borrow for maximum of 21 days!\n")
                return_date=borrow_date+timedelta(days=number_of_days)
                print(f"\nYou are supposed to return the book by {return_date}! Otherwise a fine of 100₹ has to be paid!\n")
                file_1=open("user_details.txt","a")
                file_1.write(f"\nReturn Date : {return_date}\n\n")
                file_1.write("============================================================================\n")
                file_1.close()
                file_2=open("phone_numbers.txt","a")
                file_2.write("============================================================================\n")
                file_2.close()
                file=open("borrowed_books.txt","a")
                file.write("============================================================================\n")
                file.close()
                exit()
            elif i>=3 :

                print("You can only have a total of 3 Books")
                #print(f"\n{view_cart_books(cart)}")
                view_cart_books(cart)
                while(True):
                    number_of_days=int(input("How many days you want to borrow these books :(maximum of 21 days): "))
                    if number_of_days >0 and number_of_days <= 21 :
                        break
                    else:
                        print("\nInvalid Input!You can only borrow for maximum of 21 days!\n")

                return_date=borrow_date+datetime.timedelta(days=number_of_days)
                file_1=open("user_details.txt","a")

                file_1.write(f"\nReturn Date : {return_date}\n\n")
                file_1.write("==================================================================================\n")
                file_1.close()
                exit()

            while(True):

                switch_category=input("Do you want to switch category :(yes/no): ")
                if switch_category.lower() not in choice_options:

                    print("Enter a valid Input (yes/no)!")
                    
                else:
                    break
            if switch_category.lower()=="no":

                continue
            else:
                print("\nFiction\nScience\nMystery")
                while(True):
                    category_choice_customer=input("\nWhich category do you want :")
                    if category_choice_customer.lower() not in category:
                        print("\nPlease enter a valid Category\n")
                        continue
                    else:
                        break
                if category_choice_customer.lower()=="fiction":
                    category_choice_customer=fiction_books

                elif category_choice_customer.lower()=="science":
                    category_choice_customer=science_books

                elif category_choice_customer.lower()=="mystery":
                    category_choice_customer=mystery_books
            print("number of days")
    else:

        #   RETURN BOOK
        #====================== 

        user_name=input("Enter your name : ")

        while(True):
            ph_num=int(input("Enter your phone number :"))
            ph_num=str(ph_num)
            if len(str(ph_num))!=10:
                print("Invalid Phone number! Should have 10 digits")
            else:
                break
        check_user(ph_num)
        check_for_fine(ph_num)
        view_borrowed_books(ph_num)

        return_choice="yes"

        while(return_choice=="yes"):

            return_book()
            return_choice=input("Do you have any more books to return (yes/no) : ")


        

