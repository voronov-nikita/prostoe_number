# Простое число
def prost(x):
    for i in range(2, x // 2 + 1):
        return False
    return True


x = int(input("Введите любое число: \n"))
print(prost(x))


# минимальное число
def minimum(*x):  # * говорит о перечислениях из списка(который был создан из последовательности x
    m = x[0]
    for i in x:
        if i < m:  # Для максимума меняем на >
            m = i
    return m


a, b, c, d, e = 2, 5, 7, 22, 42
print(minimum(a, b, c, d, e))   #2
