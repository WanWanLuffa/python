#在Python中，如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们成为迭代（Iteration）。
集合是指包含一组元素的数据结构，我们已经介绍的包括：
#1. 有序集合：list，tuple，str和unicode；
#2. 无序集合：set
#3. 无序集合并且具有 key-value 对：dict
#
for i in range(1, 101):
    if i % 7 == 0:
        print i而迭代是一个动词，它指的是一种操作，在Python中，就是 for 循环。

#Python中，迭代永远是取出元素本身，而非元素的索引。
#对于有序集合，元素确实是有索引的。有的时候，我们确实想在 for 循环中拿到索引，怎么办？ 方法是使用 enumerate() 函数：
#使用 enumerate() 函数，我们可以在for循环中同时绑定索引index和元素name。但是，这不是 enumerate() 的特殊语法。实际上，enumerate() 函数把：
#['Adam', 'Lisa', 'Bart', 'Paul']
#enumerate(L)
#变成了类似：
#[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]

#因此，迭代的每一个元素实际上是一个tuple：
#for t in enumerate(L):
#   index = t[0]
#   name = t[1]
#   print index, '-', name


#zip()函数可以把两个 list 变成一个 list：
#>>> zip([10, 20, 30], ['A', 'B', 'C'])
#[(10, 'A'), (20, 'B'), (30, 'C')]

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1, len(L)+1), L):
    print index, '-', name
	
#我们已经了解了dict对象本身就是可迭代对象，用 for 循环直接迭代 dict，可以每次拿到dict的一个key。
#dict 对象有一个 values() 方法，这个方法把dict转换成一个包含所有value的list，这样，我们迭代的就是 dict的每一个 value：
#d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
#print d.values()
# [85, 95, 59]
#for v in d.values():
 #   print v
# 85
# 95
# 59
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for v in d.itervalues():
    sum = sum + v
print sum / len(d)


#首先，我们看看 dict 对象的 items() 方法返回的值：可以看到，items() 方法把dict对象转换成了包含tuple的list，我们对这个list进行迭代，可以同时获得key和value：
#和 values() 有一个 itervalues() 类似， items() 也有一个对应的 iteritems()，iteritems() 不把dict转换成list，而是在迭代过程中不断给出 tuple，所以， iteritems() 不占用额外的内存。

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for k, v in d.iteritems():
    sum = sum + v
    print k, ':', v
print 'average', ':', sum / len(d)