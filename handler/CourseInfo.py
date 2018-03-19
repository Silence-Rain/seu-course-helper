#!coding: utf-8

import requests
import json
from bs4 import BeautifulSoup

def get_content():
	url = "http://xk.urp.seu.edu.cn/jw_css/xk/runMainmainSelectClassAction.action"
	headers = {
		"Cookie": "gr_user_id=d69c57dd-3903-4dfb-b017-208fe1953b55; zg_did=%7B%22did%22%3A%20%221608cd8c4031a5-054a8238e01962-b7a103e-1fa400-1608cd8c4049cf%22%7D; zg_8da79c30992d48dfaf63d538e31b0b27=%7B%22sid%22%3A%201514876541296%2C%22updated%22%3A%201514876726817%2C%22info%22%3A%201514876541302%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%7D; JSESSIONID=0000FDaWKYve-1Cuo-k7uw3LFG5:16tmsl2mi",
		"Referer": "http://xk.urp.seu.edu.cn/jw_css/system/showLogin.action"
		}

	r = requests.get(url, headers = headers)
	soup = BeautifulSoup(r.text, "lxml")
	course_list = soup.find("table", attrs={"id": "selectList"}).find_all("tr")
	res = {}

	for item in course_list:
		try:
			temp = item.find_all("td")
			label = str(temp[0].find("font").string)
			btn_info = temp[-1].find("button", attrs={"class": "button1"})["onclick"].split("'")

			temp_info = {
				"select_jxbbh": btn_info[3],
				"select_xkkclx": 11,
				"select_jhkcdm": btn_info[1],
			}
			print(label)
			res[label] = temp_info

		except TypeError as e:
			continue

	return res

def write_json(content):
	c = json.dumps(content, ensure_ascii=False)
	with open("data/course&code.json", "a", encoding="utf8") as f:
		f.write(c)
		print("\n写入成功！")

if __name__ == '__main__':
	res = get_content()
	write_json(res)