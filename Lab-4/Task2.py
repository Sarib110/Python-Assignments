
class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
        self.Next = None
class Data:
    def __init__(self):
        self.head = None
    def AddAtEnd(self,Address):
        random = self.head
        if random == None:
            self.head = Address
        else:
            while random.Next != None:
                random = random.Next
            random.Next = Address
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
    def PrintData(self):
        random = self.head
        while random != None:
            print("**********Data************")
            print("Name : ",random.name)
            print("Age  : ",random.age)
            print("City  : ",random.city)
            random = random.Next
H1 = Person("Sarib",20,"AJK")
H2 = Person("Mushtaq",30,"Lahore")
H3 = Person("Sohail",25,"Karachi")
D = Data()
D.AddAtEnd(H1)
D.AddAtEnd(H2)
D.AddAtEnd(H3)
D.PrintData()
print("\nAfter Removing From End : \n")
D.RemoveAtEnd()
D.PrintData()