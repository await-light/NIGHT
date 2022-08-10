import os
import json
import pprint
import requests
from dns import resolver
try:
	from dns_over_https import SecureDNS
except:
	print("installing dns_over_https...")
	os.system("pip3 install dns_over_https")
try:
	from lxml import etree
except:
	print("installing lxml...")
	os.system("pip3 install lxml")

DNS_SERVER = "8.8.8.8"
UA = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10"
		".0; Win64; x64) AppleWebKit/537.36 "
		"(KHTML, like Gecko) Chrome/98.0.475"
		"8.82 Safari/537.36",
	}

def getinfo(domain_name,write=False):
	url = "https://api.devopsclub.cn/api/whoisquery"
	data = {"domain":domain_name,"type":"json"}
	r = requests.request("post",url,data=data,headers=UA)
	r.encoding = "utf8"
	detaildomain = r.json()
	if write:
		with open("./data/whois-%s.json" % domain_name,"w") as f:
			json.dump(detaildomain,f,indent=6)
	return detaildomain 

def getip(domain_name):
	# answer = resolver.resolve(domain_name)
	# return answer.response.answer
	return SecureDNS().gethostbyname(domain_name)
