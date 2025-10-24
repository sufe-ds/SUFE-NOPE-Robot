# -*- coding: utf-8 -*-
timeout=""
speech=""
foreshow=""
url=""
import numpy as np
navlist=np.array([[]],dtype="S")
dest=""
error_in=[False,0,""]
error_out=[False,0,""]
button=""
def main(error_in,button,navlist):
    error_out=error_in
    navlist_0246=navlist.transpose()[0]
    navlist_025C=navlist.transpose()[1]
    navlist_02C3=navlist.transpose()[2]
    navlist_02E7=navlist.transpose()[3]
    navlist_0134=navlist.transpose()[4]
    navlist_0151=navlist.transpose()[5]
    button_0307=button
    i_01DD=-1
    ForS_D1S_ADS_BBS_B7_0564_Stop=False
    ForS_D1S_ADS_BBS_B7_01CB_IndexsIn=[]
    ForS_D1S_ADS_BBS_B7_01CB_IndexsIn.append(len(navlist_0246))
    ForS_D1S_ADS_BBS_B7_01CB_IndexsIn.append(len(navlist_025C))
    ForS_D1S_ADS_BBS_B7_01CB_IndexsIn.append(len(navlist_02C3))
    ForS_D1S_ADS_BBS_B7_01CB_IndexsIn.append(len(navlist_02E7))
    ForS_D1S_ADS_BBS_B7_01CB_IndexsIn.append(len(navlist_0134))
    ForS_D1S_ADS_BBS_B7_01CB_IndexsIn.append(len(navlist_0151))
    ForS_D1S_ADS_BBS_B7_01CB_Indexmin=min(ForS_D1S_ADS_BBS_B7_01CB_IndexsIn)
    ForS_D1S_ADS_BBS_B7_01CB_count=ForS_D1S_ADS_BBS_B7_01CB_Indexmin
    while ForS_D1S_ADS_BBS_B7_0564_Stop==False and i_01DD<ForS_D1S_ADS_BBS_B7_01CB_count-1:
    	i_01DD=i_01DD+1
    	UID0397=button_0307==navlist_0246[i_01DD]
    	UID0451=navlist_025C[i_01DD]
    	UID0302=navlist_02C3[i_01DD]
    	UID035D=navlist_02E7[i_01DD]
    	UID01FB=navlist_0134[i_01DD]
    	UID0290=navlist_0151[i_01DD]
    	if UID0397==True:
    		UID02B0=UID0290
    		UID021C=UID01FB
    		UID0375=UID035D
    		UID0330=UID0302
    		UID05BE=True
    		UID0479=UID0451
    	else: 
    		Constant_UID05DF=""
    		UID02B0=Constant_UID05DF
    		UID021C=Constant_UID05DF
    		UID0375=Constant_UID05DF
    		UID0330=Constant_UID05DF
    		UID05BE=False
    		UID0479=Constant_UID05DF
    	ForS_D1S_ADS_BBS_B7_0564_Stop=UID05BE
    	UID02C6=UID02B0
    	UID0235=UID021C
    	UID038A=UID0375
    	UID031C=UID0330
    	UID0465=UID0479
    dest=UID0465
    url=UID031C
    foreshow=UID038A
    speech=UID0235
    timeout=UID02C6
    return error_out,speech,url,dest,foreshow,timeout
if __name__ == "__main__":
    error_out,speech,url,dest,foreshow,timeout=main(error_in,button,navlist)
