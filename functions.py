# shift + ctrl + L
# UNPARAMETIZED
# def addition():
#     value1 = int(input('Enter first value: '))
#     value2 = int(input('Enter second value: '))
#     result = value1 + value2
#     print('Answer: ', result)
# addition()
# PARAMETIZED
# def addition(value1, value2 = 10):
#     result = value1 + value2
#     print('Answer: ', result)
# addition(value1 = int(input('Enter first value: ')), 
# value2 = int(input('Enter second value: ')))
# addition(4, 5)
# val1 = 12
# def addition(val3):
#     global val2
#     val2 = 10
#     result = val1 + val2 + val3
#     print('Answer: ', result, 'nice')
#     subtraction()
# def subtraction():
#     result = val1 - val2
#     print('Answer: ', result, 'amazing')
# addition(int(input('Enter value 3: ')))]

# val1 = 'David'
# def know_me():
#     val2 = 'Data Scientist'
#     print('My name is', val1, 'I am a', val2)
#     print(f'My name is {val1} I am a {val2}')
# know_me()
# def about():
#     print(val1, 'is a', val2)
# about()
    

# def landing_page():
#     global value1
#     global value2
#     name = input('Name: ')
#     value1 = float(input('Value 1: '))
#     value2 = float(input('Value 2: '))
#     user = input(f'''
#                 My Alata Calculator. Welcome {name}
#             1. Addition
#             2. Subtraction
#             #. Exit

#         Choose your operation: ''').strip()
#     if user == '1':
#         addition()
#     elif user == '2':
#         subtraction()
#     elif user == '#':
#         exit()
#     else:
#         print('Invalid input')
#         landing_page() #recursive function
# def addition():
#     print(f'Answer is {value1 + value2}')
#     decide()
# def subtraction():
#     print('Answer is', value1 - value2)
#     decide()
# def decide():
#     user = input('Press 1 to go to Home or # to exit: ').strip()
#     if user == '1':
#         landing_page()
#     else:
#         exit()
# landing_page()
    
# def add(val1: float, val2: float = 10):
#     '''
#     I add things up
#     '''
#     return val1 + val2
# print(add(10, 20))
# print(add(float(input('Val: '))))
# def arithmetic():
#     res = 2 ** add(10)
#     return res
# arithmetic()
# def printf(name):
#     print(f'{name}, your result is {arithmetic()}')

# printf(input('Your name: '))
    

# class Dust:
#     def __init__(self): #initialize first 
#         self.first_name = 'Dave'
#         self.last_name = 'Temi'
#         self.naming()
#     def naming(self):
#         print(f'My name is {self.first_name} {self.last_name}')
# father = Dust()
# father.naming()
# print(type(dave))


# surname = 'Ojo'
# def call_name():
#     global fname 
#     fname = input('First name: ').strip()
#     print('My name is', fname, surname)

# def say():
#     print(surname, fname)

# # basket = list()
# class Calculator:
#     def __init__(self):
#         self.calc_name = 'Casio'
#         # self.home()
        
#     def home(self):
#         print('Welcome to', self.calc_name)
#         self.val1 = float(input('First value: '))
#         self.val2 = float(input('Second value: '))
#         user = input('''
#             Choose your operation:
#               1. Addition
#               2. Subtraction
#               #. Exit
#             Option: ''')
#         if user == '1':
#             self.addition()
#         elif user == '2':
#             self.subtraction()
#         elif user == '#':
#             exit()
#         else:
#             print('Invalid function. Try again')
#             self.home()

#     def addition(self):
#         print(f'Answer =  {self.val1 + self.val2}')
#         self.decide()
#     def subtraction(self):
#         print(f'Answer = ', self.val1 - self.val2)
#         self.decide()
#     def decide(self):
#         user = input('Press 1 to go to home or # to exit')
#         if user == '1':
#             self.home()
#         else:
#             exit()

# mycalc = Calculator() # casio is the object, calculator is the class
# print(mycalc.calc_name)
# mycalc.home()
            
#INHERITANCE
class Parent:
    def __init__(self):
        self.surname = 'Ojo.'
        self.firstname = 'Mary'
        self.hobby = 'Eating.'

        self.describe()

    def describe(self):
        print('My name is', self.firstname, self.surname, 'I love', self.hobby)

