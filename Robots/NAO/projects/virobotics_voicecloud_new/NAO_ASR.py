# -*- coding: utf-8 -*-
import os
from ctypes import *
import platform
if platform.system()=="Linux":
    libfolder=os.path.split(os.path.realpath(__file__))[0]
    libpath=os.path.join(libfolder,"xunfei.so")
    xfdll=cdll.LoadLibrary(libpath)
else:
    xfdll=windll.LoadLibrary("msc.dll")
Ref=0
error_out=[False,0,""]
error_in__no_error_=[False,0,""]
naoip=""
import imp
import SpeechRecognition_Recognize
imp.reload (SpeechRecognition_Recognize)
import socket
import time
import thread
import Queue
Stringout=""
import struct
import numpy as np
def UID021E(SessionID_0220,connection_ID_023E,queue_connection_ID_024A,queue_SessionIDOut_037C,ErrorOut_0490,queue_error_out_04CB,ALLedRefOut_04F3,queue_ALLedRefOut_0561,UID0228,queue_UID0228,UID0231,error_in__no_error_,Ref,naoip,):
    i_0278=-1
    WhileS_D1S_ADS_BBS_B7_027B_Stop=False
    while WhileS_D1S_ADS_BBS_B7_027B_Stop==False:
        if ErrorOut_0490[0]== False:
            try:
                UID03CF=connection_ID_023E
                connection_ID_023E.settimeout(25)
                UID03D2=connection_ID_023E.recv(16384)
                UID0380=ErrorOut_0490
            except Exception, errorMsg:
                UID0380=[True,1,str(errorMsg)]
                UID03D2=""
                UID03CF=0
        else:
            UID0380=ErrorOut_0490
            UID03D2=""
            UID03CF=0
        UID0231=2
        
        ALLedRefOut_0561=ALLedRefOut_04F3
        if UID0380[0]== False:
            try:
                UID036C=SessionID_0220
                UID033B=c_int(0)
                UID0375=c_int(0)
                UID0328=xfdll.QISRAudioWrite(SessionID_0220,UID03D2,len(UID03D2),UID0231,byref(UID0375),byref(UID033B))
                UID033B=UID033B.value
                UID0375=UID0375.value
                if UID033B==0:
                    xfdll.QISRGetResult.restype = c_char_p
                    error_out=c_int(0)
                    rsltStatus_out=c_int(0)
                    UID0369=xfdll.QISRGetResult(SessionID_0220, byref(rsltStatus_out), Ctl_waitTime, byref(error_out))
                    if UID0369==None:
                        UID0369=""
                else:
                    UID0369=""
                UID03ED=UID0380
            except Exception, errorMsg:
                UID03ED=[True,1,str(errorMsg)]
                UID0369=""
                UID0328=0
                UID036C=""
                UID033B=0
                UID0375=0
        else:
            UID03ED=UID0380
            UID0369=""
            UID0328=0
            UID036C=""
            UID033B=0
            UID0375=0
        UID0228=UID0228+UID0369
        UID036F=UID0375==3
        SessionIDOut_037C=UID036C
        WhileS_D1S_ADS_BBS_B7_027B_Stop=UID036F
        UID0202=UID036F
        if UID0202==True:
            UID0287=1
        else: 
            UID0287=0
        
        if UID03ED[0]== False:
            try:
                UID03CC=struct.pack(['>','@','<'][2]+'i',UID0287)
                UID03C6=UID03ED
            except Exception, errorMsg:
                UID03C6=[True,1,str(errorMsg)]
                UID03E7=np.array([],dtype="int16")
                UID03CC=""
        else:
            UID03C6=UID03ED
            UID03E7=np.array([],dtype="int16")
            UID03CC=""
        if UID03C6[0]== False:
            try:
                UID024D=UID03CF
                UID03CF.settimeout(25)
                UID03CF.send(UID03CC)
                UID04C7=UID03C6
            except Exception, errorMsg:
                UID04C7=[True,1,str(errorMsg)]
                UID03C0=0
                UID024D=0
        else:
            UID04C7=UID03C6
            UID03C0=0
            UID024D=0
        error_out_04CB=UID04C7
        connection_ID_024A=UID024D
    queue_connection_ID_024A.put(connection_ID_024A)
    queue_SessionIDOut_037C.put(SessionIDOut_037C)
    queue_error_out_04CB.put(error_out_04CB)
    queue_ALLedRefOut_0561.put(ALLedRefOut_0561)
    UID0228=UID0228
    queue_UID0228.put(UID0228)
