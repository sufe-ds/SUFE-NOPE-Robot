# -*- coding: utf-8 -*-
ms=0
error_out=[False,0,""]
error_in=[False,0,""]
IP="127.0.0.1"
from naoqi import ALProxy
def main(error_in,IP):
    if error_in[0]== False:
    	try:
    		
    		TabletService1 = ALProxy("ALTabletService",IP,9559)
    		
    		milliseconds = TabletService1.getVideoLength()
    		UID00BC=milliseconds
    		UID02E1=error_in
    	except Exception, errorMsg:
    		UID02E1=[True,1,str(errorMsg)]
    		UID00BC=0
    else:
    	UID02E1=error_in
    	UID00BC=0
    error_out=UID02E1
    ms=int(UID00BC)
    return error_out,ms
if __name__ == "__main__":
    error_out,ms=main(error_in,IP)