# parent = Parent()
# print(parent.firstname)

class Child(Parent):
    def __init__(self):
        Parent.__init__(self) 
        #or
        # super().__init__()
        self.firstname = 'Maimunah'
        self.hobby = 'Sleeping'
        self.bestfood = 'Fufu and Egusi'

        # self.describe()
        # self.cooking()

    def cooking(self):
        print(f'{self.firstname} is cooking {self.bestfood}')

# child = Child()

class Grandchild(Child):
    def __init__(self):
        Child.__init__(self)
        self.firstname = 'Richard'
        self.hobby = 'Talking'

        self.describe()
        # self.cooking()
        
# grandchild = Grandchild()

# Script: any file with .py
# Module: Any python script that has more than one class in it
# Library: Has different modules in it
        
# ERROR HANDLING
# Run-time error
# Compile-time error
# try, except, else, finally (block codes)

# container = ['pen', 'pencil', 'phone', 'drink']
# print(container[5])

# user = int(input())

# try: 
#     container
# except:
#     print('Invalid entry')
# else:
#     print('Valid entry')
# finally:
#     print('I will always show up if there is an error or not')

# You can be specific with the type of error being handled

# try:
#     container[5]
# except NameError:
#     print('Invalid entry')
# except IndexError:
#     print('Index out of range')
# except:
#     print('There is something wrong somewhere')

# try:
#     val1 = int(input('Input Value 1: '))
#     val2 = int(input('Input Value 2: '))

# except ValueError as v: 
#     print(v)
#     # raise TypeError ('The value must be an integer')
#     # print('The value must be an integer')
# except Exception as e:
#     print(e)

class Calc:
    def __init__(self):
        self.home()
    def home(self):
        try:
            self.val1 = int(input('Input Value 1: '))
            self.val2 = int(input('Input Value 2: '))
        except Exception as e:
            print(e)
            self.home()

        user = input('''
        Choose option:
        1. Addition
        2. Division
                      
        Option: ''')
        if user == '1':
            self.add()
        elif user == '2':
            self.div()
        else:
            print('Invalid input')
            self.home()
    def add(self):
        res = self.val1 + self.val2
        print('Your result is ', res)
    def div(self):
        try:
            res = self.val1 / self.val2
        except Exception as e:
            print(e)
        else:
            print('Your result is ', res)
        finally:
            self.home()
# calculator = Calc()
            

# File-handling
'''
r - read only
w - write
a - append
x - create
'''
            
# myfile = open(r'C:\Users\okanl\OneDrive\Documents\Python\myfile.txt')
# print(myfile.read())
# print(myfile.readlines())
# x = 0
# for line in myfile.readlines():
#     print(line)
#     if x == 5:
#         break
#     x += 1
# myfile.close()
# with open(r'C:\Users\okanl\OneDrive\Documents\Python\myfile.txt', mode = 'r', encoding = ) as file:
#     print(file.read())
# file.read()
# myfile = open(r'C:\Users\okanl\OneDrive\Documents\Python\myfile2.txt', mode = 'x')

# with open(r'C:\Users\okanl\OneDrive\Documents\Python\myfile2.txt', mode = 'wt') as myfile:
#     myfile.write('Hello...')
# with open(r'C:\Users\okanl\OneDrive\Documents\Python\myfile2.txt', mode = 'a') as myfile:
#     myfile.write('Hello world...\n')




import os
# os.mkdir(r'C:\Users\okanl\OneDrive\Documents\Python\New folder')
# os.rmdir(r'C:\Users\okanl\OneDrive\Documents\Python\New folder')
# os.remove(r'C:\Users\okanl\OneDrive\Documents\Python\myfile2.txt')
# print(os.path.exists(r'C:\Users\okanl\OneDrive\Documents\Python\myfile.txt'))

# if os.path.exists(r'C:\Users\okanl\OneDrive\Documents\Python\myfile3.txt'):
#     print('File exists')
#     print('_'*98)
# else:
#     print('File does not exist')
#     with open(r'C:\Users\okanl\OneDrive\Documents\Python\myfile3.txt') as myfile:
#         print(myfile.read())

