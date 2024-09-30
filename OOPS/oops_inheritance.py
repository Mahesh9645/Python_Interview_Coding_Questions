# class Animal():   #parent class
#     def speak(self):
#         return "animal speaks"

# class dog(Animal): #child class
#     def speak(self):
#         return "woof"
    
# class cat(Animal):
#     def speak(self):
#         print("mmm")

# d = dog()  
# print(d.speak())

# c = cat()
# c.speak()

a = "mahesh"
b = ""
for i in a:
    if i not in b:
        b.append(i)
        
print(b)