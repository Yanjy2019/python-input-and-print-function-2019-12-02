print("hello world")

#基本输入输出函数
#print输出函数
print("世界和平")
a=100
b=10
print("a的变量值是{},b的变量值为{}".format(a,b))
print(a,end=" ")   #直接跟在后面进行输出内容
print(b,end="\n")  #换行操作
print(b,end="%")
print(a)

#input输入函数
#a=input("请输入一行字符串：")
print(a)

#变量及其保留字
a=100
a+=1
print(a)
Aa_3机器学习=99
print(Aa_3机器学习) #需要注意的是python标识符不可以和内部所存在的33个保留字相同

#Python数据类型
print(180)           #十进制输出变量
print(0b10110100)    #二进制输出变量
print(0o264)         #八进制输出变量
print(0xb4)          #十六进制输出变量
print(1.23466255752342e2)

print("对酒当歌，人生几何？"[1:4])
print("对酒当歌，人生几何？"[-4:-2])#切片操作

#表达式与赋值语句
a=1024*32
print(a)
a="对酒当歌，人生几何？"+"譬如朝露，去日苦多!"
print(a)
a,b=3,4
a,b=b,a  #变量交换
print(a,b)
print(type(a))
print(type("对酒当歌，人生几何")) #type可以获得任何变量的数据类型
a=input("请输入任意字符类型：")
b=type(a)
print(b)

#eval函数:经常与input函数一起连用来进行获取输入的数据类型
a=eval("1.2+3.4")
print(a)  #eval函数可以直接将字符串的引号去掉，然后按照正常的表达式进行计算和运算合并
a=eval(input("请输入数据为："))  #eval函数获取所输入数据的数据内容
print(a*2+311)

#浮点数与复数
print(type(11100))
print(type(111.0))
print(pow(2,3))  #pow表示的是2的3次方
print(round(0.1+0.2,1))  #浮点数的特殊诉情况“浮点数的表示都是以二进制来进行表示，产生了不确定的尾数，这是由于计算机表示浮点数的存储宽度有限所导致的,可以使用round函数来进行解决尾数的不确定问题

#Python中复数的表示，实部和虚部在Python里面都是浮点型的数据类型
a=23+4J
print(type(a))
print(a.real)
print(a.imag)











