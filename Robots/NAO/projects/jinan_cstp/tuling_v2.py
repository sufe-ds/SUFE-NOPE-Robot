# -*- coding: utf-8 -*-
error_in=[False,0,""]
error_out=[False,0,""]
url=""
answer=""
import imp
import Clear_Errors
imp.reload (Clear_Errors)
import json
import urllib2
location='{"city": "上海","province": "上海","street": "五角场"}'
userid="marui"
key="36f566b00576f4037bfca354e1af6555"
question=""
import copy
def main(key,error_in,location,userid,question):
    UID03D8=["",""]
    UID009B='{"reqType":0,"perception": {"inputText": {"text":"'+question+'"},"selfInfo": {"location": '+location+'}},"userInfo": {"apiKey":"'+key+'","userId": "'+userid+'"}}'
    if error_in[0]== False:
    	try:
    		UID0086=0
    		UID0089="<Not A Path>"
    		UID00AA=10000
    		UID0092=UID0086
    		if UID0086==0:
    			UID0086_ref=urllib2.urlopen("http://openapi.turingapi.com/openapi/api/v2",UID009B,timeout=UID00AA/1000.0)
    			UID02A2=UID0086_ref.read()
    			UID0098=UID0086_ref.info().dict
    		else:
    			UID0086_req=urllib2.Request("http://openapi.turingapi.com/openapi/api/v2")
    			UID0086_ref=UID0086.open(UID0086_req,UID009B,timeout=UID00AA/1000.0)
    			UID02A2=UID0086_ref.read()
    			UID0098=UID0086_ref.info().dict
    		if UID0089=="" or UID0089=="<Not A Path>":
    			pass
    		else:
    			UID0086_file=open(UID0089,"wb+")
    			UID0086_file.write(UID02A2)
    			UID0086_file.close()
    		UID07E9=error_in
    	except Exception, errorMsg:
    		UID07E9=[True,1,str(errorMsg)]
    		UID0092=0
    		UID0098=""
    		UID02A2=""
    else:
    	UID07E9=error_in
    	UID0092=0
    	UID0098=""
    	UID02A2=""
    UID07F2=0
    UID07DA=Clear_Errors.main(UID07E9,UID07F2)
    UID029C=UID07DA[0]
    UID07E6=UID07DA[1]
    if UID029C[0]== False:
    	try:
    		UID07C2=json.loads(UID02A2)
    		UID0184=0
    		UID0181=0
    		UID07B9=UID029C
    	except Exception, errorMsg:
    		UID07B9=[True,1,str(errorMsg)]
    		UID0181=0
    		UID0184=0
    		UID07C2=None
    else:
    	UID07B9=UID029C
    	UID0181=0
    	UID0184=0
    	UID07C2=None
    if UID07B9[0]== False:
    	try:
    		UID07AA=UID07C2
    		try:
    			UID08A8=UID07C2["results"]
    			UID07A4=False
    		except:
    			UID08A8=[]
    			UID07A4=True
    		UID089F=UID07B9
    	except Exception, errorMsg:
    		UID089F=[True,1,str(errorMsg)]
    		UID07A4=False
    		UID08A8=None
    		UID07AA=None
    else:
    	UID089F=UID07B9
    	UID07A4=False
    	UID08A8=None
    	UID07AA=None
    if UID089F[0]== False:
    	try:
    		UID097D=UID08A8
    		UID088D=len(UID08A8)
    		UID09C8=UID089F
    	except Exception, errorMsg:
    		UID09C8=[True,1,str(errorMsg)]
    		UID088D=0
    		UID097D=None
    else:
    	UID09C8=UID089F
    	UID088D=0
    	UID097D=None
    UID08EE=UID088D>0
    UID0512=UID088D
    UID0BE5=UID03D8
    if UID08EE==True:
    	ForS_D1S_ADS_BBS_B7_0538=UID0512
    	JSON_Tree_Passthrough__JSON_Array__05B0=UID097D
    	error_out_09D9=UID09C8
    	result_093B=UID0BE5
    	i_0534=-1
    	ForS_D1S_ADS_BBS_B7_0515_count=ForS_D1S_ADS_BBS_B7_0538
    	for i in range(0, ForS_D1S_ADS_BBS_B7_0515_count):
    		i_0534=i_0534+1
    		if error_out_09D9[0]== False:
    			try:
    				UID0743=JSON_Tree_Passthrough__JSON_Array__05B0
    				UID02EF=JSON_Tree_Passthrough__JSON_Array__05B0[i_0534]
    				UID073D=False
    				UID02E6=error_out_09D9
    			except Exception, errorMsg:
    				UID02E6=[True,1,str(errorMsg)]
    				UID073D=False
    				UID02EF=None
    				UID0743=None
    		else:
    			UID02E6=error_out_09D9
    			UID073D=False
    			UID02EF=None
    			UID0743=None
    		if UID02E6[0]== False:
    			try:
    				UID02D7=UID02EF
    				try:
    					UID064C=UID02EF["values"]
    					UID02C7=False
    				except:
    					UID064C={}
    					UID02C7=True
    				UID0361=UID02E6
    			except Exception, errorMsg:
    				UID0361=[True,1,str(errorMsg)]
    				UID02C7=False
    				UID064C=None
    				UID02D7=None
    		else:
    			UID0361=UID02E6
    			UID02C7=False
    			UID064C=None
    			UID02D7=None
    		if UID0361[0]== False:
    			try:
    				UID0365=""
    				UID0B38=UID064C
    				try:
    					UID01CD=UID064C["text"]
    					UID01C9=False
    				except:
    					UID01CD=""
    					UID01C9=True
    				
    				UID08B8=UID0361
    			except Exception, errorMsg:
    				UID08B8=[True,1,str(errorMsg)]
    				UID01C9=False
    				UID01CD=""
    				UID0B38=None
    		else:
    			UID08B8=UID0361
    			UID01C9=False
    			UID01CD=""
    			UID0B38=None
    		UID031B=""!=UID01CD
    		UID0AAF=result_093B
    		UID0689=UID01CD
    		if UID031B==True:
    			UID0195=copy.copy(UID0AAF)
    			UID0195[0]=UID0689
    			UID08C3=UID08B8
    			UID06BA=UID0195
    		else: 
    			UID0C33=0
    			UID05CE=Clear_Errors.main(UID08B8,UID0C33)
    			UID0630=UID05CE[0]
    			UID092D=UID05CE[1]
    			if UID0630[0]== False:
    				try:
    					UID063B=""
    					UID05C8=UID0B38
    					try:
    						UID0BCB=UID0B38["url"]
    						UID033C=False
    					except:
    						UID0BCB=""
    						UID033C=True
    					
    					UID0970=UID0630
    				except Exception, errorMsg:
    					UID0970=[True,1,str(errorMsg)]
    					UID033C=False
    					UID0BCB=""
    					UID05C8=None
    			else:
    				UID0970=UID0630
    				UID033C=False
    				UID0BCB=""
    				UID05C8=None
    			UID0191=copy.copy(UID0AAF)
    			UID0191[1]=UID0BCB
    			UID0C43=0
    			UID002C=Clear_Errors.main(UID0970,UID0C43)
    			UID044C=UID002C[0]
    			UID0969=UID002C[1]
    			UID08C3=UID044C
    			UID06BA=UID0191
    		result_093B=UID06BA
    		
    		error_out_08E0=UID08C3
    	UID098E=error_out_08E0
    	UID0A27=result_093B
    else: 
    	UID098E=UID09C8
    	UID0A27=UID0BE5
    UID03C1=UID0A27[0]
    UID05AC=UID0A27[1]
    error_out=UID098E
    url=UID05AC
    try:
    	UID0142=UID03C1.encode('utf-8')
    except:
    	UID0142=UID03C1
    answer=UID0142
    return error_out,answer,url
if __name__ == "__main__":
    error_out,answer,url=main(key,error_in,location,userid,question)
