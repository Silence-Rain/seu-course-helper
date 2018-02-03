#!coding=utf8
# 成绩信息
# 格式：[课程名，学分，成绩，状态（首修，重修，补考），全校通选课备注]
res = []
# 对非数字成绩的翻译
level_dict = {"优": 95, "良": 85, "中": 75, "通过": 65}
# 东大GPA计算方案
tenth_arr_seu = [0, 0, 0, 0, 0, 0, 1, 2, 3, 4]
unit_arr_seu = [0, 0, 0, 0.5, 0.5, 0.5, 0.8, 0.8, 0.8, 0.8]


def read_file():
	with open("data/score.txt", "r") as file:
		for line in file.readlines():
			temp = []
			# 以空格分开各个字段
			info = line.split(" ")
			# 第一个字段以tab细分为3个子字段，最后一个是课程名
			temp.append(info[0].split("\t")[3])
			# 其余字段除掉空字符
			for item in info[1:5]:
				temp.append(item.strip())

			res.append(temp)

def preprocess():
	# 对标记“补考”“重修”的课程，根据课程名寻找到该课程的所有成绩，取最高一次，其余删去
	for row in res:
		toDel = []

		if row[3] == "补考" or row[3] == "重修":
			for i in range(0, len(res)):
				if row[0] == res[i][0] and row[2] > res[i][2]:
					toDel.append(i)

		for i in toDel:
			del res[i]

def calc(handler):
	# 计算GPA，GPA=总成绩*总学分/总学分
	tGPA = 0
	tScore = 0

	for row in res[:13]:
		if row[4] != "":
			continue

		tScore += float(row[1])
		if handler == "seu":
			tGPA += correspond_gpa_seu(row[2]) * float(row[1])
		elif handler == "wes":
			tGPA += correspond_gpa_wes(row[2]) * float(row[1])

	print(tGPA / tScore)	

def correspond_gpa_seu(grade):
	# 根据数字成绩计算出对应GPA（东大）
	if grade == "优" or grade == "良" or grade == "中" or grade == "通过":
		temp = level_dict[grade]
	else:
		temp = int(grade)

	# 个位十位累加计算
	tenth = int(temp / 10)
	unit = temp % 10

	return tenth_arr_seu[tenth] + unit_arr_seu[unit]

def correspond_gpa_wes(grade):
	# 根据数字成绩计算出对应GPA（WES）
	temp = int(grade)

	if temp <= 100 and temp >= 85:
		return 4
	elif temp <= 84 and temp >= 75:
		return 3
	elif temp <= 74 and temp >= 60:
		return 2
	else:
		return 1


if __name__ == "__main__":
	read_file()
	preprocess()
	calc("wes")