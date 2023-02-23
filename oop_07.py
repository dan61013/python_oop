# 繼承(Inheritance)

class Animal(object):
    
    def __init__(self, name="No Name"):
        self.name = name
        self._shout_num = 3
    
    @property
    def shout_num(self):
        return self._shout_num
    
    @shout_num.setter
    def shout_num(self, num: int):
        if num < 0:
            raise ValueError
        self._shout_num = num

class Cat(Animal):
    
    def __init__(self, name="No Name"):
        super().__init__(name)
    
    def shout(self):
        result = ""
        for _ in range(self.shout_num):
            result += "meow~ "
        return f"My name is {self.name}. {result}"

class Dog(Animal):
    
    # 不需要設定init，原本就繼承了父類屬性及方法
    def shout(self):
        result = ""
        for _ in range(self.shout_num):
            result += "woof~ "
        return f"My name is {self.name}. {result}"

def main():
    
    cat = Cat("Mia")
    dog = Dog("Brian")
    
    print(cat.shout())
    
    dog.shout_num = 4
    print(dog.shout())

if __name__ == "__main__":
    main()