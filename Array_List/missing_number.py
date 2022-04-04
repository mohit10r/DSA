# find the missing number from a list

li = [1,2,3,4,5,6,7,8,9,11,12,13]

def find_missing(li, n):
    sum_of_list = int(n*(n+1)/2)
    sum_of_li = sum(li)
    print(sum_of_list-sum_of_li)

find_missing(li,13)
