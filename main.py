# expression = input("Введите арифметическое выражение (например, 23+12): ")
#
#
# num1, operator, num2 = expression.split()
#
#
# num1 = float(num1)
# num2 = float(num2)
#
#
# if operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '/':
#     result = num1 / num2
# else:
#     print("Некорректный оператор!")
#     exit()
#
#
# print(f"Результат выражения {expression}: {result}")


# import random
#
#
# numbers = [random.randint(-10, 10) for _ in range(10)]
#
#
# min_element = numbers[0]
# max_element = numbers[0]
# negative_count = 0
# positive_count = 0
# zero_count = 0
#
#
# for num in numbers:
#
#     if num < min_element:
#         min_element = num
#
#
#     if num > max_element:
#         max_element = num
#
#
#     if num < 0:
#         negative_count += 1
#
#
#     if num > 0:
#         positive_count += 1
#
#
#     if num == 0:
#         zero_count += 1
#
#
# print("Список чисел:", numbers)
# print("Минимальный элемент:", min_element)
# print("Максимальный элемент:", max_element)
# print("Количество отрицательных элементов:", negative_count)
# print("Количество положительных элементов:", positive_count)
# print("Количество нулей:", zero_count)