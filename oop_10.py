"""
「多型」的涵義是指「子類可以以父類的身分出現」，而因為是以父類的角色出現，
所以只能執行父類擁有的方法，也就是只能執行這些子類共同泛化分享的方法，
當然不同的子類實現後的效果會不一樣，不然使用「多型」的意義就不大了，
至於子類自己的特殊方法則不可以使用「多型」去執行。
"""

class Animal(object):
    
    def __init__(self, name="No Name"):
        self._name = name
        self._shout_num = 3
    
    @property
    def shout_num(self):
        return self._shout_num
    
    @shout_num.setter
    def shout_num(self, num: int):
        self._shout_num = num
    
    def shout(self):
        result = ""
        for _ in range(self._shout_num):
            result += self._getShoutSound() + " "
        return f"My name is {self._name}. {result}"
    
    def _getShoutSound(self):
        raise NotImplementedError

class Cat(Animal):
    
    def _getShoutSound(self):
        return "meow~"

class Dog(Animal):
    
    def _getShoutSound(self):
        return "woof~"

def main():
    # shout game
    arrayAnimal = []
    arrayAnimal.append(Cat("Mira"))
    arrayAnimal.append(Dog("Ben"))
    arrayAnimal.append(Cat("May"))

    for animal in arrayAnimal:
        # 檢查是否繼承自Animal parent class
        if not isinstance(animal, Animal):
            raise TypeError
        print(animal.shout())

if __name__ == "__main__":
    main()