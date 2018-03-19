#!coding=utf-8

import requests
import sys
import threading
from bs4 import BeautifulSoup

# reload(sys)
# sys.setdefaultencoding("utf8")
content = [[], [], [], []]

# 获得网页内容并解析
def get_content(ids, year, index):
	for i in ids[index]:
		# 获取内容
		base = "http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action"
		url = "%s?queryStudentId=%s&queryAcademicYear=%s" % (base, i, year)
		r = requests.post(url)
		r.encoding = "utf-8"

		# 解析内容
		try: 
			soup = BeautifulSoup(r.text, "lxml")
			name = soup.find("table", attrs={"cellpadding": "5", "cellspacing": "5"}).find_all("tr")[4].find("table").find("tr").find_all("td")[4].string[3:]
			row_all = soup.find("table", attrs={"class": "tableline"}).find_all("tr")
		except AttributeError as e:
			continue

		res_all = [i, name]
		for row in row_all[1:-1]:
			val = str(row.find_all("td")[2].string.strip())

			if val != "":
				res_all.append(val)

		content[index].append(res_all)


# 写入文件记录
def write_txt(content):
	with open("data/09015.txt", "w") as file:
		for c in content:
			for row in c:
				for item in row:
					file.write(item + " ")
				file.write("\r\n")

	print("写入成功")


# 09015所有学生学号迭代器（按班级分隔）
def stuID_iter():
	ret = [[], [], [], []]

	for c in range(1, 5):
		for i in range(1, 45):
			if i < 10:
				ret[c - 1].append("09015%s0%s" % (c, i))
			else:
				ret[c - 1].append("09015%s%s" % (c, i))

	return ret


if __name__ == "__main__":
	ids = stuID_iter()
	year = "17-18-3"

	threads = []
	t1 = threading.Thread(target=get_content, args=(ids, year, 0))
	t2 = threading.Thread(target=get_content, args=(ids, year, 1))
	t3 = threading.Thread(target=get_content, args=(ids, year, 2))
	t4 = threading.Thread(target=get_content, args=(ids, year, 3))
	threads.append(t1)
	threads.append(t2)
	threads.append(t3)
	threads.append(t4)

	try:
		for item in threads:
			item.start()
		for item in threads:
			item.join()
	except:
		pass

	write_txt(content)