# -*- coding: utf-8 -*-
import numpy as np
Action=np.array([],dtype="S")
parameter=np.array([],dtype="S")
error_out=[False,0,""]
JSON_Tree=None
error_in__no_error_=[False,0,""]
def main(error_in__no_error_,JSON_Tree):
    UID0220=np.array(["RerunVoicecloud"],dtype="S")
    if error_in__no_error_[0]== False:
    	try:
    		UID0107=JSON_Tree
    		try:
    			UID015C=JSON_Tree["semantic"]
    			UID0101=False
    		except:
    			UID015C={}
    			UID0101=True
    		UID0153=error_in__no_error_
    	except Exception, errorMsg:
    		UID0153=[True,1,str(errorMsg)]
    		UID0101=False
    		UID015C=None
    		UID0107=None
    else:
    	UID0153=error_in__no_error_
    	UID0101=False
    	UID015C=None
    	UID0107=None
    if UID0153[0]== False:
    	try:
    		UID0144=UID015C
    		UID0141=UID015C[0]
    		UID013E=False
    		UID055B=UID0153
    	except Exception, errorMsg:
    		UID055B=[True,1,str(errorMsg)]
    		UID013E=False
    		UID0141=None
    		UID0144=None
    else:
    	UID055B=UID0153
    	UID013E=False
    	UID0141=None
    	UID0144=None
    if UID055B[0]== False:
    	try:
    		UID054C=UID0141
    		try:
    			UID066C=UID0141["intent"]
    			UID0546=False
    		except:
    			UID066C={}
    			UID0546=True
    		UID0663=UID055B
    	except Exception, errorMsg:
    		UID0663=[True,1,str(errorMsg)]
    		UID0546=False
    		UID066C=None
    		UID054C=None
    else:
    	UID0663=UID055B
    	UID0546=False
    	UID066C=None
    	UID054C=None
    if UID0663[0]== False:
    	try:
    		try:
    			UID02AA=UID066C.encode('utf-8')
    		except:
    			UID02AA=UID066C
    		UID018F=UID0663
    	except Exception, errorMsg:
    		UID018F=[True,1,str(errorMsg)]
    		UID02AA=""
    else:
    	UID018F=UID0663
    	UID02AA=""
    if UID018F[0]== False:
    	try:
    		UID0180=UID0141
    		try:
    			UID01D4=UID0141["slots"]
    			UID017A=False
    		except:
    			UID01D4={}
    			UID017A=True
    		UID01CB=UID018F
    	except Exception, errorMsg:
    		UID01CB=[True,1,str(errorMsg)]
    		UID017A=False
    		UID01D4=None
    		UID0180=None
    else:
    	UID01CB=UID018F
    	UID017A=False
    	UID01D4=None
    	UID0180=None
    UID02BF="robotarm_"+UID02AA
    if UID01CB[0]== False:
    	try:
    		UID01BC=UID01D4
    		UID01B9=len(UID01D4)
    		UID0527=UID01CB
    	except Exception, errorMsg:
    		UID0527=[True,1,str(errorMsg)]
    		UID01B9=0
    		UID01BC=None
    else:
    	UID0527=UID01CB
    	UID01B9=0
    	UID01BC=None
    UID00F9=np.concatenate(([UID02BF],UID0220))
    Action=UID00F9
    if UID0527[0]== False:
    	try:
    		UID0518=UID01BC
    		ForS_D1S_ADS_BBS_B7_05BF=len(UID01BC)
    		error_out_0615=UID0527
    	except Exception, errorMsg:
    		error_out_0615=[True,1,str(errorMsg)]
    		ForS_D1S_ADS_BBS_B7_05BF=0
    		UID0518=None
    else:
    	error_out_0615=UID0527
    	ForS_D1S_ADS_BBS_B7_05BF=0
    	UID0518=None
    JSON_Tree_Passthrough__JSON_Array__0600=UID01BC
    UID099E=np.array([],dtype="S")
    i_05BB=-1
    ForS_D1S_ADS_BBS_B7_0595_count=ForS_D1S_ADS_BBS_B7_05BF
    for i in range(0, ForS_D1S_ADS_BBS_B7_0595_count):
    	i_05BB=i_05BB+1
    	if error_out_0615[0]== False:
    		try:
    			UID01EE=JSON_Tree_Passthrough__JSON_Array__0600
    			UID0263=JSON_Tree_Passthrough__JSON_Array__0600[i_05BB]
    			UID01E8=False
    			UID025A=error_out_0615
    		except Exception, errorMsg:
    			UID025A=[True,1,str(errorMsg)]
    			UID01E8=False
    			UID0263=None
    			UID01EE=None
    	else:
    		UID025A=error_out_0615
    		UID01E8=False
    		UID0263=None
    		UID01EE=None
    	if UID025A[0]== False:
    		try:
    			UID024B=UID0263
    			try:
    				UID029F=UID0263["normValue"]
    				UID0245=False
    			except:
    				UID029F={}
    				UID0245=True
    			UID0296=UID025A
    		except Exception, errorMsg:
    			UID0296=[True,1,str(errorMsg)]
    			UID0245=False
    			UID029F=None
    			UID024B=None
    	else:
    		UID0296=UID025A
    		UID0245=False
    		UID029F=None
    		UID024B=None
    	if UID0296[0]== False:
    		try:
    			try:
    				UID099A=UID029F.encode('utf-8')
    			except:
    				UID099A=UID029F
    			error_out_0615=UID0296
    		except Exception, errorMsg:
    			error_out_0615=[True,1,str(errorMsg)]
    			UID099A=""
    	else:
    		error_out_0615=UID0296
    		UID099A=""
    	
    	UID099E=np.concatenate((UID099E,[UID099A]))
    error_out=error_out_0615
    parameter=UID099E
    return error_out,parameter,Action
if __name__ == "__main__":
    error_out,parameter,Action=main(error_in__no_error_,JSON_Tree)
