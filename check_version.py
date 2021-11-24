import sys
import requests

def check_versios(ip):
	XML='''<?xml version="1.0" encoding="UTF-8"?><Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/"><Body><RetrieveServiceContent xmlns="urn:vim25"><_this type="ServiceInstance">ServiceInstance</_this></RetrieveServiceContent></Body></Envelope>'''
	resp = requests.post("https://" + ip + "/sdk", data=XML, headers={'Soapaction':'urn:vim26/6.7', 'Content-Type':'text/xml; charset="utf-8"'}, verify=False)
	return resp.text



if __name__ == "__main__":
	
	print(check_versios(sys.argv[1]))