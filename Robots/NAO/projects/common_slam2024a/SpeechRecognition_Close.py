# -*- coding: utf-8 -*-
SessionID=""
function_return=0
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
def main(error_in__no_error_,SessionID):
    if error_in__no_error_[0]== False:
    	try:
    		UID007C=""
    		UID00B8=xfdll.QISRSessionEnd(SessionID,UID007C)
    		UID014F=error_in__no_error_
    	except Exception, errorMsg:
    		UID014F=[True,1,str(errorMsg)]
    		UID00B8=0
    else:
    	UID014F=error_in__no_error_
    	UID00B8=0
    error_out=UID014F
    function_return=UID00B8
    return error_out,function_return
if __name__ == "__main__":
    error_out,function_return=main(error_in__no_error_,SessionID)
