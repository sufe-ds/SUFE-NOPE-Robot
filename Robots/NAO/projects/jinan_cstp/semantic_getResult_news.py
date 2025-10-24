# -*- coding: utf-8 -*-
import numpy as np
Parameter=np.array([],dtype="S")
Action=np.array([],dtype="S")
error_in__no_error_=[False,0,""]
error_out=[False,0,""]
JSON_Tree=None
def main(error_in__no_error_,JSON_Tree):
    if error_in__no_error_[0]== False:
    	try:
    		UID013C=JSON_Tree
    		try:
    			UID0191=JSON_Tree["data"]
    			UID0136=False
    		except:
    			UID0191={}
    			UID0136=True
    		UID0188=error_in__no_error_
    	except Exception, errorMsg:
    		UID0188=[True,1,str(errorMsg)]
    		UID0136=False
    		UID0191=None
    		UID013C=None
    else:
    	UID0188=error_in__no_error_
    	UID0136=False
    	UID0191=None
    	UID013C=None
    if UID0188[0]== False:
    	try:
    		UID0179=UID0191
    		try:
    			JSON_Object_04AA=UID0191["result"]
    			UID0173=False
    		except:
    			JSON_Object_04AA={}
    			UID0173=True
    		error_out_0520=UID0188
    	except Exception, errorMsg:
    		error_out_0520=[True,1,str(errorMsg)]
    		UID0173=False
    		JSON_Object_04AA=None
    		UID0179=None
    else:
    	error_out_0520=UID0188
    	UID0173=False
    	JSON_Object_04AA=None
    	UID0179=None
    ForS_D1S_ADS_BBS_B7_046D=3
    UID070A=np.array([],dtype="S")
    UID0256=np.array([],dtype="S")
    i_0469=-1
    ForS_D1S_ADS_BBS_B7_0457_count=ForS_D1S_ADS_BBS_B7_046D
    for i in range(0, ForS_D1S_ADS_BBS_B7_0457_count):
    	i_0469=i_0469+1
    	if error_out_0520[0]== False:
    		try:
    			UID038E=JSON_Object_04AA
    			UID0613=JSON_Object_04AA[i_0469]
    			UID0388=False
    			UID060A=error_out_0520
    		except Exception, errorMsg:
    			UID060A=[True,1,str(errorMsg)]
    			UID0388=False
    			UID0613=None
    			UID038E=None
    	else:
    		UID060A=error_out_0520
    		UID0388=False
    		UID0613=None
    		UID038E=None
    	UID0256=np.concatenate((UID0256,["AnimatedSay"]))
    	if UID060A[0]== False:
    		try:
    			UID05E6=UID0613
    			try:
    				UID01CD=UID0613["title"]
    				UID05E0=False
    			except:
    				UID01CD={}
    				UID05E0=True
    			UID01C4=UID060A
    		except Exception, errorMsg:
    			UID01C4=[True,1,str(errorMsg)]
    			UID05E0=False
    			UID01CD=None
    			UID05E6=None
    	else:
    		UID01C4=UID060A
    		UID05E0=False
    		UID01CD=None
    		UID05E6=None
    	if UID01C4[0]== False:
    		try:
    			try:
    				UID0706=UID01CD.encode('utf-8')
    			except:
    				UID0706=UID01CD
    			error_out_0520=UID01C4
    		except Exception, errorMsg:
    			error_out_0520=[True,1,str(errorMsg)]
    			UID0706=""
    	else:
    		error_out_0520=UID01C4
    		UID0706=""
    	
    	UID070A=np.concatenate((UID070A,[UID0706]))
    error_out=error_out_0520
    Parameter=UID070A
    UID010B=np.concatenate((UID0256,["RerunVoicecloud"]))
    Action=UID010B
    return error_out,Parameter,Action
if __name__ == "__main__":
    error_out,Parameter,Action=main(error_in__no_error_,JSON_Tree)
