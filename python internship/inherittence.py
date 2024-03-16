# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def make_sound(self):
#         return "kikiki"
# d1=Dog("soumbi")
# print(d1.name)
# print(d1.make_sound())



# class Brands:
#     brand_name_1 = "Amazon"
#     brand_name_2 = "flipkart"

# class products(Brands):
#     prod_1 = "e store"
#     prod_2 = "online market"

# obj_1 = products()
# print(obj_1.brand_name_1+ obj_1.prod_1)

class Brands:
    brand_name_1 = "Amazon"
    brand_name_2 = "flipkart"

class products:
    prod_1 = "e store"
    prod_2 = "online market"

class popularity(Brands,products):
    prod_1_popularity = 100
    prod_2_popularity = 80

obj_1 = popularity()
print(obj_1.brand_name_1+" is an "+obj_1.prod_1)

