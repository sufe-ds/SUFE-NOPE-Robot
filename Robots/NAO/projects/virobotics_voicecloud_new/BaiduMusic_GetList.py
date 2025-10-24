# -*- coding: utf-8 -*-
songs=[]
import json
import urllib2
type=1
error_out=[False,0,""]
error_in__no_error_=[False,0,""]
offset=0
size=10
import imp
import BaiduMusic_Head
imp.reload (BaiduMusic_Head)
import Clear_Errors
imp.reload (Clear_Errors)
import copy
def main(error_in__no_error_,offset,size,type):
    UID002B=BaiduMusic_Head.main()
    UID00A5=UID002B
    UID0185=" "*(0-len('%d' %type))+'%d' %type
    UID020A=" "*(0-len('%d' %size))+'%d' %size
    UID02A7=" "*(0-len('%d' %offset))+'%d' %offset
    UID040D=UID00A5+"baidu.ting.billboard.billList&format=json&type="+UID0185+"&size="+UID020A+"&offset="+UID02A7
    if error_in__no_error_[0]== False:
    	try:
    		UID03FE=0
    		UID0401="<Not A Path>"
    		UID0422=10000
    		UID040A=UID03FE
    		if UID03FE==0:
    			UID03FE_ref=urllib2.urlopen(UID040D,timeout=UID0422/1000.0)
    			UID0530=UID03FE_ref.read()
    			UID0410=UID03FE_ref.info().dict
    		else:
    			UID03FE_req=urllib2.Request(UID040D)
    			UID03FE_ref=UID03FE.open(UID03FE_req,timeout=UID0422/1000.0)
    			UID0530=UID03FE_ref.read()
    			UID0410=UID03FE_ref.info().dict
    		if UID0401=="" or UID0401=="<Not A Path>":
    			pass
    		else:
    			UID03FE_file=open(UID0401,"wb+")
    			UID03FE_file.write(UID0530)
    			UID03FE_file.close()
    		UID052A=error_in__no_error_
    	except Exception, errorMsg:
    		UID052A=[True,1,str(errorMsg)]
    		UID040A=0
    		UID0410=""
    		UID0530=""
    else:
    	UID052A=error_in__no_error_
    	UID040A=0
    	UID0410=""
    	UID0530=""
    if UID052A[0]== False:
    	try:
    		UID051B=json.loads(UID0530)
    		UID0518=0
    		UID0515=0
    		UID017D=UID052A
    	except Exception, errorMsg:
    		UID017D=[True,1,str(errorMsg)]
    		UID0515=0
    		UID0518=0
    		UID051B=None
    else:
    	UID017D=UID052A
    	UID0515=0
    	UID0518=0
    	UID051B=None
    if UID017D[0]== False:
    	try:
    		UID016E=UID051B
    		try:
    			UID016A=UID051B["song_list"]
    			UID0163=False
    		except:
    			UID016A={}
    			UID0163=True
    		UID0219=UID017D
    	except Exception, errorMsg:
    		UID0219=[True,1,str(errorMsg)]
    		UID0163=False
    		UID016A=None
    		UID016E=None
    else:
    	UID0219=UID017D
    	UID0163=False
    	UID016A=None
    	UID016E=None
    if UID0219[0]== False:
    	try:
    		UID0207=UID016A
    		ForS_D1S_ADS_BBS_B7_0378=len(UID016A)
    		error_out_07CF=UID0219
    	except Exception, errorMsg:
    		error_out_07CF=[True,1,str(errorMsg)]
    		ForS_D1S_ADS_BBS_B7_0378=0
    		UID0207=None
    else:
    	error_out_07CF=UID0219
    	ForS_D1S_ADS_BBS_B7_0378=0
    	UID0207=None
    JSON_Tree_039C=UID051B
    JSON_Object_03D3=UID016A
    UID0B4A=[]
    i_0374=-1
    ForS_D1S_ADS_BBS_B7_035F_count=ForS_D1S_ADS_BBS_B7_0378
    for i in range(0, ForS_D1S_ADS_BBS_B7_035F_count):
    	UID0642=["","",""]
    	i_0374=i_0374+1
    	UID039B=JSON_Tree_039C
    	UID0456=JSON_Object_03D3
    	UID0453=JSON_Object_03D3[i_0374]
    	UID0450=False
    	if error_out_07CF[0]== False:
    		try:
    			UID05D2=""
    			UID05BF=UID0453
    			try:
    				UID0A16=UID0453["song_id"]
    				UID05B8=False
    			except:
    				UID0A16=""
    				UID05B8=True
    			
    			UID069D=error_out_07CF
    		except Exception, errorMsg:
    			UID069D=[True,1,str(errorMsg)]
    			UID05B8=False
    			UID0A16=""
    			UID05BF=None
    	else:
    		UID069D=error_out_07CF
    		UID05B8=False
    		UID0A16=""
    		UID05BF=None
    	if UID069D[0]== False:
    		try:
    			UID066B=UID0453
    			try:
    				UID09B4=UID0453["title"]
    				UID0665=False
    			except:
    				UID09B4={}
    				UID0665=True
    			UID099A=UID069D
    		except Exception, errorMsg:
    			UID099A=[True,1,str(errorMsg)]
    			UID0665=False
    			UID09B4=None
    			UID066B=None
    	else:
    		UID099A=UID069D
    		UID0665=False
    		UID09B4=None
    		UID066B=None
    	if UID099A[0]== False:
    		try:
    			UID0B1B=UID09B4.encode("utf-8")
    			UID0341=UID099A
    		except Exception, errorMsg:
    			UID0341=[True,1,str(errorMsg)]
    			UID0B1B=""
    	else:
    		UID0341=UID099A
    		UID0B1B=""
    	UID034A=0
    	UID032C=Clear_Errors.main(UID0341,UID034A)
    	UID050C=UID032C[0]
    	UID033E=UID032C[1]
    	if UID050C[0]== False:
    		try:
    			UID04FD=UID0453
    			try:
    				UID04DC=UID0453["author"]
    				UID04F7=False
    			except:
    				UID04DC={}
    				UID04F7=True
    			UID04D3=UID050C
    		except Exception, errorMsg:
    			UID04D3=[True,1,str(errorMsg)]
    			UID04F7=False
    			UID04DC=None
    			UID04FD=None
    	else:
    		UID04D3=UID050C
    		UID04F7=False
    		UID04DC=None
    		UID04FD=None
    	if UID04D3[0]== False:
    		try:
    			UID0BEE=UID04DC.encode("utf-8")
    			UID03C1=UID04D3
    		except Exception, errorMsg:
    			UID03C1=[True,1,str(errorMsg)]
    			UID0BEE=""
    	else:
    		UID03C1=UID04D3
    		UID0BEE=""
    	UID0B46=copy.copy(UID0642)
    	UID0B46[0]=UID0A16
    	UID0B46[1]=UID0B1B
    	UID0B46[2]=UID0BEE
    	UID03CB=0
    	UID03A8=Clear_Errors.main(UID03C1,UID03CB)
    	error_out_07CF=UID03A8[0]
    	UID03BE=UID03A8[1]
    	
    	UID0B4A.append(UID0B46)
    error_out=error_out_07CF
    songs=UID0B4A
    return error_out,songs
if __name__ == "__main__":
    error_out,songs=main(error_in__no_error_,offset,size,type)
