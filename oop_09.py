# Interface
"""
在Java之中只允許單一繼承，但是卻可以有多個「接口」；
而Python沒有現成的「接口」可以使用，我們必須使用「抽象方法」來創造「接口」，
所以開發者要謹記「接口」的限制：不能有任何的具體方法。
"""

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

class IFly(object):
    
    def flyTo(self, place: str):
        raise NotImplementedError

class FlyingCat(Cat, IFly):
    
    def flyTo(self, place: str):
        return f"{self.shout()} I am go to fly to {place}."

def main():
    
    cat = FlyingCat("May")
    print(cat.flyTo("Taiwan"))

if __name__ == "__main__":
    main()