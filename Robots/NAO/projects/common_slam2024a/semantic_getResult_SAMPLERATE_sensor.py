# -*- coding: utf-8 -*-
import numpy as np
Action=np.array([],dtype="S")
parameter=np.array([],dtype="S")
error_out=[False,0,""]
JSON_Tree=None
error_in__no_error_=[False,0,""]
def main(error_in__no_error_,JSON_Tree):
    Constant_UID0BCF=""
    UID0DB5=np.array(["RerunVoicecloud"],dtype="S")
    UID018D=np.array([],dtype="S")
    if error_in__no_error_[0]== False:
    	try:
    		UID022C=JSON_Tree
    		try:
    			UID039E=JSON_Tree["semantic"]
    			UID0226=False
    		except:
    			UID039E={}
    			UID0226=True
    		UID0395=error_in__no_error_
    	except Exception, errorMsg:
    		UID0395=[True,1,str(errorMsg)]
    		UID0226=False
    		UID039E=None
    		UID022C=None
    else:
    	UID0395=error_in__no_error_
    	UID0226=False
    	UID039E=None
    	UID022C=None
    parameter=UID018D
    if UID0395[0]== False:
    	try:
    		UID0386=UID039E
    		UID04A0=UID039E[0]
    		UID0380=False
    		UID0495=UID0395
    	except Exception, errorMsg:
    		UID0495=[True,1,str(errorMsg)]
    		UID0380=False
    		UID04A0=None
    		UID0386=None
    else:
    	UID0495=UID0395
    	UID0380=False
    	UID04A0=None
    	UID0386=None
    if UID0495[0]== False:
    	try:
    		UID0486=UID04A0
    		try:
    			UID0530=UID04A0["slots"]
    			UID0480=False
    		except:
    			UID0530={}
    			UID0480=True
    		UID0527=UID0495
    	except Exception, errorMsg:
    		UID0527=[True,1,str(errorMsg)]
    		UID0480=False
    		UID0530=None
    		UID0486=None
    else:
    	UID0527=UID0495
    	UID0480=False
    	UID0530=None
    	UID0486=None
    if UID0527[0]== False:
    	try:
    		UID1107=UID0530
    		UID0515=len(UID0530)
    		UID10FE=UID0527
    	except Exception, errorMsg:
    		UID10FE=[True,1,str(errorMsg)]
    		UID0515=0
    		UID1107=None
    else:
    	UID10FE=UID0527
    	UID0515=0
    	UID1107=None
    if UID10FE[0]== False:
    	try:
    		UID10EF=UID1107
    		UID0D63=UID1107[0]
    		UID10E9=False
    		UID0D59=UID10FE
    	except Exception, errorMsg:
    		UID0D59=[True,1,str(errorMsg)]
    		UID10E9=False
    		UID0D63=None
    		UID10EF=None
    else:
    	UID0D59=UID10FE
    	UID10E9=False
    	UID0D63=None
    	UID10EF=None
    if UID0D59[0]== False:
    	try:
    		UID0D43=UID0D63
    		try:
    			UID0ED7=UID0D63["normValue"]
    			UID0D3D=False
    		except:
    			UID0ED7={}
    			UID0D3D=True
    		UID0ECC=UID0D59
    	except Exception, errorMsg:
    		UID0ECC=[True,1,str(errorMsg)]
    		UID0D3D=False
    		UID0ED7=None
    		UID0D43=None
    else:
    	UID0ECC=UID0D59
    	UID0D3D=False
    	UID0ED7=None
    	UID0D43=None
    if UID0ECC[0]== False:
    	try:
    		try:
    			UID1472=UID0ED7.encode('utf-8')
    		except:
    			UID1472=UID0ED7
    		UID1014=UID0ECC
    	except Exception, errorMsg:
    		UID1014=[True,1,str(errorMsg)]
    		UID1472=""
    else:
    	UID1014=UID0ECC
    	UID1472=""
    error_out=UID1014
    UID14F3="sensor_"+UID1472
    UID0D1A=np.concatenate(([UID14F3],UID0DB5))
    Action=UID0D1A
    return error_out,Action,parameter
if __name__ == "__main__":
    error_out,Action,parameter=main(error_in__no_error_,JSON_Tree)
