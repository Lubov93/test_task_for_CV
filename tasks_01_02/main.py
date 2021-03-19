# Task 01

def slice_less(my_list,lesser):
    return [i for i in sorted(my_list, reverse=True) if i > lesser]


#print(slice_less([1,2,3,4,5], 5))
#print(slice_less([10,21,3,40,5], 4))


# Task 02

for i in range(11, 80):
    if i % 3 == 0 and i % 5 == 0:
        print('$$@@')
    elif i % 5 == 0:
        print('@@')
    elif i % 3 == 0:
        print('$$')
    else:
        print(i)




