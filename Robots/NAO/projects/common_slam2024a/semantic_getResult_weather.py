# -*- coding: utf-8 -*-
import re
errorIn=[False,0,""]
import numpy as np
parameter=np.array([],dtype="S")
error_IO=[False,0,""]
JSON_Tree=None
def main(errorIn,JSON_Tree):
    UID095E=np.array(["answer","text"],dtype="S")
    UID08BC=np.array([0,0],dtype="uint16")
    if errorIn[0]== False:
    	try:
    		UID0F5D=JSON_Tree
    		UID08BC_number=0
    		for i in UID095E:
    			if UID08BC[UID08BC_number]==0:
    				UID0F5D=UID0F5D[i]
    			else:
    				UID0F5D=UID0F5D[int(i)]
    			UID08BC_number=UID08BC_number+1
    		UID0F42=errorIn
    	except Exception, errorMsg:
    		UID0F42=[True,1,str(errorMsg)]
    		UID0F5D=None
    else:
    	UID0F42=errorIn
    	UID0F5D=None
    if UID0F42[0]== False:
    	try:
    		try:
    			UID00FE=UID0F5D.encode('utf-8')
    		except:
    			UID00FE=UID0F5D
    		UID2210=UID0F42
    	except Exception, errorMsg:
    		UID2210=[True,1,str(errorMsg)]
    		UID00FE=""
    else:
    	UID2210=UID0F42
    	UID00FE=""
    error_IO=UID2210
    UID07BB,UID0113=re.subn('"',"",UID00FE,int(not True))
    UID095A=np.array([UID07BB])
    parameter=UID095A
    return error_IO,parameter
if __name__ == "__main__":
    error_IO,parameter=main(errorIn,JSON_Tree)
