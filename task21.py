
#1)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = list(zip(l1, l2))
print(l)
tpl=tuple(l)
print(tpl)


#output 

[(1, 4), (2, 5), (3, 6)]
((1, 4), (2, 5), (3, 6))




#2)

l1=[1,2,3,4,5,6,7,8]
l2=[20,40,50,60,59]
x=list(zip(l1,l2))
print(x)
tpl=tuple(x)
print(tpl)


#output

[(1, 20), (2, 40), (3, 50), (4, 60), (5, 59)]
((1, 20), (2, 40), (3, 50), (4, 60), (5, 59))


#3)

lst= [6, 9, 3, 1,2,10,5,8,7]
x= sorted(lst)
print("sorted list in ascending order:",x)

#output
sorted list in ascending order:
[1, 2, 3, 5, 6, 7, 8, 9, 10]


#4)

numbers = [1,2,6,7,13,14,12,17,16,53,67,34,75,48]
def even_numbers(num):
    if(num%2 == 0):
        return True
    else:
        return False

evenNums = filter(even_numbers, numbers)
print('Even Numbers are:')
for num in evenNums:
    print(num)


#output


Even Numbers are:
2
6
14
12
16
34
48

[Program finished]



