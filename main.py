def prost(x):
    for i in range(2, x//2+1):
        return False
    return True

x = int(input("Введите любое число: \n"))
print(prost(x))

