import random

eng = ["cat","car","see","win","can","bee","apple","word","good","hit"]
kor = ["고양이","차","보다","이기다","캔","벌","사과","단어","좋은","치다"]
score = 0
running = True

while running:

    ok = 0
    for i in range(10):
        if kor[i] == input(f"{eng[i]}"):
            print("정답")
            ok += 1
    else:
        print("오답")
        break
    print
    running = False