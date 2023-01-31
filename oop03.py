# https://ycc.idv.tw/introduction-object-oriented-programming_2.html#method-overloading
# 方法多載 Method Overloading
# Python當中，不允許相同方式，卻又不同參數形式。採用default參數數值來實現多載

class Cat(object):
    
    def __init__(self, name="No-Name") -> None:
        self.name = name
    
    def shout(self):
        return "My name is " + self.name + ". meow~"

def main():
    
    cat = Cat()
    print(cat.shout())

if __name__ == "__main__":
    main()