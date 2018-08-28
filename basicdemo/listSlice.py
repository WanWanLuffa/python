#对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
#对应上面的问题，取前3个元素，用一行代码就可以完成切片：
#>>> L[0:3]
#只用一个 : ，表示从头到尾：
#因此，L[:]实际上复制出了一个新list。
#第三个参数表示每N个取一个，上面的 L[::2] 会每两个元素取出一个来，也就是隔一个取一个。
#把list换成tuple，切片操作完全相同，只是切片的结果也变成了tuple。
#range()函数可以创建一个数列：
L = range(1, 101)
print L[:10]
print L[2::3]
print L[4:50:5]

#对于list，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
#记住倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引。
L = range(1, 101)
print L[-10:]
print L[-46::5]
#字符串 'xxx'和 Unicode字符串 u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
def firstCharUpper(s):
    return s[0].upper() + s[1:]#字符串有个方法 upper() 可以把字符变成大写字母：
print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')