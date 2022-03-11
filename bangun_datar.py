from abc import abstractmethod, ABC

#Class
class geometri(ABC):
    
    #Abstract Method
    @abstractmethod
    def calculate_area(self):
        pass

    
class Circle(geometri):
    """Kelas untuk membuat sebuah objek lingkaran"""
    
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
            """Method untuk menghitung
            luas lingkaran"""
            print("Area of circle:", self.pi * self.radius * self.radius)
            
            
            
        
class Square(geometri):

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        print("Area of Square:", self.side*self.side)
        
        
        
        
class Triangle(geometri):

    def __init__(self, alas, tinggi):
        self.tinggi = tinggi
        self.alas = alas

    def calculate_area(self):
        print("Area of Square:", (self.alas*self.tinggi)/2)

        
#Function 
def hello():
    print("Hello")
    
def pertambahan(a, b):
    return a+b























    
    