# 判断这个字符串中有多少个字符、数字、空格、特殊字符
#首先定义一个字符串
str1 =input('请输入一个字符串:')
#初始化字符、数字、空格、特殊字符的计数
str_sum = 0
dig_sum = 0
spa_sum = 0
other_sum = 0
for strs in str1:
    #如果在字符串中有字符，那么字符的数量+1
    if strs.isalpha():
        str_sum += 1
    #如果在字符串中有数字，那么数字的数量+1
    elif strs.isdigit():
         dig_sum += 1
     #如果在字符串中有空格，那么空格的数量+1
    elif strs == ' ':
         spa_sum += 1
     #如果在字符串中有特殊字符那么特殊字符的数量+1
    else:
        other_sum += 1
print("该字符串中的字符有:",str_sum)
print("该字符串中的数字有:",dig_sum)
print("该字符串中的空格有:",spa_sum)
print("该字符串中的特殊字符有:",other_sum)