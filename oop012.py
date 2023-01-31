# Install application

class Wizard(object):
    def install(self, mode):
        self._first()
        self._second(mode)
        self._third()
    
    def _first(self):
        print("Install first step of wizard")
    
    def _second(self, mode):
        print("Install second step of wizard at mode " + mode)
    
    def _third(self):
         print("Install third step of wizard")

class Install(object):
    def install(self, wizard, mode):
        wizard.install(mode)

if __name__ == "__main__":
    wizard = Wizard()
    install = Install()
    
    install.install(wizard, "test")