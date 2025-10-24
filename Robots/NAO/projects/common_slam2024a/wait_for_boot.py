# -*- coding: utf-8 -*-
pIP_out="127.0.0.1"
pIP="127.0.0.1"
ErrorOut=[False,0,""]
import imp
import Clear_Errors
imp.reload (Clear_Errors)
import thread
import Queue
from naoqi import ALProxy
import time
def UID025F(AutonomousLifeRef_0156,error_out_0145,queue_ErrorOut_024A,pIP,):
	i_0271=-1
	WhileS_D1S_ADS_BBS_B7_0274_Stop=False
	while WhileS_D1S_ADS_BBS_B7_0274_Stop==False:
		if error_out_0145[0]== False:
			try:
				UID0060=AutonomousLifeRef_0156
				UID029C=AutonomousLifeRef_0156.getState()
				UID0246=error_out_0145
			except Exception, errorMsg:
				UID0246=[True,1,str(errorMsg)]
				UID029C=""
				UID0060=0
		else:
			UID0246=error_out_0145
			UID029C=""
			UID0060=0
		time.sleep(1000/1000.0)
		WhileS_D1S_ADS_BBS_B7_0274=UID029C!="disabled"
		ErrorOut_024A=UID0246
		WhileS_D1S_ADS_BBS_B7_0274_Stop=WhileS_D1S_ADS_BBS_B7_0274
	queue_ErrorOut_024A.put(ErrorOut_024A)
def main(pIP):
    try:
    	AutonomousLifeRef_0156=ALProxy("ALAutonomousLife",pIP,9559)
    	UID0168=[False,0,""]
    except Exception, errorMsg:
    	UID0168=[True,1,str(errorMsg)]
    	AutonomousLifeRef_0156=0
    pIP_out=pIP
    UID0171=0
    UID0140=Clear_Errors.main(UID0168,UID0171)
    error_out_0145=UID0140[0]
    UID0165=UID0140[1]
    queue_ErrorOut_024A=Queue.Queue()
    thread.start_new_thread(UID025F,(AutonomousLifeRef_0156,error_out_0145,queue_ErrorOut_024A,pIP,))
    ErrorOut_024A=queue_ErrorOut_024A.get()
    queue_ErrorOut_024A.put(ErrorOut_024A)
    UID01DC=ErrorOut_024A
    
    time.sleep(2000/1000.0)
    UID01F6=UID01DC
    UID0275=0
    UID0252=Clear_Errors.main(UID01F6,UID0275)
    UID0373=UID0252[0]
    UID0263=UID0252[1]
    ErrorOut=UID0373
    return ErrorOut,pIP_out
if __name__ == "__main__":
    ErrorOut,pIP_out=main(pIP)
