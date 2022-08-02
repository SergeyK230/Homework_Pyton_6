# Найти сумму чисел списка стоящих на нечетной позиции

list = [1, 2, 3, 5, 1, 5, 3, 10]
list = sum([list[i] for i in range(len(list)) if not i%2])
print(list)