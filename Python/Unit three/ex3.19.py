#输入身份证号码输出对应的出生年月日
ID = input('请输入十八位身份证号码: ')
if len(ID) == 18:
    print("你的身份证号码是 " + ID)
else:
    print("错误的身份证号码")
year = ID[6:10]
moon = ID[10:12]
day = ID[12:14]
print("出生年月: " + year + '年' + moon + '月' + day + '日')
