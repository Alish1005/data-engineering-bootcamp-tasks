import csv

#Class Object
class Item:
    all=[];
    pay_rate=0.8
    #constructor with paramenters
    #to specify the dataType of the attrib use attr:datatype
    def __init__(self,name:str='',price:int=1,quantity:int=1): #the values that are on the parameter are the deafult value for each attribute
        print(f"I'am here! {name} price is {price}")
        # throwing Exception if any of this are false
        #gives limit to each attr.
        assert price>=0,f"Price can't be below zero"
        assert  quantity>=0,f"Quantity can't be below zero"

        #initalize attr. : _attr is a private attr.
        self.__name=name
        self.__price=price
        self.__quantity=quantity

        #Actions to execute
        Item.all.append(self)

#Getters and Setters
    #Getters - Read-Only
    @property
    def name(self):
        return self.__name
    #Setters - Write-Only
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value
    @property
    def rate(self):
        return self.__pay_rate

    @rate.setter
    def rate(self, value):
        self.__rate = value
    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value



    #Object function
    def calculate_total(self):
        return self.price * self.quantity

    #function that set the price after descount
    def apply_discount(self):
        self.price=self.price*self.pay_rate
        return  self.price
    #it is the same of the toString() method in java
    def __repr__(self):
        return f"{self.__name} {self.__class__.__name__} prise is {self.price} and the quantity we have {self.quantity}"
    @classmethod
    def instantiate_from_csv(cls):
        with open('task5_pract.csv', 'r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        #count in float
        if isinstance(num,float):
            return num.is_integer()
        else:
            return isinstance(num,int)

