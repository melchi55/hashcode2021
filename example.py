file = open("a_example", mode="r")
first_line = file.readline().split(" ")

pizza_2_com = []
pizza_3_com = []
pizza_4_com = []

pizza_list = []

list_2_person = []
list_3_person = []
list_4_person = []

total_delivery = 0

remaining = file.read().split("\n")
for pizza in remaining:
    pizza_list.append((pizza.split(" ")))

for pizza in pizza_list:
    for ing in pizza:
        if "" == ing:
            pizza_list.remove(pizza)

for pizza in pizza_list:
    pizza.remove(pizza[0])

num_pizza = int(first_line[0])
num_2_teams = int(first_line[1])
num_3_teams = int(first_line[2])
num_4_teams = int(first_line[3])

print(
    "\n Number of Pizza :", num_pizza,
    "\n", num_2_teams, "team of two",
    "\n", num_3_teams, "team of three",
    "\n", num_4_teams, "team of four"
)

print("\n")

pizza_index_list = []


def make_pizza_index_list():
    for pizza in pizza_list:
        pizza_index_list.append(pizza_list.index(pizza))


def make_2_pizza():
    for pizza_1 in pizza_list:
        for pizza_2 in pizza_list:
            if pizza_1 != pizza_2:
                pizzas = list(set(pizza_1 + pizza_2))
                pizza_2_com.append([pizza_list.index(pizza_1), pizza_list.index(pizza_2), pow(len(pizzas), 2)])
    for pizza in pizza_2_com:
        pizza = pizza.sort()

    for pizzas in pizza_2_com:
        for pizzas in pizza_2_com:
            pizza = pizzas
            pizza_2_com.remove(pizza)
            if pizza not in pizza_2_com:
                pizza_2_com.append(pizza)


def make_3_pizza():
    for pizza_1 in pizza_list:
        for pizza_2 in pizza_list:
            for pizza_3 in pizza_list:
                if pizza_1 != pizza_2 and pizza_1 != pizza_3 and pizza_2 != pizza_3:
                    pizzas = list(set(pizza_1 + pizza_2 + pizza_3))
                    pizza_3_com.append([pizza_list.index(pizza_1), pizza_list.index(pizza_2), pizza_list.index(pizza_3),
                                        pow(len(pizzas), 2)])
    for pizza in pizza_3_com:
        pizza = pizza.sort()
    for pizzas in pizza_3_com:
        for pizzas in pizza_3_com:
            pizza = pizzas
            pizza_3_com.remove(pizza)
            if pizza not in pizza_3_com:
                pizza_3_com.append(pizza)


def make_4_pizza():
    for pizza_1 in pizza_list:
        for pizza_2 in pizza_list:
            for pizza_3 in pizza_list:
                for pizza_4 in pizza_list:
                    if pizza_1 != pizza_2 and pizza_1 != pizza_3 and pizza_2 != pizza_3 and pizza_1 != pizza_4 \
                            and pizza_2 != pizza_4 and pizza_3 != pizza_4:
                        pizzas = list(set(pizza_1 + pizza_2 + pizza_3 + pizza_4))
                        pizza_4_com.append(
                            [pizza_list.index(pizza_1), pizza_list.index(pizza_2), pizza_list.index(pizza_3),
                             pizza_list.index(pizza_4),
                             pow(len(pizzas), 2)])
    for pizza in pizza_4_com:
        pizza = pizza.sort()
    for pizzas in pizza_4_com:
        for pizzas in pizza_4_com:
            pizza = pizzas
            pizza_4_com.remove(pizza)
            if pizza not in pizza_4_com:
                pizza_4_com.append(pizza)


for x in range(len(pizza_list)):
    print(" Pizza :", x, "has ", len(pizza_list[x]), "ingredients")
    for ing in pizza_list[x]:
        print("* :", ing)
    print("\n")

make_2_pizza()
make_3_pizza()
make_4_pizza()

for pizzas in pizza_2_com:
    print(pizzas)

print("\n")

for pizzas in pizza_3_com:
    print(pizzas)

print("\n")

for pizzas in pizza_4_com:
    print(pizzas)

stop = True

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
print(selected_2_person_team_num)
print(selected_3_person_team_num)
print(selected_4_person_team_num)

print(num_pizza)

make_pizza_index_list()

print(pizza_index_list)

