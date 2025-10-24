# -*- coding: utf-8 -*-
import imp
import Clear_Errors
imp.reload (Clear_Errors)
# -*- coding:utf-8 -*-
from naoqi import ALProxy
question=""
import SpeechRecognition_Initial_Normal
imp.reload (SpeechRecognition_Initial_Normal)
Ref=0
error_out=[False,0,""]
error_in__no_error_=[False,0,""]
naoip=""
import SpeechRecognition_Close
imp.reload (SpeechRecognition_Close)
import socket
import time
import thread
import Queue
import SpeechRecognition_Recognize
imp.reload (SpeechRecognition_Recognize)
import SpeechRecognition_Write_stream
imp.reload (SpeechRecognition_Write_stream)
import struct
import numpy as np
def UID021E(SessionID_0220,connection_ID_023E,queue_connection_ID_024A,queue_SessionIDOut_037C,ErrorOut_0490,queue_error_out_04CB,ALLedRefOut_04F3,queue_ALLedRefOut_0561,ALMemoryRef_094E,queue_UID0645,UID0228,queue_UID0228,UID0231,error_in__no_error_,Ref,naoip,):
	i_0278=-1
	WhileS_D1S_ADS_BBS_B7_027B_Stop=False
	while WhileS_D1S_ADS_BBS_B7_027B_Stop==False:
		if ErrorOut_0490[0]== False:
			try:
				UID03CF=connection_ID_023E
				if 2000<0:
					connection_ID_023E.settimeout(None)
				else:
					connection_ID_023E.settimeout(2000/1000.0)
				UID03D2=connection_ID_023E.recv(16384)
				UID048F=ErrorOut_0490
			except Exception, errorMsg:
				UID048F=[True,1,str(errorMsg)]
				UID03D2=""
				UID03CF=0
		else:
			UID048F=ErrorOut_0490
			UID03D2=""
			UID03CF=0
		UID0536=ALMemoryRef_094E
		UID0591=ALMemoryRef_094E.getData("VIRobotics_Page")
		UID0231=2
		
		ALLedRefOut_0561=ALLedRefOut_04F3
		UID049C=0
		UID0178=Clear_Errors.main(UID048F,UID049C)
		UID0380=UID0178[0]
		UID048A=UID0178[1]
		if UID0591=="home":
			UID0599=False
		else: 
			UID0599=True
		UID012D=SpeechRecognition_Write_stream.main(UID0380,UID0231,UID03D2,SessionID_0220)
		UID0703=UID012D[0]
		UID0369=UID012D[1]
		UID0328=UID012D[2]
		UID036C=UID012D[3]
		UID033B=UID012D[4]
		UID0716=UID012D[5]
		UID0645=UID0599
		UID0228=UID0228+UID0369
		if UID0703[0]==True:
			UID080B=UID0703
			UID0731=True
		else: 
			UID072F=UID0716==3
			UID080B=UID0703
			UID0731=UID072F
		SessionIDOut_037C=UID036C
		UID0202=UID0731
		if UID0202==True:
			UID0287=1
		else: 
			UID0287=0
		
		if UID080B[0]== False:
			try:
				UID03CC=struct.pack(['>','@','<'][2]+'i',UID0287)
				UID03C6=UID080B
			except Exception, errorMsg:
				UID03C6=[True,1,str(errorMsg)]
				UID03E7=np.array([],dtype="int16")
				UID03CC=""
		else:
			UID03C6=UID080B
			UID03E7=np.array([],dtype="int16")
			UID03CC=""
		if UID03C6[0]== False:
			try:
				UID024D=UID03CF
				if 2000<0:
					UID03CF.settimeout(None)
				else:
					UID03CF.settimeout(2000/1000.0)
				UID03CF.send(UID03CC)
				UID03BD=UID03C6
			except Exception, errorMsg:
				UID03BD=[True,1,str(errorMsg)]
				UID03C0=0
				UID024D=0
		else:
			UID03BD=UID03C6
			UID03C0=0
			UID024D=0
		UID093D=UID03BD[0]
		error_out_04CB=UID03BD
		connection_ID_024A=UID024D
		UID0475=UID093D|UID0731
		WhileS_D1S_ADS_BBS_B7_027B=UID0475|UID0599
		WhileS_D1S_ADS_BBS_B7_027B_Stop=WhileS_D1S_ADS_BBS_B7_027B
	queue_connection_ID_024A.put(connection_ID_024A)
	queue_SessionIDOut_037C.put(SessionIDOut_037C)
	queue_error_out_04CB.put(error_out_04CB)
	queue_ALLedRefOut_0561.put(ALLedRefOut_0561)
	queue_UID0645.put(UID0645)
	UID0228=UID0228
	queue_UID0228.put(UID0228)
