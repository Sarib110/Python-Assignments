
class Community:
    def __init__(self):
        self.head = None
    def AddAtStart(self,Address):
        Address.Next = self.head
        self.head = Address
    def RemoveFromStart(self):
        self.head = self.head.Next
    def PrintCommunity(self):
        random = self.head
        while random != None:
            print(random.number)
            random = random.Next
class House:
    def __init__(self,number):
        self.Next = None
        self.number = number
H1 = House(1)
H2 = House(2)
H3 = House(3)
C = Community()
C.AddAtStart(H1)
C.AddAtStart(H2)
C.AddAtStart(H3)
C.PrintCommunity()
C.RemoveFromStart()
print("After Removing From Start : ")
C.PrintCommunity()
C.RemoveFromStart()
print("After Removing From Start : ")
C.PrintCommunity()