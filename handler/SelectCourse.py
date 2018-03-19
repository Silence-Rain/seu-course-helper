import requests

jxbbh = "09033120201720000"
xkkclx = "11"
jhkcdm = "09033120"

base = ""
url = "%s/runSelectclassSelectionAction.action?select_jxbbh=%s&select_xkkclx=%s&select_jhkcdm=%s" % (base, jxbbh, xkkclx, jhkcdm)
r = requests.post(url)
res = r.json()

if res.rso.isSuccess == 'true':
	print "已成功选择"