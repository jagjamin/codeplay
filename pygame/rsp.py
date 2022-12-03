u = 0
c = 0
rcp = ["가위","바위", "보"]
import random

running = True
u == input("가위바위보")
while running:
        c == random.randint(0,2) / random.choice("rcp")
        print(f"{c}")

        if u == "가위":
            c == "바위"
            print("짐")

            

        elif u == "보":
            c == "가위"
            print("짐")

            if u == "바위":
                c == "가위"
                print("이김")

            elif u == "가위":
                c == "보"
                print("이김")

                if u == "보":
                    c == "바위"
                    print("이김")

                elif u == "바위":
                    c == "보"
                    print("짐")
                if u == c:
                    print("비김")

                elif u == "q":
                    running = False

       



    

