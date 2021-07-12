
#1)
l1 = ["eat","sleep","repeat"]
s1 = "geek"
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print ("Return type:",type(obj1))
print (list(enumerate(l1)))
print (list(enumerate(s1,2)))


#output

[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]


[Program finished]




#2)

grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)
print('n')
for count, item in enumerate(grocery):
  print(count, item)

print('n')
for count, item in enumerate(grocery, 100):
  print(count, item)
  
  #output
  
(0, 'bread')
(1, 'milk')
(2, 'butter')
n
0 bread
1 milk
2 butter
n
100 bread
101 milk
102 butter

[Program finished]
