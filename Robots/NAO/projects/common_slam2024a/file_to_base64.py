# -*- coding: utf-8 -*-
import base64
error_out=[False,0,""]
error_in=[False,0,""]
base64_output=""
FilePath="/home/nao/abc.jpg"
def main(error_in,FilePath):
    if error_in[0]== False:
    	try:
    		UID00C3=open(FilePath,"rb+")
    		UID00BA=error_in
    	except Exception, errorMsg:
    		UID00BA=[True,1,str(errorMsg)]
    		UID00C3=0
    else:
    	UID00BA=error_in
    	UID00C3=0
    if UID00BA[0]== False:
    	try:
    		UID0055=UID00C3
    		if -1==0:
    			UID0162=UID00C3.read()
    		else:
    			UID0162=UID00C3.read(-1)
    		UID004C=UID00BA
    	except Exception, errorMsg:
    		UID004C=[True,1,str(errorMsg)]
    		UID0162=""
    		UID0055=0
    else:
    	UID004C=UID00BA
    	UID0162=""
    	UID0055=0
    if UID004C[0]== False:
    	try:
    		UID0055.close()
    		UID0318=UID004C
    	except Exception, errorMsg:
    		UID0318=[True,1,str(errorMsg)]
    else:
    	UID0318=UID004C
    UID01F5=base64.b64encode(UID0162)
    base64_output=UID01F5
    error_out=UID0318
    return error_out,base64_output
if __name__ == "__main__":
    error_out,base64_output=main(error_in,FilePath)
