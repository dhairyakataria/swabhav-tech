def calculate_product(list_arg):
    product = 1
    for ele in list_arg:
        product = product*ele
    return product

list1 = [10,20,30]
print(calculate_product(list1))

list2 = [int(range(1,6,2))]
print(calculate_product(list2))