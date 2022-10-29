import numbers
import random
from unicodedata import numeric

def wordmemorrize():
    eng = ["cat","car","see","win","can","bee","apple","word","good","hit"]
    kor = ["고양이","차","보다","이기다","캔","벌","사과","단어","좋은","치다"]
    pick = 0
    score = 0
    answer = 0

    while len(eng) > 0:
        pick = random.randint(0, len(kor) - 1)

        answer = input(f"{kor[pick]}의 뜻은?")
        if answer == eng[pick]:
            print("정답")
            kor.pop(pick)
            eng.pop(pick)
        else:
            print("오답")

    print("다 외었군")
    if score < 6:
        print("올")
    elif 5 < score <9:
        print("ㅋ")
    else:
        print("ㅋㅋㅋ")

def lotto():
    pass

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
dangchum = []
pick = 0
answer = 0


# for i in range(7):
#     pick = numbers.pop(random.randint(0, len(numbers) -1))
#     dangchum.append(pick)

dangchum = random.sample(numbers, 7)

print("당첨번호")
print(dangchum)