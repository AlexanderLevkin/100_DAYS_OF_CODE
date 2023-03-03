with open("file1.txt") as file_1:
    file_1_list = file_1.readlines()

with open("file2.txt") as file_2:
    file_2_list = file_2.readlines()

list_2 = [int(num.replace("\n", "")) for num in file_2_list]
list_1 = [int(num.replace("\n", "")) for num in file_1_list]
result = [num for num in list_1 if num in list_2]
