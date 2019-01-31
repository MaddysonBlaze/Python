# OOPS

class Employee(object):
    
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = self.fname + '.' + self.lname + '@company.com'

    def fullname(self):
        return self.fname + ' ' + self.lname
    
    def __repr__(self):
        return f'Employee({self.fname})'
    
class Developer(Employee):
    
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang
        
    def __repr__(self):
        return f'Developer({self.fname})'
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

class Manager(Employee):
    
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        
        if not employees:
            self.employees = []
        else:
            self.employees = employees
    
    def __repr__(self):
        return f'Manager({self.fname})'

def main():
    dev_1 = Developer('Mickey', 'Arther', 40000, 'Java')
    dev_2 = Developer('Haise', 'Sasaki', 60000, 'Python')
    
    mgr = Manager('Chale', 'Sonnen', 60000, [dev_1])
    
#    print(mgr)
#    print(Developer.__add__(dev_1, dev_2))
    print(len(dev_1))

if __name__ == '__main__':
    main()
    
