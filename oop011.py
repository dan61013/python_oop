# 迪米特原則 Law of Demeter, LoD

# 假設今天一名老師給了學生名條想叫班長幫忙點名
class Student(object):
    
    def __init__(self, name):
        self.name = name

class Leader(object):
    
    def giveNameList(self, name_list: list):
        self._student_list = [Student(name) for name in name_list]
    
    def countStudents(self):
        print(f"Total number of students is {len(self._student_list)}")

class Teacher(object):
    
    def command(self, name_list, leader):
        leader.giveNameList(name_list)
        leader.countStudents()

if __name__ == "__main__":
    teacher = Teacher()
    leader = Leader()
    name_list = ['A', 'B', 'C', 'D', 'E']
    teacher.command(name_list, leader)