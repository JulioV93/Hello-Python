### List Comprehension ###

#Formato para crear listas de manera comprimida

my_original_list = [35, 24, 62, 52, 30, 30, 17]
print(my_original_list)

my_list = [i for i in my_original_list]
print(my_list)

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_list = [i for i in range(len(my_original_list))]
print(my_list)

my_list = [i for i in range(8)]
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)