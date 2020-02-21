# 숫자 맞추기 게임
import random
import os

def input_check(msg, casting = int):
    while True:
        try:
            user_input = int(input("몇 일까요? "))
            return user_input
        except:
            print('숫자를 입력해 이 새끼야!')
            continue

count = 0
chance = 10
number = random.randint(1, 99)

os.system('cls')
print('1부터 99까지의 숫자를 10번 안에 맞춰보십쇼')

while (count < chance):
    count += 1
    user_input = input_check("몇 일까요?")
    if number == user_input:
        break
    elif user_input < number:
        print('{}보다 큰 숫자입니다.'.format(user_input))
    elif user_input > number:
        print('{}보다 작은 숫자입니다'.format(user_input))

if number == user_input:
    print('정답')
else:
    print('실패 정답은', number, '입니다')   