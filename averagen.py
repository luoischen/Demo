N = 10 # 控制输入条数
sum = 0 # 总和
count = 0 # 基础数
print("please input 10 numbers:") # 打印内容
while count < N:  # 如果cnunt小于N就执行下面内容
	number = float(input()) # nuber 用来收集数字信息
	sum = sum + number # sun等于 sun + 输入的信息值
	count = count + 1 # 在基础数上 每次加1
average = sum / N # 定义平均数的变量，平均数等于 sum总和除以N所有条数
print("N = {}, Sum = {}".format(N, sum)) # 打印 条数和总和
print("Average = {:.2f}".format(average)) # 打印 平均数值到小数点后两位

