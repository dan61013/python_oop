# 重整父類: 運動員
# https://ithelp.ithome.com.tw/articles/10267306
from abc import abstractmethod  # import abstract method decorator

class Athlete(object):
    
    def __init__(self, name: str) -> None:
        self.name = name
    
    @abstractmethod  # 改成抽象方式
    def hit(self):
        pass

class BaseballPlayer(Athlete):
    
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def pitch(self):
        print(f"{self.name} can pitch the ball")
    
    # abstact method後新增hit
    def hit(self):
        print(f"{self.name} can hit baseball")

class TennisPlayer(Athlete):
    
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def serve(self):
        print(f"{self.name} can serve the ball")

    # abstact method後新增hit
    def hit(self):
        print(f"{self.name} can hit tennis")

def main():
    
    jeter = BaseballPlayer("jeter")
    federer = TennisPlayer("federer")
    someone = Athlete("someone")
    
    jeter.hit()
    federer.hit()
    someone.hit()  # 修改成abstract方式後，則不會顯示值

if __name__ == "__main__":
    main()