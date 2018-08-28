# while 循环，while 循环不会迭代 list 或 tuple 的元素，而是根据表达式判断循环是否结束。
sum = 0
x = 1
while x < 100:
    sum += x;
    x += 2;
print sum


sum = 0
x = 1
n = 1
while True:
    sum += x;
    x *=2;
    n +=1;
    if n> 20:
        break;
print sum

sum = 0
x = 0;
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue;
    sum = sum + x;
print sum


for x in [ 1,2,3,4,5,6,7,8,9 ]:
    for y in [ 0,1,2,3,4,5,6,7,8,9 ]:
        if (x<y):
            print 10*x+y;