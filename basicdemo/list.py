#list。list是一种有序的集合，可以随时添加和删除其中的元素。用[]表示；
a = ['ni ba','nima','nima'];
print a;

b = ['nige','nijie','nidi','nige'];
a+=b;
print a;

#按照索引访问list
print a[0];
#print a[10];
print a[-1];#可以看出list可以倒叙访问，-1为最后一个 元素；
#添加新的元素j，自动保存到末尾；
a.append('niyeye');
print a[-1];
#插入元素，到第几个位置，后面的一次向后移动；
print a[3];
a.insert(3,'nidabo');
print a[3];
print a[4];
print u'*******************************'
#删除元素
b = a.pop();#缺省值删除末尾最后一个
print b;
a +=b;
b = a.pop(2);#取出放到另一个list中，再插回到原来的位置
print b;
a.insert(2,b);
print a[2];
print u'*******************************'
