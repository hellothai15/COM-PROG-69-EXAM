'''Student'''

class Student:
    '''Student'''

    def __init__(self, sid, name, gpa):
        self.sid = sid
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        '''get student id'''
        return self.sid

    def get_name(self):
        '''get student name'''
        return self.name

    def get_gpa(self):
        '''get student gpa'''
        return self.gpa

    def print_detail(self):
        '''print detail'''
        print("ID: {}\nName: {}\nGPA: {}".format(self.sid, self.name, "%.2f" % self.gpa))



def main(text_in):
    '''main fucntion'''
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_detail()

main(input())