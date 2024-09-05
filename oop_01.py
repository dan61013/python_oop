# 父類別
class BaseballPlayer(object):
    
    def __init__(self, name: str) -> None:
        self.name = name
    
    def hit(self):
        print(f"{self.name} can hit")
    
    def pitch(self):
        print(f"{self.name} can pitch the ball")

# 繼承 (游擊手)
class Shortstop(BaseballPlayer):
    
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def run(self):
        print(f"{self.name} can run")

# 繼承 (外野手)
class Outfielder(BaseballPlayer):
    
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def run(self):
        print(f"{self.name} can run very fast")

# 奇怪的繼承 (網球選手)
class TennisPlayer(BaseballPlayer):
    
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def serve(self):  # 發球
        print(f"{self.name} can serve")

def main():
    
    # 透過類別所建立的物件，通常稱作實例 (instance)
    ichiro = BaseballPlayer("ichiro")
    shuzuki = BaseballPlayer("shuzuki")
    
    ichiro.hit()
    shuzuki.hit()
    
    # child可以一直延伸，像代代傳承一樣
    jeter = Shortstop("jeter")
    jeter.hit()  # 繼承後可以直接調用父類別 class function
    jeter.run()  # 可以使用自己的function
    
    # 外野手繼承
    betts = Outfielder("betts")
    betts.hit()
    betts.run()  # 與游擊手的run不一樣

    # 錯誤的繼承
    federer = TennisPlayer("federer")
    federer.hit()
    federer.serve()
    # 在BaseballPlayer新增投球pitch
    federer.pitch()  # 不正確

if __name__ == "__main__":
    main()