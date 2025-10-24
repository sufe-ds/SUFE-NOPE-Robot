# -*- coding: utf-8 -*-
error_in=[False,0,""]
error_out=[False,0,""]
import numpy as np
datalist=np.array([[]],dtype="S")
import imp
import Clear_Errors
imp.reload (Clear_Errors)
FilePath="/home/nao/1.txt"
import copy
import re
import thread
import Queue
def UID01A7(queue_UID01A9,queue_UID051C,result_string_01AF,error_in,FilePath,):
	UID01A9=np.array([],dtype="S")
	i_01C0=-1
	WhileS_D1S_ADS_BBS_B7_01C3_Stop=False
	while WhileS_D1S_ADS_BBS_B7_01C3_Stop==False:
		i_01C0=i_01C0+1
		UID01CF_result=re.split("\n",result_string_01AF[0:],1)
		UID01DA=result_string_01AF[:0]+UID01CF_result[0]
		if len(UID01CF_result)==2:
			UID01DD="\n"
			result_string_01AF=UID01CF_result[1]
			UID01E3=len(UID01DA)+len("\n")
		else:
			UID01DD=""
			result_string_01AF=""
			UID01E3=-1
		UID051C=i_01C0
		WhileS_D1S_ADS_BBS_B7_01C3=UID01DA==""
		
		UID01A9=np.concatenate((UID01A9,[UID01DA]))
		WhileS_D1S_ADS_BBS_B7_01C3_Stop=WhileS_D1S_ADS_BBS_B7_01C3
	queue_UID01A9.put(UID01A9)
	queue_UID051C.put(UID051C)
def main(error_in,FilePath):
    if error_in[0]== False:
    	try:
    		UID0158=open(FilePath,"rb+")
    		UID0153=error_in
    	except Exception, errorMsg:
    		UID0153=[True,1,str(errorMsg)]
    		UID0158=0
    else:
    	UID0153=error_in
    	UID0158=0
    if UID0153[0]==True:
    	UID02B8=np.array([[]],dtype="S")
    	UID0167=UID02B8
    	UID0162=UID0153
    	UID015D=UID0158
    else: 
    	if UID0153[0]== False:
    		try:
    			UID0160=UID0158
    			if -1==0:
    				UID0370=UID0158.read()
    			else:
    				UID0370=UID0158.read(-1)
    			UID0165=UID0153
    		except Exception, errorMsg:
    			UID0165=[True,1,str(errorMsg)]
    			UID0370=""
    			UID0160=0
    	else:
    		UID0165=UID0153
    		UID0370=""
    		UID0160=0
    	result_string_01AF,UID0385=re.subn("\r","",UID0370,int(not True))
    	UID0162=UID0165
    	UID015D=UID0160
    	queue_UID01A9=Queue.Queue()
    	queue_UID051C=Queue.Queue()
    	thread.start_new_thread(UID01A7,(queue_UID01A9,queue_UID051C,result_string_01AF,error_in,FilePath,))
    	UID01A9=queue_UID01A9.get()
    	queue_UID01A9.put(UID01A9)
    	UID051C=queue_UID051C.get()
    	queue_UID051C.put(UID051C)
    	UID0493=UID01A9[UID051C]
    	UID0209=np.delete(UID01A9,[UID051C])
    	UID020F=np.array([],dtype="S")
    	UID0215=np.array([],dtype="S")
    	i_0229=-1
    	ForS_D1S_ADS_BBS_B7_0203_IndexsIn=[]
    	ForS_D1S_ADS_BBS_B7_0203_IndexsIn.append(len(UID0209))
    	ForS_D1S_ADS_BBS_B7_0203_Indexmin=min(ForS_D1S_ADS_BBS_B7_0203_IndexsIn)
    	ForS_D1S_ADS_BBS_B7_0203_count=ForS_D1S_ADS_BBS_B7_0203_Indexmin
    	for i in range(0, ForS_D1S_ADS_BBS_B7_0203_count):
    		i_0229=i_0229+1
    		UID0235_result=re.split("\t",UID0209[i_0229][0:],1)
    		UID0212=UID0209[i_0229][:0]+UID0235_result[0]
    		if len(UID0235_result)==2:
    			UID0243="\t"
    			UID0218=UID0235_result[1]
    			UID0249=len(UID0212)+len("\t")
    		else:
    			UID0243=""
    			UID0218=""
    			UID0249=-1
    		UID0215=np.concatenate((UID0215,[UID0218]))
    		UID020F=np.concatenate((UID020F,[UID0212]))
    	UID03F6=np.concatenate(([UID020F],[UID0215]))
    	UID016A=np.transpose(UID03F6)
    	UID0167=UID016A
    if UID0162[0]== False:
    	try:
    		UID015D.close()
    		UID02FA=UID0162
    	except Exception, errorMsg:
    		UID02FA=[True,1,str(errorMsg)]
    else:
    	UID02FA=UID0162
    datalist=UID0167
    UID0303=0
    UID02EB=Clear_Errors.main(UID02FA,UID0303)
    UID00AD=UID02EB[0]
    UID02F7=UID02EB[1]
    error_out=UID00AD
    return error_out,datalist
if __name__ == "__main__":
    error_out,datalist=main(error_in,FilePath)
