# A bike Rental system
class A:
    def __init__(self,stock):
        self.stock=stock
    def f1(self):
        print("total bike ",self.stock)
    def f2(self,a):
        if(a<=0):
            print("enter the  value a is grather than 0")
        elif(a>self.stock):
            print("enter the value less than stock")
        else:
            self.stock=self.stock-a
            print("total price",a*100)
            print("total bike",self.stock)
obj=A(100)
while True:
    b=int(input(''' 
                1.Display stock
                2.Bent bike
                3.Exit 
                :-'''))
    if(b==1):
            obj.f1()
    elif(b==2):
            n=int(input("enter the qty :- "))
            obj.f2(n)
    else: 
        exit


   
        
