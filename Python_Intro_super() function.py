class rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*self.length+2*self.width


class square(rectangle):
    def __init__(self,length):
        super().__init__(length,length)


my_square=square(4)
print(my_square.area())

    
