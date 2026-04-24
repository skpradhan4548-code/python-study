# Desine and create an online store for product's (name,Price)
# class product:
#     def __init__(self,name,Price):
#         self.name = name
#         self.Price = Price

#     def get_info(self):
#         print(f"price of the {self.name} is Rs.{self.Price}")

# p1 = product("phone",20_000)
# p2 = product("Laptop",50_000)
# p3 = product("TV",60_000)

# p1.get_info()
    
#=============================================================================
#Trake total product being created :
# class product:
#     count = 0
#     def __init__(self,name,Price):
#         self.name = name
#         self.Price = Price
#         product.count += 1

#     def get_info(self): # THis is the instance method 
#         print(f"price of the {self.name} is Rs.{self.Price}")
#     @classmethod
#     def get_count(cls):
#         print(f"Total product of the store = {cls.count}")


# p1 = product("phone",20_000)
# p2 = product("Laptop",50_000)
# p3 = product("TV",60_000)

# product.get_count()
#===================================================================================
# Create a static method to calculate discount on each product based on a % Parameter
class product:
    count = 0
    def __init__(self,name,Price):
        self.name = name
        self.Price = Price
        product.count += 1

    def get_info(self): # THis is the instance method 
        print(f"price of the {self.name} is Rs.{self.Price}")

    @classmethod
    def get_count(cls):
        print(f"Total product of the store = {cls.count}")

    @staticmethod
    def get_discount(Price,discount):
        print(f"Toala price = {Price-(Price*discount/100)}")


p1 = product("phone",20_000)
p2 = product("Laptop",50_000)
p3 = product("TV",60_000)

# product.get_count()
p1.get_discount(20_000,12)


   