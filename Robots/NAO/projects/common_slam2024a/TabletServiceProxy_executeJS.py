# -*- coding: utf-8 -*-
error_out=[False,0,""]
error_in=[False,0,""]
IP="127.0.0.1"
from naoqi import ALProxy
script=""
def main(error_in,script,IP):
    if error_in[0]== False:
    	try:
    		
    		TabletService1 = ALProxy("ALTabletService",IP,9559)
    		
    		TabletService1.executeJS(script)
    		UID02E1=error_in
    	except Exception, errorMsg:
    		UID02E1=[True,1,str(errorMsg)]
    else:
    	UID02E1=error_in
    error_out=UID02E1
    return error_out
if __name__ == "__main__":
    error_out=main(error_in,script,IP)
