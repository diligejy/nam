'''
1. 특정 숫자를 포함해서 로또 번호를 생성해주는 기능
2. 특정 숫자를 제외해서 로또 번호를 생성해주는 기능
3. 정해진 자리수만큼 연속 숫자를 포함하는 번호를 생성하는 기능
'''

import numpy as np

def make_lotto_number(**kwargs):
    rand_number = np.random.choice(range(1, 46), 6, replace= False)
    rand_number.sort()

    # 최종 로또 번호가 완성될 변수
    lotto = []
    
    
    if kwargs.get('include'):
        include = kwargs.get('include')
        lotto.extend(include)

        cnt_make = 6 - len(lotto)

        for _ in range(cnt_make):
            for j in rand_number:
                # 중복 여부 확인
                if lotto.count(j) == 0:
                    lotto.append(j)
                    break
    else:
        lotto.extend(rand_number)

    if kwargs.get('exclude'):
        exclude = kwargs.get('exclude')
        lotto = list(set(lotto) - set(exclude))

        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                rand_number = np.random.choice(range(1, 46), 6, replace= False)
                rand_number.sort()

                for j in rand_number:
                    if lotto.count(j) == 0 and j not in exclude:
                        lotto.append(j)
                        break

    if kwargs.get('continuty'):
        continuty = kwargs.get('continuty')
        start_number = np.random.choice(lotto, 1)
        
        seq_num = []

        for i in range(start_number[0], start_number[0] + continuty):
            seq_num.append(i)
        seq_num.sort()
        cnt_make = 6 - len(seq_num)
        lotto = []

        lotto.extend(seq_num)

        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                rand_number = np.random.choice(range(1, 46), 6, replace = True)
                rand_number.sort()

                for j in rand_number:
                    if lotto.count(j) == 0 and j not in seq_num:
                        lotto.append(j)
                        break
                
                lotto = list(set(lotto))


    lotto.sort()
    return lotto

count = int(input('로또 번호를 몇개 생성할까요? \n'))
for j in range(count):
    print(make_lotto_number(j))