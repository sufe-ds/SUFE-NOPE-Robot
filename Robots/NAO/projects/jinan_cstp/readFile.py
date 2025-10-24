# -*- coding: utf-8 -*-
textout=""
LocalPath_out="/home/nao/abc.txt"
error_in=[False,0,""]
error_out=[False,0,""]
LocalPath="/home/nao/abc.txt"
def main(error_in,LocalPath):
    if error_in[0]== False:
    	try:
    		UID0136=open(LocalPath,"rb+")
    		UID012D=error_in
    	except Exception, errorMsg:
    		UID012D=[True,1,str(errorMsg)]
    		UID0136=0
    else:
    	UID012D=error_in
    	UID0136=0
    LocalPath_out=LocalPath
    if UID012D[0]== False:
    	try:
    		UID017E=UID0136
    		if -1==0:
    			UID0158=UID0136.read()
    		else:
    			UID0158=UID0136.read(-1)
    		UID0175=UID012D
    	except Exception, errorMsg:
    		UID0175=[True,1,str(errorMsg)]
    		UID0158=""
    		UID017E=0
    else:
    	UID0175=UID012D
    	UID0158=""
    	UID017E=0
    if UID0175[0]== False:
    	try:
    		UID017E.close()
    		UID05C4=UID0175
    	except Exception, errorMsg:
    		UID05C4=[True,1,str(errorMsg)]
    else:
    	UID05C4=UID0175
    textout=UID0158
    error_out=UID05C4
    return error_out,textout,LocalPath_out
if __name__ == "__main__":
    error_out,textout,LocalPath_out=main(error_in,LocalPath)
