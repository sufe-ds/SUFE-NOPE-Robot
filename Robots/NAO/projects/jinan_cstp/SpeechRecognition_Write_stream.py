# -*- coding: utf-8 -*-
SessionID=""
SessionIDOut=""
stream_in=""
stringout=""
error_out=[False,0,""]
error_in__no_error_=[False,0,""]
import os
from ctypes import *
import platform
if platform.system()=="Linux":
 libfolder=os.path.split(os.path.realpath(__file__))[0]
 libpath=os.path.join(libfolder,"xunfei.so")
 xfdll=cdll.LoadLibrary(libpath)
else:
 xfdll=windll.LoadLibrary("msc.dll")
recStatus=0
return_type=0
import imp
import no_Error_1097
imp.reload (no_Error_1097)
epStatus=0
audstat=0
def main(error_in__no_error_,audstat,stream_in,SessionID):
    UID017C=len(stream_in)
    SessionIDOut=SessionID
    if error_in__no_error_[0]== False:
    	try:
    		UID0167=c_int(0)
    		UID00B4=c_int(0)
    		UID014D=xfdll.QISRAudioWrite(SessionID,stream_in,UID017C,audstat,byref(UID00B4),byref(UID0167))
    		UID0167=UID0167.value
    		UID00B4=UID00B4.value
    		UID00DA=error_in__no_error_
    	except Exception, errorMsg:
    		UID00DA=[True,1,str(errorMsg)]
    		UID00B4=0
    		UID0167=0
    		UID014D=0
    else:
    	UID00DA=error_in__no_error_
    	UID00B4=0
    	UID0167=0
    	UID014D=0
    epStatus=UID00B4
    UID00D4=1097
    UID00BF=no_Error_1097.main(UID00D4,UID00DA)
    UID0101=UID00BF
    return_type=UID014D
    recStatus=UID0167
    UID00E6=no_Error_1097.main(1517,UID0101)
    UID0134=UID00E6
    UID012E=1097
    UID0119=no_Error_1097.main(UID012E,UID0134)
    UID004E=UID0119
    UID0044=UID0167
    UID0049=SessionID
    if UID0044==0:
    	if UID004E[0]== False:
    		try:
    			UID0088=0
    			xfdll.QISRGetResult.restype = c_char_p
    			CID00=c_int(0)
    			UID0073=c_int(0)
    			UID0056=xfdll.QISRGetResult(UID0049, byref(UID0073), UID0088, byref(CID00))
    			CID00=CID00.value
    			UID0073=UID0073.value
    			if UID0056==None:
    					UID0056=""
    			UID005B=UID004E
    		except Exception, errorMsg:
    			UID005B=[True,1,str(errorMsg)]
    			UID0073=0
    			UID0056=""
    			UID007C=0
    	else:
    		UID005B=UID004E
    		UID0073=0
    		UID0056=""
    		UID007C=0
    	UID0058=UID005B
    	UID0053=UID0056
    else: 
    	UID0053=""
    	UID0058=UID004E
    error_out=UID0058
    stringout=UID0053
    return error_out,stringout,return_type,SessionIDOut,recStatus,epStatus
if __name__ == "__main__":
    error_out,stringout,return_type,SessionIDOut,recStatus,epStatus=main(error_in__no_error_,audstat,stream_in,SessionID)
