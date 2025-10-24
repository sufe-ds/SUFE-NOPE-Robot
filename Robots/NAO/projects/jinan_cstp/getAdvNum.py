# -*- coding: utf-8 -*-
RobotID=""
error_out=[False,0,""]
ErrorIn=[False,0,""]
number=0
import json
import urllib2
def main(ErrorIn,RobotID):
    UID00F9="http://116.198.207.45:8080/naoservice/advertisement/getadvnumber?robotid="+RobotID
    if ErrorIn[0]== False:
    	try:
    		UID00EA=0
    		UID00ED="<Not A Path>"
    		UID010E=10000
    		UID00F6=UID00EA
    		if UID00EA==0:
    			UID00EA_ref=urllib2.urlopen(UID00F9,timeout=UID010E/1000.0)
    			UID01C3=UID00EA_ref.read()
    			UID00FC=UID00EA_ref.info().dict
    		else:
    			UID00EA_req=urllib2.Request(UID00F9)
    			UID00EA_ref=UID00EA.open(UID00EA_req,timeout=UID010E/1000.0)
    			UID01C3=UID00EA_ref.read()
    			UID00FC=UID00EA_ref.info().dict
    		if UID00ED=="" or UID00ED=="<Not A Path>":
    			pass
    		else:
    			UID00EA_file=open(UID00ED,"wb+")
    			UID00EA_file.write(UID01C3)
    			UID00EA_file.close()
    		UID01BD=ErrorIn
    	except Exception, errorMsg:
    		UID01BD=[True,1,str(errorMsg)]
    		UID00F6=0
    		UID00FC=""
    		UID01C3=""
    else:
    	UID01BD=ErrorIn
    	UID00F6=0
    	UID00FC=""
    	UID01C3=""
    if UID01BD[0]== False:
    	try:
    		UID01ED=json.loads(UID01C3)
    		UID01AB=0
    		UID01A8=0
    		UID01E4=UID01BD
    	except Exception, errorMsg:
    		UID01E4=[True,1,str(errorMsg)]
    		UID01A8=0
    		UID01AB=0
    		UID01ED=None
    else:
    	UID01E4=UID01BD
    	UID01A8=0
    	UID01AB=0
    	UID01ED=None
    if UID01E4[0]== False:
    	try:
    		UID01E7=0.000000
    		UID01D5=UID01ED
    		try:
    			UID020A=UID01ED["number"]
    			UID01CF=False
    		except:
    			UID020A=0
    			UID01CF=True
    		
    		UID00C9=UID01E4
    	except Exception, errorMsg:
    		UID00C9=[True,1,str(errorMsg)]
    		UID01CF=False
    		UID020A=0.000000
    		UID01D5=None
    else:
    	UID00C9=UID01E4
    	UID01CF=False
    	UID020A=0.000000
    	UID01D5=None
    UID003E=int(UID020A)
    error_out=UID00C9
    number=UID003E
    return error_out,number
if __name__ == "__main__":
    error_out,number=main(ErrorIn,RobotID)
