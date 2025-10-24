# -*- coding: utf-8 -*-
concatenated_string=""
endTimeout=1000
SessionID=""
errorCode_out=0
semantic=0
format="plain"
aue="seppx-wb"
error_out=[False,0,""]
import os
from ctypes import *
import platform
if platform.system()=="Linux":
 libfolder=os.path.split(os.path.realpath(__file__))[0]
 libpath=os.path.join(libfolder,"xunfei.so")
 xfdll=cdll.LoadLibrary(libpath)
else:
 xfdll=windll.LoadLibrary("msc.dll")
coding=0
error_in__no_error_=[False,0,""]
Language=0
def main(endTimeout,semantic,aue,error_in__no_error_,coding,format,Language):
    UID0843=["",0,0,""]
    UID024D=Language
    if UID024D==1:
    	UID0291="sms-en16k"
    else: 
    	UID0291="sms16k"
    UID0446=coding
    if UID0446==1:
    	UID044B="utf8"
    else: 
    	UID044B="gb2312"
    UID0302=" "*(0-len('%d' %semantic))+'%d' %semantic
    UID029D=" "*(0-len('%d' %endTimeout))+'%d' %endTimeout
    UID02CC="sub=iat,sch="+UID0302+",auf=audio/L16;rate=16000,aue="+aue+",ent="+UID0291+",rst="+format+",rse="+UID044B+",vad_speech_tail="+UID029D+",nlp_version=3.0"
    if error_in__no_error_[0]== False:
    	try:
    		UID00A0=""
    		UID01E4=c_int(0)
    		UID0088=xfdll.QISRSessionBegin(UID00A0,UID02CC,byref(UID01E4))
    		UID01E4=UID01E4.value
    		UID02BD=error_in__no_error_
    	except Exception, errorMsg:
    		UID02BD=[True,1,str(errorMsg)]
    		UID01E4=0
    		UID0088=""
    else:
    	UID02BD=error_in__no_error_
    	UID01E4=0
    	UID0088=""
    concatenated_string=UID02CC
    UID0298=""==UID0088
    errorCode_out=UID01E4
    SessionID=UID0088
    if UID0298==True:
    	UID0353=[True,5783,"Speech Recognition Intial Failure!"]
    	UID02E5=UID0353
    else: 
    	UID02E5=UID02BD
    error_out=UID02E5
    return error_out,errorCode_out,SessionID
if __name__ == "__main__":
    error_out,errorCode_out,SessionID=main(endTimeout,semantic,aue,error_in__no_error_,coding,format,Language)
