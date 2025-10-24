# -*- coding: utf-8 -*-
import numpy as np
import imp
import Clear_Errors
imp.reload (Clear_Errors)
parameter=np.array([],dtype="S")
error_out=[False,0,""]
error_in__no_error_=[False,0,""]
JSON_Tree=None
def main(error_in__no_error_,JSON_Tree):
    UID0A12=np.array(["category","special","name"],dtype="S")
    if error_in__no_error_[0]== False:
    	try:
    		UID03C1=JSON_Tree
    		try:
    			UID0468=JSON_Tree["semantic"]
    			UID03BB=False
    		except:
    			UID0468={}
    			UID03BB=True
    		UID045F=error_in__no_error_
    	except Exception, errorMsg:
    		UID045F=[True,1,str(errorMsg)]
    		UID03BB=False
    		UID0468=None
    		UID03C1=None
    else:
    	UID045F=error_in__no_error_
    	UID03BB=False
    	UID0468=None
    	UID03C1=None
    if UID045F[0]== False:
    	try:
    		UID0450=UID0468
    		try:
    			UID044D=UID0468["slots"]
    			UID044A=False
    		except:
    			UID044D={}
    			UID044A=True
    		UID088C=UID045F
    	except Exception, errorMsg:
    		UID088C=[True,1,str(errorMsg)]
    		UID044A=False
    		UID044D=None
    		UID0450=None
    else:
    	UID088C=UID045F
    	UID044A=False
    	UID044D=None
    	UID0450=None
    if UID088C[0]== False:
    	try:
    		UID087D=UID044D
    		try:
    			UID0AEE=UID044D["location"]
    			UID0877=False
    		except:
    			UID0AEE={}
    			UID0877=True
    		UID0AE3=UID088C
    	except Exception, errorMsg:
    		UID0AE3=[True,1,str(errorMsg)]
    		UID0877=False
    		UID0AEE=None
    		UID087D=None
    else:
    	UID0AE3=UID088C
    	UID0877=False
    	UID0AEE=None
    	UID087D=None
    if UID0AE3[0]== False:
    	try:
    		UID0AE8=""
    		UID0ACC=UID0AEE
    		try:
    			UID0C0F=UID0AEE["poi"]
    			UID0AC6=False
    		except:
    			UID0C0F=""
    			UID0AC6=True
    		
    		UID0C06=UID0AE3
    	except Exception, errorMsg:
    		UID0C06=[True,1,str(errorMsg)]
    		UID0AC6=False
    		UID0C0F=""
    		UID0ACC=None
    else:
    	UID0C06=UID0AE3
    	UID0AC6=False
    	UID0C0F=""
    	UID0ACC=None
    if UID0C06[0]== False:
    	try:
    		try:
    			UID11B9=UID0C0F.encode('utf-8')
    		except:
    			UID11B9=UID0C0F
    		UID015A=UID0C06
    	except Exception, errorMsg:
    		UID015A=[True,1,str(errorMsg)]
    		UID11B9=""
    else:
    	UID015A=UID0C06
    	UID11B9=""
    UID0163=0
    UID0147=Clear_Errors.main(UID015A,UID0163)
    error_out_0C31=UID0147[0]
    UID0157=UID0147[1]
    JSON_Object_0B4C=UID044D
    UID0B70=UID0A12
    UID0BCD=np.array([],dtype="S")
    i_0B1B=-1
    ForS_D1S_ADS_BBS_B7_00F9_IndexsIn=[]
    ForS_D1S_ADS_BBS_B7_00F9_IndexsIn.append(len(UID0B70))
    ForS_D1S_ADS_BBS_B7_00F9_Indexmin=min(ForS_D1S_ADS_BBS_B7_00F9_IndexsIn)
    ForS_D1S_ADS_BBS_B7_00F9_count=ForS_D1S_ADS_BBS_B7_00F9_Indexmin
    for i in range(0, ForS_D1S_ADS_BBS_B7_00F9_count):
    	i_0B1B=i_0B1B+1
    	if error_out_0C31[0]== False:
    		try:
    			UID0509=""
    			UID04F7=JSON_Object_0B4C
    			try:
    				UID090F=JSON_Object_0B4C[UID0B70[i_0B1B]]
    				UID04F1=False
    			except:
    				UID090F=""
    				UID04F1=True
    			
    			UID06E1=error_out_0C31
    		except Exception, errorMsg:
    			UID06E1=[True,1,str(errorMsg)]
    			UID04F1=False
    			UID090F=""
    			UID04F7=None
    	else:
    		UID06E1=error_out_0C31
    		UID04F1=False
    		UID090F=""
    		UID04F7=None
    	if UID06E1[0]== False:
    		try:
    			try:
    				UID0BC9=UID090F.encode('utf-8')
    			except:
    				UID0BC9=UID090F
    			UID0776=UID06E1
    		except Exception, errorMsg:
    			UID0776=[True,1,str(errorMsg)]
    			UID0BC9=""
    	else:
    		UID0776=UID06E1
    		UID0BC9=""
    	UID077F=0
    	UID075F=Clear_Errors.main(UID0776,UID077F)
    	error_out_0C31=UID075F[0]
    	UID0773=UID075F[1]
    	UID0BCD=np.concatenate((UID0BCD,[UID0BC9]))
    	
    error_out=error_out_0C31
    UID1280=np.concatenate(([UID11B9],UID0BCD))
    parameter=UID1280
    return error_out,parameter
if __name__ == "__main__":
    error_out,parameter=main(error_in__no_error_,JSON_Tree)
