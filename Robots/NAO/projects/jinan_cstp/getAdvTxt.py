# -*- coding: utf-8 -*-
index=""
txt=""
RobotID=""
error_out=[False,0,""]
ErrorIn=[False,0,""]
import json
import urllib2
def main(ErrorIn,index,RobotID):
    UID00F9="http://116.198.207.45:8080/naoservice/advertisement/getadvtext?robotid="+RobotID+"&advindex="+index
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
    		UID01E7=""
    		UID01D5=UID01ED
    		try:
    			UID0168=UID01ED["text"]
    			UID01CF=False
    		except:
    			UID0168=""
    			UID01CF=True
    		
    		UID015F=UID01E4
    	except Exception, errorMsg:
    		UID015F=[True,1,str(errorMsg)]
    		UID01CF=False
    		UID0168=""
    		UID01D5=None
    else:
    	UID015F=UID01E4
    	UID01CF=False
    	UID0168=""
    	UID01D5=None
    if UID015F[0]== False:
    	try:
    		try:
    			UID0180=UID0168.encode('utf-8')
    		except:
    			UID0180=UID0168
    		UID00C9=UID015F
    	except Exception, errorMsg:
    		UID00C9=[True,1,str(errorMsg)]
    		UID0180=""
    else:
    	UID00C9=UID015F
    	UID0180=""
    error_out=UID00C9
    txt=UID0180
    return error_out,txt
if __name__ == "__main__":
    error_out,txt=main(ErrorIn,index,RobotID)
