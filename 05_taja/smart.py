import time
import random
import os
'''

한글 = ((초성 * 21) + 중성) * 28 + 종성 + 44032

초성 = ((x - 44032) / 28) / 21
중성 = ((x - 44032) / 28) % 21
종성 = (x - 44032) % 28

'''


cho = ['ㄱ', 'ㄲ',  'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ' , 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jung = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jong = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']



def break_korean(string):
    word_list = list(string)
    break_word = []
    for k in word_list:
        if ord(k) >= ord("가") and ord(k) <= ord("힣"):
            # 유니코드 상 몇 번째 글자인지 인덱스를 구합니다.
            char_index = ord(k) - ord('가') # 가 = 44032
            
            # 초성 = (유니코드 인덱스 / 28) / 21
            char1 = int((char_index / 28) / 21)
            break_word.append(cho[char1])

            # 중성 = (인덱스 / 28) % 21
            char2 = int((char_index / 28) % 21)
            break_word.append(jung[char2])

            # 종성 = 인덱스 % 28
            char3 = int(char_index % 28)
            
            if char3 > 0:
                break_word.append(jong[char3])
            
        else: 
            break_word.append(k)
    
    return break_word

WORD_LIST = [
    "호우호우 진영쓰",
    "인연을 중시하는 사람이죵. 신뢰를 중요시합니다.",
    "툴툴 댈 때도 있지만, 마음을 줄 때 확 주는 편입니다요.",
    "코딩합시다 코딩",
    "돈을 많이 벌어서 경제적인 자유를 찾고 싶습니다.",
    "노력 해봐야죠"
]

random.shuffle(WORD_LIST)

for q in WORD_LIST:
    start_time = time.time()
    user_input = str(input(q + '\n')).strip()
    end_time = time.time() - start_time

    src = break_korean(q)
    tar = break_korean(user_input)

    if user_input == '/exit':
        break

    correct = 0
    for i, c in enumerate(tar):
        if i >= len(src):
            break
        if c == src[i]:
            correct += 1

    tot_len = len(src)
    c = correct / tot_len * 100
    e = (tot_len - correct) / tot_len * 100
    speed = (correct / end_time) * 60
    
    print('속도 : {:0.2f} 정확도 : {:0.2f} 오타율 : {:0.2f}'.format(speed, c, e))

user_input = input('입력 \n')
word_list = list(user_input)
