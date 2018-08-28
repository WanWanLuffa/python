#我们把名字称为key，对应的成绩称为value，dict就是通过 key 来查找 value
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}

print 'Adam:',d['Adam'];
print 'Lisa:',d['Lisa'];
print 'Bart:',d['Bart'];
#dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。
#由于dict是按 key 查找，所以，在一个dict中，key不能重复。
#dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样：
print d;#打印的顺序不一定是我们创建时的顺序

#dict的第三个特点是作为 key 的元素必须不可变，Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。
e = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}

e[72] = 'Paul';#请根据Paul的成绩 72 更新下面的dict：

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print key + ':',d[key];#通过d[key]获取对应的value。
	
	
s = set(['Adam', 'Lisa', 'Bart', 'Paul'])#set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。
s = set(['Adam', 'adam', 'Lisa', 'lisa', 'Bart', 'bart', 'Paul', 'paul'])
print 'adam' in s
print 'bart' in s #区分大小写

x = 'jame' # 用户输入的字符串
if x in s:
    print 'input ok'
else:
    print 'input error'
	
months = set(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print 'x1: ok'
else:
    print 'x1: error'

if x2 in months:
    print 'x2: ok'
else:
    print 'x2: error'
	
v = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in v:
    print x[0] + ':', x[1]
	
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:
    if name in s:
        s.remove(name);
    else:
        s.add(name);
print s