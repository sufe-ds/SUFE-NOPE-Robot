# -*- coding: utf-8 -*-
error_out=[False,0,""]
ErrorIn=[False,0,""]
IP="127.0.0.1"
import numpy as np
new_action=np.array([],dtype="S")
ALMemory=0
action=np.array(["Page"],dtype="S")
import imp
import Clear_Errors
imp.reload (Clear_Errors)
import TabletServiceProxy_executeJS
imp.reload (TabletServiceProxy_executeJS)
def main(ErrorIn,IP,ALMemory,action):
    if ErrorIn[0]== False:
    	try:
    		UID00A4=ALMemory
    		UID00D6=ALMemory.getData("VIRobotics_Page")
    		UID0953=ErrorIn
    	except Exception, errorMsg:
    		UID0953=[True,1,str(errorMsg)]
    		UID00D6=""
    		UID00A4=0
    else:
    	UID0953=ErrorIn
    	UID00D6=""
    	UID00A4=0
    UID00E0=action
    UID087E=IP
    if UID00D6=="home" or UID00D6=="xunfei":
    	UID004A=TabletServiceProxy_executeJS.main(UID0953,"document.getElementById('AI').style.display='block'",UID087E)
    	UID0080=UID004A
    	UID00DB=UID00E0
    	UID0089=0
    	UID0071=Clear_Errors.main(UID0080,UID0089)
    	UID0B00=UID0071[0]
    	UID007D=UID0071[1]
    	UID0B04=UID0B00
    else: 
    	UID00ED=np.array(["Page"],dtype="S")
    	UID0B04=UID0953
    	UID00DB=UID00ED
    new_action=UID00DB
    error_out=UID0B04
    return error_out,new_action
if __name__ == "__main__":
    error_out,new_action=main(ErrorIn,IP,ALMemory,action)
