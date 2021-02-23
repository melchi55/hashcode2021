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

print("\n")

for x in range(len(pizza_list)):
    print(" Pizza :", x, "has ", len(pizza_list[x]), "ingredients")
    for ing in pizza_list[x]:
        print("* :", ing)
    print("\n")

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

print(selected_2_person_team_num)
print(selected_3_person_team_num)
print(selected_4_person_team_num)

total_oder = selected_2_person_team_num + selected_3_person_team_num + selected_4_person_team_num

oder_3 = []
oder_4 = []
oder_2 = []


def make_oder_2_people():
    for pizza in pizza_list:
        pass


def make_oder_3_people():
    for x in range(3):
        for pizza in pizza_list:
            if len(oder_3) == 0:
                oder_3.append(pizza)
                break
            else:
                pass
                




def make_oder_4_people():
    pass


def main():
    for x in range(selected_3_person_team_num):
        make_oder_3_people()
    print(oder_3)






if __name__ == '__main__':
    main()
