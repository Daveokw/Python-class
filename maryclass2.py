#python escape characters
#\n(next line or enter)
#\t tab
# print ("I am a\t\tgenius")
# \b backspace
# print("I am a\b\b\bgenius")
# \r(return, it will delete  everything before r)
# print('I am a\r genius')

# python collections
'''1. list
2.tuple
3. set
4. dictionary

1. LIST [] or list()
Properties of a class list
   a. ordered
   b. changeable/mutable
   c. it allows duplicate values
   d. it can be indexed
   '''
   
# my_list = ['maimunat', 'joshua', 45, 42, True, ['Yam', 'Rice', 'Semo'], 'Bottle']
# print(len(my_list))
# print(my_list[0])
# print(my_list[-2][-2])
#slicing
# print(my_list[4:6])
# my_list[0] = 'Mary'
# print(my_list)
# my_list[0:3] = ['tolu', 'mary', 'dave']
# print(my_list)

#Some functions a list can perform

li = []

# you cannot put 2 argument unless you put list inside
# print(li)
# li.extend(['slessor''adepoju'])
# learn all my_list.


# python_students = ['tolu', 'joshua', 'mary', 'maimunat']
# for each in python_students:
#     '''  print('Welcome to class',each)
#     function called zip
   #  mark the question in the list
#     ask your user how many student want'''

# li = ['maimunat', 'joshua', 45, 42, True, 'Yam', 'Rice', 'Semo', 'Bottle']
# li.append('folu')
# li.extend(['aja', 'film'])
# li.clear()
# print(li)

# sle_list = ["goat", "beans", 15, "marvellous", 'great', 'banana']
# del sle_list
# sle_list.pop()
# sle_list.remove("beans")

# Sl.reverse
# Sl.insert
# print(sl.count('')
# print(sl.index())
# print(sle_list)




# num = 
# python_students = ['ajala', 'adepoju', 'sali', 'atewo', 'ola', 'ajib']
# for each in python_students:
#    print('Welcome to python class', each)


# print ('Each of the following questions attract equal marks, \n
# ')
# score = 0
# print("Press enter to start the test or 1 to exit: ")
# user = input('')
# if user == '1':
#    exit()
# else:
#     name_of_student = []
# for x in range(10):
#    name = input(f'Name {x+1}:')
# print(name_of_student)
# # for each in "name":
# #   print('Welcome to the test', )
# questions = ['1.Which bird is the fastest in the world?\na. penguin b. falcon c. duck d. ostrich',
#             '2.What is the chemical symbol for gold?\na. Co b. Au c. Fe d. Ni',
#             '3.What is the hottest planet in the solar system?\na. earth b. venus c. mars d. mercury',
#             '4.What is the name of the largest ocean?\na. atlantic b. arctic c. pacific d. red sea',
#             '5.What is the hottest planet in the solar system?\na. earth b. venus b. mars d. mercury',
#              ]
# for each_quest in questions:
#    print(each_quest) 
#    user = input('Ans:')
#    count = +5


#zip function is used for joining 2 tuples together
# x = ("ade", "bola", 'ayo')
# y = ('man', 'woman', 'child')
# a = zip(x, y)

# #yesterday class
# #list comprehension
# print("Press enter to start the test or '1' to exit")
# pers = input('')
# if pers == '1':
#     exit()
# else: 
#        numbers = [ x for x in range(1, 21)]
# user = int(input('How many students are taking the test: '))
# student_list = [input(f'Name of student {student + 1}: ') for student in range(user)]
# student_scores = []
# score_list = []
# for each_student in student_list: 
#     print(f'\n{each_student},  its time for your test\n')
#     score = 0
#     questions = ['1.Which bird is the fastest in the world?\na. penguin b. falcon c. duck d. ostrich',
#                 '2.What is the chemical symbol for gold?\na. Co b. Au c. Fe d. Ni',
#                 '3.What is the hottest planet in the solar system?\na. earth b. venus c. mars d. mercury',
#                 '4.What is the name of the largest ocean?\na. atlantic b. arctic c. pacific d. red sea',
#                 '5.What is the hottest planet in the solar system?\na. earth b. venus b. mars d. mercury',
#                 ]
#     answers = ['b', 'b', 'd', 'c', 'd']
#     for question, answer in zip(questions, answers):
#         print(question)
#         user_ans = input('Answer: ').strip().lower()
        
