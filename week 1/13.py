# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере
# (важно в точности соблюдать вывод программы: обратите внимание на пробелы и на точки).
# Нельзя пользоваться конкатенацией строк, используйте print с несколькими параметрами.
# Формат ввода
# Вводится целое число (гарантируется, что число находится в диапазоне от -1000 до +1000).
# Формат вывода
# Выведите две строки, согласно образцу.
n = int(input())
print('The next number for the number ' + str(n) + ' is ' + str(n+1)+'.')
print('The previous number for the number ' + str(n) + ' is ' + str(n-1)+'.')
