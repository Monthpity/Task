#计算平均分和总分
name=input("学生姓名：")
Chinese=float(input("语文成绩:"))
Maths=float(input("数学成绩:"))
English=float(input("英语成绩:"))
sum=Chinese+Maths+English
average=sum/3
print("总成绩=%.2f" %sum)
print("平均成绩=%.2f" %average)