# -*- coding: utf-8 -*-
SessionID=""
SessionIDOut=""
timeout=8000
import time
error_out=[False,0,""]
error_in__no_error_=[False,0,""]
String=""
import thread
import Queue
import os
from ctypes import *
import platform
if platform.system()=="Linux":
 libfolder=os.path.split(os.path.realpath(__file__))[0]
 libpath=os.path.join(libfolder,"xunfei.so")
 xfdll=cdll.LoadLibrary(libpath)
else:
 xfdll=windll.LoadLibrary("msc.dll")
def UID00BD(queue_error_out_00C3,SessionID_0304,error_in__no_error__03EB,millisecond_timer_value_04C2,timeout_05D1,UID00C7,queue_UID00C7,error_in__no_error_,timeout,SessionID,):
	i_00DC=-1
	WhileS_D1S_ADS_BBS_B7_00DF_Stop=False
	while WhileS_D1S_ADS_BBS_B7_00DF_Stop==False:
		UID049F=int(time.time()*1000)
		time.sleep((200-int(time.time()*1000)%200)/1000.0)
		if error_in__no_error__03EB[0]== False:
			try:
				UID0118=0
				xfdll.QISRGetResult.restype = c_char_p
				CID00=c_int(0)
				UID0129=c_int(0)
				UID0147=xfdll.QISRGetResult(SessionID_0304, byref(UID0129), UID0118, byref(CID00))
				CID00=CID00.value
				UID0129=UID0129.value
				if UID0147==None:
						UID0147=""
				UID00FD=error_in__no_error__03EB
			except Exception, errorMsg:
				UID00FD=[True,1,str(errorMsg)]
				UID0129=0
				UID0147=""
				UID010C=0
		else:
			UID00FD=error_in__no_error__03EB
			UID0129=0
			UID0147=""
			UID010C=0
		UID05A6=UID049F-millisecond_timer_value_04C2
		UID01AC=UID0129==5
		UID00C7=UID00C7+UID0147
		UID01AF=UID05A6>=timeout_05D1
		error_out_00C3=UID00FD
		UID01C2=UID01AF|UID01AC
		
		WhileS_D1S_ADS_BBS_B7_00DF=UID00FD[0]|UID01C2
		WhileS_D1S_ADS_BBS_B7_00DF_Stop=WhileS_D1S_ADS_BBS_B7_00DF
	queue_error_out_00C3.put(error_out_00C3)
	UID00C7=UID00C7
	queue_UID00C7.put(UID00C7)
def main(error_in__no_error_,timeout,SessionID):
    millisecond_timer_value_04C2=int(time.time()*1000)
    UID00C7=""
    error_in__no_error__03EB=error_in__no_error_
    timeout_05D1=timeout
    SessionID_0304=SessionID
    queue_error_out_00C3=Queue.Queue()
    queue_UID00C7=Queue.Queue()
    thread.start_new_thread(UID00BD,(queue_error_out_00C3,SessionID_0304,error_in__no_error__03EB,millisecond_timer_value_04C2,timeout_05D1,UID00C7,queue_UID00C7,error_in__no_error_,timeout,SessionID,))
    SessionIDOut=SessionID
    UID00C7=queue_UID00C7.get()
    queue_UID00C7.put(UID00C7)
    String=UID00C7
    error_out_00C3=queue_error_out_00C3.get()
    queue_error_out_00C3.put(error_out_00C3)
    error_out=error_out_00C3
    return error_out,String,SessionIDOut
if __name__ == "__main__":
    error_out,String,SessionIDOut=main(error_in__no_error_,timeout,SessionID)
