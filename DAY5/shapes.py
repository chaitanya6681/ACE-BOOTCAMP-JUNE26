from abc import abstractmethod
class Shapes:
    @abstractmethod #if want to make a method abstract then we have to use @abstractmethod decorator
    def area(self):
        pass
    @abstractmethod   
    def perimeter(self):
        pass
class Rectangle(Shapes):
    def area(length,breadth):
        return length*breadth
    def perimeter(length,breadth):
        return 2*(length+breadth)
class Square(Shapes):
    def area(side):
        return side*side
    def perimeter(side):
        return 4*side
class Triangle(Shapes):
    def area(base,height):
        return 0.5*height*base
    def perimeter(s1,s2,s3):
        return s1+s2+s3
print(Square.area(int(input("Enter the side of square: "))))
