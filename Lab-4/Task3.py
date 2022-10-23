from turtle import title


class Shelves:
    def __init__(self):
        self.head = None
        self.Menu()
    def AddAtStart(self,Address):
        Address.Next = self.head
        self.head = Address
        print("Successfully Added ! ")
        self.Menu()
    def RemoveFromStart(self):
        if self.head == None:
            print("Linked List is already Empty !")
        else:
            self.head = self.head.Next
            print("Successfully Removed ! ")
        self.Menu()
    def AddAtEnd(self,Address):
        random = self.head
        if random == None:
            self.head = Address
        else:
            while random.Next != None:
                random = random.Next
            random.Next = Address
        print("Successfully Added ! ")
        self.Menu()
    def RemoveAtEnd(self):
        random = self.head
        if random == None:
            print("Linked List is already Empty!")
        else:
            while random.Next != None:
                if random.Next.Next == None:
                    break
                random = random.Next
            random.Next = None
            print("Successfully Removed ! ")
        self.Menu()
    def SearchBooks(self):
        book = input("Enter the Name of Book : ")
        random = self.head
        found = False
        while random != None:
            if random.title == book:
                found = True
                break
            else:
                random = random.Next
        print(found)
        self.Menu()
    def PrintBooks(self):
        random = self.head
        while random != None:
            print("**********Books************")
            print("Title   : ",random.title)
            print("Author  : ",random.Author)
            print("Edition : ",random.edition)
            random = random.Next
        self.Menu()
    def CountBooks(self):
        random = self.head
        count = 0
        while  random != None:
            count+=1
            random = random.Next
        print("Total Books Present : ",count)
        self.Menu()
    def Exit(self):
        pass
    def Menu(self):
        print("What do you want to do : \n1 Add at Start \n2 Remove From Start \n3 Add at End \n4 Remove From End \n5 Search Books \n6 Count Books \n7 Display Books \n8 Exit ")
        choice = input("Enter your Choice : ")
        if choice == "1":
            add = Books(input("Enter Name :"),input("Enter Author : "),input("Enter Edition : "))
            self.AddAtStart(add)
        elif choice == "2":
            self.RemoveFromStart()
        elif choice == "3":
            add = Books(input("Enter Name :"),input("Enter Author : "),input("Enter Edition : "))
            self.AddAtEnd(add)
        elif choice == "4":
            self.RemoveAtEnd()
        elif choice == "5":
            self.SearchBooks()
        elif choice == "6":
            self.CountBooks()
        elif choice == "7":
            self.PrintBooks()
        elif choice == "8":
            self.Exit()
        else:
            print("Invalid Input!")
class Books:
    def __init__(self,title,author,edition):
        self.title = title
        self.Author = author
        self.edition = edition
        self.Next = None
Book = Shelves()