def main(error_in__no_error_,Ref,naoip):
    if error_in__no_error_[0]== False:
        try:
            connection_ID_023E=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            connection_ID_023E.settimeout(60)
            connection_ID_023E.connect((naoip,9580))
            UID0332=error_in__no_error_
        except Exception, errorMsg:
            UID0332=[True,1,str(errorMsg)]
            connection_ID_023E=0
    else:
        UID0332=error_in__no_error_
        connection_ID_023E=0
    if UID0332[0]== False:
        try:
            UID032F="seppx-wb"
            params="sub=iat,sch="+str(0)+",auf=audio/L16;rate=16000,aue="+str(UID032F)+",ent="+["sms16k","sms-en16k"][0]+",rst="+"plain"+",rse="+["gb2312","utf8"][1]+",vad_speech_tail="+str(500)+",nlp_version=3.0"
            UID031D=c_int(0)
            SessionID_0220=xfdll.QISRSessionBegin("",params,byref(UID031D))
            UID031D=UID031D.value
            UID040B=UID0332
        except Exception, errorMsg:
            UID040B=[True,1,str(errorMsg)]
            UID031D=0
            SessionID_0220=""
    else:
        UID040B=UID0332
        UID031D=0
        SessionID_0220=""
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
    queue_UID0228=Queue.Queue()
    thread.start_new_thread(UID021E,(SessionID_0220,connection_ID_023E,queue_connection_ID_024A,queue_SessionIDOut_037C,ErrorOut_0490,queue_error_out_04CB,ALLedRefOut_04F3,queue_ALLedRefOut_0561,UID0228,queue_UID0228,UID0231,error_in__no_error_,Ref,naoip,))
    connection_ID_024A=queue_connection_ID_024A.get()
    queue_connection_ID_024A.put(connection_ID_024A)
    error_out_04CB=queue_error_out_04CB.get()
    queue_error_out_04CB.put(error_out_04CB)
    if error_out_04CB[0]== False:
        try:
            connection_ID_024A.close()
            UID0742=error_out_04CB
        except Exception, errorMsg:
            UID0742=[True,1,str(errorMsg)]
            UID06C2=0
    else:
        UID0742=error_out_04CB
        UID06C2=0
    SessionIDOut_037C=queue_SessionIDOut_037C.get()
    queue_SessionIDOut_037C.put(SessionIDOut_037C)
    UID02C5=SpeechRecognition_Recognize.main(UID0742,8000,SessionIDOut_037C)
    UID052B=UID02C5[0]
    UID069A=UID02C5[1]
    UID07B3=UID02C5[2]
    UID0228=queue_UID0228.get()
    queue_UID0228.put(UID0228)
    UID0394=UID0228+UID069A
    ALLedRefOut_0561=queue_ALLedRefOut_0561.get()
    queue_ALLedRefOut_0561.put(ALLedRefOut_0561)
    if UID052B[0]== False:
        try:
            UID0528=0.000000
            UID051C=ALLedRefOut_0561
            ALLedRefOut_0561.fadeRGB("FaceLeds",16777215,UID0528)
            UID07AA=UID052B
        except Exception, errorMsg:
            UID07AA=[True,1,str(errorMsg)]
            UID051C=0
    else:
        UID07AA=UID052B
        UID051C=0
    if UID07AA[0]== False:
        try:
            UID079B=xfdll.QISRSessionEnd(UID07B3,"")
            UID0374=UID07AA
        except Exception, errorMsg:
            UID0374=[True,1,str(errorMsg)]
            UID079B=0
    else:
        UID0374=UID07AA
        UID079B=0
    if UID0374[0]== False:
        try:
            datalen=c_int(0)
            ret=c_int(0)
            xfdll.MSPSearch.restype = c_char_p
            UID00FD=xfdll.MSPSearch("nlp_version =3.0,scene = main",UID0394,byref(datalen),byref(ret))
            UID034E=datalen.value
            UID034B=ret.value
            UID03B7=UID0374
        except Exception, errorMsg:
            UID03B7=[True,1,str(errorMsg)]
            UID034B=0
            UID034E=0
            UID00FD=""
    else:
        UID03B7=UID0374
        UID034B=0
        UID034E=0
        UID00FD=""
    Stringout=UID00FD
    error_out=UID03B7
    return error_out,Stringout
if __name__ == "__main__":
    error_out,Stringout=main(error_in__no_error_,Ref,naoip)