#         if user_ans == answer: 
#             print('correct')
#             score +=5
            
#     print(f'Thanks for taking the test, your total score is {score}')
#     score_list.append(score)
# print(student_list)
# print(score_list)
# maximum = max(score_list)
# print(maximum)
# minimum = min(score_list)
# print(minimum)
# stud_max = [('The student with the ')]

# #print out the student with max and min score

# #Tuple (), tuple()
# #properties:
# '''
# 1. Unlike list, tuple are unchangeable or immutable
# 2. They can be indexed
# 3. They allow duplicate values
# 4. It is ordered
# # '''
# students = ('Damilare', 'Slessor', 'Slessor', "Maimunat", 'Richard', 23, True, [23, 34, 56],)
# # # print(students)
# # # print(students[3]) 
# # # print(students[-3])
# # # print(students[1:4])
# # list_students = list(students)
# # print(list_students)

# #changing from tuple to list
# # mary = ('ade', 'ayo')
# # mary_list = list(mary)
# # print(mary_list)
# # mary_list[1] = 'mary'
# # print(mary_list)
# # mtuple = tuple(mary_list)
# # print(mtuple)

# #Unpacking(it automatically convert to a list)
# # (*list_student,) = students
# # print(list_student)

# # (student1, student2, *alls) = students
# # print(student1)

# # fruits = ('banana', 'mango', 'apple', 'goat')
# # (*fruit1, fruit2, alls) = fruits
# # print(fruit1)

# #functions of tuple
# # print(students.count('Slessor'))
# # print(students.index('Slessor'))

# # stud = ['mary', 'lola', 'ayo']
# # scores = [23, 45, 65]
# # # print(max(scores))
# # index_max = scores.index(max(scores))

# # print(stud[index_max])

# # mean_scores = sum(scores)/len(scores)
# # print(mean_scores)

# # for loop
# # names = ('mary', 'lola', 'ayo', 'femi')
# # for name in names:
# #    print(name)


# # names = ('mary', 'lola', 'ayo', 'femi')
# # scores = [23, 45, 65]
# # for names, score in zip(names,scores):
# #    print(f'{names} scored {score}.')

# # details = [('mary', 23),('lola', 45),('ayo', 95),('femi', 65)]
# # print(details)

# #Today's class
# score = 0
# details = [
#    ('1.Which bird is the fastest in the world?\na. penguin b. falcon c. duck d. ostrich', 'b'),
#    ('2.What is the chemical symbol for gold?\na. Co b. Au c. Fe d. Ni', 'b'),
#    ('3.What is the hottest planet in the solar system?\na. earth b. venus c. mars d. mercury', 'd'),
#    ('4.What is the name of the largest ocean?\na. atlantic b. arctic c. pacific d. red sea', 'c'),
#    ('5.What is the hottest planet in the solar system?\na. earth b. venus b. mars d. mercury', 'd'),
# ]

# for question, answer in details:
#         print(question)
#         user_ans = input('Answer: ').strip().lower()
        
#         if user_ans == answer: 
#             print('correct')
#             score +=5
#         else:
#            print('wrong')  
           
# print(f'Thanks for taking the test, your total score is {score}')

# #Assignment
# '''
# 1. Available food, available drinks'
# 2. Ask user the food he or she want and check if its there


# Entrance Application
# There is a gate(Are you A student, are you a staff, are you a visitor)
# if your name is there and have you paid fully, then it let you come in
# visitor will visit the front desk
# '''

