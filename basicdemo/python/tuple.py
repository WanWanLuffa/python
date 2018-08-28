#tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。用()标识
a = (1,2,3,4);
print a;
#创建单个tuple
b = (124);
print b;
#tuple里边放一个list
c = (1,2,3,[4]);#tuple包好list
print c;


d = c[3];
d.append(5);#这个方式可以改变C[3]的值，tuple复制都是给出指针；
print d;
print type(d);
d = 6;#将d的类型强制转化成了int,成了一个新的变量，不在跟c中的list有关系，不在是list,不会造成tuple中的值的改变
print d;
print type(d);
print c;

#c[2].append(e,f,g);#这个用法不可以，为什么呢？tuple不能复赋值
f = (1,2,[a,b,c])############注意此处只是把值放进去了，并没有把a,b,c的特性放进去
print f;

e = f[2];
e[0] = 'e';#可以看到d[3]给出去的是list的指针，值的改变会影响到tuple内部
e[1] = 78;#tuple放到list之后，可以变了?//e1的类型也变了，但是e1仍然是e的一个元素，e类型没变还是f中的那个list所以78穿进去了，但是e1的类型变了，不再是tuple b了，所以不会造成b的变化。
e[2] = 99;#反正我觉得好乱哟

print f;
print a;#a的值并没有改变
print b;
print c;

#(1, 2, 3, 4)
#124
#(1, 2, 3, [4])
#[4, 5]
#<type 'list'>
##<type 'int'>
##(1, 2, [(1, 2, 3, 4), 124, (1, 2, 3, [4, 5])])
#(1, 2, ['e', 78, 99])
#(1, 2, 3, 4)
#124
#(1, 2, 3, [4, 5])