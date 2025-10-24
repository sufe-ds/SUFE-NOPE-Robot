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
import readlist2
imp.reload (readlist2)
import re
import getAdvNum
imp.reload (getAdvNum)
import NAO_ASR_Common
imp.reload (NAO_ASR_Common)
import touchheadstopsay1
imp.reload (touchheadstopsay1)
import random
import writeFile
imp.reload (writeFile)
import activiate_Evaluation
imp.reload (activiate_Evaluation)
import TabletServiceProxy_executeJS
imp.reload (TabletServiceProxy_executeJS)
import getAdvImg
imp.reload (getAdvImg)
import getAdvTxt
imp.reload (getAdvTxt)
import qalib
imp.reload (qalib)
import check_page
imp.reload (check_page)
import yiku_getSongLink
imp.reload (yiku_getSongLink)
import local_filter
imp.reload (local_filter)
import touch_stop_move1
imp.reload (touch_stop_move1)
import semantic_getResult
imp.reload (semantic_getResult)
import json
import tuling_v2
imp.reload (tuling_v2)
import match6
imp.reload (match6)
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
					UID4C6B=UID4BF1
					UID4BF1.say("抱歉，服务启动失败，请检查网络。")
				UID4BDF=UID4C2B
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
			UID1546=[["VIRobotics_question",""],["VIRobotics_answer",""],["VIRobotics_Page","home"]]
			UID3DD5=np.array(["LoadMem","Readlist","Behavior","Html","Page"],dtype="S")
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
			UID2538=0
			UID2279=Clear_Errors.main(UID248D,UID2538)
			UID1CD0=UID2279[0]
			UID252C=UID2279[1]
			if UID1CD0[0]== False:
				try:
					UID4B1F=UID1CE5
					UID1CE5.wakeUp()
					UID4B11=UID1CD0
				except Exception, errorMsg:
					UID4B11=[True,1,str(errorMsg)]
					UID4B1F=0
			else:
				UID4B11=UID1CD0
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
					UID2A1B=UID2A4B
					UID2A4B.setIdlePostureEnabled("Legs",True)
					UID0D1E=UID2A39
				except Exception, errorMsg:
					UID0D1E=[True,1,str(errorMsg)]
					UID2A1B=0
			else:
				UID0D1E=UID2A39
				UID2A1B=0
			if UID0D1E[0]== False:
				try:
					UID0D0F=UID0D27
					UID0D27.setLanguage(Constant_UID0D6A)
					UID3D1F=UID0D1E
				except Exception, errorMsg:
					UID3D1F=[True,1,str(errorMsg)]
					UID0D0F=0
			else:
				UID3D1F=UID0D1E
				UID0D0F=0
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
					UID152D=UID3330
				except Exception, errorMsg:
					UID152D=[True,1,str(errorMsg)]
					UID32CD=0
			else:
				UID152D=UID3330
				UID32CD=0
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
			UID258F=os.path.join(UID3F37,"speech.txt")
			UID4A95=UID3F6E
			UID4D0B=UID3F81
			UID2578=UID258F
			UID4A8C=[False,0,""]
			UID48E1=readFile.main(UID4A8C,UID4A95)
			UID4D02=UID48E1[0]
			UID452B=UID48E1[1]
			UID4A7D=UID48E1[2]
			UID4C38=readFile.main(UID4D02,UID4D0B)
			UID2564=UID4C38[0]
			UID46A2=UID4C38[1]
			UID4CF3=UID4C38[2]
			UID24FF=readFile.main(UID2564,UID2578)
			UID4528=UID24FF[0]
			UID2496=UID24FF[1]
			UID2551=UID24FF[2]
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
					UID24BD=UID46A8
					UID46A8.insertData("VIRobotics_settings",UID46A2)
					UID248C=UID469E
				except Exception, errorMsg:
					UID248C=[True,1,str(errorMsg)]
					UID24BD=0
			else:
				UID248C=UID469E
				UID24BD=0
			if UID248C[0]== False:
				UID2451=UID24BD
				UID24BD.insertData("VIRobotics_speech",UID2496)
		elif UID0351=="Readlist":
			UID0A5D=False
			UID3631=os.path.join(UID21A4,"config")
			UID095E=UID473C
			UID1EDA=os.path.join(UID3631,"qa.txt")
			UID34F3=os.path.join(UID3631,"settings.txt")
			UID3421=UID1EDA
			UID37A2=UID34F3
			UID3416=[False,0,""]
			UID0515=readlist2.main(UID3416,UID3421)
			UID378D=UID0515[0]
			UID1E2A=UID0515[1]
			UID0507=readlist2.main(UID378D,UID37A2)
			UID375C=UID0507[0]
			UID376B=UID0507[1]
			UID4964=UID376B.transpose()[1]
			try:
				UID4502=UID4964[0+0]
			except:
				UID4502=""
			try:
				UID2D7A=UID4964[1+0]
			except:
				UID2D7A=""
			UID3528=copy.copy(UID3F54)
			UID3528[6]=UID1E2A
			UID3528[7]=UID376B
			UID3528[9]=UID4502
			UID3528[10]=UID2D7A
			UID3E77=UID3528
		elif UID0351=="Behavior":
			Constant_UID30A3="naosoundwave/behavior_1"
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
			UID3484=UID347D[0]
			UID348E=UID347D[1]
		elif UID0351=="Html":
			UID0A5D=False
			UID5D84=UID1272[0]
			UID5D81=UID4C4D+"/home.html"
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
			UID3C69=UID3B40[0]
			UID3C15=UID3B40[1]
			
			UID3C64=UID3C69
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
			UID35A4=np.array(["ADV"],dtype="S")
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
		elif UID0351=="ADV":
			UID0A5D=False
			UID2721=UID1272[4]
			UID47F3=UID3F54[5]
			UID28E6=UID3F54[11]
			UID47F1_result=re.split("_",UID47F3[0:],1)
			UID47FC=UID47F3[:0]+UID47F1_result[0]
			if len(UID47F1_result)==2:
				UID47FF="_"
				UID4803=UID47F1_result[1]
				UID4806=len(UID47FC)+len("_")
			else:
				UID47FF=""
				UID4803=""
				UID4806=-1
			UID47E5=[False,0,""]
			UID47CA=getAdvNum.main(UID47E5,UID47FC)
			UID47CD=UID47CA[0]
			UID47D6=UID47CA[1]
			UID52E9=UID47D6>0
			UID2AB2=UID47FC
			UID23FC=UID47D6
			UID471D=UID3F54
			UID364D=UID271A
			if UID52E9==True:
				UID2AE9=np.array(["Page"],dtype="S")
				UID32BA=" "*(0-len('%d' %UID28E6))+'%d' %UID28E6
				UID2122=UID28E6//UID23FC
				UID2501=UID28E6%UID23FC
				UID555F=UID2AE9
				UID3FDC=[False,0,""]
				UID3D4B=getAdvImg.main(UID3FDC,UID32BA,UID2AB2)
				UID2D90=UID3D4B[0]
				UID3C2E=UID3D4B[1]
				UID479F=UID2501+1
				UID2899=copy.copy(UID471D)
				UID2899[11]=UID479F
				UID2DA2="showADV('"+UID3C2E+"')"
				UID283A=TabletServiceProxy_executeJS.main(UID2D90,UID2DA2,UID364D)
				UID2520=UID283A
				UID289E=UID2899
				UID254C=0
				UID2171=Clear_Errors.main(UID2520,UID254C)
				UID3063=UID2171[0]
				UID251B=UID2171[1]
				UID3027=getAdvTxt.main(UID3063,UID32BA,UID2AB2)
				UID35CA=UID3027[0]
				UID35D1=UID3027[1]
				if UID35CA[0]== False:
					try:
						UID35B2=UID2721
						UID2721.say(UID35D1)
						UID4489=UID35CA
					except Exception, errorMsg:
						UID4489=[True,1,str(errorMsg)]
						UID35B2=0
				else:
					UID4489=UID35CA
					UID35B2=0
				UID4492=0
				UID3847=Clear_Errors.main(UID4489,UID4492)
				UID4239=UID3847[0]
				UID4486=UID3847[1]
				UID41FF=TabletServiceProxy_executeJS.main(UID4239,"closeADV()",UID364D)
				UID4209=UID41FF
			else: 
				UID543B=np.array(["Page"],dtype="S")
				UID289E=UID471D
				UID555F=UID543B
			UID3E77=UID289E
			UID095E=UID555F
		elif UID0351=="Xunfei":
			UID0A5D=False
			UID228D=UID1272[15]
			UID18B5=UID1272[6]
			UID275A=UID3F54[9]
			UID2277=[False,0,""]
			UID222F=NAO_ASR_Common.main(UID2277,UID228D,UID271A)
			UID2C0C=UID222F[0]
			UID2254=UID222F[1]
			UID2D20=UID2C0C[0]
			UID1ACB=len(UID2254)
			UID2D25=UID1ACB<9
			UID2E5D=UID2D25|UID2D20
			UID31CA=UID2254
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
					elif UID0CD7=="更新":
						UID4953=np.array(["Readlist","Say","Page"],dtype="S")
						UID4618=np.array(["更新完成"])
						UID23D4=UID0840
						UID0CF7=UID4953
						UID45F1=copy.copy(UID0D05)
						UID45F1[2]=UID4618
						UID0D2A=UID45F1
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
					elif UID0CD7=="广告":
						UID21C5=np.array(["ADV"],dtype="S")
						UID23D4=UID0840
						UID0D2A=UID0D05
						UID0CF7=UID21C5
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
								UID26C6=match6.main(UID1686,UID182F)
								UID183F=UID26C6[0]
								UID0F4E=UID26C6[1]
								UID3239=UID26C6[2]
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
									UID3275=UID203B.encode('utf-8')
								except:
									UID3275=UID203B
								UID3255=[False,0,""]
							except Exception, errorMsg:
								UID3255=[True,1,str(errorMsg)]
								UID3275=""
							UID1B3B=UID2413
							UID3264='{"city": "上海","province": "上海","street": "五角场"}'
							UID31FB=tuling_v2.main("e0bada8cf5fb4afc81292ccc47fef250",UID3255,UID3264,UID163A,UID3275)
							UID1EC6=UID31FB[0]
							UID2637=UID31FB[1]
							UID3229=UID31FB[2]
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
			UID1C8B=UID1272[4]
			UID0FD1=UID1272[3]
			UID0F00=UID1272[6]
			UID4A27=UID3F54[2]
			try:
				UID24E4=UID473C[0]
			except:
				UID24E4=""
			UID095E=UID473C
			UID4A22=UID4A27[0]
			UID4B62=np.delete(UID4A27,[0])
			try:
				UID0FB5=UID0FD1
				if True==True:
					UID0FD1.post.say(UID4A22,"contextual")
				else:
					UID0FD1.say(UID4A22,"contextual")
				UID3068=[False,0,""]
			except Exception, errorMsg:
				UID3068=[True,1,str(errorMsg)]
				UID0FB5=0
			UID31DA=copy.copy(UID3F54)
			UID31DA[2]=UID4B62
			UID1703=UID4A22
			if UID24E4=="Music":
				UID17A4=UID1703+"<font color = '#ff8000'>（长按头部停止唱歌）</font>"
				UID312F=UID3068
				UID17AA=UID17A4
			else: 
				UID1B76=len(UID1703)
				UID312F=UID3068
				UID1A5A=UID1B76>100
				UID1EB5=UID1703
				if UID1A5A==True:
					UID2025="<font color = '#ff8000'>（长按头部停止回答）</font>"+UID1EB5
					UID2029=UID2025
				else: 
					UID2029=UID1EB5
				UID17AA=UID2029
			UID3E77=UID31DA
			if UID312F[0]== False:
				try:
					UID1BB5=UID0F00
					UID0F00.insertData("VIRobotics_answer",UID17AA)
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
			UID1B9D=UID1B8D[1]
			UID1CEE=0
			UID1CCC=Clear_Errors.main(UID1CE3,UID1CEE)
			UID1C81=UID1CCC[0]
			UID1CDE=UID1CCC[1]
			if UID1C81[0]== False:
				UID1C60=UID1C8B
				UID1C8B.stopAll()
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
			queue_ErrorOut_3ABF=Queue.Queue()
			thread.start_new_thread(UID3AB1,(ErrorOut_3AB4,ALMemoryRef_3AB8,queue_ErrorOut_3ABF,millisecond_timer_value_3AC4,musicTime_3ACB,))
			ErrorOut_3ABF=queue_ErrorOut_3ABF.get()
			queue_ErrorOut_3ABF.put(ErrorOut_3ABF)
			if ErrorOut_3ABF[0]== False:
				try:
					UID3CA0=UID3CC3
					UID3CC3.stopAll()
					UID3CE7=ErrorOut_3ABF
				except Exception, errorMsg:
					UID3CE7=[True,1,str(errorMsg)]
					UID3CA0=0
			else:
				UID3CE7=ErrorOut_3ABF
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
			UID17D4=np.array(["Page"],dtype="S")
			UID0A5D=False
			content_22AB=UID3F54[2]
			UID3E77=UID3F54
			UID095E=UID17D4
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
			UID3437=os.path.join(UID3771,"speech.txt")
			UID3E77=UID21CA
			UID4843=UID37A0
			UID2C24=UID37E3
			if UID3D41[0]== False:
				try:
					UID349C=UID3D5F
					UID2C19=UID3D5F.getData("VIRobotics_settings")
					UID3481=UID3D41
				except Exception, errorMsg:
					UID3481=[True,1,str(errorMsg)]
					UID2C19=""
					UID349C=0
			else:
				UID3481=UID3D41
				UID2C19=""
				UID349C=0
			UID34F2=UID3437
			if UID3481[0]== False:
				try:
					UID282D=UID349C
					UID34EC=UID349C.getData("VIRobotics_speech")
					UID483A=UID3481
				except Exception, errorMsg:
					UID483A=[True,1,str(errorMsg)]
					UID34EC=""
					UID282D=0
			else:
				UID483A=UID3481
				UID34EC=""
				UID282D=0
			UID2B35=writeFile.main(UID483A,UID4840,UID4843)
			UID2BFD=UID2B35[0]
			UID2B51=UID2B35[1]
			UID2B5C=writeFile.main(UID2BFD,UID2C19,UID2C24)
			UID34D6=UID2B5C[0]
			UID2BA6=UID2B5C[1]
			UID34B5=writeFile.main(UID34D6,UID34EC,UID34F2)
			UID2818=UID34B5[0]
			UID34C1=UID34B5[1]
			if UID2818[0]== False:
				UID2788=UID282D
				UID282D.insertData("VIRobotics_Page","home")
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
					UID2680=[False,0,""]
				except Exception, errorMsg:
					UID2680=[True,1,str(errorMsg)]
					UID2A79=0
				if UID2680[0]== False:
					try:
						UID2644=UID2719
						UID2640=UID2719.goToPosture("Stand",0.500000)
						UID2E8B=UID2680
					except Exception, errorMsg:
						UID2E8B=[True,1,str(errorMsg)]
						UID2640=False
						UID2644=0
				else:
					UID2E8B=UID2680
					UID2640=False
					UID2644=0
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
			UID24BE=np.array(["儿童科技园"],dtype="S")
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
				UID24F0=UID253A
				UID253A.insertData("VIRobotics_Page","exit")
				UID2298=[False,0,""]
			except Exception, errorMsg:
				UID2298=[True,1,str(errorMsg)]
				UID24F0=0
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
			UID3463=UID384E
			if UID3463[0]== False:
				try:
					UID3405=UID346F
					UID346F.say("即将退出程序")
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
			UID3884=np.array([],dtype="S")
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
def UID3AB1(ErrorOut_3AB4,ALMemoryRef_3AB8,queue_ErrorOut_3ABF,millisecond_timer_value_3AC4,musicTime_3ACB,):
	i_3ADD=-1
	WhileS_D1S_ADS_BBS_B7_3AE0_Stop=True
	while WhileS_D1S_ADS_BBS_B7_3AE0_Stop==True:
		UID3AE4=np.array(["Device/SubDeviceList/Head/Touch/Front/Sensor/Value","Device/SubDeviceList/Head/Touch/Rear/Sensor/Value","Device/SubDeviceList/Head/Touch/Middle/Sensor/Value"],dtype="S")
		UID3BC8=int(time.time()*1000)
		if ErrorOut_3AB4[0]== False:
			try:
				UID3C07=ALMemoryRef_3AB8
				UID3BA7=np.array(ALMemoryRef_3AB8.getListData(UID3AE4.tolist()))
				UID3BF8=ErrorOut_3AB4
			except Exception, errorMsg:
				UID3BF8=[True,1,str(errorMsg)]
				UID3BA7=np.array([],dtype="float64")
				UID3C07=0
		else:
			UID3BF8=ErrorOut_3AB4
			UID3BA7=np.array([],dtype="float64")
			UID3C07=0
		UID3BD4=UID3BC8-millisecond_timer_value_3AC4
		try:
			UID3BB7=UID3BA7.tolist().index(1.000000)
		except:
			UID3BB7=-1
		UID3B8D=UID3BD4<musicTime_3ACB
		if UID3BF8[0]== False:
			try:
				UID3BE5=UID3C07
				UID3C2B=UID3C07.getData("VIRobotics_Page")
				UID3AC2=UID3BF8
			except Exception, errorMsg:
				UID3AC2=[True,1,str(errorMsg)]
				UID3C2B=""
				UID3BE5=0
		else:
			UID3AC2=UID3BF8
			UID3C2B=""
			UID3BE5=0
		UID3B90=UID3BB7<0
		UID3C37=UID3C2B=="home"
		ErrorOut_3ABF=UID3AC2
		UID3C3A=UID3B90&UID3B8D
		WhileS_D1S_ADS_BBS_B7_3AE0=UID3C3A&UID3C37
		WhileS_D1S_ADS_BBS_B7_3AE0_Stop=WhileS_D1S_ADS_BBS_B7_3AE0
	queue_ErrorOut_3ABF.put(ErrorOut_3ABF)
def main():
    UID3C62=int(time.time()*1000)
    Constant_UID532A="127.0.0.1"
    UID0E31=os.path.realpath(__file__)
    UID5E5B=[0,True,np.array([],dtype="S"),0,np.array([],dtype="S"),"",np.array([[]],dtype="S"),np.array([[]],dtype="S"),np.array([[]],dtype="S"),"Pepper","欢迎光临",1,"qianqian"]
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
