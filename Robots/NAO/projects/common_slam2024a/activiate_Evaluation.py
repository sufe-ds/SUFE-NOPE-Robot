# -*- coding: utf-8 -*-
body=""
import urllib2
E_Mail="wangstoudamire@163.com"
Days=7
error_out=[False,0,""]
error_in=[False,0,""]
RobotID=""
def main(error_in,E_Mail,Days,RobotID):
    UID0486=" "*(0-len('%d' %Days))+'%d' %Days
    UID04AD="http://116.198.207.45:8080/naoservice/naolicense/createevaluationlicense?email="+E_Mail+"&Days="+UID0486+"&RobotID="+RobotID
    if error_in[0]== False:
    	try:
    		UID049E=0
    		UID04A1="<Not A Path>"
    		UID04C2=10000
    		UID04AA=UID049E
    		if UID049E==0:
    			UID049E_ref=urllib2.urlopen(UID04AD,timeout=UID04C2/1000.0)
    			UID00D8=UID049E_ref.read()
    			UID04B0=UID049E_ref.info().dict
    		else:
    			UID049E_req=urllib2.Request(UID04AD)
    			UID049E_ref=UID049E.open(UID049E_req,timeout=UID04C2/1000.0)
    			UID00D8=UID049E_ref.read()
    			UID04B0=UID049E_ref.info().dict
    		if UID04A1=="" or UID04A1=="<Not A Path>":
    			pass
    		else:
    			UID049E_file=open(UID04A1,"wb+")
    			UID049E_file.write(UID00D8)
    			UID049E_file.close()
    		UID00B5=error_in
    	except Exception, errorMsg:
    		UID00B5=[True,1,str(errorMsg)]
    		UID04AA=0
    		UID04B0=""
    		UID00D8=""
    else:
    	UID00B5=error_in
    	UID04AA=0
    	UID04B0=""
    	UID00D8=""
    error_out=UID00B5
    body=UID00D8
    return error_out,body
if __name__ == "__main__":
    error_out,body=main(error_in,E_Mail,Days,RobotID)
