# -*- coding: utf-8 -*-
mode="song"
import urllib
error_in=[False,0,""]
error_out=[False,0,""]
results=[]
source=""
import json
key=""
import urllib2
import numpy as np
import copy
def main(error_in,mode,key):
    UID015C=urllib.quote(key)
    UID0043="http://116.198.207.45:8080/services/song/searchSongID?"+"key="+UID015C+"&mode="+mode
    if error_in[0]== False:
    	try:
    		UID0034=0
    		UID0037="<Not A Path>"
    		UID0058=10000
    		UID0040=UID0034
    		if UID0034==0:
    			UID0034_ref=urllib2.urlopen(UID0043,timeout=UID0058/1000.0)
    			UID0107=UID0034_ref.read()
    			UID0046=UID0034_ref.info().dict
    		else:
    			UID0034_req=urllib2.Request(UID0043)
    			UID0034_ref=UID0034.open(UID0034_req,timeout=UID0058/1000.0)
    			UID0107=UID0034_ref.read()
    			UID0046=UID0034_ref.info().dict
    		if UID0037=="" or UID0037=="<Not A Path>":
    			pass
    		else:
    			UID0034_file=open(UID0037,"wb+")
    			UID0034_file.write(UID0107)
    			UID0034_file.close()
    		UID0101=error_in
    	except Exception, errorMsg:
    		UID0101=[True,1,str(errorMsg)]
    		UID0040=0
    		UID0046=""
    		UID0107=""
    else:
    	UID0101=error_in
    	UID0040=0
    	UID0046=""
    	UID0107=""
    if UID0101[0]== False:
    	try:
    		UID0189=json.loads(UID0107)
    		UID00EF=0
    		UID00E6=0
    		UID0180=UID0101
    	except Exception, errorMsg:
    		UID0180=[True,1,str(errorMsg)]
    		UID00E6=0
    		UID00EF=0
    		UID0189=None
    else:
    	UID0180=UID0101
    	UID00E6=0
    	UID00EF=0
    	UID0189=None
    if UID0180[0]== False:
    	try:
    		UID0183=""
    		UID0242=UID0189
    		try:
    			UID0278=UID0189["source"]
    			UID0169=False
    		except:
    			UID0278=""
    			UID0169=True
    		
    		UID026F=UID0180
    	except Exception, errorMsg:
    		UID026F=[True,1,str(errorMsg)]
    		UID0169=False
    		UID0278=""
    		UID0242=None
    else:
    	UID026F=UID0180
    	UID0169=False
    	UID0278=""
    	UID0242=None
    if UID026F[0]== False:
    	try:
    		UID0377=UID0278.encode("utf-8")
    		UID0239=UID026F
    	except Exception, errorMsg:
    		UID0239=[True,1,str(errorMsg)]
    		UID0377=""
    else:
    	UID0239=UID026F
    	UID0377=""
    if UID0239[0]== False:
    	try:
    		UID022A=UID0242
    		try:
    			UID03FC=UID0242["results"]
    			UID0224=False
    		except:
    			UID03FC={}
    			UID0224=True
    		UID03F3=UID0239
    	except Exception, errorMsg:
    		UID03F3=[True,1,str(errorMsg)]
    		UID0224=False
    		UID03FC=None
    		UID022A=None
    else:
    	UID03F3=UID0239
    	UID0224=False
    	UID03FC=None
    	UID022A=None
    source=UID0377
    if UID03F3[0]== False:
    	try:
    		UID069A=UID03FC
    		UID03E1=len(UID03FC)
    		UID06A6=UID03F3
    	except Exception, errorMsg:
    		UID06A6=[True,1,str(errorMsg)]
    		UID03E1=0
    		UID069A=None
    else:
    	UID06A6=UID03F3
    	UID03E1=0
    	UID069A=None
    UID068A=UID03E1>0
    UID0717=UID03E1
    if UID068A==True:
    	JSON_Tree_Passthrough__JSON_Array__0458=UID069A
    	error_out_0413=UID06A6
    	ForS_D1S_ADS_BBS_B7_0438=UID0717
    	UID0290=[]
    	i_0434=-1
    	ForS_D1S_ADS_BBS_B7_0415_count=ForS_D1S_ADS_BBS_B7_0438
    	for i in range(0, ForS_D1S_ADS_BBS_B7_0415_count):
    		i_0434=i_0434+1
    		UID00A7=["","",""]
    		UID0C26=np.array(["title","artist","songID"],dtype="S")
    		if error_out_0413[0]== False:
    			try:
    				UID0498=JSON_Tree_Passthrough__JSON_Array__0458
    				JSON_Object_0D5E=JSON_Tree_Passthrough__JSON_Array__0458[i_0434]
    				UID0492=False
    				error_out_03C4=error_out_0413
    			except Exception, errorMsg:
    				error_out_03C4=[True,1,str(errorMsg)]
    				UID0492=False
    				JSON_Object_0D5E=None
    				UID0498=None
    		else:
    			error_out_03C4=error_out_0413
    			UID0492=False
    			JSON_Object_0D5E=None
    			UID0498=None
    		UID0311=UID0C26
    		UID0360=np.array([],dtype="S")
    		i_028B=-1
    		ForS_D1S_ADS_BBS_B7_0244_IndexsIn=[]
    		ForS_D1S_ADS_BBS_B7_0244_IndexsIn.append(len(UID0311))
    		ForS_D1S_ADS_BBS_B7_0244_Indexmin=min(ForS_D1S_ADS_BBS_B7_0244_IndexsIn)
    		ForS_D1S_ADS_BBS_B7_0244_count=ForS_D1S_ADS_BBS_B7_0244_Indexmin
    		for i in range(0, ForS_D1S_ADS_BBS_B7_0244_count):
    			i_028B=i_028B+1
    			if error_out_03C4[0]== False:
    				try:
    					UID050D=""
    					UID04FB=JSON_Object_0D5E
    					try:
    						UID042F=JSON_Object_0D5E[UID0311[i_028B]]
    						UID04F5=False
    					except:
    						UID042F=""
    						UID04F5=True
    					
    					UID0424=error_out_03C4
    				except Exception, errorMsg:
    					UID0424=[True,1,str(errorMsg)]
    					UID04F5=False
    					UID042F=""
    					UID04FB=None
    			else:
    				UID0424=error_out_03C4
    				UID04F5=False
    				UID042F=""
    				UID04FB=None
    			if UID0424[0]== False:
    				try:
    					UID035C=UID042F.encode("utf-8")
    					error_out_03C4=UID0424
    				except Exception, errorMsg:
    					error_out_03C4=[True,1,str(errorMsg)]
    					UID035C=""
    			else:
    				error_out_03C4=UID0424
    				UID035C=""
    			
    			UID0360=np.concatenate((UID0360,[UID035C]))
    		try:
    			UID01DC=UID0360[0]
    		except:
    			UID01DC=""
    		try:
    			UID01F7=UID0360[1]
    		except:
    			UID01F7=""
    		try:
    			UID01FD=UID0360[2]
    		except:
    			UID01FD=""
    		error_out_0413=error_out_03C4
    		
    		UID028C=copy.copy(UID00A7)
    		UID028C[0]=UID01DC
    		UID028C[1]=UID01F7
    		UID028C[2]=UID01FD
    		UID0290.append(UID028C)
    	UID06BE=error_out_0413
    	UID06B2=UID0290
    else: 
    	UID0773=[]
    	UID06BE=UID06A6
    	UID06B2=UID0773
    results=UID06B2
    error_out=UID06BE
    return error_out,results,source
if __name__ == "__main__":
    error_out,results,source=main(error_in,mode,key)
