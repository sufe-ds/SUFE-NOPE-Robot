# -*- coding: utf-8 -*-
import numpy as np
qalist=np.array([[]],dtype="S")
a=""
error_in=[False,0,""]
error_out=[False,0,""]
q=""
import re
def main(error_in,q,qalist):
    error_out=error_in
    qalist_0246=qalist.transpose()[0]
    qalist_025C=qalist.transpose()[1]
    q_0307=q
    i_01DD=-1
    ForS_D1S_ADS_BBS_B7_0564_Stop=False
    ForS_D1S_ADS_BBS_B7_01CB_IndexsIn=[]
    ForS_D1S_ADS_BBS_B7_01CB_IndexsIn.append(len(qalist_0246))
    ForS_D1S_ADS_BBS_B7_01CB_IndexsIn.append(len(qalist_025C))
    ForS_D1S_ADS_BBS_B7_01CB_Indexmin=min(ForS_D1S_ADS_BBS_B7_01CB_IndexsIn)
    ForS_D1S_ADS_BBS_B7_01CB_count=ForS_D1S_ADS_BBS_B7_01CB_Indexmin
    while ForS_D1S_ADS_BBS_B7_0564_Stop==False and i_01DD<ForS_D1S_ADS_BBS_B7_01CB_count-1:
    	i_01DD=i_01DD+1
    	UID0264_result=re.split(qalist_0246[i_01DD],q_0307[0:],1)
    	UID02CD=q_0307[:0]+UID0264_result[0]
    	if len(UID0264_result)==2:
    		UID010D=qalist_0246[i_01DD]
    		UID02D3=UID0264_result[1]
    		UID02D6=len(UID02CD)+len(qalist_0246[i_01DD])
    	else:
    		UID010D=""
    		UID02D3=""
    		UID02D6=-1
    	UID0397=UID010D!=""
    	UID0451=qalist_025C[i_01DD]
    	if UID0397==True:
    		UID05BE=True
    		UID0479=UID0451
    	else: 
    		Constant_UID05F6=""
    		UID05BE=False
    		UID0479=""
    	ForS_D1S_ADS_BBS_B7_0564_Stop=UID05BE
    	UID0465=UID0479
    a=UID0465
    return error_out,a
if __name__ == "__main__":
    error_out,a=main(error_in,q,qalist)
