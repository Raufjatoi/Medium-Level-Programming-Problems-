# 2. Simple Quiz:
#  Create a program that asks the user 5 multiple-choice questions with three answer options
# each.
#  Store the correct answers in a separate list.
#  After the user answers all questions, calculate the user's score and display a message
# indicating their performance.
ans = ['B','B','B','A','A']
marks = 0
print ('\t\t\tQuiz Game')
print('1: Wha is the capital of Germany ? ')
print(' A : paris \n B : Berlin \n C : Normandy ')
user1 = input('Answer: ').upper()
if ans[0] == user1:
    marks += 1
print('Who is the Father of modern Computer')
print(' A : Charles babbage \n B : Alan tuning \n C : flora cash ')
user2 = input('Answer: ').upper()
if ans[1] == user2:
    marks += 1
print('Python is a ____')
print(' A : Compiling Lan \n B : interpreting Lan \n C : Machine : Lan ')
user3 = input('Answer: ').upper()
if ans[2] == user3:
    marks += 1
print('Which lan is only based OOP')
print(' A : Java \n B : Python \n C : Javasropt ')
user4 = input('Answer: ').upper()
if ans[3] == user4:
    marks += 1
print('Which language is most widely used in web dev')
print(' A : PHP \n B : Js \n C : Typescrpt ')
user5 = input('Answer: ').upper()
if ans[4] == user5:
    marks += 1

if marks < 5 :
    print(f'You got {marks} from 5')
    print(f'here the ans key {ans}')
elif marks == 5:
    print(f'Congrats {marks} from 5')
    print(f'here the ans key {ans}')