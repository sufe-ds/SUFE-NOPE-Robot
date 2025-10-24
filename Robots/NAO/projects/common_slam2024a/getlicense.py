# -*- coding: utf-8 -*-
product=""
RobotID=""
error_out=[False,0,""]
ErrorIn=[False,0,""]
pIP="127.0.0.1"
state=0
import json
# -*- coding:utf-8 -*-
from naoqi import ALProxy
import urllib2
def main(ErrorIn,product,pIP):
    if ErrorIn[0]== False:
    	try:
    		UID00E8=ALProxy("ALMemory",pIP,9559)
    		UID00DF=ErrorIn
    	except Exception, errorMsg:
    		UID00DF=[True,1,str(errorMsg)]
    		UID00E8=0
    else:
    	UID00DF=ErrorIn
    	UID00E8=0
    if UID00DF[0]== False:
    	try:
    		UID00D0=UID00E8
    		UID01CC=UID00E8.getData("RobotConfig/Head/FullHeadId")
    		UID0055=UID00DF
    	except Exception, errorMsg:
    		UID0055=[True,1,str(errorMsg)]
    		UID01CC=""
    		UID00D0=0
    else:
    	UID0055=UID00DF
    	UID01CC=""
    	UID00D0=0
    UID01C5=UID01CC+"_"+product
    UID0043="http://116.198.207.45:8080/naoservice/naolicense/getLicenseState?RobotID="+UID01C5
    RobotID=UID01C5
    if UID0055[0]== False:
    	try:
    		UID0034=0
    		UID0037="<Not A Path>"
    		UID0058=10000
    		UID0040=UID0034
    		if UID0034==0:
    			UID0034_ref=urllib2.urlopen(UID0043,timeout=UID0058/1000.0)
    			UID01C6=UID0034_ref.read()
    			UID0046=UID0034_ref.info().dict
    		else:
    			UID0034_req=urllib2.Request(UID0043)
    			UID0034_ref=UID0034.open(UID0034_req,timeout=UID0058/1000.0)
    			UID01C6=UID0034_ref.read()
    			UID0046=UID0034_ref.info().dict
    		if UID0037=="" or UID0037=="<Not A Path>":
    			pass
    		else:
    			UID0034_file=open(UID0037,"wb+")
    			UID0034_file.write(UID01C6)
    			UID0034_file.close()
    		UID01C0=UID0055
    	except Exception, errorMsg:
    		UID01C0=[True,1,str(errorMsg)]
    		UID0040=0
    		UID0046=""
    		UID01C6=""
    else:
    	UID01C0=UID0055
    	UID0040=0
    	UID0046=""
    	UID01C6=""
    if UID01C0[0]== False:
    	try:
    		UID0219=json.loads(UID01C6)
    		UID01AE=0
    		UID01AB=0
    		UID0210=UID01C0
    	except Exception, errorMsg:
    		UID0210=[True,1,str(errorMsg)]
    		UID01AB=0
    		UID01AE=0
    		UID0219=None
    else:
    	UID0210=UID01C0
    	UID01AB=0
    	UID01AE=0
    	UID0219=None
    if UID0210[0]== False:
    	try:
    		UID0213=0.000000
    		UID0201=UID0219
    		try:
    			UID02DB=UID0219["LicenseState"]
    			UID01FB=False
    		except:
    			UID02DB=0
    			UID01FB=True
    		
    		UID0273=UID0210
    	except Exception, errorMsg:
    		UID0273=[True,1,str(errorMsg)]
    		UID01FB=False
    		UID02DB=0.000000
    		UID0201=None
    else:
    	UID0273=UID0210
    	UID01FB=False
    	UID02DB=0.000000
    	UID0201=None
    UID02FD=int(UID02DB)
    error_out=UID0273
    state=UID02FD
    return error_out,state,RobotID
if __name__ == "__main__":
    error_out,state,RobotID=main(ErrorIn,product,pIP)
