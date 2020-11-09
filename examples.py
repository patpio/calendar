class Auto:
    def __init__(self, name):
        self.name = name
        self.dupa = 'xD'


bmw = Auto('BMW')
print(bmw.name)
attr = 'dupa2'
print(getattr(bmw, attr, None))
a = 20
print(10 < a < 30)
print(10 < a and a < 30)
print(a in range(10, 30))
