# -*- coding: utf-8 -*-
ErrorIn=[False,0,""]
from naoqi import ALProxy
Proxies=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
import imp
import Clear_Errors
imp.reload (Clear_Errors)
pIP="127.0.0.1"
ErrorOut=[False,0,""]
# -*- coding:utf-8 -*-
def main(ErrorIn,pIP):
    if ErrorIn[0]== False:
    	try:
    		UID034F=ALProxy("AutonomousMoves",pIP,9559)
    		UID0346=ErrorIn
    	except Exception, errorMsg:
    		UID0346=[True,1,str(errorMsg)]
    		UID034F=0
    else:
    	UID0346=ErrorIn
    	UID034F=0
    if UID0346[0]== False:
    	try:
    		UID0337=UID034F
    		UID034F.setExpressiveListeningEnabled(False)
    		UID036B=UID0346
    	except Exception, errorMsg:
    		UID036B=[True,1,str(errorMsg)]
    		UID0337=0
    else:
    	UID036B=UID0346
    	UID0337=0
    UID0374=0
    UID035C=Clear_Errors.main(UID036B,UID0374)
    UID02F8=UID035C[0]
    UID0368=UID035C[1]
    if UID02F8[0]== False:
    	try:
    		UID018C=ALProxy("ALTabletService",pIP,9559)
    		UID02D1=UID02F8
    	except Exception, errorMsg:
    		UID02D1=[True,1,str(errorMsg)]
    		UID018C=0
    else:
    	UID02D1=UID02F8
    	UID018C=0
    UID02DA=0
    UID02C2=Clear_Errors.main(UID02D1,UID02DA)
    UID0274=UID02C2[0]
    UID02CE=UID02C2[1]
    if UID0274[0]== False:
    	try:
    		UID018F=ALProxy("ALAutonomousLife",pIP,9559)
    		UID028F=UID0274
    	except Exception, errorMsg:
    		UID028F=[True,1,str(errorMsg)]
    		UID018F=0
    else:
    	UID028F=UID0274
    	UID018F=0
    UID0298=0
    UID0280=Clear_Errors.main(UID028F,UID0298)
    UID01D8=UID0280[0]
    UID028C=UID0280[1]
    if UID01D8[0]== False:
    	try:
    		UID0192=ALProxy("ALBehaviorManager",pIP,9559)
    		UID0153=UID01D8
    	except Exception, errorMsg:
    		UID0153=[True,1,str(errorMsg)]
    		UID0192=0
    else:
    	UID0153=UID01D8
    	UID0192=0
    if UID0153[0]== False:
    	try:
    		UID0195=ALProxy("ALAnimatedSpeech",pIP,9559)
    		UID0076=UID0153
    	except Exception, errorMsg:
    		UID0076=[True,1,str(errorMsg)]
    		UID0195=0
    else:
    	UID0076=UID0153
    	UID0195=0
    if UID0076[0]== False:
    	try:
    		UID0198=ALProxy("ALTextToSpeech",pIP,9559)
    		UID017A=UID0076
    	except Exception, errorMsg:
    		UID017A=[True,1,str(errorMsg)]
    		UID0198=0
    else:
    	UID017A=UID0076
    	UID0198=0
    if UID017A[0]== False:
    	try:
    		UID019B=ALProxy("ALAudioDevice",pIP,9559)
    		UID00B7=UID017A
    	except Exception, errorMsg:
    		UID00B7=[True,1,str(errorMsg)]
    		UID019B=0
    else:
    	UID00B7=UID017A
    	UID019B=0
    if UID00B7[0]== False:
    	try:
    		UID019E=ALProxy("ALMemory",pIP,9559)
    		UID0105=UID00B7
    	except Exception, errorMsg:
    		UID0105=[True,1,str(errorMsg)]
    		UID019E=0
    else:
    	UID0105=UID00B7
    	UID019E=0
    if UID0105[0]== False:
    	try:
    		UID01A1=ALProxy("ALMotion",pIP,9559)
    		UID004C=UID0105
    	except Exception, errorMsg:
    		UID004C=[True,1,str(errorMsg)]
    		UID01A1=0
    else:
    	UID004C=UID0105
    	UID01A1=0
    if UID004C[0]== False:
    	try:
    		UID01A4=ALProxy("ALSpeechRecognition",pIP,9559)
    		UID06B3=UID004C
    	except Exception, errorMsg:
    		UID06B3=[True,1,str(errorMsg)]
    		UID01A4=0
    else:
    	UID06B3=UID004C
    	UID01A4=0
    UID06BC=0
    UID04C4=Clear_Errors.main(UID06B3,UID06BC)
    UID00DE=UID04C4[0]
    UID06B0=UID04C4[1]
    if UID00DE[0]== False:
    	try:
    		UID01A7=ALProxy("ALRobotPosture",pIP,9559)
    		UID012C=UID00DE
    	except Exception, errorMsg:
    		UID012C=[True,1,str(errorMsg)]
    		UID01A7=0
    else:
    	UID012C=UID00DE
    	UID01A7=0
    if UID012C[0]== False:
    	try:
    		UID01AA=ALProxy("ALAudioPlayer",pIP,9559)
    		UID01FF=UID012C
    	except Exception, errorMsg:
    		UID01FF=[True,1,str(errorMsg)]
    		UID01AA=0
    else:
    	UID01FF=UID012C
    	UID01AA=0
    if UID01FF[0]== False:
    	try:
    		UID01AD=ALProxy("ALFaceDetection",pIP,9559)
    		UID0226=UID01FF
    	except Exception, errorMsg:
    		UID0226=[True,1,str(errorMsg)]
    		UID01AD=0
    else:
    	UID0226=UID01FF
    	UID01AD=0
    if UID0226[0]== False:
    	try:
    		UID01B0=ALProxy("ALTracker",pIP,9559)
    		UID024D=UID0226
    	except Exception, errorMsg:
    		UID024D=[True,1,str(errorMsg)]
    		UID01B0=0
    else:
    	UID024D=UID0226
    	UID01B0=0
    if UID024D[0]== False:
    	try:
    		UID01B3=ALProxy("ALNavigation",pIP,9559)
    		UID02B6=UID024D
    	except Exception, errorMsg:
    		UID02B6=[True,1,str(errorMsg)]
    		UID01B3=0
    else:
    	UID02B6=UID024D
    	UID01B3=0
    if UID02B6[0]== False:
    	try:
    		UID01B6=ALProxy("ALPhotoCapture",pIP,9559)
    		UID0392=UID02B6
    	except Exception, errorMsg:
    		UID0392=[True,1,str(errorMsg)]
    		UID01B6=0
    else:
    	UID0392=UID02B6
    	UID01B6=0
    if UID0392[0]== False:
    	try:
    		UID01B9=ALProxy("ALLeds",pIP,9559)
    		UID04B8=UID0392
    	except Exception, errorMsg:
    		UID04B8=[True,1,str(errorMsg)]
    		UID01B9=0
    else:
    	UID04B8=UID0392
    	UID01B9=0
    if UID04B8[0]== False:
    	try:
    		UID065D=ALProxy("ALMotion",pIP,9559)
    		UID09B3=UID04B8
    	except Exception, errorMsg:
    		UID09B3=[True,1,str(errorMsg)]
    		UID065D=0
    else:
    	UID09B3=UID04B8
    	UID065D=0
    UID0949=[UID018C,UID018F,UID0192,UID0195,UID0198,UID019B,UID019E,UID01A1,UID01A4,UID01A7,UID01AA,UID01AD,UID01B0,UID01B3,UID01B6,UID01B9,UID065D]
    ErrorOut=UID09B3
    Proxies=UID0949
    return ErrorOut,Proxies
if __name__ == "__main__":
    ErrorOut,Proxies=main(ErrorIn,pIP)
