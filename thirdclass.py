#Python collections

# my_list = ['Dave', 'Anu', 'Joshua', 23, 23, 56.6, True, ['beans','pencil']]
# print(len(my_list))
# print(my_list[0:4])

# my_list[0] = 'David'
# print(my_list) 

# my_list[0:3] = ['Olu', '4',]
# print(my_list)

# li = []
# li.append(['Habeeb', 'Dave'])
# li.extend(['Habeeb', 'Dave'])     
# print(li)
# my_list.clear()
# del my_list

# print(my_list.index(23))
# print(my_list.count(23))
# my_list.pop(4)
# my_list.remove(True)
# my_list.reverse()
# my_list.sort
# my_list.insert(0, 'Anu')
# print(my_list)

# num = [3,5,6,8,2,8]
# print(sum(num))
# print(max(num))
# print(min(num))

# python_students = ['Dave', 'Anu', 'Mary', 'Joshua', 'Marv']
# # print('Welcome to class', python_students[0])
# for each in  python_students:
#     print('Welcome to class', each)
#     # print('eeeeeeeeeee')
# questions = ['1. Who is the President of Nigeria?\n a. Buhari b. BAT'
#             '2. Which is the capital of France?\n a. Paris b. London'
#             ]
# for each_quest in questions:
#     print(each_quest)
#     user = input('Ans: ')

# num = []
# for x in range(10):
#     # print(x)
#     num.append(x)
# print(num)

# names_of_students = []
# for x in range(10):
#     name = input(f'Name{x+1}: ')
#     names_of_students.append(name)
# print(names_of_students)

# tuple()
students = ('Dave', 'Anu', 'Mary', 'Damilare', 4, 2, True, ('beans', 'yam'), [23, 'big', 7])
# print(students)
# print(students[1:4])
# students = ['Mary']
list_students = list(students)
# print(list_students)
list_students [1] = 'Mary'
print(list_students)
students = tuple(list_students)
print(students)

# changing from tuple to list
mary = ('ade', 'ayo')
mary_list = list(mary)
print(mary_list)
mary_list[1] = 'mary'
print(mary_list)
mtuple = tuple(mary_list)
print(mtuple)

# Unpacking(it automatically convert to a list)
(*list_student,) = students
print(list_student)

(student1, student2, *alls) = students
print(student1)

fruits = ('banana', 'mango', 'apple', 'goat')
(*fruit1, fruit2, alls) = fruits
print(fruit1)

# functions of tuple
print(students.count('Slessor'))
print(students.index('Slessor'))

stud = ['mary', 'lola', 'ayo']
scores = [23, 45, 65]
print(max(scores))
index_max = scores.index(max(scores))

print(stud[index_max])

mean_scores = sum(scores)/len(scores)
print(mean_scores)

# for loop
names = ('mary', 'lola', 'ayo', 'femi')
for name in names:
   print(name)


names = ('mary', 'lola', 'ayo', 'femi')
scores = [23, 45, 65]
for names, score in zip(names,scores):
   print(f'{names} scored {score}.')
   print(names, 'scored', score)

details = [('mary', 23),('lola', 45),('ayo', 95),('femi', 65)]
print(details)

# Today's class
score = 0
details = [
   ('1.Which bird is the fastest in the world?\na. penguin b. falcon c. duck d. ostrich', 'b'),
   ('2.What is the chemical symbol for gold?\na. Co b. Au c. Fe d. Ni', 'b'),
   ('3.What is the hottest planet in the solar system?\na. earth b. venus c. mars d. mercury', 'd'),
   ('4.What is the name of the largest ocean?\na. atlantic b. arctic c. pacific d. red sea', 'c'),
   ('5.What is the hottest planet in the solar system?\na. earth b. venus b. mars d. mercury', 'd'),
]

for question, answer in details:
        print(question)
        user_ans = input('Answer: ').strip().lower()
        
        if user_ans == answer: 
            print('correct')
            score +=5
        else:
           print('wrong')  
           
print(f'Thanks for taking the test, your total score is {score}')

