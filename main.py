'''x=20
y=10
z=y-x
z=y
y=x
print(z,y)'''

'''print(' how\n'+' are\n'+' you')'''

'''a=23
b="a"*29
print(b)'''

'''print('hello', '$'*23 ,'python')
print('hello\n'*2 ,'python\n')'''


'''bh = ord('a')
print(bh)'''
'''a=545
b=26562
div=b//a
print(div)'''
'''
def add(a,b):
    Return sum the given arguments.
    return a+b
print(add.__doc__)
def power(b, e):
    Return the power value.
    b--is the base
    e--is exponent
    
    return b**e
print(power.__doc__)
#print'''

'''lo=[1,3,5,7,9,11,13,15,17,19]
print(lo[-1:])
print(lo[:-1])'''

'''lo=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(lo[::2])
print(lo[::-1])'''

'''if(45652):
    print('hekk')'''

'''number = input("")
first_digit = number[0]
second_digit = number[1]
add = int(first_digit) + int(second_digit)
print(add)'''


'''a=int(input('Enter your age: '))
b=int(input('years now: '))
s=a-b
x=ayears
y=months
z=months
math=x*365,+y*52,z*months
print(f"math")'''

'''n=int(input(''))
p=n**0.25
print(p)'''
'''
k=int(input(''))
sum1=0
a=0
b=1
c=0
s=0
p=0
while(c<=k):
    print(c)
    a=b
    b=c
    if(p%2==0):
        s+=c
    p=p+1
    c=a+b
print('sum:',s)
'''

'''
k=int(input(''))
i=0
while i<k:
    if(i%2==0):
        print(i,'even no')
    else:
        print(i,'odd no')
    i+=1
'''
'''numbers=[1,10,20,30,40,50]
sum=0
for item in numbers:
    sum+=item
    print('The sum of numbers is',sum)

colors=['red','orange','green','yellow','white','violet']
for a in colors:
    sum+=a
    print(sum)'''

'''x=int(input(''))
y=int(input(''))
s=0
for i in range(1,y+1):
    if(y>20):
        print(y)
    else:
        print(x,'*',i,'=',x*i)

else:
    print('row is limited to 20')'''

'''value=int(input(''))
n=int(input('Enter  the n number'))
for num in range (value,n+1):        ### end=' ' for same line
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)'''
'''num=
for i in range(0,10):
    if (num%5==0):
        break
    print()
    num=num+1'''
'''a=int(input('Num:1'))
p=''
for i in range(a):
    for j in range(i):
        if i>=4 and i<=5:
            p+='1234'
        print(p)'''

'''char=['a','b','c']
list2=[1,2,3]
char.extend(list2)
print(char)'''

'''a=[9,8,7,6,5,4,]
print('a[0:3]: ',a[0:3])
print('a[:4]: ',a[:4])
print('a[1:]: ',a[1:])
print('a[:]: ',a[:])
print('a[2:2]: ',a[2:2])
print('a[0:6:2]: ',a[0:6:2])
'''

data=input('data: ')
list1=data.split(',')
list2=list1
print('list1 is list:',list1 is list2)
print('list2 is list1:',list2 is list1)
index=int(input('index: ')
