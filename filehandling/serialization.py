import pickle

class student:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)

s1=student("mohit",56)
s2=student("gole",45)

std=[s1,s2]

f=open("Emploee11223.dat","wb")
pickle.dump(std,f)
f.close()  
