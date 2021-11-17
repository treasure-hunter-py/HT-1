''' 6 '''

arr_2 = input('Enter arr ').split()
key_arr = input('Enter locket ')
bable = False
for iter_arr in range (len(arr_2)):
    if arr_2[iter_arr] == key_arr:
        bable = True
        break
print(bable)
