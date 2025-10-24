# -*- coding: utf-8 -*-
MemRefOut=0
stop=False
skip=False
momeryRef=0
ErrorIn=[False,0,""]
ErrorOut=[False,0,""]
import thread
import Queue
import imp
import Clear_Errors
imp.reload (Clear_Errors)
import time
import numpy as np
def UID002B(momeryRef_002D,ErrorIn_0035,queue_UID0249,queue_error_out_0307,queue_UID0780,queue_RefOut_03B7,ErrorIn,momeryRef,):
	i_0041=-1
	WhileS_D1S_ADS_BBS_B7_0044_Stop=False
	while WhileS_D1S_ADS_BBS_B7_0044_Stop==False:
		UID0047=np.array(["Device/SubDeviceList/Head/Touch/Front/Sensor/Value","Device/SubDeviceList/Head/Touch/Rear/Sensor/Value","Device/SubDeviceList/Head/Touch/Middle/Sensor/Value"],dtype="S")
		if ErrorIn_0035[0]== False:
			try:
				UID0238=momeryRef_002D
				UID00B5=np.array(momeryRef_002D.getListData(UID0047.tolist()))
				UID0327=ErrorIn_0035
			except Exception, errorMsg:
				UID0327=[True,1,str(errorMsg)]
				UID00B5=np.array([],dtype="float64")
				UID0238=0
		else:
			UID0327=ErrorIn_0035
			UID00B5=np.array([],dtype="float64")
			UID0238=0
		time.sleep((500-int(time.time()*1000)%500)/1000.0)
		UID00BD=np.sum(UID00B5)
		UID0330=0
		UID0314=Clear_Errors.main(UID0327,UID0330)
		UID0224=UID0314[0]
		UID0324=UID0314[1]
		UID00BA=UID00BD>0
		if UID0224[0]== False:
			try:
				UID00E4=UID0238
				UID0270=UID0238.getData("VIRobotics_Page")
				UID0509=UID0224
			except Exception, errorMsg:
				UID0509=[True,1,str(errorMsg)]
				UID0270=""
				UID00E4=0
		else:
			UID0509=UID0224
			UID0270=""
			UID00E4=0
		UID026D="home"==UID0270
		UID0512=0
		UID04F6=Clear_Errors.main(UID0509,UID0512)
		UID00DB=UID04F6[0]
		UID0506=UID04F6[1]
		UID0249=UID00BA
		if UID00DB[0]== False:
			try:
				UID03B3=UID00E4
				UID00F8=UID00E4.getData("ALTextToSpeech/CurrentSentence")
				UID0236=UID00DB
			except Exception, errorMsg:
				UID0236=[True,1,str(errorMsg)]
				UID00F8=""
				UID03B3=0
		else:
			UID0236=UID00DB
			UID00F8=""
			UID03B3=0
		UID0103=UID00BA|UID026D
		UID0780=UID026D
		UID0100=UID00F8==""
		UID023F=0
		UID0223=Clear_Errors.main(UID0236,UID023F)
		UID0303=UID0223[0]
		UID0233=UID0223[1]
		RefOut_03B7=UID03B3
		WhileS_D1S_ADS_BBS_B7_0044=UID0103|UID0100
		error_out_0307=UID0303
		WhileS_D1S_ADS_BBS_B7_0044_Stop=WhileS_D1S_ADS_BBS_B7_0044
	queue_UID0249.put(UID0249)
	queue_error_out_0307.put(error_out_0307)
	queue_UID0780.put(UID0780)
	queue_RefOut_03B7.put(RefOut_03B7)
def main(ErrorIn,momeryRef):
    ErrorIn_0035=ErrorIn
    momeryRef_002D=momeryRef
    queue_UID0249=Queue.Queue()
    queue_error_out_0307=Queue.Queue()
    queue_UID0780=Queue.Queue()
    queue_RefOut_03B7=Queue.Queue()
    thread.start_new_thread(UID002B,(momeryRef_002D,ErrorIn_0035,queue_UID0249,queue_error_out_0307,queue_UID0780,queue_RefOut_03B7,ErrorIn,momeryRef,))
    error_out_0307=queue_error_out_0307.get()
    queue_error_out_0307.put(error_out_0307)
    ErrorOut=error_out_0307
    UID0249=queue_UID0249.get()
    queue_UID0249.put(UID0249)
    skip=UID0249
    UID0780=queue_UID0780.get()
    queue_UID0780.put(UID0780)
    stop=UID0780
    RefOut_03B7=queue_RefOut_03B7.get()
    queue_RefOut_03B7.put(RefOut_03B7)
    MemRefOut=RefOut_03B7
    return ErrorOut,stop,skip,MemRefOut
if __name__ == "__main__":
    ErrorOut,stop,skip,MemRefOut=main(ErrorIn,momeryRef)
