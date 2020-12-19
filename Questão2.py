import math
import statistics
list = []
for number in range(0, 10):
    if number % 2 == 0:
        x = pow(3, number) + 7 * math.factorial(number)
    else:
        x = pow(2, number) + 4 * math.log(number)
    list.append(x)
print("Valor Máximo: " + str(max(list)) + "\n" + "Posição do Valor Máximo: " + str(list.index(max(list))))
print("Média: "+ str(round(statistics.mean(list), 2)))