import csv

with open("scores.csv", "r") as file:
    data = list(csv.reader(file))

user_value = input("Enter the batsman name to know the runs : ")
for batsman in data:
    if batsman[0] == user_value:
        print(f"{batsman[0]} scored {batsman[1]} runs ")
