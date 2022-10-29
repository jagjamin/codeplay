

result = 0

question = 0

numbers = []

running = True
while running:

    question = input("입력")
    if "+" in question:
        numbers = question.split("+")
        result = int(numbers[0]) + int(numbers[1])

    elif "-" in question:
        numbers = question.split("-")
        result = int(numbers[0]) + int(numbers[1])

    elif "/" in question:
        numbers = question.split("/")
        result = int(numbers[0]) + int(numbers[1])

    elif "*" in question:
        numbers = question.split("*")
        result = int(numbers[0]) + int(numbers[1])

    elif "꺼져" in question:
        break

    


    

    print(f"{question} = {result}")