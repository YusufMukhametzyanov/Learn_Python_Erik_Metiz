my_number = int(input("Enter your number: \n\t"))
my_list = []

for item in range(0, 11):
    my_list.append(item)
    if item == my_number:
        my_list.pop(item)
        my_list.append('straight way'.upper())
if 'STRAIGHT WAy' in my_list:
    print(True)
else:
    print(False)
