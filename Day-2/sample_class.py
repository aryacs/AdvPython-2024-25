class MyClass:
    def getName(self, n, age):
        self.n = n
        self.age = 35

    def putName(self):
        print("Name", self.n)
        print("Age",self.age)


m1 = MyClass()
print(id(m1))
print(type(m1))
m1.getName("Amar", 19)
m1.putName()