def main(error_in__no_error_,Ref,naoip):
    if error_in__no_error_[0]== False:
    	try:
    		ALMemoryRef_094E=ALProxy("ALMemory",naoip,9559)
    		UID06A9=error_in__no_error_
    	except Exception, errorMsg:
    		UID06A9=[True,1,str(errorMsg)]
    		ALMemoryRef_094E=0
    else:
    	UID06A9=error_in__no_error_
    	ALMemoryRef_094E=0
    if UID06A9[0]== False:
    	try:
    		connection_ID_023E=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    		connection_ID_023E.settimeout(60)
    		connection_ID_023E.connect((naoip,9580))
    		UID0332=UID06A9
    	except Exception, errorMsg:
    		UID0332=[True,1,str(errorMsg)]
    		connection_ID_023E=0
    else:
    	UID0332=UID06A9
    	connection_ID_023E=0
    UID032F="seppx-wb"
    UID0314=SpeechRecognition_Initial_Normal.main(1000,0,UID032F,UID0332,1,"plain",0)
    UID040B=UID0314[0]
    UID031D=UID0314[1]
    SessionID_0220=UID0314[2]
    if UID040B[0]== False:
    	try:
    		UID0408=0.000000
    		ALLedRefOut_04F3=Ref
    		Ref.fadeRGB("FaceLeds",16860,UID0408)
    		ErrorOut_0490=UID040B
    	except Exception, errorMsg:
    		ErrorOut_0490=[True,1,str(errorMsg)]
    		ALLedRefOut_04F3=0
    else:
    	ErrorOut_0490=UID040B
    	ALLedRefOut_04F3=0
    UID0231=1
    UID0228=""
    queue_connection_ID_024A=Queue.Queue()
    queue_SessionIDOut_037C=Queue.Queue()
    queue_error_out_04CB=Queue.Queue()
    queue_ALLedRefOut_0561=Queue.Queue()
    queue_UID0645=Queue.Queue()
    queue_UID0228=Queue.Queue()
    thread.start_new_thread(UID021E,(SessionID_0220,connection_ID_023E,queue_connection_ID_024A,queue_SessionIDOut_037C,ErrorOut_0490,queue_error_out_04CB,ALLedRefOut_04F3,queue_ALLedRefOut_0561,ALMemoryRef_094E,queue_UID0645,UID0228,queue_UID0228,UID0231,error_in__no_error_,Ref,naoip,))
    error_out_04CB=queue_error_out_04CB.get()
    queue_error_out_04CB.put(error_out_04CB)
    UID04F9=0
    UID0251=Clear_Errors.main(error_out_04CB,UID04F9)
    UID06C5=UID0251[0]
    UID04E9=UID0251[1]
    connection_ID_024A=queue_connection_ID_024A.get()
    queue_connection_ID_024A.put(connection_ID_024A)
    if UID06C5[0]== False:
    	try:
    		connection_ID_024A.close()
    		UID0580=UID06C5
    	except Exception, errorMsg:
    		UID0580=[True,1,str(errorMsg)]
    		UID06C2=0
    else:
    	UID0580=UID06C5
    	UID06C2=0
    UID0589=0
    UID056A=Clear_Errors.main(UID0580,UID0589)
    UID052B=UID056A[0]
    UID057D=UID056A[1]
    ALLedRefOut_0561=queue_ALLedRefOut_0561.get()
    queue_ALLedRefOut_0561.put(ALLedRefOut_0561)
    if UID052B[0]== False:
    	try:
    		UID0528=0.000000
    		UID051C=ALLedRefOut_0561
    		ALLedRefOut_0561.fadeRGB("FaceLeds",16777215,UID0528)
    		UID0806=UID052B
    	except Exception, errorMsg:
    		UID0806=[True,1,str(errorMsg)]
    		UID051C=0
    else:
    	UID0806=UID052B
    	UID051C=0
    UID0228=queue_UID0228.get()
    queue_UID0228.put(UID0228)
    UID07BD=UID0228
    SessionIDOut_037C=queue_SessionIDOut_037C.get()
    queue_SessionIDOut_037C.put(SessionIDOut_037C)
    UID07D8=SessionIDOut_037C
    UID0645=queue_UID0645.get()
    queue_UID0645.put(UID0645)
    UID078D=UID0645
    if UID078D==True:
    	UID0817=UID0806
    	UID07E6=""
    	UID07CA=UID07D8
    else: 
    	UID02C5=SpeechRecognition_Recognize.main(UID0806,2000,UID07D8)
    	UID06D1=UID02C5[0]
    	UID069A=UID02C5[1]
    	UID07C9=UID02C5[2]
    	UID07E5=UID07BD+UID069A
    	UID06DC=0
    	UID06B1=Clear_Errors.main(UID06D1,UID06DC)
    	UID0816=UID06B1[0]
    	UID06CE=UID06B1[1]
    	UID07CA=UID07C9
    	UID0817=UID0816
    	UID07E6=UID07E5
    question=UID07E6
    UID08E2=0
    UID08C6=Clear_Errors.main(UID0817,UID08E2)
    UID07AA=UID08C6[0]
    UID08D6=UID08C6[1]
    UID078B=SpeechRecognition_Close.main(UID07AA,UID07CA)
    UID03B7=UID078B[0]
    UID079B=UID078B[1]
    error_out=UID03B7
    return error_out,question
if __name__ == "__main__":
    error_out,question=main(error_in__no_error_,Ref,naoip)
