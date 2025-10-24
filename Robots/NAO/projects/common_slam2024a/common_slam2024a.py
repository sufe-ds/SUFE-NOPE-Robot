# -*- coding: utf-8 -*-
import numpy as np
import imp
import wait_for_boot
imp.reload (wait_for_boot)
import os
import sys
import copy
import CreateProxies
imp.reload (CreateProxies)
import time
import thread
import Queue
import Clear_Errors
imp.reload (Clear_Errors)
import getlicense
imp.reload (getlicense)
from ctypes import *
import platform
if platform.system()=="Linux":
 libfolder=os.path.split(os.path.realpath(__file__))[0]
 libpath=os.path.join(libfolder,"xunfei.so")
 xfdll=cdll.LoadLibrary(libpath)
else:
 xfdll=windll.LoadLibrary("msc.dll")
import BasicAwarenessProxy_enable
imp.reload (BasicAwarenessProxy_enable)
import readFile
imp.reload (readFile)
import readlist6
imp.reload (readlist6)
import readlist2
imp.reload (readlist2)
import NAO_ASR_Ansteel
imp.reload (NAO_ASR_Ansteel)
import get_nav_name_from_answer
imp.reload (get_nav_name_from_answer)
import random
import writeFile
imp.reload (writeFile)
import TabletServiceProxy_executeJS
imp.reload (TabletServiceProxy_executeJS)
import yiku_storagePic
imp.reload (yiku_storagePic)
import isNearTheTargetA
imp.reload (isNearTheTargetA)
import navlib
imp.reload (navlib)
import activiate_Evaluation
imp.reload (activiate_Evaluation)
import qalib
imp.reload (qalib)
import check_page
imp.reload (check_page)
import touchheadstopsay1
imp.reload (touchheadstopsay1)
import yiku_getSongLink
imp.reload (yiku_getSongLink)
import touchheadstopsay2
imp.reload (touchheadstopsay2)
import re
import local_filter
imp.reload (local_filter)
import TabletServiceProxy_getVideoLength
imp.reload (TabletServiceProxy_getVideoLength)
import touch_stop_move1
imp.reload (touch_stop_move1)
import semantic_getResult
imp.reload (semantic_getResult)
import json
import tuling_v2
imp.reload (tuling_v2)
import match6
imp.reload (match6)
import touchheadstopsay3
imp.reload (touchheadstopsay3)
def UID02C8(name_0C27,stripped_path_21B2,Proxies_11D3,UID4C7B,pIP_2392,action_0919,S_BFS_E7S_D7S_B4S_CCS_ACS_CAS_FDS_BES_DD_30D4,queue_UID02C8,):
	i_02E8=-1
	WhileS_D1S_ADS_BBS_B7_02F1_Stop=False
	while WhileS_D1S_ADS_BBS_B7_02F1_Stop==False:
		UID0351=action_0919[0]
		UID473C=np.delete(action_0919,[0])
		UID0C3E=name_0C27
		UID21A4=stripped_path_21B2
		UID1272=Proxies_11D3
		UID3F54=S_BFS_E7S_D7S_B4S_CCS_ACS_CAS_FDS_BES_DD_30D4
		UID4C4D=UID4C7B
		UID271A=pIP_2392
		if UID0351=="checkLicense":
			UID0A5D=False
			UID50D9=UID1272[4]
			UID4774=UID1272[0]
			UID5284=UID1272[1]
			try:
				UID4BF1=UID50D9
				UID50D9.setLanguage("Chinese")
				UID4BB9=[False,0,""]
			except Exception, errorMsg:
				UID4BB9=[True,1,str(errorMsg)]
				UID4BF1=0
			UID4B95=getlicense.main(UID4BB9,UID0C3E,UID271A)
			UID5083=UID4B95[0]
			UID4BD1=UID4B95[1]
			UID4BA6=UID4B95[2]
			UID49FD=copy.copy(UID3F54)
			UID49FD[5]=UID4BA6
			UID508C=0
			UID506E=Clear_Errors.main(UID5083,UID508C)
			UID4C04=UID506E[0]
			UID5080=UID506E[1]
			UID4C1C=30
			UID0405=UID4BA6
			if UID4BD1==1 or UID4BD1==2:
				UID4CC1=np.array(["login"],dtype="S")
				UID4BDF=UID4CC1
			elif UID4BD1==3:
				UID4D95=np.array(["False"],dtype="S")
				if UID4C04[0]== False:
					UID4DD6=UID4BF1
					UID4BF1.say("抱歉，您的许可证已过期。")
				UID4BDF=UID4D95
			elif UID4BD1==4:
				UID4E5A=np.array(["login"],dtype="S")
				UID4F2D="wangstoudamire@163.com"
				UID4F0F=activiate_Evaluation.main(UID4C04,UID4F2D,UID4C1C,UID0405)
				UID4F03=UID4F0F[0]
				UID4F1B=UID4F0F[1]
				UID501A=" "*(0-len('%d' %UID4C1C))+'%d' %UID4C1C
				UID4BDF=UID4E5A
				UID4F0C=0
				UID4EF4=Clear_Errors.main(UID4F03,UID4F0C)
				UID5005=UID4EF4[0]
				UID4F00=UID4EF4[1]
				UID500B="您没有许可证，我已经为您申请了"+UID501A+"天试用权。"
				if UID5005[0]== False:
					UID4FF6=UID4BF1
					UID4BF1.say(UID500B)
			else: 
				UID4C2B=np.array(["False"],dtype="S")
				if UID4C04[0]== False:
					try:
						UID4C6B=UID4BF1
						UID4BF1.say("抱歉，服务启动失败，请检查网络并重启。")
						UID483F=UID4C04
					except Exception, errorMsg:
						UID483F=[True,1,str(errorMsg)]
						UID4C6B=0
				else:
					UID483F=UID4C04
					UID4C6B=0
				UID4BDF=UID4C2B
				if UID483F[0]== False:
					try:
						UID4815=UID5284
						UID5284.setState("disabled")
						UID3FFB=UID483F
					except Exception, errorMsg:
						UID3FFB=[True,1,str(errorMsg)]
						UID4815=0
				else:
					UID3FFB=UID483F
					UID4815=0
				if UID3FFB[0]== False:
					UID3FE6=UID4774
					UID4774.showWebview("http://198.18.0.1")
			UID3E77=UID49FD
			UID095E=UID4BDF
		elif UID0351=="login":
			UID0A5D=False
			UID248E=UID1272[4]
			UID3E77=UID3F54
			try:
				UID469D=UID248E
				UID248E.setLanguage("Chinese")
				UID18BB=[False,0,""]
			except Exception, errorMsg:
				UID18BB=[True,1,str(errorMsg)]
				UID469D=0
			if UID18BB[0]== False:
				try:
					UID18A5=xfdll.MSPLogout()
					UID18D6=UID18BB
				except Exception, errorMsg:
					UID18D6=[True,1,str(errorMsg)]
					UID18A5=0
			else:
				UID18D6=UID18BB
				UID18A5=0
			UID18E0=0
			UID18C7=Clear_Errors.main(UID18D6,UID18E0)
			error_out_2B10=UID18C7[0]
			UID18D3=UID18C7[1]
			appid_4221="appid = 5948e6e8"
			queue_UID4050=Queue.Queue()
			thread.start_new_thread(UID2ABF,(error_out_2B10,queue_UID4050,appid_4221,))
			UID4050=queue_UID4050.get()
			queue_UID4050.put(UID4050)
			UID4355=UID4050
			if UID4355==True:
				UID1825=np.array(["Initial"],dtype="S")
				UID2537=UID1825
			else: 
				UID260B=np.array(["False"],dtype="S")
				UID4455=UID469D
				UID469D.say("抱歉，登录讯飞账号失败！")
				UID2537=UID260B
			UID095E=UID2537
		elif UID0351=="Initial":
			Constant_UID0D6A="Chinese"
			Constant_UID1EAF="disabled"
			UID1546=[["VIRobotics_question",""],["VIRobotics_answer",""],["VIRobotics_Page","home"],["VIRobotics_enableTalk","1"]]
			UID3DD5=np.array(["LoadMem","Readlist","Behavior","Html","Page"],dtype="S")
			UID5995=[["ENABLE_DEACTIVATION_OF_FALL_MANAGER",1.000000]]
			UID0A5D=False
			UID1D41=UID1272[1]
			UID1CE5=UID1272[7]
			UID0D27=UID1272[4]
			UID3D2B=UID1272[8]
			UID0D67=UID1272[11]
			UID3318=UID1272[0]
			UID36FF=UID1272[14]
			UID1536=UID1272[6]
			UID3E77=UID3F54
			UID095E=UID3DD5
			try:
				UID2383=UID1D41
				UID21C3=UID1D41.getState()
				UID23ED=[False,0,""]
			except Exception, errorMsg:
				UID23ED=[True,1,str(errorMsg)]
				UID21C3=""
				UID2383=0
			UID2147=Constant_UID1EAF==UID21C3
			UID243A=Constant_UID1EAF
			if UID2147==True:
				UID248D=UID23ED
			else: 
				if UID23ED[0]== False:
					try:
						UID2305=UID2383
						UID2383.setState(UID243A)
						UID2482=UID23ED
					except Exception, errorMsg:
						UID2482=[True,1,str(errorMsg)]
						UID2305=0
				else:
					UID2482=UID23ED
					UID2305=0
				UID248D=UID2482
			if UID248D[0]== False:
				try:
					UID4B1F=UID1CE5
					UID1CE5.wakeUp()
					UID4B11=UID248D
				except Exception, errorMsg:
					UID4B11=[True,1,str(errorMsg)]
					UID4B1F=0
			else:
				UID4B11=UID248D
				UID4B1F=0
			if UID4B11[0]== False:
				try:
					UID42F6=UID4B1F
					UID4B1F.setBreathEnabled("Arms",True)
					UID42ED=UID4B11
				except Exception, errorMsg:
					UID42ED=[True,1,str(errorMsg)]
					UID42F6=0
			else:
				UID42ED=UID4B11
				UID42F6=0
			if UID42ED[0]== False:
				try:
					UID2A4B=UID42F6
					UID42F6.setIdlePostureEnabled("Head",True)
					UID2A39=UID42ED
				except Exception, errorMsg:
					UID2A39=[True,1,str(errorMsg)]
					UID2A4B=0
			else:
				UID2A39=UID42ED
				UID2A4B=0
			if UID2A39[0]== False:
				try:
					UID4FF2=UID2A4B
					UID2A4B.setIdlePostureEnabled("Legs",True)
					UID4FE3=UID2A39
				except Exception, errorMsg:
					UID4FE3=[True,1,str(errorMsg)]
					UID4FF2=0
			else:
				UID4FE3=UID2A39
				UID4FF2=0
			if UID4FE3[0]== False:
				try:
					UID33A0=UID4FF2
					UID4FF2.setMotionConfig(UID5995)
					UID3390=UID4FE3
				except Exception, errorMsg:
					UID3390=[True,1,str(errorMsg)]
					UID33A0=0
			else:
				UID3390=UID4FE3
				UID33A0=0
			if UID3390[0]== False:
				try:
					UID335A=UID33A0
					UID33A0.setExternalCollisionProtectionEnabled("Arms",False)
					UID2824=UID3390
				except Exception, errorMsg:
					UID2824=[True,1,str(errorMsg)]
					UID335A=0
			else:
				UID2824=UID3390
				UID335A=0
			UID2837=0
			UID048D=Clear_Errors.main(UID2824,UID2837)
			UID0D1E=UID048D[0]
			UID2817=UID048D[1]
			if UID0D1E[0]== False:
				try:
					UID4B25=UID0D27
					UID0D27.setLanguage(Constant_UID0D6A)
					UID4ADF=UID0D1E
				except Exception, errorMsg:
					UID4ADF=[True,1,str(errorMsg)]
					UID4B25=0
			else:
				UID4ADF=UID0D1E
				UID4B25=0
			if UID4ADF[0]== False:
				try:
					UID4AC9=UID4B25
					UID4B25.setParameter("speed",90.000000)
					UID3D1F=UID4ADF
				except Exception, errorMsg:
					UID3D1F=[True,1,str(errorMsg)]
					UID4AC9=0
			else:
				UID3D1F=UID4ADF
				UID4AC9=0
			if UID3D1F[0]== False:
				try:
					UID191E=UID3D2B
					UID3D2B.setLanguage("English")
					UID1913=UID3D1F
				except Exception, errorMsg:
					UID1913=[True,1,str(errorMsg)]
					UID191E=0
			else:
				UID1913=UID3D1F
				UID191E=0
			if UID1913[0]== False:
				try:
					UID05A3=UID191E
					UID191E.setLanguage(Constant_UID0D6A)
					UID056A=UID1913
				except Exception, errorMsg:
					UID056A=[True,1,str(errorMsg)]
					UID05A3=0
			else:
				UID056A=UID1913
				UID05A3=0
			if UID056A[0]== False:
				try:
					UID0559=UID05A3
					UID05A3.setAudioExpression(False)
					UID0D57=UID056A
				except Exception, errorMsg:
					UID0D57=[True,1,str(errorMsg)]
					UID0559=0
			else:
				UID0D57=UID056A
				UID0559=0
			if UID0D57[0]== False:
				try:
					UID0D41=UID0D67
					UID0D67.subscribe(UID0C3E,100,1.000000)
					UID2407=UID0D57
				except Exception, errorMsg:
					UID2407=[True,1,str(errorMsg)]
					UID0D41=0
			else:
				UID2407=UID0D57
				UID0D41=0
			UID2378=BasicAwarenessProxy_enable.main(UID2407,True,UID271A)
			UID330F=UID2378
			if UID330F[0]== False:
				try:
					UID32FB=UID3318
					UID32F8=UID3318.setVolume(10)
					UID36F5=UID330F
				except Exception, errorMsg:
					UID36F5=[True,1,str(errorMsg)]
					UID32F8=False
					UID32FB=0
			else:
				UID36F5=UID330F
				UID32F8=False
				UID32FB=0
			if UID36F5[0]== False:
				try:
					UID3340=UID36FF
					UID36FF.setResolution(2)
					UID3330=UID36F5
				except Exception, errorMsg:
					UID3330=[True,1,str(errorMsg)]
					UID3340=0
			else:
				UID3330=UID36F5
				UID3340=0
			if UID3330[0]== False:
				try:
					UID32CD=UID3340
					UID3340.setPictureFormat("jpg")
					UID4ECA=UID3330
				except Exception, errorMsg:
					UID4ECA=[True,1,str(errorMsg)]
					UID32CD=0
			else:
				UID4ECA=UID3330
				UID32CD=0
			UID4EF9=0
			UID4DCC=Clear_Errors.main(UID4ECA,UID4EF9)
			UID152D=UID4DCC[0]
			UID4EC7=UID4DCC[1]
			if UID152D[0]== False:
				UID151E=UID1536
				UID1536.insertListData(UID1546)
		elif UID0351=="LoadMem":
			UID0A5D=False
			UID3F37=os.path.join(UID21A4,"config")
			UID4531=UID1272[6]
			UID3E77=UID3F54
			UID095E=UID473C
			UID3F6E=os.path.join(UID3F37,"qa.txt")
			UID3F81=os.path.join(UID3F37,"settings.txt")
			UID2840=os.path.join(UID3F37,"nav.txt")
			UID4A95=UID3F6E
			UID4D0B=UID3F81
			UID2891=UID2840
			UID4A8C=[False,0,""]
			UID48E1=readFile.main(UID4A8C,UID4A95)
			UID4D02=UID48E1[0]
			UID452B=UID48E1[1]
			UID4A7D=UID48E1[2]
			UID4C38=readFile.main(UID4D02,UID4D0B)
			UID287D=UID4C38[0]
			UID46A2=UID4C38[1]
			UID4CF3=UID4C38[2]
			UID285F=readFile.main(UID287D,UID2891)
			UID4528=UID285F[0]
			UID357B=UID285F[1]
			UID286D=UID285F[2]
			if UID4528[0]== False:
				try:
					UID46A8=UID4531
					UID4531.insertData("VIRobotics_qa",UID452B)
					UID469E=UID4528
				except Exception, errorMsg:
					UID469E=[True,1,str(errorMsg)]
					UID46A8=0
			else:
				UID469E=UID4528
				UID46A8=0
			if UID469E[0]== False:
				try:
					UID3585=UID46A8
					UID46A8.insertData("VIRobotics_settings",UID46A2)
					UID3573=UID469E
				except Exception, errorMsg:
					UID3573=[True,1,str(errorMsg)]
					UID3585=0
			else:
				UID3573=UID469E
				UID3585=0
			if UID3573[0]== False:
				UID3560=UID3585
				UID3585.insertData("VIRobotics_nav",UID357B)
		elif UID0351=="Readlist":
			UID0A5D=False
			UID3631=os.path.join(UID21A4,"config")
			UID095E=UID473C
			UID1EDA=os.path.join(UID3631,"qa.txt")
			UID34F3=os.path.join(UID3631,"settings.txt")
			UID3BF2=os.path.join(UID3631,"nav.txt")
			UID3421=UID1EDA
			UID37A2=UID34F3
			UID5E70=UID3BF2
			UID3416=[False,0,""]
			UID0515=readlist2.main(UID3416,UID3421)
			UID378D=UID0515[0]
			UID1E2A=UID0515[1]
			UID0507=readlist2.main(UID378D,UID37A2)
			UID5E66=UID0507[0]
			UID376B=UID0507[1]
			UID4964=UID376B.transpose()[1]
			UID063B=readlist6.main(UID5E66,UID5E70)
			UID5E1E=UID063B[0]
			UID3F85=UID063B[1]
			try:
				UID4502=UID4964[0+0]
			except:
				UID4502=""
			try:
				UID2D7A=UID4964[1+0]
			except:
				UID2D7A=""
			try:
				UID3AC1=UID4964[2+0]
			except:
				UID3AC1=""
			UID3528=copy.copy(UID3F54)
			UID3528[6]=UID1E2A
			UID3528[7]=UID376B
			UID3528[9]=UID4502
			UID3528[10]=UID2D7A
			UID3528[13]=UID3AC1
			UID3528[8]=UID3F85
			UID3E77=UID3528
		elif UID0351=="Behavior":
			Constant_UID30A3="naosoundwave/behavior_1"
			Constant_UID41AA="naocamera_http/behavior_1"
			UID0A5D=False
			UID309A=UID1272[2]
			UID3E77=UID3F54
			UID095E=UID473C
			try:
				UID30B8=UID309A
				UID30B3=UID309A.isBehaviorRunning(Constant_UID30A3)
				UID30BF=[False,0,""]
			except Exception, errorMsg:
				UID30BF=[True,1,str(errorMsg)]
				UID30B3=False
				UID30B8=0
			UID39D6=Constant_UID30A3
			if UID30B3==True:
				UID2908=UID30B8
				UID30D1=UID30BF
			else: 
				if UID30BF[0]== False:
					try:
						UID28EF=UID30B8
						UID30B8.startBehavior(UID39D6)
						UID30D5=UID30BF
					except Exception, errorMsg:
						UID30D5=[True,1,str(errorMsg)]
						UID28EF=0
				else:
					UID30D5=UID30BF
					UID28EF=0
				UID2908=UID28EF
				UID30D1=UID30D5
			UID349A=0
			UID347D=Clear_Errors.main(UID30D1,UID349A)
			UID4197=UID347D[0]
			UID348E=UID347D[1]
			if UID4197[0]== False:
				try:
					UID41C2=UID2908
					UID41BC=UID2908.isBehaviorRunning(Constant_UID41AA)
					UID41C7=UID4197
				except Exception, errorMsg:
					UID41C7=[True,1,str(errorMsg)]
					UID41BC=False
					UID41C2=0
			else:
				UID41C7=UID4197
				UID41BC=False
				UID41C2=0
			UID41D2=Constant_UID41AA
			if UID41BC==True:
				UID41D7=UID41C2
				UID41CC=UID41C7
			else: 
				if UID41C7[0]== False:
					try:
						UID41DA=UID41C2
						UID41C2.startBehavior(UID41D2)
						UID41CF=UID41C7
					except Exception, errorMsg:
						UID41CF=[True,1,str(errorMsg)]
						UID41DA=0
				else:
					UID41CF=UID41C7
					UID41DA=0
				UID41D7=UID41DA
				UID41CC=UID41CF
			UID4288=0
			UID426F=Clear_Errors.main(UID41CC,UID4288)
			UID4272=UID426F[0]
			UID427B=UID426F[1]
		elif UID0351=="Html":
			UID0A5D=False
			UID5D84=UID1272[0]
			UID5D81=UID4C4D+"/homea.html"
			UID3E77=UID3F54
			UID095E=UID473C
			try:
				UID5D64=UID5D84
				UID5D84.showWebview(UID5D81)
				UID3C1B=[False,0,""]
			except Exception, errorMsg:
				UID3C1B=[True,1,str(errorMsg)]
				UID5D64=0
			UID3C30=0
			UID3B40=Clear_Errors.main(UID3C1B,UID3C30)
			UID4FB9=UID3B40[0]
			UID3C15=UID3B40[1]
			
			UID4FB5=UID4FB9
			time.sleep(2000/1000.0)
		elif UID0351=="Page":
			UID0A5D=False
			UID31C7=UID1272[6]
			time.sleep(200/1000.0)
			UID3E77=UID3F54
			try:
				UID31A9=UID31C7
				UID31EB=UID31C7.getData("VIRobotics_Page")
				UID31D8=[False,0,""]
			except Exception, errorMsg:
				UID31D8=[True,1,str(errorMsg)]
				UID31EB=""
				UID31A9=0
			UID31F0=UID271A
			if UID31D8[0]==True:
				UID31E6="Page"
			else: 
				UID3203=UID31EB
				UID3218=UID31D8
				UID3221=UID31F0
				if UID3203=="home":
					UID3267=TabletServiceProxy_executeJS.main(UID3218,"document.getElementById('AI').style.display='none'",UID3221)
					UID32A2=UID3267
					UID320E="Face1"
					UID32AD=0
					UID328F=Clear_Errors.main(UID32A2,UID32AD)
					UID3292=UID328F[0]
					UID329D=UID328F[1]
				elif UID3203=="update":
					UID320E=UID3203
				elif UID3203=="photo":
					UID320E=UID3203
				elif UID3203=="nav":
					UID320E=UID3203
				elif UID3203=="route":
					UID320E=UID3203
				elif UID3203=="video":
					UID320E=UID3203
				elif UID3203=="refresh":
					UID320E=UID3203
				elif UID3203=="exit":
					UID320E="请退出程序"
				else: 
					UID320E="Page"
				UID31E6=UID320E
			UID3112=np.array([UID31E6])
			UID095E=UID3112
		elif UID0351=="Face1":
			UID0A5D=False
			UID10C6=UID1272[6]
			UID513E=UID1272[8]
			UID32E4=UID3F54[10]
			UID21F5=UID3F54[9]
			try:
				UID3AE8=UID10C6
				UID3B05=UID10C6.getData("FaceDetected")
				UID377C=len(UID3B05)>0
				UID35C6=[False,0,""]
			except Exception, errorMsg:
				UID35C6=[True,1,str(errorMsg)]
				UID377C=False
				UID3B05=[[0,0],[[[0.000000,0.000000,0.000000,0.000000,0.000000],[0,0.000000,"",[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000],[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000],"","",[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000],[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]]],np.array([],dtype="S")],[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000],[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000],0]
				UID3AE8=0
				UID10B1=""
			UID5DBD=UID0C3E
			UID3256=UID3F54
			if UID35C6[0]==True:
				UID3E89=UID3256
				UID3736="Page"
			else: 
				UID37D3=UID377C
				UID3B45=UID3B05
				UID3227=UID3256
				UID216F=UID21F5
				UID5128=UID513E
				UID533A=UID5DBD
				UID3BAC=UID3AE8
				UID33CF=UID32E4
				if UID37D3==True:
					UID34FF=int(time.time()*1000)
					UID3B7A=UID3B45[1][0][1][2]
					UID3D71=UID3B45[1][0][1][1]
					UID34E2=copy.copy(UID3227)
					UID34E2[0]=UID34FF
					UID09B5=UID3D71>0.600000
					UID09BC=UID3B7A!=""
					UID1F70=UID09BC&UID09B5
					UID04E3=UID3B7A
					UID0531=UID34E2
					UID0D52=UID34E2
					UID2104=UID216F
					UID3460=UID33CF
					if UID1F70==True:
						UID13FE=UID0D52[4]
						try:
							UID3B47=UID13FE.tolist().index(UID04E3)
						except:
							UID3B47=-1
						UID161C=UID3B47<0
						UID2A27=UID04E3
						UID212A=UID13FE
						UID0510=UID0531
						if UID161C==True:
							UID2945=np.concatenate((UID212A,[UID2A27]))
							UID3CEB="欢迎您！"+UID2A27
							UID33DB="Greet"
							UID0C98=np.array([UID3CEB])
							UID01E9=copy.copy(UID0510)
							UID01E9[2]=UID0C98
							UID01E9[4]=UID2945
							UID01ED=UID01E9
						else: 
							UID01ED=UID0510
							UID33DB="Xunfei"
						UID05C8=UID01ED
						UID33C7=UID33DB
					else: 
						UID2F08=UID0D52[1]
						UID212E=UID2104
						UID1BD6=UID0531
						UID34D8=UID3460
						if UID2F08==True:
							UID39A6=UID34D8+"，我是机器人"+UID212E
							UID3209="Greet"
							UID197A=np.array([UID39A6])
							UID1E1F=copy.copy(UID1BD6)
							UID1E1F[2]=UID197A
							UID1E1F[1]=False
							UID1E57=UID1E1F
						else: 
							UID1E57=UID1BD6
							UID3209="Xunfei"
						UID05C8=UID1E57
						UID33C7=UID3209
					UID3E9B=UID05C8
					UID33B2=UID33C7
				else: 
					UID1A3A=UID3227[0]
					UID3DAF=UID3227[1]
					UID33B2="Page"
					UID26DA=UID3227
					UID51B4=UID5128
					UID52D0=UID533A
					UID3D33=UID3BAC
					if UID3DAF==True:
						UID0C04=UID26DA
					else: 
						UID16B6=int(time.time()*1000)
						UID3A24=UID16B6-UID1A3A
						UID42A0=UID3A24>60000
						UID0698=UID26DA
						UID51A2=UID51B4
						UID52BE=UID52D0
						UID3D06=UID3D33
						if UID42A0==True:
							UID17EB=np.array([],dtype="S")
							UID044F=copy.copy(UID0698)
							UID044F[1]=True
							UID044F[4]=UID17EB
							UID054F=UID044F
						else: 
							UID054F=UID0698
						UID0C04=UID054F
					UID3E9B=UID0C04
				UID3E89=UID3E9B
				UID3736=UID33B2
			UID103B=np.array([UID3736])
			UID3E77=UID3E89
			UID095E=UID103B
		elif UID0351=="Greet":
			UID4DDE=[["LAnklePitch",[[1.000000,0.090464,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.090464,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.090464,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.090464,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.090464,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.090464,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.090464,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.090464,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LAnkleRoll",[[1.000000,-0.127280,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.127280,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.127280,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.127280,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LElbowRoll",[[1.000000,-0.412604,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.401866,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.401866,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.401866,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.401866,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.401866,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.401866,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.401866,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LElbowYaw",[[1.000000,-1.191960,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-1.191960,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-1.191960,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-1.191960,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-1.191960,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-1.191960,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-1.191960,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-1.191960,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LHand",[[1.000000,0.293200,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.293200,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.293200,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.293200,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.293200,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.293200,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.293200,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.293200,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LHipPitch",[[1.000000,0.122762,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.122762,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.122762,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.122762,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.122762,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.122762,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.122762,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.122762,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LHipRoll",[[1.000000,0.099752,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.104354,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.104354,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.104354,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.104354,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.104354,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.104354,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.104354,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LHipYawPitch",[[1.000000,-0.170232,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.170232,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.170232,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.170232,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LKneePitch",[[1.000000,-0.087480,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.087480,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.087480,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.087480,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.087480,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.087480,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.087480,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.087480,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LShoulderPitch",[[1.000000,1.481800,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,1.481800,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,1.481800,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,1.481800,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,1.481800,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,1.471060,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,1.471060,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,1.481800,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LShoulderRoll",[[1.000000,0.185572,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.156426,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.156426,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.142620,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.142620,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.185572,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.185572,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.174834,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LWristYaw",[[1.000000,0.110406,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.110406,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.110406,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.110406,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.110406,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.110406,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.110406,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.110406,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RAnklePitch",[[1.000000,0.092082,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.092082,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.092082,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.092082,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.092082,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.092082,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.092082,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.092082,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RAnkleRoll",[[1.000000,0.125830,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.125830,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.125830,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.125830,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.125830,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.125830,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.125830,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.125830,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RElbowRoll",[[1.000000,0.398882,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.773178,[3,-0.400000,-0.137293],[3,0.133333,0.045764]],[2.600000,0.948054,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.767042,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.957258,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.757838,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.946520,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.411154,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RElbowYaw",[[1.000000,1.179600,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,1.701160,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,1.267040,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,1.701160,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,1.267040,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,1.696560,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,1.265510,[3,-0.133333,0.017385],[3,0.400000,-0.052156]],[5.400000,1.213350,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RHand",[[1.000000,0.304800,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.752400,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.752400,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.752400,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.752400,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.745600,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.745600,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.309600,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RHipPitch",[[1.000000,0.125746,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.127280,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.127280,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.127280,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RHipRoll",[[1.000000,-0.099668,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.099668,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.099668,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.099668,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.099668,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.099668,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.099668,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.099668,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RHipYawPitch",[[1.000000,-0.170232,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.170232,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.170232,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.170232,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RKneePitch",[[1.000000,-0.091998,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.091998,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.091998,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.091998,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.091998,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.091998,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.091998,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.091998,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RShoulderPitch",[[1.000000,1.478820,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.707132,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.696394,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.696394,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.685656,[3,-0.133333,-0.010738],[3,0.133333,0.010738]],[3.800000,-0.631966,[3,-0.133333,-0.010738],[3,0.133333,0.010738]],[4.200000,-0.621228,[3,-0.133333,-0.010738],[3,0.400000,0.032214]],[5.400000,1.463480,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RShoulderRoll",[[1.000000,-0.193326,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.378940,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.107422,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.391212,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.119694,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.386610,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.148840,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.156510,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RWristYaw",[[1.000000,0.084328,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.790052,[3,-0.400000,0.156468],[3,0.133333,-0.052156]],[2.600000,-0.842208,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.822266,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.833004,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.820732,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.820732,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.082794,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]]]
			UID35A4=np.array(["Xunfei"],dtype="S")
			UID0A5D=False
			UID2D1E=UID1272[4]
			UID2BBC=UID1272[7]
			UID3F5D=UID3F54[2]
			UID3E77=UID3F54
			UID095E=UID35A4
			try:
				UID2B5F=UID2BBC
				UID4DDE_names=[]
				UID4DDE_time=[]
				UID4DDE_angle=[]
				for i in UID4DDE:
					UID4DDE_names.append(i[0])
					UID4DDE_time_one=[]
					UID4DDE_angle_one=[]
					for j in i[1]:
						UID4DDE_time_one.append(j[0])
						UID4DDE_angle_one.append([j[1],j[2],j[3]])
					UID4DDE_time.append(UID4DDE_time_one)
					UID4DDE_angle.append(UID4DDE_angle_one)
				if True==True:
					UID2BBC.post.angleInterpolationBezier(UID4DDE_names,UID4DDE_time,UID4DDE_angle)
				else:
					UID2BBC.angleInterpolationBezier(UID4DDE_names,UID4DDE_time,UID4DDE_angle)
				UID2CFB=[False,0,""]
			except Exception, errorMsg:
				UID2CFB=[True,1,str(errorMsg)]
				UID2B5F=0
			try:
				UID2D13=UID3F5D[0]
			except:
				UID2D13=""
			if UID2CFB[0]== False:
				UID2CE5=UID2D1E
				UID2D1E.say(UID2D13)
		elif UID0351=="Xunfei":
			UID0A5D=False
			UID4A5C=UID1272[15]
			UID18B5=UID1272[6]
			UID275A=UID3F54[9]
			UID4A58=[False,0,""]
			UID4972=NAO_ASR_Ansteel.main(UID4A58,UID4A5C,UID271A)
			UID2C0C=UID4972[0]
			UID4A11=UID4972[1]
			UID2D20=UID2C0C[0]
			UID1ACB=len(UID4A11)
			UID2D25=UID1ACB<9
			UID2E5D=UID2D25|UID2D20
			UID31CA=UID4A11
			UID27D4=UID271A
			UID1500=UID0C3E
			UID2B95="VIRobotics_question"
			UID2EF8=UID3F54
			if UID2E5D==True:
				UID3125=np.array(["Page"])
				UID2F5A=UID2EF8
				UID312A=UID3125
			else: 
				try:
					UID26FF=UID18B5
					UID18B5.insertData(UID2B95,UID31CA)
					UID1E36=[False,0,""]
				except Exception, errorMsg:
					UID1E36=[True,1,str(errorMsg)]
					UID26FF=0
				UID1E3F=UID2EF8[6]
				UID1E0A=qalib.main(UID1E36,UID31CA,UID1E3F)
				UID1E13=UID1E0A[0]
				UID1E24=UID1E0A[1]
				UID26E2=UID1E24==""
				UID2711=UID275A
				UID276C=UID1500
				UID279D=UID2EF8
				UID27DB=UID31CA
				UID2FF0=UID1E24
				if UID26E2==True:
					UID2E3C=local_filter.main(UID27DB)
					UID0CD7=UID2E3C
					UID0840=UID26FF
					UID2738=UID2711
					UID159A=UID276C
					UID0D05=UID279D
					UID15F1=UID27DB
					if UID0CD7=="请退出程序":
						UID0CF5=np.array([UID0CD7])
						UID23D4=UID0840
						UID0D2A=UID0D05
						UID0CF7=UID0CF5
					elif UID0CD7=="声音开大点":
						UID1F32=np.array([UID0CD7])
						UID23D4=UID0840
						UID0D2A=UID0D05
						UID0CF7=UID1F32
					elif UID0CD7=="声音开小点":
						UID1F52=np.array([UID0CD7])
						UID23D4=UID0840
						UID0D2A=UID0D05
						UID0CF7=UID1F52
					elif UID0CD7=="你叫什么名字":
						UID14D0=np.array(["Say","Page"],dtype="S")
						UID2B4F="我的名字叫"+UID2738+"，很高兴为您服务！"
						UID23D4=UID0840
						UID0CF7=UID14D0
						UID25A8=np.array([UID2B4F])
						UID2083=copy.copy(UID0D05)
						UID2083[2]=UID25A8
						UID0D2A=UID2083
					elif UID0CD7=="握手":
						UID0304=np.array(["Motion"])
						UID1AF2=np.array(["shakehand"])
						UID23D4=UID0840
						UID030F=copy.copy(UID0D05)
						UID030F[2]=UID1AF2
						UID0CF7=UID0304
						UID0D2A=UID030F
					elif UID0CD7=="跳舞":
						UID4389=np.array(["dance"],dtype="S")
						UID43B8=np.array(["littleapple","gangnamstyle","thriller","eagledance","taiji","caravanpalace","flamengo","vangelisdance","GetLucky","happyheart"],dtype="S")
						UID421F=copy.copy(UID0D05)
						UID421F[2]=UID43B8
						UID23D4=UID0840
						UID0CF7=UID4389
						UID0D2A=UID421F
					elif UID0CD7=="小苹果":
						UID45F7=np.array(["dance"],dtype="S")
						UID473A=np.array(["littleapple"],dtype="S")
						UID45A7=copy.copy(UID0D05)
						UID45A7[2]=UID473A
						UID23D4=UID0840
						UID0CF7=UID45F7
						UID0D2A=UID45A7
					elif UID0CD7=="骑马舞":
						UID48A7=np.array(["dance"],dtype="S")
						UID4887=np.array(["gangnamstyle"],dtype="S")
						UID4867=copy.copy(UID0D05)
						UID4867[2]=UID4887
						UID23D4=UID0840
						UID0CF7=UID48A7
						UID0D2A=UID4867
					elif UID0CD7=="太空舞":
						UID4A13=np.array(["dance"],dtype="S")
						UID49E8=np.array(["thriller"],dtype="S")
						UID49AB=copy.copy(UID0D05)
						UID49AB[2]=UID49E8
						UID23D4=UID0840
						UID0CF7=UID4A13
						UID0D2A=UID49AB
					elif UID0CD7=="飞鹰舞":
						UID4BDA=np.array(["dance"],dtype="S")
						UID4B8B=np.array(["eagledance"],dtype="S")
						UID4B64=copy.copy(UID0D05)
						UID4B64[2]=UID4B8B
						UID23D4=UID0840
						UID0CF7=UID4BDA
						UID0D2A=UID4B64
					elif UID0CD7=="太极舞":
						UID4E6C=np.array(["dance"],dtype="S")
						UID4DC8=np.array(["taiji"],dtype="S")
						UID4D87=copy.copy(UID0D05)
						UID4D87[2]=UID4DC8
						UID23D4=UID0840
						UID0CF7=UID4E6C
						UID0D2A=UID4D87
					elif UID0CD7=="大篷车":
						UID50D8=np.array(["dance"],dtype="S")
						UID50A8=np.array(["caravanpalace"],dtype="S")
						UID505C=copy.copy(UID0D05)
						UID505C[2]=UID50A8
						UID23D4=UID0840
						UID0CF7=UID50D8
						UID0D2A=UID505C
					elif UID0CD7=="西班牙舞蹈":
						UID521C=np.array(["dance"],dtype="S")
						UID51F3=np.array(["flamengo"],dtype="S")
						UID51C4=copy.copy(UID0D05)
						UID51C4[2]=UID51F3
						UID23D4=UID0840
						UID0CF7=UID521C
						UID0D2A=UID51C4
					elif UID0CD7=="范吉利斯":
						UID5355=np.array(["dance"],dtype="S")
						UID532F=np.array(["vangelisdance"],dtype="S")
						UID5307=copy.copy(UID0D05)
						UID5307[2]=UID532F
						UID23D4=UID0840
						UID0CF7=UID5355
						UID0D2A=UID5307
					elif UID0CD7=="祝你好运":
						UID54B3=np.array(["dance"],dtype="S")
						UID5490=np.array(["GetLucky"],dtype="S")
						UID5470=copy.copy(UID0D05)
						UID5470[2]=UID5490
						UID23D4=UID0840
						UID0CF7=UID54B3
						UID0D2A=UID5470
					elif UID0CD7=="快乐的心":
						UID560B=np.array(["dance"],dtype="S")
						UID55EB=np.array(["happyheart"],dtype="S")
						UID55CB=copy.copy(UID0D05)
						UID55CB[2]=UID55EB
						UID23D4=UID0840
						UID0CF7=UID560B
						UID0D2A=UID55CB
					elif UID0CD7=="参观":
						UID46B8=np.array(["Say","JS","Page"],dtype="S")
						UID4673=np.array(["好的，请大家跟在我的身边。","routeOne()"],dtype="S")
						UID4640=copy.copy(UID0D05)
						UID4640[2]=UID4673
						UID23D4=UID0840
						UID0CF7=UID46B8
						UID0D2A=UID4640
					else: 
						try:
							datalen=c_int(0)
							ret=c_int(0)
							xfdll.MSPSearch.restype = c_char_p
							UID0384=xfdll.MSPSearch("nlp_version =3.0,scene = main",UID15F1,byref(datalen),byref(ret))
							UID0347=datalen.value
							UID031D=ret.value
							UID38ED=[False,0,""]
						except Exception, errorMsg:
							UID38ED=[True,1,str(errorMsg)]
							UID031D=0
							UID0347=0
							UID0384=""
						UID23D4=UID0840
						UID1B21=UID0384!=""
						UID3924=0
						UID38C9=Clear_Errors.main(UID38ED,UID3924)
						UID38D6=UID38C9[0]
						UID38E7=UID38C9[1]
						UID1B47=UID0D05
						UID203B=UID0CD7
						UID1D02=UID0384
						UID163A=UID159A
						if UID1B21==True:
							try:
								UID2CAC=json.loads(UID1D02)
								UID2C54=0
								UID2C4E=0
								UID2CA3=[False,0,""]
							except Exception, errorMsg:
								UID2CA3=[True,1,str(errorMsg)]
								UID2C4E=0
								UID2C54=0
								UID2CAC=None
							UID2C83=semantic_getResult.main(UID2CA3,UID2CAC)
							UID1821=UID2C83[0]
							UID182F=UID2C83[1]
							UID1851=UID1B47
							UID1686=UID163A
							if UID1821[0]==True:
								UID1957=np.array(["Page"],dtype="S")
								UID1862=UID1851
								UID1840=UID1957
							else: 
								UID0BA0=match6.main(UID1686,UID182F)
								UID183F=UID0BA0[0]
								UID0F4E=UID0BA0[1]
								UID3239=UID0BA0[2]
								UID1861=copy.copy(UID1851)
								UID1861[2]=UID3239
								UID1861[12]=UID0F4E
								UID1840=UID183F
								UID1862=UID1861
							UID1B53=UID1862
							UID1B3B=UID1840
						else: 
							UID2413=np.array(["AnimatedSay","Page"],dtype="S")
							try:
								try:
									UID23FA=UID203B.encode('utf-8')
								except:
									UID23FA=UID203B
								UID23D6=[False,0,""]
							except Exception, errorMsg:
								UID23D6=[True,1,str(errorMsg)]
								UID23FA=""
							UID1B3B=UID2413
							UID23DE='{"city": "上海","province": "上海","street": "五角场"}'
							UID04E4=tuling_v2.main("e0bada8cf5fb4afc81292ccc47fef250",UID23D6,UID23DE,UID163A,UID23FA)
							UID1EC6=UID04E4[0]
							UID2637=UID04E4[1]
							UID138A=UID04E4[2]
							UID1ECF=0
							UID1EB4=Clear_Errors.main(UID1EC6,UID1ECF)
							UID1EB8=UID1EB4[0]
							UID1EC3=UID1EB4[1]
							UID1ED7="**"+UID2637
							UID20FF=np.array([UID1ED7])
							UID1B51=copy.copy(UID1B47)
							UID1B51[2]=UID20FF
							UID1B53=UID1B51
						UID0D2A=UID1B53
						UID0CF7=UID1B3B
					UID273C=UID23D4
					UID2724=UID0CF7
					UID26F2=UID0D2A
				else: 
					UID364C=np.array(["AnimatedSay","Page"],dtype="S")
					UID3160=np.array([UID2FF0])
					UID273C=UID26FF
					UID2724=UID364C
					UID26EF=copy.copy(UID279D)
					UID26EF[2]=UID3160
					UID26F2=UID26EF
				UID2044=[False,0,""]
				UID2019=check_page.main(UID2044,UID27D4,UID273C,UID2724)
				UID2023=UID2019[0]
				UID311F=UID2019[1]
				UID2F5A=UID26F2
				UID312A=UID311F
			UID3E77=UID2F5A
			UID095E=UID312A
		elif UID0351=="AnimatedSay":
			UID0A5D=False
			UID55A7=UID1272[4]
			UID5587=UID1272[3]
			UID5617=UID1272[6]
			UID4A27=UID3F54[2]
			try:
				UID55DC=UID473C[0]
			except:
				UID55DC=""
			UID4A22=UID4A27[0]
			UID4B62=np.delete(UID4A27,[0])
			UID31DA=copy.copy(UID3F54)
			UID31DA[2]=UID4B62
			UID4F6A=[False,0,""]
			UID4ED2=get_nav_name_from_answer.main(UID4F6A,UID4A22)
			UID5DF2=UID4ED2[0]
			UID5528=UID4ED2[1]
			UID5CF3=UID4ED2[2]
			UID59AF=UID473C
			UID5B55=UID4A22
			if UID5528==True:
				UID64A5=np.array(["nav"],dtype="S")
				if UID5DF2[0]== False:
					try:
						UID6770=UID5617
						UID5617.insertData("VIRobotics_nav_button",UID5CF3)
						UID6767=UID5DF2
					except Exception, errorMsg:
						UID6767=[True,1,str(errorMsg)]
						UID6770=0
				else:
					UID6767=UID5DF2
					UID6770=0
				UID20C3="setNavDest('"+UID5CF3+"')"
				UID5AC8=UID64A5
				if UID6767[0]== False:
					try:
						UID6B5C=UID6770
						UID6770.insertData("VIRobotics_Page","nav")
						UID6B4F=UID6767
					except Exception, errorMsg:
						UID6B4F=[True,1,str(errorMsg)]
						UID6B5C=0
				else:
					UID6B4F=UID6767
					UID6B5C=0
				if UID6B4F[0]== False:
					try:
						UID6B3F=UID6B5C
						UID6B5C.insertData("VIRobotics_answer",UID5B55)
						UID1FA5=UID6B4F
					except Exception, errorMsg:
						UID1FA5=[True,1,str(errorMsg)]
						UID6B3F=0
				else:
					UID1FA5=UID6B4F
					UID6B3F=0
				UID115D=TabletServiceProxy_executeJS.main(UID1FA5,UID20C3,"127.0.0.1")
				UID6E4D=UID115D
				
				time.sleep(500/1000.0)
				UID6E48=UID6E4D
			else: 
				if UID5DF2[0]== False:
					try:
						UID0FB5=UID5587
						if True==True:
							UID5587.post.say(UID5B55,"contextual")
						else:
							UID5587.say(UID5B55,"contextual")
						UID3068=UID5DF2
					except Exception, errorMsg:
						UID3068=[True,1,str(errorMsg)]
						UID0FB5=0
				else:
					UID3068=UID5DF2
					UID0FB5=0
				UID5AC8=UID59AF
				UID24E4=UID55DC
				UID6FD9=UID5B55
				if UID24E4=="Music":
					UID17A4=UID6FD9+"<font color = '#ff8000'>（长按头部停止唱歌）</font>"
					UID312F=UID3068
					UID17AA=UID17A4
				else: 
					UID1B76=len(UID6FD9)
					UID312F=UID3068
					UID1A5A=UID1B76>100
					UID70B3=UID6FD9
					if UID1A5A==True:
						UID2025="<font color = '#ff8000'>（长按头部停止回答）</font>"+UID70B3
						UID2029=UID2025
					else: 
						UID2029=UID70B3
					UID17AA=UID2029
				if UID312F[0]== False:
					try:
						UID1BB5=UID5617
						UID5617.insertData("VIRobotics_answer",UID17AA)
						UID365E=UID312F
					except Exception, errorMsg:
						UID365E=[True,1,str(errorMsg)]
						UID1BB5=0
				else:
					UID365E=UID312F
					UID1BB5=0
				UID366E=0
				UID1308=Clear_Errors.main(UID365E,UID366E)
				UID2263=UID1308[0]
				UID365B=UID1308[1]
				
				time.sleep(1000/1000.0)
				UID225F=UID2263
				UID1B8D=touchheadstopsay1.main(UID225F,UID1BB5)
				UID1CE3=UID1B8D[0]
				UID1B9A=UID1B8D[1]
				UID1B9D=UID1B8D[2]
				UID1CEE=0
				UID1CCC=Clear_Errors.main(UID1CE3,UID1CEE)
				UID1C81=UID1CCC[0]
				UID1CDE=UID1CCC[1]
				if UID1C81[0]== False:
					UID1C60=UID55A7
					UID55A7.stopAll()
			UID3E77=UID31DA
			UID095E=UID5AC8
		elif UID0351=="Say":
			UID0A5D=False
			UID1D74=UID1272[4]
			UID2338=UID1272[6]
			UID1AD9=UID3F54[2]
			UID095E=UID473C
			UID1AD5=UID1AD9[0]
			UID1AEC=np.delete(UID1AD9,[0])
			UID1A19=copy.copy(UID3F54)
			UID1A19[2]=UID1AEC
			try:
				UID230F=UID2338
				UID2338.insertData("VIRobotics_answer",UID1AD5)
				UID1D67=[False,0,""]
			except Exception, errorMsg:
				UID1D67=[True,1,str(errorMsg)]
				UID230F=0
			if UID1D67[0]== False:
				UID1D58=UID1D74
				UID1D74.say(UID1AD5)
			UID3E77=UID1A19
		elif UID0351=="Music":
			UID4628=np.array(["move1.py","move2.py","move3.py","move4.py"],dtype="S")
			UID0A5D=False
			TextToSpeechRef_208E=UID1272[4]
			ALMemoryRef_3829=UID1272[6]
			ALMotionRef_3836=UID1272[7]
			AudioPlayer_381A=UID1272[10]
			UID49A6=UID1272[9]
			appended_path_2C82=os.path.join(UID21A4,"movements")
			UID010E=UID3F54[2]
			musicSource_2BC2=UID3F54[12]
			UID3E77=UID3F54
			UID095E=UID473C
			UID2AF8=UID4628
			UID2E50=np.array([],dtype="S")
			i_2910=-1
			ForS_D1S_ADS_BBS_B7_28F3_IndexsIn=[]
			ForS_D1S_ADS_BBS_B7_28F3_IndexsIn.append(len(UID2AF8))
			ForS_D1S_ADS_BBS_B7_28F3_Indexmin=min(ForS_D1S_ADS_BBS_B7_28F3_IndexsIn)
			ForS_D1S_ADS_BBS_B7_28F3_count=ForS_D1S_ADS_BBS_B7_28F3_Indexmin
			for i in range(0, ForS_D1S_ADS_BBS_B7_28F3_count):
				i_2910=i_2910+1
				UID2E4B=os.path.join(appended_path_2C82,UID2AF8[i_2910])
				UID2E50=np.concatenate((UID2E50,[UID2E4B]))
			UID1F78=len(UID010E)
			UID1248=UID1F78-1
			UID3843=UID2E50
			content_0045=UID010E
			queue_error_out_37F8=Queue.Queue()
			thread.start_new_thread(UID0DC6,(queue_error_out_37F8,AudioPlayer_381A,ALMemoryRef_3829,ALMotionRef_3836,UID3843,content_0045,UID1248,TextToSpeechRef_208E,musicSource_2BC2,))
			error_out_37F8=queue_error_out_37F8.get()
			queue_error_out_37F8.put(error_out_37F8)
			if error_out_37F8[0]== False:
				UID498E=UID49A6
				UID498B=UID49A6.goToPosture("Stand",0.500000)
		elif UID0351=="dance":
			UID2E2C=random.random()
			UID3760=np.array(["dancemusic"],dtype="S")
			UID0A5D=False
			UID2D09=os.path.join(UID21A4,"movements")
			UID2BED=UID1272[7]
			UID2C39=UID1272[9]
			UID2F8C=UID1272[6]
			UID2E0B=UID3F54[2]
			UID095E=UID3760
			UID2C95=UID2D09
			UID2E27=len(UID2E0B)
			try:
				UID2F28=UID2F8C
				UID2F8C.insertData("VIRobotics_answer","<font color = '#ff8000'>（长按头部停止舞蹈）</font>")
				UID2DC1=[False,0,""]
			except Exception, errorMsg:
				UID2DC1=[True,1,str(errorMsg)]
				UID2F28=0
			UID2E3D=np.floor((UID2E2C*int(UID2E27)))
			UID2E9E=int(UID2E3D)
			try:
				UID2E93=UID2E0B[UID2E9E+0]
			except:
				UID2E93=""
			UID2F02=UID2C95+"/"+UID2E93+".mp3"
			UID2DDF=UID2E93+".py"
			UID2DD2=os.path.join(UID2D09,UID2DDF)
			UID2EDD=np.array([UID2F02])
			if UID2DC1[0]== False:
				try:
					pythonmodulefolder,pythonmodepath=os.path.split(UID2DD2)
					pythonmodule=pythonmodepath[:pythonmodepath.find(".")]
					imp_bbb=pythonmodulefolder+"/"+pythonmodule
					imp_ccc=imp.find_module(pythonmodule,[pythonmodulefolder])
					imp_ddd=imp.load_module(imp_bbb,imp_ccc[0],imp_ccc[1],imp_ccc[2])
					imp_eee=imp_ddd.main()
					UID2C36=imp_eee[0]
					UID2C41=imp_eee[1]
					UID2DB1=imp_eee[2]
					UID2C30=UID2DC1
				except Exception, errorMsg:
					UID2C30=[True,1,str(errorMsg)]
					UID2C36=""
					UID2C41=0
					UID2DB1=[]
			else:
				UID2C30=UID2DC1
				UID2C36=""
				UID2C41=0
				UID2DB1=[]
			if UID2C30[0]== False:
				try:
					UID2C33=0.800000
					UID2C1E=UID2C39
					UID2C1A=UID2C39.goToPosture(UID2C36,UID2C33)
					UID2BD8=UID2C30
				except Exception, errorMsg:
					UID2BD8=[True,1,str(errorMsg)]
					UID2C1A=False
					UID2C1E=0
			else:
				UID2BD8=UID2C30
				UID2C1A=False
				UID2C1E=0
			try:
				UID2D43=UID2DB1[0]
			except:
				UID2D43=["",[]]
			if UID2BD8[0]== False:
				try:
					UID2BBB=UID2BED
					UID2DB1_names=[]
					UID2DB1_time=[]
					UID2DB1_angle=[]
					for i in UID2DB1:
						UID2DB1_names.append(i[0])
						UID2DB1_time_one=[]
						UID2DB1_angle_one=[]
						for j in i[1]:
							UID2DB1_time_one.append(j[0])
							UID2DB1_angle_one.append([j[1],j[2],j[3]])
						UID2DB1_time.append(UID2DB1_time_one)
						UID2DB1_angle.append(UID2DB1_angle_one)
					if True==True:
						UID2BED.post.angleInterpolationBezier(UID2DB1_names,UID2DB1_time,UID2DB1_angle)
					else:
						UID2BED.angleInterpolationBezier(UID2DB1_names,UID2DB1_time,UID2DB1_angle)
					UID2C45=UID2BD8
				except Exception, errorMsg:
					UID2C45=[True,1,str(errorMsg)]
					UID2BBB=0
			else:
				UID2C45=UID2BD8
				UID2BBB=0
			UID2D46=UID2D43[1]
			
			time.sleep(int(UID2C41)/1000.0)
			UID2C4D=UID2C45
			UID2D57=len(UID2D46)
			UID2D62=UID2D57-1
			try:
				UID2D69=UID2D46[UID2D62+0]
			except:
				UID2D69=[0.000000,0.000000,[0,0.000000,0.000000],[0,0.000000,0.000000]]
			UID2D78=UID2D69[0]
			UID2D91=UID2D78*1000.000000
			UID2EE1=int(UID2D91)
			UID2917=copy.copy(UID3F54)
			UID2917[2]=UID2EDD
			UID2917[3]=UID2EE1
			UID3E77=UID2917
		elif UID0351=="dancemusic":
			millisecond_timer_value_3AC4=int(time.time()*1000)
			UID3D89=np.array(["Page"],dtype="S")
			UID0A5D=False
			ALMemoryRef_3AB8=UID1272[6]
			UID3D00=UID1272[7]
			UID3AA1=UID1272[9]
			UID3A0F=UID1272[10]
			UID3A33=UID1272[8]
			UID3D7B=UID3F54[2]
			musicTime_3ACB=UID3F54[3]
			UID3E77=UID3F54
			UID095E=UID3D89
			try:
				UID3A0B=UID3D7B[0]
			except:
				UID3A0B=""
			try:
				UID3CC3=UID3A0F
				if True==True:
					UID3A0F.post.playFile(UID3A0B)
				else:
					UID3A0F.playFile(UID3A0B)
				UID3D17=[False,0,""]
			except Exception, errorMsg:
				UID3D17=[True,1,str(errorMsg)]
				UID3CC3=0
			
			time.sleep(2000/1000.0)
			UID3D23=UID3D17
			ErrorOut_3AB4=UID3D23
			queue_ErrorOut_2419=Queue.Queue()
			thread.start_new_thread(UID3AB1,(ErrorOut_3AB4,ALMemoryRef_3AB8,millisecond_timer_value_3AC4,musicTime_3ACB,queue_ErrorOut_2419,))
			ErrorOut_2419=queue_ErrorOut_2419.get()
			queue_ErrorOut_2419.put(ErrorOut_2419)
			if ErrorOut_2419[0]== False:
				try:
					UID3CA0=UID3CC3
					UID3CC3.stopAll()
					UID3CE7=ErrorOut_2419
				except Exception, errorMsg:
					UID3CE7=[True,1,str(errorMsg)]
					UID3CA0=0
			else:
				UID3CE7=ErrorOut_2419
				UID3CA0=0
			if UID3CE7[0]== False:
				try:
					UID3CD3=UID3D00
					UID3D00.killAll()
					UID3A97=UID3CE7
				except Exception, errorMsg:
					UID3A97=[True,1,str(errorMsg)]
					UID3CD3=0
			else:
				UID3A97=UID3CE7
				UID3CD3=0
			if UID3A97[0]== False:
				try:
					UID3A88=UID3AA1
					UID3A85=UID3AA1.goToPosture("Stand",0.600000)
					UID3A4E=UID3A97
				except Exception, errorMsg:
					UID3A4E=[True,1,str(errorMsg)]
					UID3A85=False
					UID3A88=0
			else:
				UID3A4E=UID3A97
				UID3A85=False
				UID3A88=0
			UID3A5B=0
			UID3A39=Clear_Errors.main(UID3A4E,UID3A5B)
			UID3A3C=UID3A39[0]
			UID3A49=UID3A39[1]
		elif UID0351=="JS":
			UID0A5D=False
			content_22AB=UID3F54[2]
			UID3E77=UID3F54
			UID095E=UID473C
			pIP_2245=UID271A
			i_2232=-1
			ForS_D1S_ADS_BBS_B7_2208_IndexsIn=[]
			ForS_D1S_ADS_BBS_B7_2208_IndexsIn.append(len(content_22AB))
			ForS_D1S_ADS_BBS_B7_2208_Indexmin=min(ForS_D1S_ADS_BBS_B7_2208_IndexsIn)
			ForS_D1S_ADS_BBS_B7_2208_count=ForS_D1S_ADS_BBS_B7_2208_Indexmin
			for i in range(0, ForS_D1S_ADS_BBS_B7_2208_count):
				i_2232=i_2232+1
				UID176F=[False,0,""]
				UID1751=TabletServiceProxy_executeJS.main(UID176F,content_22AB[i_2232],pIP_2245)
				UID2252=UID1751
				error_out_2253=UID2252
			UID1796=0
			UID177D=Clear_Errors.main(error_out_2253,UID1796)
			UID179B=UID177D[0]
			UID178A=UID177D[1]
			
			UID17A1=UID179B
			time.sleep(1000/1000.0)
		elif UID0351=="update":
			UID2B63=np.array(["Readlist","Say","Page"],dtype="S")
			UID290A=np.array(["更新完成"],dtype="S")
			UID0A5D=False
			UID43A5=UID1272[6]
			UID3771=os.path.join(UID21A4,"config")
			UID21CA=copy.copy(UID3F54)
			UID21CA[2]=UID290A
			UID095E=UID2B63
			UID37A0=os.path.join(UID3771,"qa.txt")
			UID37E3=os.path.join(UID3771,"settings.txt")
			try:
				UID3D5F=UID43A5
				UID4840=UID43A5.getData("VIRobotics_qa")
				UID3D41=[False,0,""]
			except Exception, errorMsg:
				UID3D41=[True,1,str(errorMsg)]
				UID4840=""
				UID3D5F=0
			UID4F44=os.path.join(UID3771,"nav.txt")
			UID3E77=UID21CA
			UID4843=UID37A0
			UID2C24=UID37E3
			if UID3D41[0]== False:
				try:
					UID38CF=UID3D5F
					UID2C19=UID3D5F.getData("VIRobotics_settings")
					UID38BB=UID3D41
				except Exception, errorMsg:
					UID38BB=[True,1,str(errorMsg)]
					UID2C19=""
					UID38CF=0
			else:
				UID38BB=UID3D41
				UID2C19=""
				UID38CF=0
			UID4A3F=UID4F44
			if UID38BB[0]== False:
				try:
					UID282D=UID38CF
					UID4A3B=UID38CF.getData("VIRobotics_nav")
					UID483A=UID38BB
				except Exception, errorMsg:
					UID483A=[True,1,str(errorMsg)]
					UID4A3B=""
					UID282D=0
			else:
				UID483A=UID38BB
				UID4A3B=""
				UID282D=0
			UID2B35=writeFile.main(UID483A,UID4840,UID4843)
			UID2BFD=UID2B35[0]
			UID2B51=UID2B35[1]
			UID2B5C=writeFile.main(UID2BFD,UID2C19,UID2C24)
			UID4A1A=UID2B5C[0]
			UID2BA6=UID2B5C[1]
			UID3885=writeFile.main(UID4A1A,UID4A3B,UID4A3F)
			UID2818=UID3885[0]
			UID49E2=UID3885[1]
			if UID2818[0]== False:
				try:
					UID2788=UID282D
					UID282D.insertData("VIRobotics_Page","home")
					UID28BC=UID2818
				except Exception, errorMsg:
					UID28BC=[True,1,str(errorMsg)]
					UID2788=0
			else:
				UID28BC=UID2818
				UID2788=0
			UID288B=TabletServiceProxy_executeJS.main(UID28BC,"getSlamIP()",UID271A)
			UID2B71=UID288B
			UID2B8F=0
			UID29A7=Clear_Errors.main(UID2B71,UID2B8F)
			UID2B43=UID29A7[0]
			UID2B61=UID29A7[1]
		elif UID0351=="photo":
			Constant_UID4303="photo"
			UID496D=np.array(["JS","Page"],dtype="S")
			UID0A5D=False
			UID3E40=UID1272[10]
			UID42FE=UID1272[14]
			UID4299=UID1272[6]
			UID4339=UID21A4
			UID095E=UID496D
			try:
				UID4262=UID4299
				UID4299.insertData("VIRobotics_Page","wait")
				UID42F2=[False,0,""]
			except Exception, errorMsg:
				UID42F2=[True,1,str(errorMsg)]
				UID4262=0
			UID4341=UID4339+"/html/pictures"
			UID3E3D=UID4339+"/sounds/picture.mp3"
			if UID42F2[0]== False:
				try:
					UID42CE=UID42FE
					UID42CA=UID42FE.takePicture(UID4341,Constant_UID4303)
					UID26E5=UID42F2
				except Exception, errorMsg:
					UID26E5=[True,1,str(errorMsg)]
					UID42CA=np.array([],dtype="S")
					UID42CE=0
			else:
				UID26E5=UID42F2
				UID42CA=np.array([],dtype="S")
				UID42CE=0
			UID26FC=UID4341+"/"+Constant_UID4303+".jpg"
			UID26F3="common"
			UID26A3=yiku_storagePic.main(UID26E5,UID26F3,UID26FC)
			UID2A6D=UID26A3[0]
			UID3025=UID26A3[1]
			UID2A96=0
			UID295B=Clear_Errors.main(UID2A6D,UID2A96)
			UID3E37=UID295B[0]
			UID2A5B=UID295B[1]
			UID323D="showPhoto('"+UID3025+"')"
			UID3964=np.array([UID323D])
			if UID3E37[0]== False:
				UID3E3A=False
				UID3E26=UID3E40
				if UID3E3A==True:
					UID3E40.post.playFile(UID3E3D)
				else:
					UID3E40.playFile(UID3E3D)
			UID3770=copy.copy(UID3F54)
			UID3770[2]=UID3964
			UID3E77=UID3770
		elif UID0351=="Motion":
			UID25CD=np.array(["Page"],dtype="S")
			UID0A5D=False
			UID369A=UID1272[7]
			UID3762=UID1272[4]
			UID2719=UID1272[9]
			UID2CD7=UID1272[6]
			UID2A74=UID3F54[2]
			UID3E77=UID3F54
			UID095E=UID25CD
			try:
				UID28E0=UID2A74[0]
			except:
				UID28E0=""
			if UID28E0=="shakehand":
				Constant_UID2DDA="要握手吗？好啊好啊！很高兴认识你！"
				UID2EAC=[["HeadPitch",[[0.040000,-0.193282,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,-0.193282,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,-0.193282,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,-0.193282,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,-0.193282,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,-0.193282,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[3.400000,-0.193281,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.193281,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,-0.193281,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[4.400000,-0.193281,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,-0.193281,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,-0.193281,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["HeadYaw",[[0.040000,0.012272,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,-0.006136,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,-0.006136,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,-0.006136,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,-0.006136,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,-0.006136,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[3.400000,-0.006136,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.006136,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,-0.006136,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[4.400000,-0.006136,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,-0.006136,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,-0.006136,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["HipPitch",[[0.040000,-0.024544,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,-0.024544,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,-0.024544,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,-0.009204,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,-0.009204,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,-0.009204,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[3.400000,-0.009204,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.009204,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,-0.009204,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[4.400000,-0.009204,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,-0.009204,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,-0.009204,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["HipRoll",[[0.040000,-0.018408,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,-0.007670,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,-0.007670,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,-0.007670,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,-0.007670,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,-0.007670,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[3.400000,-0.007670,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.007670,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,-0.007670,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[4.400000,-0.007670,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,-0.007670,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,-0.007670,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["KneePitch",[[0.040000,0.010738,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,-0.001534,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,-0.001534,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,-0.001534,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,-0.001534,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,-0.001534,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[3.400000,-0.001534,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.001534,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,-0.001534,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[4.400000,-0.001534,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,-0.001534,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,-0.001534,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["LElbowRoll",[[0.040000,-0.526155,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,-0.526155,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,-0.526155,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,-0.526155,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,-0.526155,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,-0.526155,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[3.400000,-0.526156,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.526156,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,-0.526156,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[4.400000,-0.526156,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,-0.526156,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,-0.526156,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["LElbowYaw",[[0.040000,-1.230250,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,-1.217980,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,-1.217980,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,-1.217980,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,-1.217980,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,-1.217980,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[3.400000,-1.217980,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-1.217980,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,-1.217980,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[4.400000,-1.217980,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,-1.217980,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,-1.217980,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["LHand",[[0.040000,0.607206,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,0.607206,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,0.607206,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,0.607206,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,0.607206,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,0.607206,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[3.400000,0.607206,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.607206,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,0.607206,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[4.400000,0.607206,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,0.607206,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,0.607206,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["LShoulderPitch",[[0.040000,1.563130,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,1.570800,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,1.570800,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,1.570800,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,1.570800,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,1.570800,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[3.400000,1.570800,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,1.570800,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,1.570800,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[4.400000,1.570800,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,1.570800,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,1.570800,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["LShoulderRoll",[[0.040000,0.139592,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,0.121185,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,0.121185,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,0.121185,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,0.121185,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,0.121185,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[3.400000,0.121185,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.121185,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,0.121185,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[4.400000,0.121185,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,0.121185,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,0.121185,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["LWristYaw",[[0.040000,0.019900,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,0.019900,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,0.019900,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,0.019900,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,0.019900,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,0.019900,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[3.400000,0.019900,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.019900,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,0.019900,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[4.400000,0.019900,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,0.019900,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,0.019900,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["RElbowRoll",[[0.040000,0.524621,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,0.616660,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,0.616660,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,0.730175,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,0.625864,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,0.635068,[3,-0.066667,-0.009204],[3,0.133333,0.018408]],[3.400000,0.730174,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.625865,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,0.635068,[3,-0.066667,-0.009203],[3,0.133333,0.018406]],[4.400000,0.730174,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,0.625865,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,0.635068,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["RElbowYaw",[[0.040000,1.234850,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,1.234850,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,1.234850,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,1.242520,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,1.242520,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,1.242520,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[3.400000,1.242520,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,1.242520,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,1.242520,[3,-0.066667,0.000000],[3,0.133333,0.000000]],[4.400000,1.242520,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,1.242520,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,1.242520,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["RHand",[[0.040000,0.594903,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,0.736380,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,0.736380,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,0.652900,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,0.728471,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,0.719684,[3,-0.066667,0.008397],[3,0.133333,-0.016794]],[3.400000,0.652900,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.728471,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,0.719684,[3,-0.066667,0.008397],[3,0.133333,-0.016794]],[4.400000,0.652900,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,0.728471,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,0.719684,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["RShoulderPitch",[[0.040000,1.570800,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,0.521554,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,0.521554,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,0.311398,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,0.509282,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,0.501612,[3,-0.066667,0.007670],[3,0.133333,-0.015340]],[3.400000,0.311398,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.509282,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,0.501611,[3,-0.066667,0.007671],[3,0.133333,-0.015341]],[4.400000,0.311398,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,0.509282,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,0.501611,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["RShoulderRoll",[[0.040000,-0.151864,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,-0.150330,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,-0.150330,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,-0.104311,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,-0.139592,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,-0.133456,[3,-0.066667,-0.003920],[3,0.133333,0.007840]],[3.400000,-0.104311,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.139592,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,-0.133456,[3,-0.066667,-0.003920],[3,0.133333,0.007840]],[4.400000,-0.104311,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,-0.139592,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,-0.133456,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]],["RWristYaw",[[0.040000,-0.019984,[3,-0.013333,0.000000],[3,0.386667,0.000000]],[1.200000,0.115008,[3,-0.386667,0.000000],[3,0.266667,0.000000]],[2.000000,0.115008,[3,-0.266667,0.000000],[3,0.133333,0.000000]],[2.400000,0.191708,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[2.800000,0.154892,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[3.000000,0.176368,[3,-0.066667,-0.004091],[3,0.133333,0.008182]],[3.400000,0.191709,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.154892,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[4.000000,0.176367,[3,-0.066667,-0.004091],[3,0.133333,0.008181]],[4.400000,0.191709,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.800000,0.154892,[3,-0.133333,0.000000],[3,0.066667,0.000000]],[5.000000,0.176367,[3,-0.066667,0.000000],[3,0.000000,0.000000]]]]]
				try:
					UID2A79=UID2CD7
					UID2CD7.insertData("VIRobotics_answer",Constant_UID2DDA)
					UID2E8B=[False,0,""]
				except Exception, errorMsg:
					UID2E8B=[True,1,str(errorMsg)]
					UID2A79=0
				if UID2E8B[0]== False:
					try:
						UID2E7C=UID369A
						UID2EAC_names=[]
						UID2EAC_time=[]
						UID2EAC_angle=[]
						for i in UID2EAC:
							UID2EAC_names.append(i[0])
							UID2EAC_time_one=[]
							UID2EAC_angle_one=[]
							for j in i[1]:
								UID2EAC_time_one.append(j[0])
								UID2EAC_angle_one.append([j[1],j[2],j[3]])
							UID2EAC_time.append(UID2EAC_time_one)
							UID2EAC_angle.append(UID2EAC_angle_one)
						if True==True:
							UID369A.post.angleInterpolationBezier(UID2EAC_names,UID2EAC_time,UID2EAC_angle)
						else:
							UID369A.angleInterpolationBezier(UID2EAC_names,UID2EAC_time,UID2EAC_angle)
						UID2E3A=UID2E8B
					except Exception, errorMsg:
						UID2E3A=[True,1,str(errorMsg)]
						UID2E7C=0
				else:
					UID2E3A=UID2E8B
					UID2E7C=0
				if UID2E3A[0]== False:
					UID2E1F=UID3762
					UID3762.say(Constant_UID2DDA)
			else: 
				pass
		elif UID0351=="nav":
			UID4C57=np.array(["JS","Page"],dtype="S")
			UID435E=np.array(["backToHome()"],dtype="S")
			UID0A5D=False
			UID5A1D=UID3F54[8]
			UID45CD=UID1272[4]
			UID4710=UID1272[3]
			UID53DF=UID1272[0]
			UID57D3=UID1272[6]
			UID4812=copy.copy(UID3F54)
			UID4812[2]=UID435E
			UID4560=[False,0,""]
			UID44DA=BasicAwarenessProxy_enable.main(UID4560,False,UID271A)
			UID57CA=UID44DA
			UID095E=UID4C57
			if UID57CA[0]== False:
				try:
					UID47E9=UID57D3
					UID57B8=UID57D3.getData("VIRobotics_nav_button")
					UID5A14=UID57CA
				except Exception, errorMsg:
					UID5A14=[True,1,str(errorMsg)]
					UID57B8=""
					UID47E9=0
			else:
				UID5A14=UID57CA
				UID57B8=""
				UID47E9=0
			UID3E77=UID4812
			UID59F3=navlib.main(UID5A14,UID57B8,UID5A1D)
			UID4702=UID59F3[0]
			UID45A8=UID59F3[1]
			UID454D=UID59F3[2]
			UID5A05=UID59F3[3]
			UID5A08=UID59F3[4]
			UID5A0E=UID59F3[5]
			UID5CD2="navigationByName('"+UID5A05+"')"
			if UID4702[0]== False:
				try:
					UID450C=UID4710
					if True==True:
						UID4710.post.say(UID5A08,"disabled")
					else:
						UID4710.say(UID5A08,"disabled")
					UID5CCC=UID4702
				except Exception, errorMsg:
					UID5CCC=[True,1,str(errorMsg)]
					UID450C=0
			else:
				UID5CCC=UID4702
				UID450C=0
			UID5CAD=TabletServiceProxy_executeJS.main(UID5CCC,UID5CD2,UID271A)
			UID47EC=UID5CAD
			UID47C6=isNearTheTargetA.main(UID47E9,UID47EC,0.500000,UID5A05,UID271A)
			UID45EC=UID47C6[0]
			UID470E=UID47C6[1]
			UID4711=UID47C6[2]
			UID4601=UID47C6[3]
			UID449A=UID4711|UID470E
			UID4538=UID57B8
			UID4637=UID271A
			UID5382=UID5A08
			if UID449A==True:
				UID5565=UID45EC
				
				time.sleep(1000/1000.0)
				UID5685=UID5565
				UID4D76=TabletServiceProxy_executeJS.main(UID5685,"cancelNav(null)",UID4637)
				UID46D8=UID4D76
				UID2049=TabletServiceProxy_executeJS.main(UID46D8,"stopWaitForNear()",UID4637)
				UID4D43=UID2049
				if UID4D43[0]== False:
					UID4D34=UID4601
					UID4601.insertData("VIRobotics_Page","home")
			else: 
				Constant_UID3603="','"
				UID31B4="changeSlide('"+UID4538+Constant_UID3603+UID454D+Constant_UID3603+UID5382+UID45A8+"')"
				UID31A2=[False,0,""]
				UID3175=TabletServiceProxy_executeJS.main(UID31A2,UID31B4,UID4637)
				UID3903=UID3175
				if UID3903[0]== False:
					try:
						UID38E5=UID450C
						if True==True:
							UID450C.post.say(UID45A8,"contextual")
						else:
							UID450C.say(UID45A8,"contextual")
						UID3B16=UID3903
					except Exception, errorMsg:
						UID3B16=[True,1,str(errorMsg)]
						UID38E5=0
				else:
					UID3B16=UID3903
					UID38E5=0
				
				time.sleep(1000/1000.0)
				UID3B0A=UID3B16
				UID3AE9=0
				UID3A81=Clear_Errors.main(UID3B0A,UID3AE9)
				UID43B5=UID3A81[0]
				UID3AB6=UID3A81[1]
				UID4233=touchheadstopsay2.main(UID43B5,UID4601)
				UID44D0=UID4233[0]
				UID4249=UID4233[1]
				UID4261=UID4233[2]
				UID48DA=UID4233[3]
				if UID44D0[0]== False:
					try:
						UID3A03=UID45CD
						UID45CD.stopAll()
						UID554C=UID44D0
					except Exception, errorMsg:
						UID554C=[True,1,str(errorMsg)]
						UID3A03=0
				else:
					UID554C=UID44D0
					UID3A03=0
				
				time.sleep(1000/1000.0)
				UID5548=UID554C
				if UID5548[0]== False:
					try:
						UID39A3=UID3A03
						UID3A03.stopAll()
						UID48CD=UID5548
					except Exception, errorMsg:
						UID48CD=[True,1,str(errorMsg)]
						UID39A3=0
				else:
					UID48CD=UID5548
					UID39A3=0
				if UID48CD[0]== False:
					UID4894=UID48DA
					UID48DA.insertData("VIRobotics_Page","home")
		elif UID0351=="route":
			UID5A46=np.array(["route_go"],dtype="S")
			UID0A5D=False
			UID5591=UID1272[6]
			UID4BE6=[False,0,""]
			UID4B56=BasicAwarenessProxy_enable.main(UID4BE6,False,UID271A)
			UID5581=UID4B56
			UID095E=UID5A46
			if UID5581[0]== False:
				UID5572=UID5591
				string_5F01=UID5591.getData("VIRobotics_route")
			queue_UID5EFB=Queue.Queue()
			queue_UID5F0A=Queue.Queue()
			thread.start_new_thread(UID5E89,(queue_UID5EFB,queue_UID5F0A,string_5F01,))
			UID5EFB=queue_UID5EFB.get()
			queue_UID5EFB.put(UID5EFB)
			UID5F0A=queue_UID5F0A.get()
			queue_UID5F0A.put(UID5F0A)
			UID5F81=UID5EFB[UID5F0A]
			UID5644=np.delete(UID5EFB,[UID5F0A])
			UID552D=copy.copy(UID3F54)
			UID552D[2]=UID5644
			UID3E77=UID552D
		elif UID0351=="route_go":
			UID66B4=np.array(["route_over"],dtype="S")
			UID0A5D=False
			ALMemoryRef_516A=UID1272[6]
			AnimatedSpeechRef_61B7=UID1272[3]
			TextToSpeechRef_62F9=UID1272[4]
			datalist3_3832=UID3F54[8]
			content_6E36=UID3F54[2]
			UID3E77=UID3F54
			UID095E=UID66B4
			pIP_6EBE=UID271A
			i_6C6C=-1
			ForS_D1S_ADS_BBS_B7_5408_Stop=False
			ForS_D1S_ADS_BBS_B7_6C5A_IndexsIn=[]
			ForS_D1S_ADS_BBS_B7_6C5A_IndexsIn.append(len(content_6E36))
			ForS_D1S_ADS_BBS_B7_6C5A_Indexmin=min(ForS_D1S_ADS_BBS_B7_6C5A_IndexsIn)
			ForS_D1S_ADS_BBS_B7_6C5A_count=ForS_D1S_ADS_BBS_B7_6C5A_Indexmin
			while ForS_D1S_ADS_BBS_B7_5408_Stop==False and i_6C6C<ForS_D1S_ADS_BBS_B7_6C5A_count-1:
				i_6C6C=i_6C6C+1
				UID6F2D=[False,0,""]
				UID360E=navlib.main(UID6F2D,content_6E36[i_6C6C],datalist3_3832)
				UID5BAA=UID360E[0]
				UID5DBB=UID360E[1]
				UID5D26=UID360E[2]
				UID3679=UID360E[3]
				UID367C=UID360E[4]
				UID6A64=UID360E[5]
				UID4077="navigationByName('"+UID3679+"')"
				if UID5BAA[0]== False:
					try:
						UID5688=AnimatedSpeechRef_61B7
						if True==True:
							AnimatedSpeechRef_61B7.post.say(UID367C,"disabled")
						else:
							AnimatedSpeechRef_61B7.say(UID367C,"disabled")
						UID4061=UID5BAA
					except Exception, errorMsg:
						UID4061=[True,1,str(errorMsg)]
						UID5688=0
				else:
					UID4061=UID5BAA
					UID5688=0
				UID3FFC=TabletServiceProxy_executeJS.main(UID4061,UID4077,pIP_6EBE)
				UID54D2=UID3FFC
				UID5440=isNearTheTargetA.main(ALMemoryRef_516A,UID54D2,0.500000,UID3679,pIP_6EBE)
				UID550A=UID5440[0]
				UID71C6=UID5440[1]
				UID580C=UID5440[2]
				UID48EE=UID5440[3]
				UID531D=TextToSpeechRef_62F9
				UID3C54=content_6E36[i_6C6C]
				UID4A6C=pIP_6EBE
				UID59AC=UID367C
				if UID71C6==True:
					UID58EE=UID550A
					
					time.sleep(1000/1000.0)
					UID58F2=UID58EE
					UID552C=True
					UID46E7=TabletServiceProxy_executeJS.main(UID58F2,"cancelNav(null)",UID4A6C)
					UID5897=UID46E7
					UID36A3=TabletServiceProxy_executeJS.main(UID5897,"stopWaitForNear()",UID4A6C)
					UID4D20=UID36A3
					if UID4D20[0]== False:
						UID4CFE=UID531D
						UID531D.say("任务终止。")
				else: 
					UID567D=UID580C
					UID46CD=UID3C54
					UID477B=UID5D26
					UID4911=UID5DBB
					UID4A5A=UID4A6C
					UID5875=UID5688
					UID4858=UID48EE
					UID52FC=UID531D
					UID5D8D=UID550A
					UID6A52=UID6A64
					UID5996=UID59AC
					if UID567D==True:
						UID52FB="跳过："+UID46CD
						UID5C89=UID5D8D
						
						time.sleep(1000/1000.0)
						UID5C8D=UID5C89
						UID59BA=False
						UID4F73=TabletServiceProxy_executeJS.main(UID5C8D,"cancelNav(null)",UID4A5A)
						UID6E25=UID4F73
						UID52D8=UID52FC
						UID52FC.say(UID52FB)
						UID275C=TabletServiceProxy_executeJS.main(UID6E25,"stopWaitForNear()",UID4A5A)
						UID6E0D=UID275C
					else: 
						Constant_UID6058="','"
						UID6018="changeSlide('"+UID46CD+Constant_UID6058+UID477B+Constant_UID6058+UID5996+UID4911+"')"
						UID6012=[False,0,""]
						UID5FF1=TabletServiceProxy_executeJS.main(UID6012,UID6018,UID4A5A)
						UID53FE=UID5FF1
						if UID53FE[0]== False:
							try:
								UID53EE=UID5875
								if True==True:
									UID5875.post.say(UID4911,"contextual")
								else:
									UID5875.say(UID4911,"contextual")
								UID549E=UID53FE
							except Exception, errorMsg:
								UID549E=[True,1,str(errorMsg)]
								UID53EE=0
						else:
							UID549E=UID53FE
							UID53EE=0
						
						time.sleep(1000/1000.0)
						UID5492=UID549E
						UID5483=0
						UID5460=Clear_Errors.main(UID5492,UID5483)
						UID3F65=UID5460[0]
						UID5471=UID5460[1]
						UID3F23=touchheadstopsay2.main(UID3F65,UID4858)
						UID4FA3=UID3F23[0]
						UID5C46=UID3F23[1]
						UID3E42=UID3F23[2]
						UID5A0D=UID3F23[3]
						UID4FAC=0
						UID4F90=Clear_Errors.main(UID4FA3,UID4FAC)
						UID4D89=UID4F90[0]
						UID4FA0=UID4F90[1]
						if UID4D89[0]== False:
							UID514C=UID52FC
							UID52FC.stopAll()
						UID588B=UID4A5A
						UID673A=UID46CD
						UID6AE3=UID6A52
						if UID5C46==True:
							UID68D2=[False,0,""]
							UID5BA6=TabletServiceProxy_executeJS.main(UID68D2,"cancelNav(null)",UID588B)
							UID5EE6=UID5BA6
							UID5EE4=True
							
							time.sleep(1000/1000.0)
							UID5EE1=UID5EE6
							if UID5EE1[0]== False:
								try:
									UID5D49=UID514C
									UID514C.stopAll()
									UID5D40=UID5EE1
								except Exception, errorMsg:
									UID5D40=[True,1,str(errorMsg)]
									UID5D49=0
							else:
								UID5D40=UID5EE1
								UID5D49=0
							if UID5D40[0]== False:
								UID5D2E=UID5D49
								UID5D49.say("任务终止。")
						else: 
							UID3FFF=UID3E42
							UID5132=UID514C
							UID5910=UID588B
							UID5B1E=UID673A
							UID5AB5=UID5A0D
							UID6B58=UID6AE3
							if UID3FFF==True:
								UID55C3=[False,0,""]
								UID3719=TabletServiceProxy_executeJS.main(UID55C3,"cancelNav(null)",UID5910)
								UID638B=UID3719
								UID4CBF="跳过："+UID5B1E
								
								time.sleep(1000/1000.0)
								UID623C=UID638B
								UID6238=UID638B
								if UID6238[0]== False:
									UID4CA8=UID5132
									UID5132.say(UID4CBF)
							else: 
								Constant_UID56DD="VIRobotics_route_pause"
								try:
									UID5D00=UID5AB5
									UID5AB5.insertData(Constant_UID56DD,"1")
									UID5768=[False,0,""]
								except Exception, errorMsg:
									UID5768=[True,1,str(errorMsg)]
									UID5D00=0
								UID5778="waitForNextNav("+UID6B58+")"
								UID572B=TabletServiceProxy_executeJS.main(UID5768,UID5778,UID5910)
								UID5CF7=UID572B
								UID5C31=touchheadstopsay3.main(UID5CF7,Constant_UID56DD,UID5D00)
								UID5CDF=UID5C31[0]
								UID57DD=UID5C31[1]
								UID57E1=UID5C31[2]
								UID5CE8=UID5C31[3]
								UID57EA=UID57E1|UID57DD
								UID57EF=UID5910
								UID57F4="goNextNav()"
								if UID57EA==True:
									UID582F=[False,0,""]
									UID580A=TabletServiceProxy_executeJS.main(UID582F,UID57F4,UID57EF)
									UID580E=UID580A
								else: 
									pass
							UID5EE4=False
						UID59BA=UID5EE4
					UID552C=UID59BA
				ForS_D1S_ADS_BBS_B7_5408_Stop=UID552C
		elif UID0351=="route_over":
			UID5B85=np.array(["JS","Page"],dtype="S")
			UID63AA=np.array(["backToHome()"],dtype="S")
			UID0A5D=False
			UID70FB=UID1272[6]
			UID64D8=copy.copy(UID3F54)
			UID64D8[2]=UID63AA
			UID095E=UID5B85
			UID5AE2=UID70FB
			UID70FB.insertData("VIRobotics_Page","wait")
			UID3E77=UID64D8
		elif UID0351=="video":
			UID381E=np.array(["Page"],dtype="S")
			UID0A5D=False
			UID3BE4=UID1272[6]
			UID40E3=UID1272[0]
			UID3E77=UID3F54
			UID095E=UID381E
			try:
				UID416A=UID3BE4
				UID55D9=UID3BE4.getData("VIRobotics_video_name")
				UID40D8=[False,0,""]
			except Exception, errorMsg:
				UID40D8=[True,1,str(errorMsg)]
				UID55D9=""
				UID416A=0
			UID40E0=UID4C4D+"/videos/"+UID55D9
			if UID40D8[0]== False:
				try:
					UID4151=UID40E3
					UID40B6=UID40E3.playVideo(UID40E0)
					UID4156=UID40D8
				except Exception, errorMsg:
					UID4156=[True,1,str(errorMsg)]
					UID40B6=False
					UID4151=0
			else:
				UID4156=UID40D8
				UID40B6=False
				UID4151=0
			UID4163=UID271A
			if UID4156[0]==True:
				UID51D6=UID416A
				UID416F=UID4156
			else: 
				millisecond_timer_value_4190=int(time.time()*1000)
				pIP_44DB=UID4163
				error_IO_44E3=UID4156
				queue_ms_44DF=Queue.Queue()
				queue_error_out_44E7=Queue.Queue()
				thread.start_new_thread(UID44D9,(pIP_44DB,queue_ms_44DF,error_IO_44E3,queue_error_out_44E7,))
				RefOut_41A1=UID416A
				error_out_44E7=queue_error_out_44E7.get()
				queue_error_out_44E7.put(error_out_44E7)
				error_out_41B7=error_out_44E7
				ms_44DF=queue_ms_44DF.get()
				queue_ms_44DF.put(ms_44DF)
				ms_41E0=ms_44DF
				queue_ErrorOut_4184=Queue.Queue()
				queue_RefOut_514B=Queue.Queue()
				thread.start_new_thread(UID417E,(queue_ErrorOut_4184,millisecond_timer_value_4190,RefOut_41A1,error_out_41B7,ms_41E0,queue_RefOut_514B,))
				RefOut_514B=queue_RefOut_514B.get()
				queue_RefOut_514B.put(RefOut_514B)
				UID51D6=RefOut_514B
				ErrorOut_4184=queue_ErrorOut_4184.get()
				queue_ErrorOut_4184.put(ErrorOut_4184)
				UID416F=ErrorOut_4184
			UID4128=0
			UID4105=Clear_Errors.main(UID416F,UID4128)
			UID4148=UID4105[0]
			UID4117=UID4105[1]
			if UID4148[0]== False:
				try:
					UID4139=UID4151
					UID4136=UID4151.stopVideo()
					UID40F7=UID4148
				except Exception, errorMsg:
					UID40F7=[True,1,str(errorMsg)]
					UID4136=False
					UID4139=0
			else:
				UID40F7=UID4148
				UID4136=False
				UID4139=0
			UID4102=0
			UID40E6=Clear_Errors.main(UID40F7,UID4102)
			UID574E=UID40E6[0]
			UID40F4=UID40E6[1]
			if UID574E[0]== False:
				UID573F=UID51D6
				UID51D6.insertData("VIRobotics_Page","home")
		elif UID0351=="refresh":
			UID4FD0=np.array(["Page"],dtype="S")
			UID0A5D=False
			UID6002=UID1272[0]
			UID5A22=UID1272[6]
			UID530C=UID4C4D+"/homea.html"
			UID3E77=UID3F54
			UID095E=UID4FD0
			try:
				UID59CF=UID5A22
				UID5A22.insertData("VIRobotics_Page","home")
				UID5FF0=[False,0,""]
			except Exception, errorMsg:
				UID5FF0=[True,1,str(errorMsg)]
				UID59CF=0
			if UID5FF0[0]== False:
				try:
					UID4F46=UID6002
					UID6002.hideWebview()
					UID518D=UID5FF0
				except Exception, errorMsg:
					UID518D=[True,1,str(errorMsg)]
					UID4F46=0
			else:
				UID518D=UID5FF0
				UID4F46=0
			
			time.sleep(2000/1000.0)
			UID550E=UID518D
			UID539B=UID518D
			UID5085=UID4F46
			if UID550E[0]== False:
				try:
					UID52D9=UID5085
					UID5085.showWebview(UID530C)
					UID5E09=UID550E
				except Exception, errorMsg:
					UID5E09=[True,1,str(errorMsg)]
					UID52D9=0
			else:
				UID5E09=UID550E
				UID52D9=0
			
			UID5E02=UID5E09
			time.sleep(1000/1000.0)
		elif UID0351=="声音开大点":
			UID25C9=np.array(["Say","Page"],dtype="S")
			UID2140=np.array(["声音已经开大"],dtype="S")
			UID0A5D=False
			UID269C=UID1272[5]
			UID1FA4=copy.copy(UID3F54)
			UID1FA4[2]=UID2140
			UID095E=UID25C9
			UID20E2=UID269C
			UID269C.setOutputVolume(80)
			UID3E77=UID1FA4
		elif UID0351=="声音开小点":
			UID27EB=np.array(["Say","Page"],dtype="S")
			UID27BC=np.array(["声音已经开小"],dtype="S")
			UID0A5D=False
			UID27AF=UID1272[5]
			UID2224=copy.copy(UID3F54)
			UID2224[2]=UID27BC
			UID095E=UID27EB
			UID2790=UID27AF
			UID27AF.setOutputVolume(50)
			UID3E77=UID2224
		elif UID0351=="请退出程序":
			Constant_UID39E8="即将退出程序"
			UID24BE=np.array(["上海仪酷"],dtype="S")
			UID37CA=np.array([],dtype="S")
			UID2B03=UID1272[1]
			UID1DAF=UID1272[11]
			UID412B=UID1272[0]
			UID346F=UID1272[4]
			UID22A2=UID1272[8]
			UID253A=UID1272[6]
			UID3E77=UID3F54
			UID0A5D=True
			UID095E=UID37CA
			try:
				UID41A6=UID253A
				UID253A.insertData("VIRobotics_Page","exit")
				UID2298=[False,0,""]
			except Exception, errorMsg:
				UID2298=[True,1,str(errorMsg)]
				UID41A6=0
			if UID2298[0]== False:
				try:
					UID23AF=UID22A2
					UID22A2.setLanguage("English")
					UID23A3=UID2298
				except Exception, errorMsg:
					UID23A3=[True,1,str(errorMsg)]
					UID23AF=0
			else:
				UID23A3=UID2298
				UID23AF=0
			if UID23A3[0]== False:
				try:
					UID21E3=UID23AF
					UID23AF.setLanguage("Chinese")
					UID21D3=UID23A3
				except Exception, errorMsg:
					UID21D3=[True,1,str(errorMsg)]
					UID21E3=0
			else:
				UID21D3=UID23A3
				UID21E3=0
			if UID21D3[0]== False:
				try:
					UID21D7=False
					UID21BB=UID21E3
					UID21E3.setVocabulary(UID24BE.tolist(),UID21D7)
					UID391D=UID21D3
				except Exception, errorMsg:
					UID391D=[True,1,str(errorMsg)]
					UID21BB=0
			else:
				UID391D=UID21D3
				UID21BB=0
			UID384E=BasicAwarenessProxy_enable.main(UID391D,False,UID271A)
			UID4175=UID384E
			if UID4175[0]== False:
				try:
					UID413B=UID41A6
					UID41A6.insertData("VIRobotics_answer",Constant_UID39E8)
					UID3463=UID4175
				except Exception, errorMsg:
					UID3463=[True,1,str(errorMsg)]
					UID413B=0
			else:
				UID3463=UID4175
				UID413B=0
			if UID3463[0]== False:
				try:
					UID3405=UID346F
					UID346F.say(Constant_UID39E8)
					UID40DB=UID3463
				except Exception, errorMsg:
					UID40DB=[True,1,str(errorMsg)]
					UID3405=0
			else:
				UID40DB=UID3463
				UID3405=0
			if UID40DB[0]== False:
				try:
					UID3578=UID412B
					UID412B.hideImage()
					UID3B63=UID40DB
				except Exception, errorMsg:
					UID3B63=[True,1,str(errorMsg)]
					UID3578=0
			else:
				UID3B63=UID40DB
				UID3578=0
			UID3B76=0
			UID2D85=Clear_Errors.main(UID3B63,UID3B76)
			UID3527=UID2D85[0]
			UID3B5F=UID2D85[1]
			if UID3527[0]== False:
				try:
					UID3509=UID3578
					UID3578.hideWebview()
					UID4088=UID3527
				except Exception, errorMsg:
					UID4088=[True,1,str(errorMsg)]
					UID3509=0
			else:
				UID4088=UID3527
				UID3509=0
			UID40E7=0
			UID4009=Clear_Errors.main(UID4088,UID40E7)
			UID1DA3=UID4009[0]
			UID4066=UID4009[1]
			if UID1DA3[0]== False:
				try:
					UID1D94=UID1DAF
					UID1DAF.unsubscribe(UID0C3E)
					UID2AEF=UID1DA3
				except Exception, errorMsg:
					UID2AEF=[True,1,str(errorMsg)]
					UID1D94=0
			else:
				UID2AEF=UID1DA3
				UID1D94=0
			if UID2AEF[0]== False:
				try:
					UID2AD6=UID2B03
					UID2B03.setState("solitary")
					UID0EEA=UID2AEF
				except Exception, errorMsg:
					UID0EEA=[True,1,str(errorMsg)]
					UID2AD6=0
			else:
				UID0EEA=UID2AEF
				UID2AD6=0
			if UID0EEA[0]== False:
				UID0ED9=xfdll.MSPLogout()
		else: 
			UID3884=np.array([""],dtype="S")
			UID3E77=UID3F54
			UID0A5D=True
			UID095E=UID3884
		WhileS_D1S_ADS_BBS_B7_02F1_Stop=UID0A5D
		S_BFS_E7S_D7S_B4S_CCS_ACS_CAS_FDS_BES_DD_30D4=UID3E77
		
		action_0919=UID095E
		
	queue_UID02C8.put(1)
def UID2ABF(error_out_2B10,queue_UID4050,appid_4221,):
	i_2AF1=-1
	WhileS_D1S_ADS_BBS_B7_2AFA_Stop=False
	while WhileS_D1S_ADS_BBS_B7_2AFA_Stop==False:
		i_2AF1=i_2AF1+1
		if error_out_2B10[0]== False:
			try:
				UID1891=""
				UID1896=""
				UID23B4=xfdll.MSPLogin(UID1896,UID1891,appid_4221)
				UID220C=error_out_2B10
			except Exception, errorMsg:
				UID220C=[True,1,str(errorMsg)]
				UID23B4=0
		else:
			UID220C=error_out_2B10
			UID23B4=0
		UID3E5D=i_2AF1>=2
		UID221A=0
		UID21E7=Clear_Errors.main(UID220C,UID221A)
		UID21EF=UID21E7[0]
		UID2207=UID21E7[1]
		if UID23B4==0:
			UID26BA=True
		else: 
			time.sleep(3000/1000.0)
			UID26BA=False
		WhileS_D1S_ADS_BBS_B7_2AFA=UID26BA|UID3E5D
		UID4050=UID26BA
		WhileS_D1S_ADS_BBS_B7_2AFA_Stop=WhileS_D1S_ADS_BBS_B7_2AFA
	queue_UID4050.put(UID4050)
def UID0DC6(queue_error_out_37F8,AudioPlayer_381A,ALMemoryRef_3829,ALMotionRef_3836,UID3843,content_0045,UID1248,TextToSpeechRef_208E,musicSource_2BC2,):
	i_37C6=-1
	WhileS_D1S_ADS_BBS_B7_37D0_Stop=False
	while WhileS_D1S_ADS_BBS_B7_37D0_Stop==False:
		i_37C6=i_37C6+1
		try:
			UID2A67=content_0045[i_37C6+0]
		except:
			UID2A67=""
		UID20F6=i_37C6>=UID1248
		UID2A55=[False,0,""]
		UID294D=yiku_getSongLink.main(UID2A55,musicSource_2BC2,UID2A67)
		UID0DFF=UID294D[0]
		UID0EAE=UID294D[1]
		UID0E3A=AudioPlayer_381A
		UID0E51=ALMemoryRef_3829
		UID0E60=ALMotionRef_3836
		UID0E6F=UID3843
		UID2124=TextToSpeechRef_208E
		if UID0DFF[0]==True:
			UID134B=UID0DFF
			UID0EC2=False
		else: 
			UID1BD8=UID0EAE[6]
			UID15E1=UID0EAE[4]
			UID1B44=UID15E1!=""
			UID1B6D=UID0E3A
			UID1B86=UID0E51
			UID1B9C=UID0E60
			UID1BBB=UID0E6F
			UID1BFF=UID15E1
			UID21FE=UID2124
			if UID1B44==True:
				UID5211,UID262D=re.subn("https://","http://",UID1BFF,1)
				try:
					UID3A1F=UID1B6D
					if True==True:
						UID1B6D.post.playWebStream(UID5211,1.000000,0.000000)
					else:
						UID1B6D.playWebStream(UID5211,1.000000,0.000000)
					UID2F57=[False,0,""]
				except Exception, errorMsg:
					UID2F57=[True,1,str(errorMsg)]
					UID3A1F=0
				UID2EF5=touch_stop_move1.main(UID1BD8,UID2F57,UID1BBB,UID1B9C,UID1B86)
				UID1829=UID2EF5[0]
				UID1BE5=UID2EF5[1]
				UID187B=0
				UID0F8C=Clear_Errors.main(UID1829,UID187B)
				UID3A13=UID0F8C[0]
				UID102A=UID0F8C[1]
				UID1BE6=UID1BE5
				if UID3A13[0]== False:
					try:
						UID39FB=UID3A1F
						UID3A1F.stopAll()
						UID1BF2=UID3A13
					except Exception, errorMsg:
						UID1BF2=[True,1,str(errorMsg)]
						UID39FB=0
				else:
					UID1BF2=UID3A13
					UID39FB=0
				UID1BF3=UID1BF2
			else: 
				try:
					UID1EEC=UID21FE
					UID21FE.say("抱歉，这首歌曲暂时无法播放！")
					UID1BF1=[False,0,""]
				except Exception, errorMsg:
					UID1BF1=[True,1,str(errorMsg)]
					UID1EEC=0
				UID1BE6=True
				UID1BF3=UID1BF1
			UID134B=UID1BF3
			UID0EC2=UID1BE6
		WhileS_D1S_ADS_BBS_B7_37D0=UID0EC2|UID20F6
		UID3A9F=0
		UID3A35=Clear_Errors.main(UID134B,UID3A9F)
		UID37F5=UID3A35[0]
		UID3A4F=UID3A35[1]
		WhileS_D1S_ADS_BBS_B7_37D0_Stop=WhileS_D1S_ADS_BBS_B7_37D0
		error_out_37F8=UID37F5
	queue_error_out_37F8.put(error_out_37F8)
def UID3AB1(ErrorOut_3AB4,ALMemoryRef_3AB8,millisecond_timer_value_3AC4,musicTime_3ACB,queue_ErrorOut_2419,):
	i_3ADD=-1
	WhileS_D1S_ADS_BBS_B7_3AE0_Stop=True
	while WhileS_D1S_ADS_BBS_B7_3AE0_Stop==True:
		UID3AE4=np.array(["Device/SubDeviceList/Head/Touch/Front/Sensor/Value","Device/SubDeviceList/Head/Touch/Rear/Sensor/Value","Device/SubDeviceList/Head/Touch/Middle/Sensor/Value"],dtype="S")
		UID3BC8=int(time.time()*1000)
		if ErrorOut_3AB4[0]== False:
			try:
				UID3B44=ALMemoryRef_3AB8
				UID3BA7=np.array(ALMemoryRef_3AB8.getListData(UID3AE4.tolist()))
				UID2356=ErrorOut_3AB4
			except Exception, errorMsg:
				UID2356=[True,1,str(errorMsg)]
				UID3BA7=np.array([],dtype="float64")
				UID3B44=0
		else:
			UID2356=ErrorOut_3AB4
			UID3BA7=np.array([],dtype="float64")
			UID3B44=0
		UID3BD4=UID3BC8-millisecond_timer_value_3AC4
		try:
			UID3BB7=UID3BA7.tolist().index(1.000000)
		except:
			UID3BB7=-1
		UID3B8D=UID3BD4<musicTime_3ACB
		ErrorOut_2419=UID2356
		UID3B90=UID3BB7<0
		WhileS_D1S_ADS_BBS_B7_3AE0=UID3B90&UID3B8D
		WhileS_D1S_ADS_BBS_B7_3AE0_Stop=WhileS_D1S_ADS_BBS_B7_3AE0
	queue_ErrorOut_2419.put(ErrorOut_2419)
def UID5E89(queue_UID5EFB,queue_UID5F0A,string_5F01,):
	UID5EFB=np.array([],dtype="S")
	i_5F16=-1
	WhileS_D1S_ADS_BBS_B7_5F1E_Stop=False
	while WhileS_D1S_ADS_BBS_B7_5F1E_Stop==False:
		i_5F16=i_5F16+1
		UID5F42_result=re.split(",",string_5F01[0:],1)
		UID5F4D=string_5F01[:0]+UID5F42_result[0]
		if len(UID5F42_result)==2:
			UID5F50=","
			string_5F01=UID5F42_result[1]
			UID5F56=len(UID5F4D)+len(",")
		else:
			UID5F50=""
			string_5F01=""
			UID5F56=-1
		UID5F0A=i_5F16
		WhileS_D1S_ADS_BBS_B7_5F1E=UID5F4D==""
		
		UID5EFB=np.concatenate((UID5EFB,[UID5F4D]))
		WhileS_D1S_ADS_BBS_B7_5F1E_Stop=WhileS_D1S_ADS_BBS_B7_5F1E
	queue_UID5EFB.put(UID5EFB)
	queue_UID5F0A.put(UID5F0A)
def UID417E(queue_ErrorOut_4184,millisecond_timer_value_4190,RefOut_41A1,error_out_41B7,ms_41E0,queue_RefOut_514B,):
	i_42AD=-1
	WhileS_D1S_ADS_BBS_B7_42B5_Stop=True
	while WhileS_D1S_ADS_BBS_B7_42B5_Stop==True:
		UID42BF=np.array(["Device/SubDeviceList/Head/Touch/Front/Sensor/Value","Device/SubDeviceList/Head/Touch/Rear/Sensor/Value","Device/SubDeviceList/Head/Touch/Middle/Sensor/Value"],dtype="S")
		UID446F=int(time.time()*1000)
		if error_out_41B7[0]== False:
			try:
				UID5147=RefOut_41A1
				UID4437=np.array(RefOut_41A1.getListData(UID42BF.tolist()))
				UID418D=error_out_41B7
			except Exception, errorMsg:
				UID418D=[True,1,str(errorMsg)]
				UID4437=np.array([],dtype="float64")
				UID5147=0
		else:
			UID418D=error_out_41B7
			UID4437=np.array([],dtype="float64")
			UID5147=0
		UID4466=millisecond_timer_value_4190+3000
		try:
			UID4446=UID4437.tolist().index(1.000000)
		except:
			UID4446=-1
		UID4491=UID446F-UID4466
		RefOut_514B=UID5147
		ErrorOut_4184=UID418D
		UID4417=UID4446<0
		UID4414=UID4491<ms_41E0
		WhileS_D1S_ADS_BBS_B7_42B5=UID4417&UID4414
		WhileS_D1S_ADS_BBS_B7_42B5_Stop=WhileS_D1S_ADS_BBS_B7_42B5
	queue_ErrorOut_4184.put(ErrorOut_4184)
	queue_RefOut_514B.put(RefOut_514B)
def UID44D9(pIP_44DB,queue_ms_44DF,error_IO_44E3,queue_error_out_44E7,):
	i_44F4=-1
	WhileS_D1S_ADS_BBS_B7_44F8_Stop=False
	while WhileS_D1S_ADS_BBS_B7_44F8_Stop==False:
		time.sleep(1000/1000.0)
		UID33F3=TabletServiceProxy_getVideoLength.main(error_IO_44E3,pIP_44DB)
		UID44EA=UID33F3[0]
		UID342D=UID33F3[1]
		WhileS_D1S_ADS_BBS_B7_44F8=UID342D>0
		error_out_44E7=UID44EA
		ms_44DF=UID342D
		WhileS_D1S_ADS_BBS_B7_44F8_Stop=WhileS_D1S_ADS_BBS_B7_44F8
	queue_ms_44DF.put(ms_44DF)
	queue_error_out_44E7.put(error_out_44E7)
def main():
    UID3C62=int(time.time()*1000)
    Constant_UID532A="127.0.0.1"
    UID0E31=os.path.realpath(__file__)
    UID5E5B=[0,True,np.array([],dtype="S"),0,np.array([],dtype="S"),"",np.array([[]],dtype="S"),np.array([[]],dtype="S"),np.array([[]],dtype="S"),"Pepper","欢迎光临",1,"qianqian","",""]
    S_BFS_E7S_D7S_B4S_CCS_ACS_CAS_FDS_BES_DD_30D4=copy.copy(UID5E5B)
    S_BFS_E7S_D7S_B4S_CCS_ACS_CAS_FDS_BES_DD_30D4[0]=UID3C62
    UID0E3B,UID0E40=os.path.split(UID0E31)
    UID3AB3=wait_for_boot.main(Constant_UID532A)
    UID4BD2=UID3AB3[0]
    UID4BE1=UID3AB3[1]
    UID4B60=CreateProxies.main(UID4BD2,UID4BE1)
    UID3D2C=UID4B60[0]
    Proxies_11D3=UID4B60[1]
    UID0E59,UID0E5D=os.path.split(UID0E3B)
    UID4C7B="http://198.18.0.1/apps/"+UID0E5D
    if UID3D2C[0]==True:
    	UID3EC8=np.array(["False"],dtype="S")
    	UID3D40=UID3EC8
    else: 
    	UID3D80=np.array(["checkLicense"],dtype="S")
    	UID29FF=np.array(["login"],dtype="S")
    	UID3D40=UID3D80
    stripped_path_21B2=UID0E3B
    name_0C27=UID0E5D
    pIP_2392=Constant_UID532A
    action_0919=UID3D40
    queue_UID02C8=Queue.Queue()
    thread.start_new_thread(UID02C8,(name_0C27,stripped_path_21B2,Proxies_11D3,UID4C7B,pIP_2392,action_0919,S_BFS_E7S_D7S_B4S_CCS_ACS_CAS_FDS_BES_DD_30D4,queue_UID02C8,))
    queue_UID02C8.get()
    
if __name__ == "__main__":
    main()
