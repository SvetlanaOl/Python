#Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("Введите число x")
x = int(input())
print("Введите число y")
y = int(input())
print("Введите число z")
z = int(input())
print(not (x or y or z) == (not x and not y and not z))