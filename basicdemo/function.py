#函数就是最基本的一种代码抽象的方式。
L = []
x = 1;
while x <= 100:
    L.append(x*x)
    x +=1;
print sum(L);

#在Python中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
		
def square_of_sum(L):
    sum = 0;
    for x in L:
        sum += x*x;
    return sum;

print square_of_sum([1, 2, 3, 4, 5])


import math
def quadratic_equation(a, b, c):
    t = math.sqrt(b * b - 4 * a * c)
    return (-b + t) / (2 * a),( -b - t )/ (2 * a)
	

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)


#默认参数
def greet(name='world'):
    print 'Hello, ' + name + '.'
greet()
greet('Bart')

#可变参数，可变参数也不是很神秘，Python解释器会把传入的一组参数组装成一个tuple传递给可变参数，因此，在函数内部，直接把变量 args 看成一个 tuple 就好了。
def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)



