def prod_of_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] * prod_of_array(arr[1:])    

print(prod_of_array([10,2,3,4]))