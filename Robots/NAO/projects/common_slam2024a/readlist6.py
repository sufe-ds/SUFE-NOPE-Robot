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
import thread
import Queue
import re
def UID0327(queue_UID0330,queue_UID0340,result_string_0337,error_in,FilePath,):
	UID0330=np.array([],dtype="S")
	i_0361=-1
	WhileS_D1S_ADS_BBS_B7_036A_Stop=False
	while WhileS_D1S_ADS_BBS_B7_036A_Stop==False:
		i_0361=i_0361+1
		UID039B_result=re.split("\n",result_string_0337[0:],1)
		UID03A7=result_string_0337[:0]+UID039B_result[0]
		if len(UID039B_result)==2:
			UID03AA="\n"
			result_string_0337=UID039B_result[1]
			UID03B0=len(UID03A7)+len("\n")
		else:
			UID03AA=""
			result_string_0337=""
			UID03B0=-1
		UID0340=i_0361
		WhileS_D1S_ADS_BBS_B7_036A=UID03A7==""
		
		UID0330=np.concatenate((UID0330,[UID03A7]))
		WhileS_D1S_ADS_BBS_B7_036A_Stop=WhileS_D1S_ADS_BBS_B7_036A
	queue_UID0330.put(UID0330)
	queue_UID0340.put(UID0340)
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
    				UID0349=UID0158.read()
    			else:
    				UID0349=UID0158.read(-1)
    			UID0165=UID0153
    		except Exception, errorMsg:
    			UID0165=[True,1,str(errorMsg)]
    			UID0349=""
    			UID0160=0
    	else:
    		UID0165=UID0153
    		UID0349=""
    		UID0160=0
    	result_string_0337,UID0362=re.subn("\r","",UID0349,int(not True))
    	UID0162=UID0165
    	UID015D=UID0160
    	queue_UID0330=Queue.Queue()
    	queue_UID0340=Queue.Queue()
    	thread.start_new_thread(UID0327,(queue_UID0330,queue_UID0340,result_string_0337,error_in,FilePath,))
    	UID0340=queue_UID0340.get()
    	queue_UID0340.put(UID0340)
    	UID0330=queue_UID0330.get()
    	queue_UID0330.put(UID0330)
    	UID03DC=UID0330[UID0340]
    	UID0209=np.delete(UID0330,[UID0340])
    	UID020F=np.array([],dtype="S")
    	UID0215=np.array([],dtype="S")
    	UID0347=np.array([],dtype="S")
    	UID0504=np.array([],dtype="S")
    	UID052C=np.array([],dtype="S")
    	UID0652=np.array([],dtype="S")
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
    			UID02AA=UID0235_result[1]
    			UID0249=len(UID0212)+len("\t")
    		else:
    			UID0243=""
    			UID02AA=""
    			UID0249=-1
    		UID029E_result=re.split("\t",UID02AA[0:],1)
    		UID0218=UID02AA[:0]+UID029E_result[0]
    		if len(UID029E_result)==2:
    			UID02BE="\t"
    			UID046F=UID029E_result[1]
    			UID02D6=len(UID0218)+len("\t")
    		else:
    			UID02BE=""
    			UID046F=""
    			UID02D6=-1
    		UID020F=np.concatenate((UID020F,[UID0212]))
    		UID01D6_result=re.split("\t",UID046F[0:],1)
    		UID0343=UID046F[:0]+UID01D6_result[0]
    		if len(UID01D6_result)==2:
    			UID047B="\t"
    			UID0336=UID01D6_result[1]
    			UID0481=len(UID0343)+len("\t")
    		else:
    			UID047B=""
    			UID0336=""
    			UID0481=-1
    		UID0215=np.concatenate((UID0215,[UID0218]))
    		UID032B_result=re.split("\t",UID0336[0:],1)
    		UID0500=UID0336[:0]+UID032B_result[0]
    		if len(UID032B_result)==2:
    			UID0367="\t"
    			UID0497=UID032B_result[1]
    			UID0387=len(UID0500)+len("\t")
    		else:
    			UID0367=""
    			UID0497=""
    			UID0387=-1
    		UID0347=np.concatenate((UID0347,[UID0343]))
    		UID01E5_result=re.split("\t",UID0497[0:],1)
    		UID0528=UID0497[:0]+UID01E5_result[0]
    		if len(UID01E5_result)==2:
    			UID04A3="\t"
    			UID064E=UID01E5_result[1]
    			UID04A9=len(UID0528)+len("\t")
    		else:
    			UID04A3=""
    			UID064E=""
    			UID04A9=-1
    		UID0504=np.concatenate((UID0504,[UID0500]))
    		UID0652=np.concatenate((UID0652,[UID064E]))
    		UID052C=np.concatenate((UID052C,[UID0528]))
    	UID03F6=np.concatenate(([UID020F],[UID0215],[UID0347],[UID0504],[UID052C],[UID0652]))
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
