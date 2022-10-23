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
    def AddAtStart(self,Address):
        Address.Next = self.head
        self.head = Address
        print("Successfully Added ! ")
    def RemoveFromStart(self):
        if self.head == None:
            print("Linked List is already Empty !")
        else:
            self.head = self.head.Next
            print("Successfully Removed ! ")
    def AddAtEnd(self,Address):
        random = self.head
        if random == None:
            self.head = Address
        else:
            while random.Next != None:
                random = random.Next
            random.Next = Address
        print("Successfully Added ! ")
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
    def CountSubjects(self):
        random = self.head
        count = 0
        while  random != None:
            count+=1
            random = random.Next
        print("Total Subjects Present : ",count)
    def PrintSubjects(self):
        random = self.head  
        while random != None:
            print("**********Books************")
            print("Title   : ",random.title)
            print("Credits  : ",random.credit)
            print("Semester : ",random.semester)
            print("Instructor : ",random.instructor)
            random = random.Next
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
    def Exit(self):
        pass
Course1 = Subject("DSA",4,3,"Shehraz Anjum")
Course2 = Subject("PS",3,3,"Mudassar Jatala")
Course3 = Subject("LA",3,3,"Israr Khan")
Course4 = Subject("DM",3,3,"Usama Manzoor")
Course5 = Subject("PoS",3,3,"Asim Raza")
Course6 = Subject("GB",2,3,"Zameer Nawaz")
Courses = Linked_List()
Courses.AddAtStart(Course1)
Courses.AddAtStart(Course2)
Courses.AddAtStart(Course3)
Courses.AddAtEnd(Course4)
Courses.AddAtEnd(Course5)
Courses.AddAtPosition(3,Course6)
Courses.PrintSubjects()
print("*************************")
Courses.CountSubjects()
Courses.RemoveAtEnd()
Courses.RemoveFromStart()
print("****************************")
Courses.PrintSubjects()
Courses.RemoveFromPosition(4)
Courses.PrintSubjects()