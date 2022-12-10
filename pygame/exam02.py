import numbers

def add(num):
    result = 0
    for number in range(num):
        result += (number + 1)
    return result

print(add(4856))