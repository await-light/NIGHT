import nmap
import pprint
from domain import *

def getserves(ip):
	nm = nmap.PortScanner()
	serves = nm.scan(ip,arguments="-sV")
	with open("./data/serves-%s.txt" % ip,"a+") as fp:
		json.dump(serves,fp,indent=6)
	return serves

def getall(ip):
	nm = nmap.PortScanner()
	allinfo = nm.scan(ip,arguments="-A")
	with open("./data/all-%s.txt" % ip,"a+") as fp:
		json.dump(allinfo,fp,indent=6)
	return allinfo

def collect(domain):
	pprint.pprint(getinfo(domain,write=True))
	ip = getip(domain)
	pprint.pprint(ip)
	pprint.pprint(getserves(ip))
	pprint.pprint(getall(ip))

collect("xq.kzw.ink")