# a=int(input('a= '))
# b=int(input('b= '))
# if a>b:
#     print("max = ", a)
# else:
#     print("max = ", b)

# ___________

for i in range(1,11):
    print(i)

# ___for and while
# # 1
s=0
for i in range(91,145):
    if i % 2 == 0:
        s=s+i
print('sum = ', s)

s=0
for i in range(92,145,2):
    s=s+i
print('sum = ', s)

i=91
s=0
while i<=145:
    if i % 2 == 0:
        s=s+i
    i=i+1
print('sum = ', s)

i=91
s=0
while True:
    if i > 145:
        break
    if i % 2 == 0:
        s=s+i
    i=i+1
print('sum = ', s)

# # 2
s=0
for i in range(1,26):
    s=s+i
print('sum = ', s)

s=0
i=1
while i<=25:
    s=s+i
    i=i+1
print('sum = ', s)

s=0
i=1
while True:
    if i >25:
        break
    s=s+i
    i=i+1
print('sum = ', s)

# # 3
n=input(': ')
answer=0
for i in n:
    if int(i)>=answer:
        answer=int(i)
print(answer)

n=int(input(': '))
n =abs(n)
answer=0
while n:
    i = n % 10
    if i>=answer:
        answer = i
    n//= 10
print(answer)