# print('Youre welcome to this great citadel of learning.\n Are you a Student, staff or a Visitor?\n Note: let your answers be in lower case')
# user = input('Ans: ')
# if user == 'student':
#    print('Has your school fees be paid fully?(Yes or No)')
#    user = input('Ans: ')
#    if user == 'yes':
#       print('You can enter with your evidence of payment.')
#    else:
#       print('You are not allowed to enter withhout full payment.')
# elif user == 'staff':
#    print('Pease enter with your Identity card')
# elif user == 'visitor':
#    print('You are highly welcome,you can proceed to the front desk')
# else: 
#    exit()

# print('Welcome to slessor canteen, please place your order')
# user_ans = input('food: ')
# detail1 = [
#    ('rice', '#200 per spoon'),
#    ('yam', '#100 per one plate'),
#    ('beans', '#150 per spoon'),
#    ('spaghetti', '#100 per spoon'),
#    ('meat', '#200 per one'),
#    ('fish', '#100 per one'),
#    ('egg', '#200 per one')
# ]
# for food, price in detail1:
#    if user_ans == 'food': 
#       print(price)
#    else:
#       print("It's not available, Thanks")

# Today's class

# user = input('USSD: ').strip()
# while user != '*321#': 
#    print('Invalid ussd code. Try again')
#    user = input('USSD: ').strip()
   
# print('Welcome to myMTN')  
 
 
# slot = 10
# admission_list = []

# while slot >= 1:
#    name = input('Aspirant name: ')
#    admission_list.append(name)
   
#    slot -= 1
# else:
#    print(admission_list)   

# x = 1
# while True:
#    print(x)
   
#    if x == 10:
#       continue
   
#    if x == 20:
#       break
   
#    x +=1   

# ticket = 10

# while ticket >= 1:
#    age = int(input('Age: '))
   
#    ticket -= 1
   
#    if age < 18:
#       continue
#    else:
#       print(ticket)

#The assignment solution and the given assignment to be submitted next week is below.

students = [
   ('Dave Temi', 'full'),
   ('Adebisi Precious', 'full'),
   ('Salim Quadri', 'part'),
   ('Tunde Remi', 'part'),
   ('John Ade', 'nil'),
   ('Adeolu James', 'part'),
   ('Olumide Bimpe', 'full')
        ]

staff = [
   ('Moses Simon', '01'),
   ('Adeoye Mercy', '02'),
   ('Oladokun Victory', '03'),
   ('Flair Rick', '04')
]

user = input('''WELCOME TO SQI COLLEGE OF ICT.
      Choose an option below to verify your identity:
      A. Staff
      B. Student
      C. Visitor
    Option: '''
)

if user.strip().capitalize() == 'A':
        staff_id = input('ID: ')
        staff_name = input('First Name: ').strip().capitalize

        fnames = []
        IDs = []

        for name, id in staff:
              fnames.append(name)
              IDs.append(id)
        
        if staff_name in fnames and staff_id in IDs :
            print('Access Granted👍. You can go in')
        else:
            print('Access Denied!')
            
if user.strip().capitalize() == 'C':
   print('You can proceed to the front desk')
   
elif user.strip().capitalize() == 'B':
   print('Welcome to School. Input your name to verify your eligibility: \n')
   student = input('Your Name: ').strip().capitalize()
   # print(student)
   Students =[]
   PaymentStatus=[]

   for name,payment in students:
      Students.append(name)
      PaymentStatus.append(payment)
   # print(Students)
   
   if student in Students:
      print(f'\n Welcome {student}, kindly wait to verify your payment status\n')
   
      _index = Students.index(student)
      _status = PaymentStatus[_index]

      if _status == 'full':
         print(f'{student}, you have made full payment, you can go in')
      elif _status == 'part':
         print(f'{student}, you have made half payment, pay up very soon to preserve your studentship')
      elif _status == 'nil':
         print(f'You are not eligible to go in')
         
   else:
      print('Your name is not registered')

# SUPERMARKET
# Take their name
# Available goods
# Check if it is in the list
# Produce a receipt with the price
# Ask if they still want another order

# print('''
#     Thanks Mr Dami. Your orders are
#       1. Nike Sneekers --> #20,000
#       2. Rolex --> #30,000

#         Total = #50,000

# ''')
      
