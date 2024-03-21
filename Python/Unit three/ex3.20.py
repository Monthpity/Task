#字符串拆分与合并函数
str1="hello,python,hello,c"
print(str1.split() )         #默认使用空格做分配符，str1中无空格，列表中只有一个元素
print(str1.split(",") )      #使用逗号做分配符
print(str1.split(",",2) )    #使用逗号做分配符,限制分隔2次
lst=['hello','python!','hello','c!']
s=" "
print(s.join(lst))            #将列表连接为字符串