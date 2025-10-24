# -*- coding: utf-8 -*-
answer=""
error_out=[False,0,""]
error_in=[False,0,""]
key="36f566b00576f4037bfca354e1af6555"
import urllib
question=""
import urllib2
import json
data=""
def main(error_in,question,key):
    UID0134=urllib.quote(question)
    UID014B="http://www.tuling123.com/openapi/api?key="+key+"&info="+UID0134+"&userid=11"
    if error_in[0]== False:
    	try:
    		UID013C=0
    		UID013F="<Not A Path>"
    		UID0148=UID013C
    		if UID013C==0:
    			UID013C_ref=urllib2.urlopen(UID014B,timeout=3000/1000.0)
    			UID01B2=UID013C_ref.read()
    			UID014E=UID013C_ref.info().dict
    		else:
    			UID013C_req=urllib2.Request(UID014B)
    			UID013C_ref=UID013C.open(UID013C_req,timeout=3000/1000.0)
    			UID01B2=UID013C_ref.read()
    			UID014E=UID013C_ref.info().dict
    		if UID013F=="" or UID013F=="<Not A Path>":
    			pass
    		else:
    			UID013C_file=open(UID013F,"wb+")
    			UID013C_file.write(UID01B2)
    			UID013C_file.close()
    		UID01AD=error_in
    	except Exception, errorMsg:
    		UID01AD=[True,1,str(errorMsg)]
    		UID0148=0
    		UID014E=""
    		UID01B2=""
    else:
    	UID01AD=error_in
    	UID0148=0
    	UID014E=""
    	UID01B2=""
    if UID01AD[0]==True:
    	UID029A=[False,0,""]
    	UID01BC=""
    	UID01B7=UID029A
    else: 
    	global data
    	data=UID01B2
    	if UID01AD[0]== False:
    		try:
    			UID022C=json.loads(UID01B2)
    			UID01EA=0
    			UID01E7=0
    			UID0223=UID01AD
    		except Exception, errorMsg:
    			UID0223=[True,1,str(errorMsg)]
    			UID01E7=0
    			UID01EA=0
    			UID022C=None
    	else:
    		UID0223=UID01AD
    		UID01E7=0
    		UID01EA=0
    		UID022C=None
    	if UID0223[0]== False:
    		try:
    			UID0214=UID022C
    			try:
    				UID026D=UID022C["text"]
    				UID020E=False
    			except:
    				UID026D={}
    				UID020E=True
    			UID0264=UID0223
    		except Exception, errorMsg:
    			UID0264=[True,1,str(errorMsg)]
    			UID020E=False
    			UID026D=None
    			UID0214=None
    	else:
    		UID0264=UID0223
    		UID020E=False
    		UID026D=None
    		UID0214=None
    	if UID0264[0]== False:
    		try:
    			try:
    				UID01BF=UID026D.encode('utf-8')
    			except:
    				UID01BF=UID026D
    			UID01BA=UID0264
    		except Exception, errorMsg:
    			UID01BA=[True,1,str(errorMsg)]
    			UID01BF=""
    	else:
    		UID01BA=UID0264
    		UID01BF=""
    	UID01BC=UID01BF
    	UID01B7=UID01BA
    error_out=UID01B7
    answer=UID01BC
    return error_out,answer,data
if __name__ == "__main__":
    error_out,answer,data=main(error_in,question,key)
