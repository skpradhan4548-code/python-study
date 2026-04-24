class laptops:
    storage_type ="SSD"

    def __init__(self,RAM,Storage):
        self.RAM = RAM
        self.Storage = Storage

    @classmethod    # That function can change the behavior of the class
    def get_storage_type(cls): # This is a class method
       print(f"storage type = {cls.storage_type}")
    
    def get_info(self):  # instance method
      print(f"The laptop RAM is {self.RAM} and the storage of the laptop is {self.Storage} and the storage type is {self.storage_type}")

    @staticmethod # That function can be the change the method's in static method
    def calc_discount(price,discount):
       final_price = price -(discount*price/100)
       print(f"Discounted Price = {final_price}")
    

L1 = laptops("16 gb","512 ")
L2 = laptops("8 gb","256")

L2.get_info()
laptops.get_storage_type() # This is called class name call
L1.calc_discount(50_000, 10)  # fnx => (price, discount) => Final price
#=====================================================================================================================
# L1.get_storage_type() # This is called object class call                                                           =
#                       [ why that's happening beacuse the object calll are the -                                    =
#                       { Higher prierity than the class so the object class have the all the element if class]      =
#=====================================================================================================================
