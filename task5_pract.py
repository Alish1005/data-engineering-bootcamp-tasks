#Class Object
class Item:
    pay_rate=0.8
    #constructor with paramenters
    #to specify the dataType of the attrib use attr:datatype
    def __init__(self,name:str='',price:int=1,quantity:int=1): #the values that are on the parameter are the deafult value for each attribute
        print(f"I'am here! {name}",name)

        #gives limit to each attr.
        assert price>=0,f"Price can't be below zero"
        assert  quantity>=0,f"Quantity can't be below zero"

        #initalize attr.
        self.name=name
        self.price=price
        self.quantity=quantity

        #Actions to execute
        ##Item.all.append(self)

    #Object function
    def calculate_total(self):
        return self.price * self.quantity

    #function that set the price after descount
    def apply_discount(self):
        self.price=self.price*self.pay_rate
        return  self.price
    #it is the same of the toString() method in java
    def __repr__(self):
        return f"{self.name} Item prise is {self.price} and the quantity we have {self.quantity}"

#create item object with no parameter constructor
item1=Item()

#set class attr. values
item1.name='phone'
item1.price=100
item1.quantity=5
print(item1.calculate_total())

#create item object with parameters constructors
item2=Item('Laptop',1200,3);
item2.has_numpad=False
print(item2.name,item2.price,item2.quantity)
print(item2.calculate_total())
print(item2.pay_rate)

#it will print all the attr. of the object
print(item2.__dict__)
#call ther toString() method
print(item2.__repr__())

print(item2.apply_discount())
##print(Item.all)