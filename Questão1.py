counter = 0
for number in range(1, 5000001):
    if (number % 2 == 0) and (number % 49 == 0) and (number % 37 == 0):
        counter += 1
print(counter)

#ALGORITMO GERAL, COM A FUNÇÃO RECEBENDO UM VETOR COM OS NÚMEROS PELOS QUAIS SE DESEJA DIVISIBILIDADE,
#O INÍCIO DO INTERVALO E O FINAL DO INTERVALO:
#=================================================================================
#def devisibility(conditions, rangestart, rangeend):
#    counter = 0
#    for number in range(rangestart, rangeend + 1):
#        conditions_satisfied = True
#        for condition in conditions:
#            if number % int(condition) != 0:
#                conditions_satisfied = False
#        if conditions_satisfied == True:
#            counter += 1
#    return counter
#print(devisibility([2, 37, 49], 1, 5000000))