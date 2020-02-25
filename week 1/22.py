# Дано четырехзначное число. Определите, является ли его десятичная запись симметричной.
# Если число симметричное, то выведите 1, иначе выведите любое другое целое число.
# Число может иметь меньше четырех знаков, тогда нужно считать, что его десятичная запись дополняется слева нулями.
# Формат ввода
# Вводится единственное число.
# Формат вывода
# Выведите ответ на задачу.
n = int(input())
n1 = n // 1000
n2 = n // 100 % 10
n3 = n // 10 - n1 * 100 - n2 * 10
n4 = n % 10
s1 = (n1 - n4) ** 2
s2 = (n2 - n3) ** 2
print(s1 + s2 + 1)
