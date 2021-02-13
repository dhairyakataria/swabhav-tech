from random import randint
list_1 = [randint(1,5) for _ in range(10)]
print('ex-1 = ', list_1)

listoflist = [[1,2,3], [4,5,6], [7,8,9]]
new_list = [ele 
              for sub_list in listoflist 
                for ele in sub_list]
print('ex-2 = ', new_list)
