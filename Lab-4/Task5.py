from operator import pos


class Subject:
    def __init__(self,title,credits,semester,instructor):
        self.title = title
        self.credit = credits
        self.semester = semester
        self.instructor = instructor
        self.Next = None
class Linked_List:
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
    def SearchSubjects(self):
        book = input("Enter the Name of Subject : ")
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
    def CountSubjects(self):
        random = self.head
        count = 0
        while  random != None:
            count+=1
            random = random.Next
        print("Total Subjects Present : ",count)
        self.Menu()
    def PrintSubjects(self):
        random = self.head  
        while random != None:
            print("**********Books************")
            print("Title   : ",random.title)
            print("Credits  : ",random.credit)
            print("Semester : ",random.semester)
            print("Instructor : ",random.instructor)
            random = random.Next
        self.Menu()
    def AddAtPosition(self,position,Address):
        random = self.head
        counter = 0
        found = True
        if position < 2:
            self.AddAtStart(Address)
            return ""
        while counter+2 < position:
            if random != None:
                random = random.Next
                counter+=1
            else:
                found = False
                break
        if found:
            Address.Next = random.Next
            random.Next = Address
            print("Added Successfully!")
        else:
            print("Limit Exceed !")
        self.Menu()
    def RemoveFromPosition(self,position):
        random = self.head
        counter = 0
        found = True
        if position < 2:
            self.RemoveFromStart()
            return ""
        while counter+2 < position:
            if random != None:
                random = random.Next
                counter+=1
            else:
                found = False
                break
        if found:
            if random.Next != None:
                random.Next = random.Next.Next
                print("Removed Successfully!")
            else:
                print("Limit Exceed")
        else:
            print("Limit Exceed !")
        self.Menu()
    def ValueAtIPosition(self,position):
        random = self.head
        count = 1
        found = False
        while random != None:
            if count == position:
                found = True
                break
            else:
                count += 1
                random = random.Next
        if found:
            print("Data Found : ")
            print("Title : ",random.title,"\nCredits : ",random.credit,"\nSemester : ",random.semester,"\nInstructor : ",random.instructor)
        else:
            print("No Data Found")
        self.Menu()
    def Exit(self):
        pass
    def Menu(self):
        print("What do you want to do : \na Add at Start \nb Remove From Start \nc Add at End \nd Remove From End \ne Add At Position \nf Remove From Position \ng Value at Position \nh Search Subjects \ni Size \nj Display Subjects \nk Exit ")
        choice = input("Enter your Choice : ")
        if choice == "a":
            add = Subject(input("Enter Title :"),input("Enter Credits : "),input("Enter Semester : "),input("Instructor : "))
            self.AddAtStart(add)
        elif choice == "b":
            self.RemoveFromStart()
        elif choice == "c":
            add = Subject(input("Enter Title :"),input("Enter Credits : "),input("Enter Semester : "),input("Instructor : "))
            self.AddAtEnd(add)
        elif choice == "d":
            self.RemoveAtEnd()
        elif choice == "h":
            self.SearchSubjects()
        elif choice == "i":
            self.CountSubjects()
        elif choice == "j":
            self.PrintSubjects()
        elif choice == "e":
            add = Subject(input("Enter Title :"),input("Enter Credits : "),input("Enter Semester : "),input("Instructor : "))
            self.AddAtPosition(int(input("Enter Position : ")),add)
        elif choice == "f":
            self.RemoveFromPosition(int(input("Enter Position : ")))
        elif choice == "g":
            self.ValueAtIPosition(int(input("Enter the Position : ")))
        elif choice == "k":
            self.Exit()
        else:
            print("Invalid Input!")
Linked_List()