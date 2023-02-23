# 封裝

class Cat(object):
    
    def __init__(self, name="No Name"):
        self.name = name
        self._shout_num = 3
    
    @property
    def shout_num(self):
        return self._shout_num
    
    @shout_num.setter
    def shout_num(self, num: int):
        if num < 0:
            raise ValueError()
        self._shout_num = num
    
    def shout(self):
        result = ""
        for _ in range(self.shout_num):
            result += "meow~ "
        return f"My name is {self.name}. {result}"

def main():
    cat = Cat("May")
    print(cat.shout_num)
    # print(cat._shout_num)
    cat.shout_num = 5
    print(cat.shout())

if __name__ == "__main__":
    main()