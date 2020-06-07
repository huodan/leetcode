# n = int(input("请输入总人数："))
# m = int(input("请规定报到数字几的人退出圈子："))
#
# circle = []
# for i in range(1, n + 1):
# 	circle.append(i)
# num = 1
# while len(circle) != m - 1:
# 	circle.append(circle.pop(0))  # 把已报数的人取出放到队尾，以此实现围成圈循环往复
# 	num += 1
# 	if num == m:
# 		del circle[0]  # 把报到规定数字的人踢出圈子
# 		num = 1  # 重新从1开始报数
# print(circle)


def main(m):
	if m <= 1 or m >= 100:
		print("ERROR!")
		return
	n = 100
	circle = []
	for i in range(1, n + 1):
		circle.append(i)
	print(circle)
	num = 1
	while len(circle) != m - 1:
		circle.append(circle.pop(0))  # 把已报数的人取出放到队尾，以此实现围成圈循环往复
		num += 1
		if num == m:
			del circle[0]  # 把报到规定数字的人踢出圈子
			num = 1  # 重新从1开始报数
	print(circle)
	circle_str = [str(i) for i in sorted(circle)]

	print(','.join(circle_str))


if __name__ == '__main__':
	main(3)

