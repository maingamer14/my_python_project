##### Category theory  ######
#1. Given a set of objects
#2. Given the definition of Homset
#3. Give the definition of composition
#4. Verificiation
 
class Category:
    def __init__(self, objC, homset, composition):
        self.objC = objC
        self.homset = homset
        self.composition = composition