# 숫자 맞추기 게임
import random

count = 0
chance = 10
number = random.randint(1, 99)


while (count < chance):
    count += 1
    user_input = input("몇 일까요? ")
    if number == user_input:
        print('정답')
    else:
        print('아닙니다')
    
    if count == chance:
        print('정답은', number, '입니다')