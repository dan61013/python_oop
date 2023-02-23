# Abstract Class, Abstract Method
# 過去建議使用abc, 但實際上大家會使用raise NotImplementedError

class Animal(object):
    
    def __init__(self, name="No Name") -> None:
        self.name = name
        self._shout_num = 3
    
    @property
    def shout_num(self):
        return self._shout_num
    
    @shout_num.setter
    def shot_num(self, num: int):
        self._shout_num = num
    
    def shout(self):
        result = ""
        for _ in range(self._shout_num):
            result += self._getShoutSound() + ""
        return f"My name is {self.name}. {result}"
    
    def _getShoutSound(self):
        # 繼承後要override這個方法，否則會報錯
        raise NotImplementedError

class Cat(Animal):
    
    def _getShoutSound(self):
        return "meow~"

class Dog(Animal):
    
    def _getShoutSound(self):
        return "woof~"

def main():
    
    animal = Animal()
    print(animal.name)
    # print(animal.shout())  # Error: No description
    
    cat = Cat("阿瑪")
    dog = Dog("白狗")
    
    print(cat.name)
    print(cat.shout())
    
    dog.shot_num = 4
    print(dog.name)
    print(dog.shout())

if __name__ == "__main__":
    main()