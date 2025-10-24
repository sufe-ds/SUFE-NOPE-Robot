# -*- coding: utf-8 -*-
import thread
import Queue
import numpy as np
Parameter=np.array([],dtype="S")
Action=np.array([],dtype="S")
JSON_Tree=None
error_in__no_error_=[False,0,""]
error_out=[False,0,""]
import re
def UID0286(queue_UID04E8,queue_gbkstring_0595,gbkstring_02EC,UID034C,queue_UID034C,error_in__no_error_,JSON_Tree,):
	i_0298=-1
	WhileS_D1S_ADS_BBS_B7_029B_Stop=True
	while WhileS_D1S_ADS_BBS_B7_029B_Stop==True:
		Constant_UID02ED="_"
		i_0298=i_0298+1
		UID02B7_result=re.split(Constant_UID02ED,gbkstring_02EC[0:],1)
		UID068C=gbkstring_02EC[:0]+UID02B7_result[0]
		if len(UID02B7_result)==2:
			UID0304=Constant_UID02ED
			gbkstring_02EC=UID02B7_result[1]
			UID02CF=len(UID068C)+len(Constant_UID02ED)
		else:
			UID0304=""
			gbkstring_02EC=""
			UID02CF=-1
		UID070D=i_0298<=1
		UID04E8=i_0298
		UID0300=Constant_UID02ED==UID0304
		
		WhileS_D1S_ADS_BBS_B7_029B_Stop=UID0300
		UID0675=UID070D|UID0300
		UID0680=UID034C
		UID0698=Constant_UID02ED
		UID09B1=gbkstring_02EC
		if UID0675==True:
			UID09CE=""
			UID06A3=UID0680+UID068C+UID0698
			UID06A4=UID06A3
		else: 
			UID09CE=UID09B1
			UID06A4=UID0680
		UID034C=UID06A4
		
		gbkstring_0595=UID09CE
	queue_UID04E8.put(UID04E8)
	queue_gbkstring_0595.put(gbkstring_0595)
	UID034C=UID034C
	queue_UID034C.put(UID034C)
def main(error_in__no_error_,JSON_Tree):
    if error_in__no_error_[0]== False:
    	try:
    		UID0037=JSON_Tree
    		try:
    			UID008B=JSON_Tree["answer"]
    			UID0031=False
    		except:
    			UID008B={}
    			UID0031=True
    		UID0082=error_in__no_error_
    	except Exception, errorMsg:
    		UID0082=[True,1,str(errorMsg)]
    		UID0031=False
    		UID008B=None
    		UID0037=None
    else:
    	UID0082=error_in__no_error_
    	UID0031=False
    	UID008B=None
    	UID0037=None
    if UID0082[0]== False:
    	try:
    		UID0085=""
    		UID0073=UID008B
    		try:
    			UID00D3=UID008B["text"]
    			UID006D=False
    		except:
    			UID00D3=""
    			UID006D=True
    		
    		UID012E=UID0082
    	except Exception, errorMsg:
    		UID012E=[True,1,str(errorMsg)]
    		UID006D=False
    		UID00D3=""
    		UID0073=None
    else:
    	UID012E=UID0082
    	UID006D=False
    	UID00D3=""
    	UID0073=None
    try:
    	UID00BB=UID00D3.encode('utf-8')
    except:
    	UID00BB=UID00D3
    error_out=UID012E
    UID034C=""
    gbkstring_02EC=UID00BB
    queue_UID04E8=Queue.Queue()
    queue_gbkstring_0595=Queue.Queue()
    queue_UID034C=Queue.Queue()
    thread.start_new_thread(UID0286,(queue_UID04E8,queue_gbkstring_0595,gbkstring_02EC,UID034C,queue_UID034C,error_in__no_error_,JSON_Tree,))
    UID034C=queue_UID034C.get()
    queue_UID034C.put(UID034C)
    UID046E=len(UID034C)
    UID04E8=queue_UID04E8.get()
    queue_UID04E8.put(UID04E8)
    UID03CB=UID04E8>0
    UID0482=UID046E-1
    UID034C=queue_UID034C.get()
    queue_UID034C.put(UID034C)
    UID0455=UID034C[0:0+UID0482]
    gbkstring_0595=queue_gbkstring_0595.get()
    queue_gbkstring_0595.put(gbkstring_0595)
    UID04C2=gbkstring_0595
    UID026D=UID00BB
    if UID03CB==True:
    	UID03DC=np.concatenate(([UID0455],["RerunVoicecloud"]))
    	UID0542=UID04C2
    	UID03DE=UID03DC
    else: 
    	UID03DD=np.concatenate((["AnimatedSay"],["RerunVoicecloud"]))
    	UID0542=UID026D
    	UID03DE=UID03DD
    UID01BC=np.array([UID0542])
    Action=UID03DE
    Parameter=UID01BC
    return error_out,Parameter,Action
if __name__ == "__main__":
    error_out,Parameter,Action=main(error_in__no_error_,JSON_Tree)
