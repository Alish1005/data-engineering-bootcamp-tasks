from task5_pract_1 import Item;

#To inherite a class in another class
class Phone(Item):
    #recall the constructor method
    def __init__(self, name: str = '', price: int = 1, quantity: int = 1, broken_phones: int = 0):
        #super function is the constructor of the parent class we use it instead of copy past the code
        super().__init__(name, price, quantity)
        print(f"I'am here! {name} price is {price}")
        #throwing Exception if any of this are false
        assert  broken_phones<=quantity,f"Broken phones can't be more than its total quantity"

        #self.name=name we can ignor in the present of the super method
        #self.price=price we can ignor in the present of the super method
        #self.quantity=quantity we can ignor in the present of the super method
        self.broken_phones=broken_phones
        Phone.all.append(self)


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
#print(item2.name,item2.price,item2.quantity)
print(item2.calculate_total())
print(item2.price)

#it will print all the attr. of the object
print(item2.__dict__)
#call ther toString() method
print(item2.__repr__())

print(item2.apply_discount())
Item.instantiate_from_csv()
print(Item.all)
print(Item.is_integer(5))
#_______________Phone test part_____________________
phone1=Phone('IphoneX',900,12,1)
phone2=Phone('Iphone7',500,23,6)
phone3=Phone('Iphone13',1200,11,3)
phone4=Phone('Iphone14 pro',1400,21,3)
phone5=Phone('Iphone11',1000,12,5)
print(phone1.calculate_total())
phone5.name='sdsa'
print(phone5.name)
