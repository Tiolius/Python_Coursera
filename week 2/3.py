# Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).
# Какое наименьшее число операторов сравнения (>, <, >=, <=) необходимо для решения этой задачи?
# Формат ввода
# Вводится три целых числа.
# Формат вывода
# Выведите ответ на задачу.
a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print(a)
elif b >= c and b >= a:
    print(b)
else:
    print(c)