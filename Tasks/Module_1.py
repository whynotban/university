# task 1

a = int(input())
b = int(input())
c = int(input())

print(a + b + c)

# task 2

a = int(input())
h = int(input())

print(a * h / 2)

# task 3

name = input()

print(f"Привет, {name}!")

# task 4

n = int(input())

print(f"Следующее число для числа {n}: {n + 1}")
print(f"Предыдущее число для числа {n}: {n - 1}")

# task 5

n = int(input())
k = int(input())

print(f"Яблок у студентов: {k // n}, в корзине: {k % n}")

# task 6

n = int(input())

hours = n // 3600
minutes = (n % 3600) // 60

total_minutes = n // 60
print(f"{hours} {total_minutes}")

# task 7

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

time_in_seconds1 = h1 * 3600 + m1 * 60 + s1
time_in_seconds2 = h2 * 3600 + m2 * 60 + s2

print(time_in_seconds2 - time_in_seconds1)
