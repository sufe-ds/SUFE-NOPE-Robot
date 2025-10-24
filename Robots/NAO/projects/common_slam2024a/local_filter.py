# -*- coding: utf-8 -*-
output=""
import numpy as np
input=""
import re
def main(input):
    UID00F5=np.array([["请退出程序","请退出程序"],["声音开大点","声音开大"],["声音开小点","声音开小"],["握手","握手"],["握手","握个手"],["跳舞","跳舞"],["跳舞","跳个舞"],["小苹果","小苹果"],["骑马舞","骑马舞"],["骑马舞","骑马"],["太空舞","太空舞"],["太空舞","太空"],["飞鹰舞","鹦鹉"],["飞鹰舞","飞鹰"],["太极舞","太极"],["大篷车","大篷车"],["西班牙舞蹈","弗拉门戈"],["西班牙舞蹈","西班牙"],["范吉利斯","范吉利斯"],["祝你好运","祝你好运"],["快乐的心","快乐的心"],["你叫什么名字","名字"],["你叫什么名字","你叫什么"],["你叫什么名字","你叫啥"],["参观","参观"],["参观","导览"],["参观","讲解"]],dtype="S")
    S_B5S_DAS_D2S_BBS_C1S_D0S_CAS_C7S_B1S_BES_B5S_D8S_B1S_EAS_D7S_BCS_BBS_AFS_B4S_CAS_CCS_F5S_A3S_ACS_B5S_DAS_B6S_FES_C1S_D0S_CAS_C7S_C4S_A3S_BAS_FDS_C6S_A5S_C5S_E4S_B4S_CAS_CCS_F5_0095=UID00F5.transpose()[1]
    S_B5S_DAS_D2S_BBS_C1S_D0S_CAS_C7S_B1S_BES_B5S_D8S_B1S_EAS_D7S_BCS_BBS_AFS_B4S_CAS_CCS_F5S_A3S_ACS_B5S_DAS_B6S_FES_C1S_D0S_CAS_C7S_C4S_A3S_BAS_FDS_C6S_A5S_C5S_E4S_B4S_CAS_CCS_F5_004C=UID00F5.transpose()[0]
    input_03F7=input
    i_0370=-1
    ForS_D1S_ADS_BBS_B7_01F7_Stop=False
    ForS_D1S_ADS_BBS_B7_035E_IndexsIn=[]
    ForS_D1S_ADS_BBS_B7_035E_IndexsIn.append(len(S_B5S_DAS_D2S_BBS_C1S_D0S_CAS_C7S_B1S_BES_B5S_D8S_B1S_EAS_D7S_BCS_BBS_AFS_B4S_CAS_CCS_F5S_A3S_ACS_B5S_DAS_B6S_FES_C1S_D0S_CAS_C7S_C4S_A3S_BAS_FDS_C6S_A5S_C5S_E4S_B4S_CAS_CCS_F5_0095))
    ForS_D1S_ADS_BBS_B7_035E_IndexsIn.append(len(S_B5S_DAS_D2S_BBS_C1S_D0S_CAS_C7S_B1S_BES_B5S_D8S_B1S_EAS_D7S_BCS_BBS_AFS_B4S_CAS_CCS_F5S_A3S_ACS_B5S_DAS_B6S_FES_C1S_D0S_CAS_C7S_C4S_A3S_BAS_FDS_C6S_A5S_C5S_E4S_B4S_CAS_CCS_F5_004C))
    ForS_D1S_ADS_BBS_B7_035E_Indexmin=min(ForS_D1S_ADS_BBS_B7_035E_IndexsIn)
    ForS_D1S_ADS_BBS_B7_035E_count=ForS_D1S_ADS_BBS_B7_035E_Indexmin
    while ForS_D1S_ADS_BBS_B7_01F7_Stop==False and i_0370<ForS_D1S_ADS_BBS_B7_035E_count-1:
    	i_0370=i_0370+1
    	UID03DE_result=re.split(S_B5S_DAS_D2S_BBS_C1S_D0S_CAS_C7S_B1S_BES_B5S_D8S_B1S_EAS_D7S_BCS_BBS_AFS_B4S_CAS_CCS_F5S_A3S_ACS_B5S_DAS_B6S_FES_C1S_D0S_CAS_C7S_C4S_A3S_BAS_FDS_C6S_A5S_C5S_E4S_B4S_CAS_CCS_F5_0095[i_0370],input_03F7[0:],1)
    	UID0491=input_03F7[:0]+UID03DE_result[0]
    	if len(UID03DE_result)==2:
    		UID0090=S_B5S_DAS_D2S_BBS_C1S_D0S_CAS_C7S_B1S_BES_B5S_D8S_B1S_EAS_D7S_BCS_BBS_AFS_B4S_CAS_CCS_F5S_A3S_ACS_B5S_DAS_B6S_FES_C1S_D0S_CAS_C7S_C4S_A3S_BAS_FDS_C6S_A5S_C5S_E4S_B4S_CAS_CCS_F5_0095[i_0370]
    		UID0497=UID03DE_result[1]
    		UID049A=len(UID0491)+len(S_B5S_DAS_D2S_BBS_C1S_D0S_CAS_C7S_B1S_BES_B5S_D8S_B1S_EAS_D7S_BCS_BBS_AFS_B4S_CAS_CCS_F5S_A3S_ACS_B5S_DAS_B6S_FES_C1S_D0S_CAS_C7S_C4S_A3S_BAS_FDS_C6S_A5S_C5S_E4S_B4S_CAS_CCS_F5_0095[i_0370])
    	else:
    		UID0090=""
    		UID0497=""
    		UID049A=-1
    	UID013B=UID0090!=""
    	UID0686=S_B5S_DAS_D2S_BBS_C1S_D0S_CAS_C7S_B1S_BES_B5S_D8S_B1S_EAS_D7S_BCS_BBS_AFS_B4S_CAS_CCS_F5S_A3S_ACS_B5S_DAS_B6S_FES_C1S_D0S_CAS_C7S_C4S_A3S_BAS_FDS_C6S_A5S_C5S_E4S_B4S_CAS_CCS_F5_004C[i_0370]
    	UID01D7=input_03F7
    	if UID013B==True:
    		UID023B=True
    		UID0699=UID0686
    	else: 
    		UID023B=False
    		UID0699=UID01D7
    	ForS_D1S_ADS_BBS_B7_01F7_Stop=UID023B
    	input_06A7=UID0699
    output=input_06A7
    return output
if __name__ == "__main__":
    output=main(input)
