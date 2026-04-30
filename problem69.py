from random import randint

class Train:
    
    def __init__(self, trainno):
        self.trainno = trainno
    
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainno} from {fro} to {to}")
        
    def getstatus(self):
        print(f"Train no: {self.trainno} is running on time")
        
    def getfare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainno} from {fro} to {to} is {randint(222, 5555)}")
        

t = Train(12345)
t.book("Islamabad", "Karachi")
t.getstatus()
t.getfare("islamabad","karachi")
