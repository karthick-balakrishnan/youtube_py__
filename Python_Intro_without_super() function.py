class rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*self.length+2*self.width


class square():
    def __init__(self,length):
        self.length=length

    def area(self):
        return self.length*self.length

    def perimeter(self):
        return 4*self.length


my_square=square(4)
print(my_square.area())

my_rectangle=rectangle(2,4)
print(my_rectangle.area())

