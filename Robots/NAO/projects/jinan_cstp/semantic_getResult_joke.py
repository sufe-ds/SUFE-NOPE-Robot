# -*- coding: utf-8 -*-
import numpy as np
gbkstring=""
Parameter=np.array([],dtype="S")
Action=np.array([],dtype="S")
error_in__no_error_=[False,0,""]
error_out=[False,0,""]
JSON_Tree=None
def main(error_in__no_error_,JSON_Tree):
    if error_in__no_error_[0]== False:
    	try:
    		UID0115=JSON_Tree
    		try:
    			UID08C5=JSON_Tree["data"]
    			UID010F=False
    		except:
    			UID08C5={}
    			UID010F=True
    		UID01EA=error_in__no_error_
    	except Exception, errorMsg:
    		UID01EA=[True,1,str(errorMsg)]
    		UID010F=False
    		UID08C5=None
    		UID0115=None
    else:
    	UID01EA=error_in__no_error_
    	UID010F=False
    	UID08C5=None
    	UID0115=None
    UID00D6=np.concatenate((["AnimatedSay"],["RerunVoicecloud"]))
    Action=UID00D6
    UID08AD=UID08C5
    try:
    	UID01F3=UID08C5["result"]
    	UID08A7=False
    except:
    	UID01F3={}
    	UID08A7=True
    if UID01EA[0]== False:
    	try:
    		UID01DB=UID01F3
    		UID016A=UID01F3[0]
    		UID01D5=False
    		UID0161=UID01EA
    	except Exception, errorMsg:
    		UID0161=[True,1,str(errorMsg)]
    		UID01D5=False
    		UID016A=None
    		UID01DB=None
    else:
    	UID0161=UID01EA
    	UID01D5=False
    	UID016A=None
    	UID01DB=None
    if UID0161[0]== False:
    	try:
    		UID0152=UID016A
    		try:
    			UID01C0=UID016A["content"]
    			UID014C=False
    		except:
    			UID01C0={}
    			UID014C=True
    		UID01B7=UID0161
    	except Exception, errorMsg:
    		UID01B7=[True,1,str(errorMsg)]
    		UID014C=False
    		UID01C0=None
    		UID0152=None
    else:
    	UID01B7=UID0161
    	UID014C=False
    	UID01C0=None
    	UID0152=None
    if UID01B7[0]== False:
    	try:
    		try:
    			UID01A8=UID01C0.encode('utf-8')
    		except:
    			UID01A8=UID01C0
    		UID007B=UID01B7
    	except Exception, errorMsg:
    		UID007B=[True,1,str(errorMsg)]
    		UID01A8=""
    else:
    	UID007B=UID01B7
    	UID01A8=""
    error_out=UID007B
    gbkstring=UID01A8
    UID00F9=np.array([UID01A8])
    Parameter=UID00F9
    return error_out,Parameter,Action
if __name__ == "__main__":
    error_out,Parameter,Action=main(error_in__no_error_,JSON_Tree)
