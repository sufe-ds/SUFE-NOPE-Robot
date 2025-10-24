# -*- coding: utf-8 -*-
import thread
import Queue
import imp
import TabletServiceProxy_executeJS
imp.reload (TabletServiceProxy_executeJS)
stop=False
MemRefOut=0
momeryRef=0
skip=False
ErrorIn=[False,0,""]
ErrorOut=[False,0,""]
minDistance=1.000000
target=""
robotIP="127.0.0.1"
import time
import numpy as np
def UID01A4(error_out_0323,queue_ErrorOut_032C,RefOut_0386,queue_RefOut_03A1,queue_UID07AD,queue_UID07F0,momeryRef,ErrorIn,minDistance,target,robotIP,):
	i_024B=-1
	WhileS_D1S_ADS_BBS_B7_024E_Stop=False
	while WhileS_D1S_ADS_BBS_B7_024E_Stop==False:
		UID0BD5=np.array(["Device/SubDeviceList/Head/Touch/Front/Sensor/Value","Device/SubDeviceList/Head/Touch/Rear/Sensor/Value","Device/SubDeviceList/Head/Touch/Middle/Sensor/Value"],dtype="S")
		if error_out_0323[0]== False:
			try:
				UID0B78=RefOut_0386
				UID0BF8=np.array(RefOut_0386.getListData(UID0BD5.tolist()))
				UID0B6F=error_out_0323
			except Exception, errorMsg:
				UID0B6F=[True,1,str(errorMsg)]
				UID0BF8=np.array([],dtype="float64")
				UID0B78=0
		else:
			UID0B6F=error_out_0323
			UID0BF8=np.array([],dtype="float64")
			UID0B78=0
		time.sleep(500/1000.0)
		if UID0B6F[0]== False:
			try:
				UID0CBD=UID0B78
				UID0BA8=UID0B78.getData("VIRobotics_Page")
				UID0CB4=UID0B6F
			except Exception, errorMsg:
				UID0CB4=[True,1,str(errorMsg)]
				UID0BA8=""
				UID0CBD=0
		else:
			UID0CB4=UID0B6F
			UID0BA8=""
			UID0CBD=0
		UID0C00=np.sum(UID0BF8)
		UID0BA2=UID0BA8=="home"
		UID0BFD=UID0C00>0
		if UID0CB4[0]== False:
			try:
				UID03A0=UID0CBD
				UID0F33=UID0CBD.getData("VIRobotics_nav_busy")
				UID032B=UID0CB4
			except Exception, errorMsg:
				UID032B=[True,1,str(errorMsg)]
				UID0F33=""
				UID03A0=0
		else:
			UID032B=UID0CB4
			UID0F33=""
			UID03A0=0
		UID0636=UID0F33=="0"
		UID0633=UID0BA2|UID0BFD
		UID07F0=UID0BFD
		UID07AD=UID0BA2
		RefOut_03A1=UID03A0
		ErrorOut_032C=UID032B
		WhileS_D1S_ADS_BBS_B7_024E=UID0636|UID0633
		WhileS_D1S_ADS_BBS_B7_024E_Stop=WhileS_D1S_ADS_BBS_B7_024E
	queue_ErrorOut_032C.put(ErrorOut_032C)
	queue_RefOut_03A1.put(RefOut_03A1)
	queue_UID07AD.put(UID07AD)
	queue_UID07F0.put(UID07F0)
def main(momeryRef,ErrorIn,minDistance,target,robotIP):
    if ErrorIn[0]== False:
    	try:
    		RefOut_0386=momeryRef
    		momeryRef.insertData("VIRobotics_nav_busy","1")
    		UID049A=ErrorIn
    	except Exception, errorMsg:
    		UID049A=[True,1,str(errorMsg)]
    		RefOut_0386=0
    else:
    	UID049A=ErrorIn
    	RefOut_0386=0
    UID0932=" "*(0-len(("%."+("%d"%2)+"f") %minDistance))+("%."+("%d"%2)+"f") %minDistance
    UID04A6="waitForNear('"+target+"',"+UID0932+")"
    UID0463=TabletServiceProxy_executeJS.main(UID049A,UID04A6,robotIP)
    error_out_0323=UID0463
    queue_ErrorOut_032C=Queue.Queue()
    queue_RefOut_03A1=Queue.Queue()
    queue_UID07AD=Queue.Queue()
    queue_UID07F0=Queue.Queue()
    thread.start_new_thread(UID01A4,(error_out_0323,queue_ErrorOut_032C,RefOut_0386,queue_RefOut_03A1,queue_UID07AD,queue_UID07F0,momeryRef,ErrorIn,minDistance,target,robotIP,))
    ErrorOut_032C=queue_ErrorOut_032C.get()
    queue_ErrorOut_032C.put(ErrorOut_032C)
    ErrorOut=ErrorOut_032C
    UID07F0=queue_UID07F0.get()
    queue_UID07F0.put(UID07F0)
    skip=UID07F0
    RefOut_03A1=queue_RefOut_03A1.get()
    queue_RefOut_03A1.put(RefOut_03A1)
    MemRefOut=RefOut_03A1
    UID07AD=queue_UID07AD.get()
    queue_UID07AD.put(UID07AD)
    stop=UID07AD
    return ErrorOut,stop,skip,MemRefOut
if __name__ == "__main__":
    ErrorOut,stop,skip,MemRefOut=main(momeryRef,ErrorIn,minDistance,target,robotIP)
