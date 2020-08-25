population = input().split(', ')
population = list(map(int, population))

minimum_wealth = int(input())

formula = (sum(population) / minimum_wealth) / len(population)

richest_ind = population.index(max(population))
poorest_ind = population.index(min(population))

is_equal = False
while formula >= 1 and population[poorest_ind] < minimum_wealth:
    change = minimum_wealth - population[poorest_ind]
    is_equal = True

    population[richest_ind] -= change
    population[poorest_ind] += change

    richest_ind = population.index(max(population))
    poorest_ind = population.index(min(population))

if is_equal:
    print(population)
else:
    print('No equal distribution possible')
