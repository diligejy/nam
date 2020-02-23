
import time
import random

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

    if user_input == '/exit':
        break

    correct = 0
    for i, c in enumerate(user_input):
        if i >= len(q):
            break
        if c == q[i]:
            correct += 1

    tot_len = len(q)
    c = correct / tot_len * 100
    e = (tot_len - correct) / tot_len * 100
    speed = (correct / end_time) * 60
    
    print('속도 : {:0.2f} 정확도 : {:0.2f} 오타율 : {:0.2f}'.format(speed, c, e))