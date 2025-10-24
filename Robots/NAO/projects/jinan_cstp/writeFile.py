# -*- coding: utf-8 -*-
text=""
LocalPath_out="/home/nao/abc.txt"
error_in=[False,0,""]
error_out=[False,0,""]
LocalPath="/home/nao/abc.txt"
def main(error_in,text,LocalPath):
    if error_in[0]== False:
    	try:
    		UID011B=open(LocalPath,"wb+")
    		UID0112=error_in
    	except Exception, errorMsg:
    		UID0112=[True,1,str(errorMsg)]
    		UID011B=0
    else:
    	UID0112=error_in
    	UID011B=0
    LocalPath_out=LocalPath
    if UID0112[0]== False:
    	try:
    		UID017E=UID011B
    		UID011B.write(text)
    		UID0175=UID0112
    	except Exception, errorMsg:
    		UID0175=[True,1,str(errorMsg)]
    		UID017E=0
    else:
    	UID0175=UID0112
    	UID017E=0
    if UID0175[0]== False:
    	try:
    		UID017E.close()
    		UID05C4=UID0175
    	except Exception, errorMsg:
    		UID05C4=[True,1,str(errorMsg)]
    else:
    	UID05C4=UID0175
    error_out=UID05C4
    return error_out,LocalPath_out
if __name__ == "__main__":
    error_out,LocalPath_out=main(error_in,text,LocalPath)
