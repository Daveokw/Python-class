# students_db = [
#     ('Dave', 'Paid'),
#     ('Tolu', 'Half-paid'),
#     ('Habeeb', 'No-paid')
#     ]

# staff_db = [
#     ('Femi', '21'),
#     ('Temi', '02')
#     ]
# user = input('''
#                 Welcome to SQI College of ICT
             
#       Kindly verify your identity
#       1. Staff
#       2. Student
#       3. Visitor
#       4. None of the above
      

#       Option: ''').strip()
# if user == '1' or user.capitalize() == 'Staff':
#     staff_id = input('ID: ').strip()
#     staff_fname = input('First name: ').strip().capitalize()
    
#     fnames = []
#     IDs = []

#     for fname, id in staff_db:
#         fnames.append(fname)
#         IDs.append(id)


#     if staff_fname in fnames and staff_id in IDs:
#         print('Access granted')
#     else:
#         print('Access denied!')
     
# if user.strip().capitalize() == 'C':
#    print('You can proceed to the front desk')
   
# elif user.strip().capitalize() == 'B':
#    print('Welcome to School, Input your name to verify your eligibility: \n')
#    student = input('Your Name: ').strip().capitalize()
#    # print(student)
#    Students = []
#    PaymentStatus = []

#    for name, payment in students_db:
#       Students.append(name)
#       PaymentStatus.append(payment)
#    # print(Students)
   
#    if student in Students:
#       print(f'\nWelcome {student}, kindly wait to verify your payment status\n')
   
#       _index = Students.index(student)
#       _status = PaymentStatus[_index]

#       if _status == 'full' :
#          print(f'{student}, you have made full payment, you can go in')
#       elif _status == 'part' :
#          print(f'{student}, you have made half payment, pay up very soon to preserve your studentship')
#       elif _status == 'nil':
#          print(f'You are not eligible to go in, return to your home')
         
#    else:
#       print('Your name is not registered')

# SET {}, set() 

myset = {'mango', 'apple', 'pineapple', 'grape'}
# print(type(myset))
# print(myset)

setnum = {5, 3, 4, 6, 7, 8, 9, 1, 2}
# print(setnum)
# fruits = myset.copy()
# myset.add('watermelon')
# print(myset)
# myset.update(['yam', 'beans'])
# myset.pop()
# print(myset)
# # print(fruits)

# print(myset)
# balance = 500
# stake = float(input('Stake: '))

# while balance > 0 and balance > stake: 
#    guess = input('Guess the chosen fruit: ').strip().lower()
#    chosen_fruit = myset.pop()
#    myset.add(chosen_fruit)
#    # print(chosen_fruit)
#    if guess == chosen_fruit:
#       balance += 2 * stake
#       print('You guessed right.\nYour current balance is ', balance)
#    else:
#       balance -= stake
#       print('Wrong\nYour current balance is ', balance)
#    user = input('Press 1 to replay or # to exit: ')
#    if user == '#':
#       break
# else: 
#    print('Insufficient fund. Go and deposit')
# print('Your cashout price is ', balance)

# myset.remove('apple') #shows error when istem isn't found
# myset.discard('apple') #doesn't show error when item isn't found
# print(myset)

setA = {5, 3, 4, 6, 7, 8, 9, 1, 2, 10, 12, 11}
setB = {3, 2, 4, 5, 6}
setC = {3, 2, 5, 6}
# print(setA.union(setB))
# print(setA.intersection(setB))
# setA.intersection_update(setB)
# print(setA.difference(setB))
# print(setA - setB)
# setA.difference_update(setB)
# print(setA)
# set4 = setA.symmetric_difference(setB)
# setA.symmetric_difference_update(setB)
# print(setA)
# print(set4)

# setA.is


# Dictionary {key:value}, dict(key = value)

# car = {'Model':'Tesla', 'Year':2022}
# print(type(car))
# print(car)
# print('The model is', car['Model'])
# car['Model'] = 'Benz'
# print(car)
car = {
   'Model':'Tesla', 
   'Year':2022,
   'Colour':['Black', 'Blue'],
   'Year1':2021,
   'Owner':{
      'Name':'Dave',
      'Price':40000
   }
   }
# print(car['Colour'][0])
# print(car['Owner']['Name'])
# print(car.keys())
# for kk in car.keys():
#    print(kk)

# print(car.values())
# print(car.items())

# questions = {'1. Dave is a male':'True',
#              '2. Apple is a fruit':'True',
#              '3. Dog is not an animal':'False'
#              }
# score = 0
# for qq, ans in questions.items():
#    print(qq)
#    user = input('Answer: ')
#    if user == ans:
#       score += 5
# print('Your total score is', score)

# car.update({'Transmission':'Automatic', 'EngineType':'V6'})
# print(car['Colour']) will show error
# print(car.get('colour', 'Not found')) won't show error
# car.popitem()
# car.pop('Colour')
# print(car)

{
   'Student1':{'Name':'Dave', 'Matric No.':'2345'},
   'Student2':{'Name':'Dami', 'Matric No.':'1234'}
}
user = input('Kindly press 1 to start registration: ')
if user == '1':
   x = 1
   students_db = {}
   while True:
      name = input('Name: ').strip().title()  
      matno = input('Matric No.: ').strip().title()

      students = {'Name':name, 'Matric No.':matno}
      students_db.update({f'Student{x}':students})
      x += 1

      user = input('Press 1 to stop or Enter key to continue: ')
      if user == '1':
         break
print(students_db)



































































