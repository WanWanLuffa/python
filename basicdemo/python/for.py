#name 这个变量是在 for 循环中定义的，意思是，依次取出list中的每一个元素，并把元素赋值给 name，然后执行for循环体
L = [45,56,78,89]
sum = 0.0;
for score in L:
	sum += score;
print sum/4;