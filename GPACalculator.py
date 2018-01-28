res = []
tenth_arr = [0, 0, 0, 0, 0, 0, 1, 2, 3, 4]
unit_arr = [0, 0, 0, 0.5, 0.5, 0.5, 0.8, 0.8, 0.8, 0.8]
level_dict = {"优": 95, "良": 85, "中": 75, "通过": 65}

def read_file():
	with open("data/score.txt", "r") as file:
		for line in file.readlines():
			temp = []
			info = line.split(" ")

			temp.append(info[0].split("\t")[3])
			for item in info[1:5]:
				temp.append(item.strip())

			res.append(temp)

def preprocess():
	for row in res:
		toDel = []

		if row[3] == "补考" or row[3] == "重修":
			for i in range(0, len(res)):
				if row[0] == res[i][0] and row[2] > res[i][2]:
					toDel.append(i)

		for i in toDel:
			del res[i]

def calc():
	totalGPA = 0
	totalScore = 0

	for row in res[:13]:
		if row[4] != "":
			continue

		totalScore += float(row[1])
		totalGPA += correspond_gpa(row[2]) * float(row[1])

	print(totalGPA / totalScore)	

def correspond_gpa(grade):
	if grade == "优" or grade == "良" or grade == "中" or grade == "通过":
		temp = level_dict[grade]
	else:
		temp = int(grade)

	tenth = int(temp / 10)
	unit = temp % 10

	return tenth_arr[tenth] + unit_arr[unit]


if __name__ == "__main__":
	read_file()
	preprocess()
	calc()