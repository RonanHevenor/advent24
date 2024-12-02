import csv

list1 = []
list2 = []

with open("input1.txt", "r") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        list1.append(int(row[0]))
        list2.append(int(row[1]))

count_dict = {}

for num in list2:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

similarity_score = 0

for num in list1:
    if num in count_dict:
        similarity_score += num * count_dict[num]

print(similarity_score)
