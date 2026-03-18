#NUMERIC
print(100**4)
print(100/4)
print(100/3)
print(100//3)


print('               I am alone'.strip())
print('In my room'.split())
print('Can I help'.replace('I',' you'))
print('In my room'.startswith('I'))
print('In my room'.endswith('I'))
print('In my room'.find('m'))
print('Hello'.upper())
print('HI HOW ARE YOU'.lower())
print('HI HOW ARE YOU'.count('H'))
name1='Tea'
name2='Lupu'
print(f'Hello there {name1} {name2}')
print('Hello there {} {}'.format(name1, name2))
print('Hi there %s %s' %(name1,name2))

mylist=[1,2,3,4,5, 't','e',True]
print(mylist)
print(mylist * 2)
print(mylist+[1000])
print(mylist.append(34))
print(mylist.insert(4,'????!!!!!'))
print(mylist)
print(mylist.pop())
mylist.remove('t')
print(   )
print(mylist)
List=[1, 2, 7, 60, 4, 300, 45, 3, 90]
List.sort()
print(List)
List.reverse()
print(List)
List.sort(reverse=True)
print(List)
print(1 in List)
print(min(List))
print(max(List))
print(sum(List))
print("        ")
first, *x, last = List
print(List)
print(first)
print(x)
print(last)
#set
newlist=[1,1,1,22,22,3,3,4,4,4,4,4,4,4,5,5,6,7,8]
print(set(newlist))
set1={1,2,3,4,5}
set2={6,7,8,9,10}
set3 = set1.union(set2)
print("    ")
print(set3)
print("TUPLE")
#tuple
mytuple=(1,2,3,4,5,'Teodora',True)
print(mytuple[3])

#dictionary
my_dict={'name':'Teodora', 'age':'21', 'Student':'True'}
print(my_dict)
print(my_dict['age'])
print(type(my_dict))

#None
type(None)
a=None
print(a)
