# -*- coding: utf-8 -*-
concatenated_string=""
error_out=[False,0,""]
import urllib
import json
import urllib2
AllSong=[]
error_in__no_error_=[False,0,""]
Keyword="刘德华"
import imp
import BaiduMusic_Head
imp.reload (BaiduMusic_Head)
import numpy as np
import copy
def main(error_in__no_error_,Keyword):
    UID0049=BaiduMusic_Head.main()
    UID007C=UID0049
    if error_in__no_error_[0]== False:
    	try:
    		UID0082=urllib.quote(Keyword)
    		UID06D0=error_in__no_error_
    	except Exception, errorMsg:
    		UID06D0=[True,1,str(errorMsg)]
    		UID0082=""
    else:
    	UID06D0=error_in__no_error_
    	UID0082=""
    UID0079=UID007C+"baidu.ting.search.catalogSug&format=json&query="+UID0082
    if UID06D0[0]== False:
    	try:
    		UID0685=0
    		UID0688="<Not A Path>"
    		UID06D8=10000
    		UID0694=UID0685
    		if UID0685==0:
    			UID0685_ref=urllib2.urlopen(UID0079,timeout=UID06D8/1000.0)
    			UID09DE=UID0685_ref.read()
    			UID069C=UID0685_ref.info().dict
    		else:
    			UID0685_req=urllib2.Request(UID0079)
    			UID0685_ref=UID0685.open(UID0685_req,timeout=UID06D8/1000.0)
    			UID09DE=UID0685_ref.read()
    			UID069C=UID0685_ref.info().dict
    		if UID0688=="" or UID0688=="<Not A Path>":
    			pass
    		else:
    			UID0685_file=open(UID0688,"wb+")
    			UID0685_file.write(UID09DE)
    			UID0685_file.close()
    		UID09D8=UID06D0
    	except Exception, errorMsg:
    		UID09D8=[True,1,str(errorMsg)]
    		UID0694=0
    		UID069C=""
    		UID09DE=""
    else:
    	UID09D8=UID06D0
    	UID0694=0
    	UID069C=""
    	UID09DE=""
    concatenated_string=UID0079
    if UID09D8[0]== False:
    	try:
    		UID0A39=json.loads(UID09DE)
    		UID09AF=0
    		UID09AA=0
    		UID0A26=UID09D8
    	except Exception, errorMsg:
    		UID0A26=[True,1,str(errorMsg)]
    		UID09AA=0
    		UID09AF=0
    		UID0A39=None
    else:
    	UID0A26=UID09D8
    	UID09AA=0
    	UID09AF=0
    	UID0A39=None
    if UID0A26[0]== False:
    	try:
    		UID0A0B=UID0A39
    		try:
    			UID054B=UID0A39["song"]
    			UID09F7=False
    		except:
    			UID054B={}
    			UID09F7=True
    		UID0536=UID0A26
    	except Exception, errorMsg:
    		UID0536=[True,1,str(errorMsg)]
    		UID09F7=False
    		UID054B=None
    		UID0A0B=None
    else:
    	UID0536=UID0A26
    	UID09F7=False
    	UID054B=None
    	UID0A0B=None
    if UID0536[0]==True:
    	UID0559=[]
    	UID0565=UID0536
    else: 
    	if UID0536[0]== False:
    		try:
    			UID0A6E=UID054B
    			ForS_D1S_ADS_BBS_B7_0B92=len(UID054B)
    			error_out_0410=UID0536
    		except Exception, errorMsg:
    			error_out_0410=[True,1,str(errorMsg)]
    			ForS_D1S_ADS_BBS_B7_0B92=0
    			UID0A6E=None
    	else:
    		error_out_0410=UID0536
    		ForS_D1S_ADS_BBS_B7_0B92=0
    		UID0A6E=None
    	JSON_Object_0BC8=UID054B
    	UID12AB=[]
    	i_0B8E=-1
    	ForS_D1S_ADS_BBS_B7_0B74_count=ForS_D1S_ADS_BBS_B7_0B92
    	for i in range(0, ForS_D1S_ADS_BBS_B7_0B74_count):
    		UID01BC=np.array(["songid","songname","artistname"],dtype="S")
    		UID0498=["","",""]
    		i_0B8E=i_0B8E+1
    		if error_out_0410[0]== False:
    			try:
    				UID1458=JSON_Object_0BC8
    				JSON_Object_02D7=JSON_Object_0BC8[i_0B8E]
    				UID1452=False
    				error_out_0504=error_out_0410
    			except Exception, errorMsg:
    				error_out_0504=[True,1,str(errorMsg)]
    				UID1452=False
    				JSON_Object_02D7=None
    				UID1458=None
    		else:
    			error_out_0504=error_out_0410
    			UID1452=False
    			JSON_Object_02D7=None
    			UID1458=None
    		UID02F6=UID01BC
    		UID03F3=np.array([],dtype="S")
    		i_02A6=-1
    		ForS_D1S_ADS_BBS_B7_0294_IndexsIn=[]
    		ForS_D1S_ADS_BBS_B7_0294_IndexsIn.append(len(UID02F6))
    		ForS_D1S_ADS_BBS_B7_0294_Indexmin=min(ForS_D1S_ADS_BBS_B7_0294_IndexsIn)
    		ForS_D1S_ADS_BBS_B7_0294_count=ForS_D1S_ADS_BBS_B7_0294_Indexmin
    		for i in range(0, ForS_D1S_ADS_BBS_B7_0294_count):
    			i_02A6=i_02A6+1
    			if error_out_0504[0]== False:
    				try:
    					UID0C8B=JSON_Object_02D7
    					try:
    						UID0378=JSON_Object_02D7[UID02F6[i_02A6]]
    						UID0C84=False
    					except:
    						UID0378={}
    						UID0C84=True
    					UID036F=error_out_0504
    				except Exception, errorMsg:
    					UID036F=[True,1,str(errorMsg)]
    					UID0C84=False
    					UID0378=None
    					UID0C8B=None
    			else:
    				UID036F=error_out_0504
    				UID0C84=False
    				UID0378=None
    				UID0C8B=None
    			if UID036F[0]== False:
    				try:
    					try:
    						UID03EF=UID0378.encode('utf-8')
    					except:
    						UID03EF=UID0378
    					error_out_0504=UID036F
    				except Exception, errorMsg:
    					error_out_0504=[True,1,str(errorMsg)]
    					UID03EF=""
    			else:
    				error_out_0504=UID036F
    				UID03EF=""
    			
    			UID03F3=np.concatenate((UID03F3,[UID03EF]))
    		try:
    			UID1247=UID03F3[0]
    		except:
    			UID1247=""
    		try:
    			UID127B=UID03F3[1]
    		except:
    			UID127B=""
    		try:
    			UID00D9=UID03F3[2]
    		except:
    			UID00D9=""
    		error_out_0410=error_out_0504
    		
    		UID12A4=copy.copy(UID0498)
    		UID12A4[0]=UID1247
    		UID12A4[1]=UID127B
    		UID12A4[2]=UID00D9
    		UID12AB.append(UID12A4)
    	UID0565=error_out_0410
    	UID0559=UID12AB
    AllSong=UID0559
    error_out=UID0565
    return error_out,AllSong
if __name__ == "__main__":
    error_out,AllSong=main(error_in__no_error_,Keyword)
