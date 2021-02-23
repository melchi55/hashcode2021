file = open("a_example", mode="r")
first_line = file.readline().split(" ")

for x in first_line:
    if x == "\n":
        first_line.remove("\n")

num_pizza, num_2_teams, num_3_teams, num_4_teams = int(first_line[0]), int(first_line[1]), int(first_line[2]), int(
    first_line[3])

remaining = file.read().split("\n")

for x in remaining:
    if x == "":
        remaining.remove("")

pizza_list = []

for pizza in remaining:
    pizza_list.append(pizza.split(sep=" "))

for pizza in pizza_list:
    pizza.remove(pizza[0])

print(
    "\n Number of Pizza :", num_pizza,
    "\n", num_2_teams, "team of two",
    "\n", num_3_teams, "team of three",
    "\n", num_4_teams, "team of four"
)

selected_2_person_team_num = 0
selected_3_person_team_num = 0
selected_4_person_team_num = 0

for x in range(num_2_teams):
    if not num_pizza < 2:
        num_pizza -= 2
        selected_2_person_team_num += 1

for x in range(num_3_teams):
    if not num_pizza < 3:
        num_pizza -= 3
        selected_3_person_team_num += 1

for x in range(num_4_teams):
    if not num_pizza < 4:
        num_pizza -= 4
        selected_4_person_team_num += 1

print("\n")

for x in range(len(pizza_list)):
    print(" Pizza :", x, "has ", len(pizza_list[x]), "ingredients")
    for ing in pizza_list[x]:
        print("* :", ing)
    print("\n")

com_2_pizza = []
com_3_pizza = []
com_4_pizza = []

for pizza_one in pizza_list:
    for pizza_two in pizza_list:
        if pizza_one != [] and pizza_two != []:
            if pizza_one != pizza_two:
                pizzas = set(pizza_one + pizza_two)
                index_score = [pizza_list.index(pizza_one), pizza_list.index(pizza_two)]
                com_2_pizza.append(index_score)
for pizzas_com in com_2_pizza:
    pizzas_com = pizzas_com.sort()

for pizzas in com_2_pizza:
    for pizzas in com_2_pizza:
        pizza = pizzas
        com_2_pizza.remove(pizza)
        if pizza not in com_2_pizza:
            com_2_pizza.append(pizza)

for pizza_one in pizza_list:
    for pizza_two in pizza_list:
        for pizza_three in pizza_list:
            if pizza_one != [] and pizza_two != [] and pizza_three != []:
                if pizza_one != pizza_two and pizza_one != pizza_three and pizza_two != pizza_three:
                    pizzas = set(pizza_one + pizza_two + pizza_three)
                    index_score = [pizza_list.index(pizza_one), pizza_list.index(pizza_two),
                                   pizza_list.index(pizza_three)]
                    com_3_pizza.append(index_score)
for pizza in com_3_pizza:
    pizza = pizza.sort()
for pizzas in com_3_pizza:
    for pizzas in com_3_pizza:
        pizza = pizzas
        com_3_pizza.remove(pizza)
        if pizza not in com_3_pizza:
            com_3_pizza.append(pizza)


for pizza_one in pizza_list:
    for pizza_two in pizza_list:
        for pizza_three in pizza_list:
            for pizza_four in pizza_list:
                if pizza_one != pizza_two and pizza_one != pizza_three and pizza_two != pizza_three and \
                        pizza_one != pizza_four and pizza_two != pizza_four and pizza_three != pizza_four:
                    pizzas = set(pizza_one + pizza_two + pizza_three + pizza_four)
                    index_score = [pizza_list.index(pizza_one), pizza_list.index(pizza_two),
                                    pizza_list.index(pizza_three),
                                    pizza_list.index(pizza_four)]
                    com_4_pizza.append(index_score)
for pizza in com_4_pizza:
    pizza = pizza.sort()
for pizzas in com_4_pizza:
    for pizzas in com_4_pizza:
        pizza = pizzas
        com_4_pizza.remove(pizza)
        if pizza not in com_4_pizza:
            com_4_pizza.append(pizza)

for pizzas in com_2_pizza:
    print(pizzas)

print("\n")

for pizzas in com_3_pizza:
    print(pizzas)

print("\n")

for pizzas in com_4_pizza:
    print(pizzas)

all_com = []







