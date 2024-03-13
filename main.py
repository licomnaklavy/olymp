with open("songs.txt", encoding="utf-8") as file:
    a = file.readline()
    s = [i.split("?")[1:3] for i in file.readlines()]

my_dict = {}

for el in s:
    song = el[1]
    artist = el[0]
    my_dict[song] = artist

while True:
    inp = input()
    if inp == "0":
        break
    elif inp in my_dict.keys():
        print(f"Песня {inp} принадлежит {my_dict[inp]}\n")
    else:
        print("К сожалению, ничего не удалось найти")
