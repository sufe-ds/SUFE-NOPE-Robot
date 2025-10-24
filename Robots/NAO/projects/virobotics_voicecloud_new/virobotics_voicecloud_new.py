# -*- coding: utf-8 -*-
import numpy as np
import os
from ctypes import *
import platform
if platform.system()=="Linux":
 libfolder=os.path.split(os.path.realpath(__file__))[0]
 libpath=os.path.join(libfolder,"xunfei.so")
 xfdll=cdll.LoadLibrary(libpath)
else:
 xfdll=windll.LoadLibrary("msc.dll")
from naoqi import ALProxy
import imp
import Clear_Errors
imp.reload (Clear_Errors)
# -*- coding:utf-8 -*-
import sys
import thread
import Queue
import copy
import time
import NAO_ASR
imp.reload (NAO_ASR)
import json
import semantic_getResult
imp.reload (semantic_getResult)
import BaiduMusic_KeyWords
imp.reload (BaiduMusic_KeyWords)
import BaiduMusic_GetList
imp.reload (BaiduMusic_GetList)
import random
import BaiduMusic_tagToTinguid
imp.reload (BaiduMusic_tagToTinguid)
import BaiduMusic_GetLink
imp.reload (BaiduMusic_GetLink)
import BaiduMusic_GetSingerInfo
imp.reload (BaiduMusic_GetSingerInfo)
import BaiduMusic_GetSingerMusic
imp.reload (BaiduMusic_GetSingerMusic)
import tuling3
imp.reload (tuling3)
def UID002B(name_for_subscribe_003D,stripped_path_004E,UID0052,pIP_1C71,UID3523,UID0034,UID0041,UID005A,UID0063,UID006C,millisecond_timer_value_0075,queue_UID002B,):
	i_0086=-1
	While_Loop_0089_Stop=False
	while While_Loop_0089_Stop==False:
		UID009A=UID0034[0]
		UID2DC3=np.delete(UID0034,[0])
		UID0136=name_for_subscribe_003D
		UID019E=UID0041
		UID0206=stripped_path_004E
		UID023A=UID0052
		UID02A2=UID005A
		UID033E=UID0063
		UID0372=UID006C
		UID040E=millisecond_timer_value_0075
		UID1C60=pIP_1C71
		UID3514=UID3523
		if UID009A=="Initial":
			Constant_UID0456="Chinese"
			Constant_UID04C8="disabled"
			UID030A=0
			UID016A=np.array([],dtype="S")
			UID0102=False
			UID06CD=UID023A[0]
			UID06A6=UID023A[6]
			UID07A1=UID023A[13]
			UID34CA=UID023A[11]
			UID05B3=UID023A[3]
			UID051D=UID023A[7]
			UID05DA=UID023A[10]
			UID00D1=np.array(["first run xunfei"])
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			try:
				UID06D7=UID06CD
				UID0735=UID06CD.getState()
				UID06DC=[False,0,""]
			except Exception, errorMsg:
				UID06DC=[True,1,str(errorMsg)]
				UID0735=""
				UID06D7=0
			UID00CE=UID00D1
			UID06D2=Constant_UID04C8==UID0735
			UID06E1=Constant_UID04C8
			if UID06D2==True:
				UID06E6=UID06DC
			else: 
				if UID06DC[0]== False:
					try:
						UID06FF=UID06D7
						UID06D7.setState(UID06E1)
						UID06E9=UID06DC
					except Exception, errorMsg:
						UID06E9=[True,1,str(errorMsg)]
						UID06FF=0
				else:
					UID06E9=UID06DC
					UID06FF=0
				UID06E6=UID06E9
			UID0753=0
			UID073B=Clear_Errors.main(UID06E6,UID0753)
			UID069D=UID073B[0]
			UID0747=UID073B[1]
			if UID069D[0]== False:
				try:
					UID068E=UID06A6
					UID06A6.wakeUp()
					UID0798=UID069D
				except Exception, errorMsg:
					UID0798=[True,1,str(errorMsg)]
					UID068E=0
			else:
				UID0798=UID069D
				UID068E=0
			if UID0798[0]== False:
				try:
					UID0789=UID07A1
					UID07A1.setPictureFormat("jpg")
					UID34D7=UID0798
				except Exception, errorMsg:
					UID34D7=[True,1,str(errorMsg)]
					UID0789=0
			else:
				UID34D7=UID0798
				UID0789=0
			UID349D=True
			if UID349D==True:
				Constant_UID04A1="Face"
				if UID34D7[0]== False:
					try:
						UID0631=UID34CA
						UID34CA.registerTarget("Face",0.150000)
						UID0628=UID34D7
					except Exception, errorMsg:
						UID0628=[True,1,str(errorMsg)]
						UID0631=0
				else:
					UID0628=UID34D7
					UID0631=0
				if UID0628[0]== False:
					try:
						UID0658=UID0631
						UID0631.setMode("Head")
						UID064F=UID0628
					except Exception, errorMsg:
						UID064F=[True,1,str(errorMsg)]
						UID0658=0
				else:
					UID064F=UID0628
					UID0658=0
				if UID064F[0]== False:
					try:
						UID067F=UID0658
						UID0658.setExtractorPeriod(Constant_UID04A1,5)
						UID0676=UID064F
					except Exception, errorMsg:
						UID0676=[True,1,str(errorMsg)]
						UID067F=0
				else:
					UID0676=UID064F
					UID067F=0
				if UID0676[0]== False:
					try:
						UID0667=UID067F
						UID067F.track(Constant_UID04A1)
						UID34E2=UID0676
					except Exception, errorMsg:
						UID34E2=[True,1,str(errorMsg)]
						UID0667=0
				else:
					UID34E2=UID0676
					UID0667=0
				UID34E3=UID34E2
			else: 
				UID34E3=UID34D7
			if UID34E3[0]== False:
				try:
					UID059B=UID05B3
					UID05B3.setLanguage(Constant_UID0456)
					UID0514=UID34E3
				except Exception, errorMsg:
					UID0514=[True,1,str(errorMsg)]
					UID059B=0
			else:
				UID0514=UID34E3
				UID059B=0
			if UID0514[0]== False:
				try:
					UID056B=UID051D
					UID051D.setLanguage(Constant_UID0456)
					UID0562=UID0514
				except Exception, errorMsg:
					UID0562=[True,1,str(errorMsg)]
					UID056B=0
			else:
				UID0562=UID0514
				UID056B=0
			if UID0562[0]== False:
				try:
					UID0565=False
					UID0544=UID056B
					UID056B.setVocabulary(UID3514.tolist(),UID0565)
					UID053B=UID0562
				except Exception, errorMsg:
					UID053B=[True,1,str(errorMsg)]
					UID0544=0
			else:
				UID053B=UID0562
				UID0544=0
			if UID053B[0]== False:
				try:
					UID052C=UID0544
					UID0544.subscribe(UID0136)
					UID05D1=UID053B
				except Exception, errorMsg:
					UID05D1=[True,1,str(errorMsg)]
					UID052C=0
			else:
				UID05D1=UID053B
				UID052C=0
			if UID05D1[0]== False:
				UID05C2=UID05DA
				UID05DA.subscribe(UID0136,100,1.000000)
		elif UID009A=="first run xunfei":
			Constant_UID1D7B="naosoundwave/behavior_1"
			UID2025=np.array(["Listen"],dtype="S")
			UID0102=False
			UID1D62=UID023A[1]
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID019E
			UID00CE=UID2025
			try:
				UID1D92=UID1D62
				UID1D8D=UID1D62.isBehaviorRunning(Constant_UID1D7B)
				UID1D97=[False,0,""]
			except Exception, errorMsg:
				UID1D97=[True,1,str(errorMsg)]
				UID1D8D=False
				UID1D92=0
			UID1EE0=Constant_UID1D7B
			if UID1D8D==True:
				pass
			else: 
				if UID1D97[0]== False:
					UID1DF3=UID1D92
					UID1D92.startBehavior(UID1EE0)
		elif UID009A=="Listen":
			UID030A=0
			UID016A=np.array([],dtype="S")
			UID0102=False
			UID0867=UID023A[5]
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			try:
				UID088D=UID0867
				UID0883=UID0867.getData('WordRecognized')
				UID087E=[False,0,""]
			except Exception, errorMsg:
				UID087E=[True,1,str(errorMsg)]
				UID0883=["",0.000000]
				UID088D=0
			if UID087E[0]==True:
				UID0888="Face1"
			else: 
				UID08C9=UID0883[0]
				UID08AE=UID0883[1]
				UID08BF=UID08AE>=0.470000
				UID08CE=UID088D
				UID08D3=UID087E
				if UID08BF==True:
					UID08C4=UID08C9
				else: 
					UID08C4="Face1"
				UID0888=UID08C4
			UID00D2=np.array([UID0888])
			UID00CE=UID00D2
		elif UID009A=="Face1":
			UID030A=0
			UID0102=False
			UID0B76=UID023A[5]
			try:
				UID0B5E=UID0B76
				UID0B9C=UID0B76.getData("FaceDetected")
				UID0B97=len(UID0B9C)>0
				UID0B8D=[False,0,""]
			except Exception, errorMsg:
				UID0B8D=[True,1,str(errorMsg)]
				UID0B97=False
				UID0B9C=[[0,0],[[[0.000000,0.000000,0.000000,0.000000,0.000000],[0,0.000000,"",[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000],[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000],"","",[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000],[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]]],np.array([],dtype="S")],[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000],[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000],0]
				UID0B5E=0
				UID0B61=""
			UID0BAB=UID0372
			UID0BBA=UID040E
			UID0BA1=UID02A2
			if UID0B8D[0]==True:
				UID0BBF=""
				UID0BB5=UID0BBA
				UID0BB0=UID0BAB
				UID0BA6=UID0BA1
				UID0B92="Listen"
			else: 
				UID0BCE=UID0B97
				UID0BD3=UID0B9C
				UID0BD8=UID0BA1
				UID0BE7=UID0BAB
				UID0BF6=UID0BBA
				if UID0BCE==True:
					UID0BF5=int(time.time()*1000)
					UID0D1C=UID0BD3[1][0][1][2]
					UID0D0D=UID0BD3[1][0][1][1]
					UID0BF1=UID0BF5
					UID0D12=UID0D0D>0.600000
					UID0D17=UID0BD8
					UID0D2B=UID0BE7
					if UID0D12==True:
						try:
							UID0E61=UID0D17.tolist().index(UID0D1C)
						except:
							UID0E61=-1
						UID0D30=UID0D2B
						UID0DCD=UID0E61>=0
						UID0DDC=UID0D17
						UID0DE6=UID0D1C
						if UID0DCD==False:
							UID0DE4="欢迎您！"+UID0DE6
							UID0DD5=np.concatenate((UID0DDC,[UID0DE6]))
							UID0DD7="Greet"
							UID0DE1=UID0DE4
							UID0DD2=UID0DD5
						elif UID0DCD==True:
							UID0DE1=UID0DE6
							UID0DD7="Listen"
							UID0DD2=UID0DDC
						UID0D35=UID0DE1
						UID0D26=UID0DD7
						UID0D21=UID0DD2
					else: 
						UID0D44=UID0D2B
						UID0D4E=UID0D17
						if UID0D44==True:
							UID0D5D="您好，欢迎光临VIRobotics创新实验室！"
							UID0D58=UID0D4E
							UID0D53="Greet"
							UID0D49=False
						else: 
							UID0D5D=""
							UID0D58=UID0D4E
							UID0D53="Listen"
							UID0D49=UID0D44
						UID0D35=UID0D5D
						UID0D30=UID0D49
						UID0D26=UID0D53
						UID0D21=UID0D58
					UID0BFB=UID0D35
					UID0BEC=UID0D30
					UID0BE2=UID0D26
					UID0BDD=UID0D21
				else: 
					UID0BFB=""
					UID0C1A=UID0BF6
					UID0C15=UID0BE7
					UID0C29=UID0BD8
					if UID0C15==True:
						UID0C24=UID0C29
						UID0C1F=UID0C15
					else: 
						UID0C4F=int(time.time()*1000)
						UID0C5A=UID0C4F-UID0C1A
						UID0C5F=UID0C5A>300000
						UID0C6E=UID0C29
						if UID0C5F==True:
							UID0C87=np.array([],dtype="S")
							UID0C69=UID0C5F
							UID0C64=UID0C87
						else: 
							UID0C69=UID0C5F
							UID0C64=UID0C6E
						UID0C24=UID0C64
						UID0C1F=UID0C69
					UID0BF1=UID0BF6
					UID0BE2="Listen"
					UID0BEC=UID0C1F
					UID0BDD=UID0C24
				UID0BBF=UID0BFB
				UID0BB5=UID0BF1
				UID0BB0=UID0BEC
				UID0BA6=UID0BDD
				UID0B92=UID0BE2
			UID00D4=np.array([UID0B92])
			UID0170=np.array([UID0BBF])
			UID03DA=UID0BB5
			UID03A6=UID0BB0
			UID02D6=UID0BA6
			UID016A=UID0170
			UID00CE=UID00D4
		elif UID009A=="Greet":
			UID0F50=[["LAnklePitch",[[1.000000,0.090464,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.090464,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.090464,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.090464,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.090464,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.090464,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.090464,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.090464,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LAnkleRoll",[[1.000000,-0.127280,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.127280,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.127280,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.127280,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LElbowRoll",[[1.000000,-0.412604,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.401866,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.401866,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.401866,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.401866,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.401866,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.401866,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.401866,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LElbowYaw",[[1.000000,-1.191960,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-1.191960,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-1.191960,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-1.191960,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-1.191960,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-1.191960,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-1.191960,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-1.191960,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LHand",[[1.000000,0.293200,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.293200,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.293200,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.293200,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.293200,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.293200,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.293200,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.293200,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LHipPitch",[[1.000000,0.122762,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.122762,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.122762,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.122762,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.122762,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.122762,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.122762,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.122762,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LHipRoll",[[1.000000,0.099752,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.104354,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.104354,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.104354,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.104354,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.104354,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.104354,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.104354,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LHipYawPitch",[[1.000000,-0.170232,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.170232,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.170232,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.170232,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LKneePitch",[[1.000000,-0.087480,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.087480,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.087480,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.087480,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.087480,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.087480,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.087480,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.087480,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LShoulderPitch",[[1.000000,1.481800,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,1.481800,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,1.481800,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,1.481800,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,1.481800,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,1.471060,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,1.471060,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,1.481800,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LShoulderRoll",[[1.000000,0.185572,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.156426,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.156426,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.142620,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.142620,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.185572,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.185572,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.174834,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["LWristYaw",[[1.000000,0.110406,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.110406,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.110406,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.110406,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.110406,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.110406,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.110406,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.110406,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RAnklePitch",[[1.000000,0.092082,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.092082,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.092082,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.092082,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.092082,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.092082,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.092082,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.092082,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RAnkleRoll",[[1.000000,0.125830,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.125830,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.125830,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.125830,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.125830,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.125830,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.125830,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.125830,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RElbowRoll",[[1.000000,0.398882,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.773178,[3,-0.400000,-0.137293],[3,0.133333,0.045764]],[2.600000,0.948054,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.767042,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.957258,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.757838,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.946520,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.411154,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RElbowYaw",[[1.000000,1.179600,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,1.701160,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,1.267040,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,1.701160,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,1.267040,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,1.696560,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,1.265510,[3,-0.133333,0.017385],[3,0.400000,-0.052156]],[5.400000,1.213350,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RHand",[[1.000000,0.304800,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.752400,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.752400,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.752400,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.752400,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.745600,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.745600,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.309600,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RHipPitch",[[1.000000,0.125746,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,0.127280,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,0.127280,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,0.127280,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.127280,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RHipRoll",[[1.000000,-0.099668,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.099668,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.099668,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.099668,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.099668,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.099668,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.099668,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.099668,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RHipYawPitch",[[1.000000,-0.170232,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.170232,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.170232,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.170232,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.170232,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RKneePitch",[[1.000000,-0.091998,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.091998,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.091998,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.091998,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.091998,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.091998,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.091998,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.091998,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RShoulderPitch",[[1.000000,1.478820,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.707132,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.696394,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.696394,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.685656,[3,-0.133333,-0.010738],[3,0.133333,0.010738]],[3.800000,-0.631966,[3,-0.133333,-0.010738],[3,0.133333,0.010738]],[4.200000,-0.621228,[3,-0.133333,-0.010738],[3,0.400000,0.032214]],[5.400000,1.463480,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RShoulderRoll",[[1.000000,-0.193326,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.378940,[3,-0.400000,0.000000],[3,0.133333,0.000000]],[2.600000,-0.107422,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.391212,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.119694,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.386610,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.148840,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,-0.156510,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]],["RWristYaw",[[1.000000,0.084328,[3,-0.333333,0.000000],[3,0.400000,0.000000]],[2.200000,-0.790052,[3,-0.400000,0.156468],[3,0.133333,-0.052156]],[2.600000,-0.842208,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.000000,-0.822266,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.400000,-0.833004,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[3.800000,-0.820732,[3,-0.133333,0.000000],[3,0.133333,0.000000]],[4.200000,-0.820732,[3,-0.133333,0.000000],[3,0.400000,0.000000]],[5.400000,0.082794,[3,-0.400000,0.000000],[3,0.000000,0.000000]]]]]
			UID030A=0
			UID0102=False
			UID10A8=UID023A[5]
			UID10A0=UID023A[7]
			UID1133=UID023A[8]
			UID10DC=UID023A[6]
			UID110C=UID023A[3]
			UID00D5=np.array(["Face2"])
			UID1109=UID019E[0]
			UID0171=np.delete(UID019E,[0])
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			try:
				UID1088=UID10A0
				UID10A0.unsubscribe(UID0136)
				UID112A=[False,0,""]
			except Exception, errorMsg:
				UID112A=[True,1,str(errorMsg)]
				UID1088=0
			UID016A=UID0171
			UID00CE=UID00D5
			if UID112A[0]== False:
				try:
					UID112D=0.800000
					UID1079=UID1133
					UID1118=UID1133.goToPosture("Stand",UID112D)
					UID10D3=UID112A
				except Exception, errorMsg:
					UID10D3=[True,1,str(errorMsg)]
					UID1118=False
					UID1079=0
			else:
				UID10D3=UID112A
				UID1118=False
				UID1079=0
			if UID10D3[0]== False:
				try:
					UID10C4=UID10DC
					UID0F50_names=[]
					UID0F50_time=[]
					UID0F50_angle=[]
					for i in UID0F50:
						UID0F50_names.append(i[0])
						UID0F50_time_one=[]
						UID0F50_angle_one=[]
						for j in i[1]:
							UID0F50_time_one.append(j[0])
							UID0F50_angle_one.append([j[1],j[2],j[3]])
						UID0F50_time.append(UID0F50_time_one)
						UID0F50_angle.append(UID0F50_angle_one)
					if True==True:
						UID10DC.post.angleInterpolationBezier(UID0F50_names,UID0F50_time,UID0F50_angle)
					else:
						UID10DC.angleInterpolationBezier(UID0F50_names,UID0F50_time,UID0F50_angle)
					UID1103=UID10D3
				except Exception, errorMsg:
					UID1103=[True,1,str(errorMsg)]
					UID10C4=0
			else:
				UID1103=UID10D3
				UID10C4=0
			if UID1103[0]== False:
				try:
					UID10F4=UID110C
					UID110C.say(UID1109)
					UID1070=UID1103
				except Exception, errorMsg:
					UID1070=[True,1,str(errorMsg)]
					UID10F4=0
			else:
				UID1070=UID1103
				UID10F4=0
			if UID1070[0]== False:
				UID1073=0.800000
				UID1061=UID1079
				UID105E=UID1079.goToPosture("Stand",UID1073)
		elif UID009A=="Face2":
			UID03A6=False
			UID030A=0
			UID016A=np.array([],dtype="S")
			UID0102=False
			UID00D6=np.array(["RerunVoicecloud"])
			UID03DA=UID040E
			UID02D6=UID02A2
			UID00CE=UID00D6
		elif UID009A=="Say":
			UID030A=0
			UID0102=False
			ALMemoryRef_1280=UID023A[5]
			UID1262=UID023A[3]
			UID1214=UID023A[7]
			UID00D7=np.array(["RerunVoicecloud"])
			UID125F=UID019E[0]
			UID0173=np.delete(UID019E,[0])
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			try:
				UID11FC=UID1214
				UID1214.unsubscribe(UID0136)
				UID1259=[False,0,""]
			except Exception, errorMsg:
				UID1259=[True,1,str(errorMsg)]
				UID11FC=0
			UID016A=UID0173
			UID00CE=UID00D7
			if UID1259[0]== False:
				try:
					UID124A=UID1262
					UID1262.say(UID125F)
					ErrorOut_1288=UID1259
				except Exception, errorMsg:
					ErrorOut_1288=[True,1,str(errorMsg)]
					UID124A=0
			else:
				ErrorOut_1288=UID1259
				UID124A=0
			queue_UID127D=Queue.Queue()
			thread.start_new_thread(UID127D,(ALMemoryRef_1280,ErrorOut_1288,queue_UID127D,))
			queue_UID127D.get()
		elif UID009A=="AnimatedSay":
			Constant_UID13D0="Stand"
			UID030A=0
			UID0102=False
			UID1628=UID023A[3]
			ALMemoryRef_14F3=UID023A[5]
			UID14A8=UID023A[2]
			UID145A=UID023A[8]
			UID14A5=UID019E[0]
			UID0174=np.delete(UID019E,[0])
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			UID00CE=UID2DC3
			try:
				UID1454=0.800000
				UID14E4=UID145A
				UID143F=UID145A.goToPosture(Constant_UID13D0,UID1454)
				UID149F=[False,0,""]
			except Exception, errorMsg:
				UID149F=[True,1,str(errorMsg)]
				UID143F=False
				UID14E4=0
			UID016A=UID0174
			if UID149F[0]== False:
				try:
					UID1490=UID14A8
					if True==True:
						UID14A8.post.say(UID14A5,"contextual")
					else:
						UID14A8.say(UID14A5,"contextual")
					ErrorOut_14FB=UID149F
				except Exception, errorMsg:
					ErrorOut_14FB=[True,1,str(errorMsg)]
					UID1490=0
			else:
				ErrorOut_14FB=UID149F
				UID1490=0
			queue_ErrorOut_14F7=Queue.Queue()
			thread.start_new_thread(UID14F0,(ALMemoryRef_14F3,queue_ErrorOut_14F7,ErrorOut_14FB,))
			ErrorOut_14F7=queue_ErrorOut_14F7.get()
			queue_ErrorOut_14F7.put(ErrorOut_14F7)
			UID1643=0
			UID162B=Clear_Errors.main(ErrorOut_14F7,UID1643)
			UID161F=UID162B[0]
			UID1637=UID162B[1]
			if UID161F[0]== False:
				try:
					UID1610=UID1628
					UID1628.stopAll()
					UID14DB=UID161F
				except Exception, errorMsg:
					UID14DB=[True,1,str(errorMsg)]
					UID1610=0
			else:
				UID14DB=UID161F
				UID1610=0
			if UID14DB[0]== False:
				UID14DE=0.800000
				UID14CC=UID14E4
				UID14C9=UID14E4.goToPosture(Constant_UID13D0,UID14DE)
		elif UID009A=="RerunVoicecloud":
			UID030A=0
			UID0102=False
			UID00DA=np.array(["Listen"])
			UID1E31=UID023A[7]
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			UID016A=UID019E
			UID1E09=UID1E31
			UID1E31.subscribe(UID0136)
			UID00CE=UID00DA
		elif UID009A=="Posture":
			UID030A=0
			UID0102=False
			UID1A3D=UID023A[8]
			UID1A64=UID023A[7]
			UID00DB=np.array(["RerunVoicecloud"])
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			UID016A=UID019E
			try:
				UID1A4C=UID1A64
				UID1A64.unsubscribe(UID0136)
				UID1A34=[False,0,""]
			except Exception, errorMsg:
				UID1A34=[True,1,str(errorMsg)]
				UID1A4C=0
			UID00CE=UID00DB
			if UID1A34[0]== False:
				UID1A37=0.800000
				UID1A3A="Crouch"
				UID1A25=UID1A3D
				UID1A22=UID1A3D.goToPosture(UID1A3A,UID1A37)
		elif UID009A=="dance":
			UID0102=False
			UID2216=os.path.join(UID0206,"movements")
			UID2128=UID023A[6]
			UID2158=UID023A[8]
			UID2101=UID023A[7]
			UID2238=os.path.join(UID0206,"dances")
			UID00DE=np.array(["dancemusic"])
			try:
				UID4984=UID019E[0+0]
			except:
				UID4984=""
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			try:
				UID20E9=UID2101
				UID2101.unsubscribe(UID0136)
				UID2202=[False,0,""]
			except Exception, errorMsg:
				UID2202=[True,1,str(errorMsg)]
				UID20E9=0
			UID2213=UID4984+".py"
			UID2235=UID4984+".mp3"
			UID00CE=UID00DE
			UID220B=os.path.join(UID2216,UID2213)
			UID2188=os.path.join(UID2238,UID2235)
			UID30E0=UID2188
			if UID2202[0]== False:
				try:
					pythonmodulefolder,pythonmodepath=os.path.split(UID220B)
					pythonmodule=pythonmodepath[:pythonmodepath.find(".")]
					imp_bbb=pythonmodulefolder+"/"+pythonmodule
					imp_ccc=imp.find_module(pythonmodule,[pythonmodulefolder])
					imp_ddd=imp.load_module(imp_bbb,imp_ccc[0],imp_ccc[1],imp_ccc[2])
					imp_eee=imp_ddd.main()
					UID2155=imp_eee[0]
					UID215D=imp_eee[1]
					UID21F3=imp_eee[2]
					UID214F=UID2202
				except Exception, errorMsg:
					UID214F=[True,1,str(errorMsg)]
					UID2155=""
					UID215D=0
					UID21F3=[]
			else:
				UID214F=UID2202
				UID2155=""
				UID215D=0
				UID21F3=[]
			if UID214F[0]== False:
				try:
					UID2152=0.800000
					UID2140=UID2158
					UID213D=UID2158.goToPosture(UID2155,UID2152)
					UID211F=UID214F
				except Exception, errorMsg:
					UID211F=[True,1,str(errorMsg)]
					UID213D=False
					UID2140=0
			else:
				UID211F=UID214F
				UID213D=False
				UID2140=0
			try:
				UID2199=UID21F3[0]
			except:
				UID2199=["",[]]
			UID017A=np.array([UID30E0])
			if UID211F[0]== False:
				try:
					UID2110=UID2128
					UID21F3_names=[]
					UID21F3_time=[]
					UID21F3_angle=[]
					for i in UID21F3:
						UID21F3_names.append(i[0])
						UID21F3_time_one=[]
						UID21F3_angle_one=[]
						for j in i[1]:
							UID21F3_time_one.append(j[0])
							UID21F3_angle_one.append([j[1],j[2],j[3]])
						UID21F3_time.append(UID21F3_time_one)
						UID21F3_angle.append(UID21F3_angle_one)
					if True==True:
						UID2128.post.angleInterpolationBezier(UID21F3_names,UID21F3_time,UID21F3_angle)
					else:
						UID2128.angleInterpolationBezier(UID21F3_names,UID21F3_time,UID21F3_angle)
					UID2161=UID211F
				except Exception, errorMsg:
					UID2161=[True,1,str(errorMsg)]
					UID2110=0
			else:
				UID2161=UID211F
				UID2110=0
			UID219C=UID2199[1]
			UID016A=UID017A
			
			UID2164=UID2161
			time.sleep(int(UID215D)/1000.0)
			UID21AD=len(UID219C)
			UID21B8=UID21AD-1
			try:
				UID21BE=UID219C[UID21B8+0]
			except:
				UID21BE=[0.000000,0.000000,[0,0.000000,0.000000],[0,0.000000,0.000000]]
			UID21CD=UID21BE[0]
			UID21D5=UID21CD*1000.000000
			UID031A=int(UID21D5)
			UID030A=UID031A
		elif UID009A=="dancemusic":
			UID030A=0
			UID0102=False
			millisecond_timer_value_231C=int(time.time()*1000)
			ALMotionRef_2324=UID023A[6]
			UID22FE=UID023A[9]
			UID22FB=UID019E[0]
			UID017B=np.delete(UID019E,[0])
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			try:
				UID2458=UID22FE
				if True==True:
					UID22FE.post.playFile(UID22FB)
				else:
					UID22FE.playFile(UID22FB)
				ErrorOut_2328=[False,0,""]
			except Exception, errorMsg:
				ErrorOut_2328=[True,1,str(errorMsg)]
				UID2458=0
			UID016A=UID017B
			UID2320=UID033E
			queue_UID2318=Queue.Queue()
			queue_ErrorOut_232C=Queue.Queue()
			thread.start_new_thread(UID2315,(queue_UID2318,millisecond_timer_value_231C,UID2320,ALMotionRef_2324,ErrorOut_2328,queue_ErrorOut_232C,))
			ErrorOut_232C=queue_ErrorOut_232C.get()
			queue_ErrorOut_232C.put(ErrorOut_232C)
			if ErrorOut_232C[0]== False:
				try:
					UID2440=UID2458
					UID2458.stopAll()
					UID2471=ErrorOut_232C
				except Exception, errorMsg:
					UID2471=[True,1,str(errorMsg)]
					UID2440=0
			else:
				UID2471=ErrorOut_232C
				UID2440=0
			UID2318=queue_UID2318.get()
			queue_UID2318.put(UID2318)
			UID245D=UID2318
			if UID245D==True:
				UID2462="danceerror"
			else: 
				UID2462="RerunVoicecloud"
			UID00DF=np.array([UID2462])
			UID00CE=UID00DF
		elif UID009A=="danceerror":
			UID030A=0
			UID0102=False
			UID25BD=UID023A[3]
			UID25E4=UID023A[6]
			UID256F=UID023A[8]
			UID25F5=UID023A[7]
			UID00E0=np.array(["RerunVoicecloud"])
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			UID016A=UID019E
			try:
				UID25CC=UID25E4
				UID25E4.wakeUp()
				UID2566=[False,0,""]
			except Exception, errorMsg:
				UID2566=[True,1,str(errorMsg)]
				UID25CC=0
			UID00CE=UID00E0
			if UID2566[0]== False:
				try:
					UID2569=0.800000
					UID2557=UID256F
					UID2554=UID256F.goToPosture("Stand",UID2569)
					UID25B4=UID2566
				except Exception, errorMsg:
					UID25B4=[True,1,str(errorMsg)]
					UID2554=False
					UID2557=0
			else:
				UID25B4=UID2566
				UID2554=False
				UID2557=0
			if UID25B4[0]== False:
				UID25A5=UID25BD
				UID25BD.say("哎呀，我摔倒了，但是我能自己站起来，别担心了！")
		elif UID009A=="moveto":
			Constant_UID2644="Stand"
			UID030A=0
			UID0102=False
			UID26F7=UID023A[6]
			UID2682=UID023A[7]
			UID26D0=UID023A[8]
			UID00E1=np.array(["RerunVoicecloud"])
			UID273B=UID019E[0]
			UID017D=np.delete(UID019E,[0])
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			try:
				UID266A=UID2682
				UID2682.unsubscribe(UID0136)
				UID26C7=[False,0,""]
			except Exception, errorMsg:
				UID26C7=[True,1,str(errorMsg)]
				UID266A=0
			if UID273B=="moveL":
				UID4ED7=[0.000000,0.300000,0.000000]
				UID2741=UID4ED7
			elif UID273B=="turnR":
				UID2789=[0.000000,0.000000,-1.570000]
				UID2741=UID2789
			elif UID273B=="moveR":
				UID5146=[0.000000,-0.300000,0.000000]
				UID2741=UID5146
			elif UID273B=="turnB":
				UID27C3=[0.000000,0.000000,-3.140000]
				UID2741=UID27C3
			elif UID273B=="moveB":
				UID4581=[-0.200000,0.000000,0.000000]
				UID2741=UID4581
			elif UID273B=="moveF":
				UID48E7=[0.300000,0.000000,0.000000]
				UID2741=UID48E7
			else: 
				UID274F=[0.000000,0.000000,1.570000]
				UID2741=UID274F
			UID016A=UID017D
			UID00CE=UID00E1
			if UID26C7[0]== False:
				try:
					UID26CA=0.800000
					UID2727=UID26D0
					UID26B5=UID26D0.goToPosture(Constant_UID2644,UID26CA)
					UID26EE=UID26C7
				except Exception, errorMsg:
					UID26EE=[True,1,str(errorMsg)]
					UID26B5=False
					UID2727=0
			else:
				UID26EE=UID26C7
				UID26B5=False
				UID2727=0
			UID26EB=UID2741[2]
			UID26F4=UID2741[0]
			UID26F1=UID2741[1]
			if UID26EE[0]== False:
				try:
					UID26DF=UID26F7
					UID26DC=UID26F7.moveTo(UID26F4,UID26F1,UID26EB)
					UID271E=UID26EE
				except Exception, errorMsg:
					UID271E=[True,1,str(errorMsg)]
					UID26DC=False
					UID26DF=0
			else:
				UID271E=UID26EE
				UID26DC=False
				UID26DF=0
			if UID271E[0]== False:
				UID2721=0.800000
				UID270F=UID2727
				UID270C=UID2727.goToPosture(Constant_UID2644,UID2721)
		elif UID009A=="向左转":
			UID5330=np.array(["moveto"],dtype="S")
			UID54C4=np.array(["turnL"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID54C4
			UID00CE=UID5330
		elif UID009A=="向左走":
			UID466F=np.array(["moveto"],dtype="S")
			UID4636=np.array(["moveL"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID4636
			UID00CE=UID466F
		elif UID009A=="向前走":
			UID4178=np.array(["moveto"],dtype="S")
			UID413D=np.array(["moveF"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID413D
			UID00CE=UID4178
		elif UID009A=="向后走":
			UID42D4=np.array(["moveto"],dtype="S")
			UID42B3=np.array(["moveB"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID42B3
			UID00CE=UID42D4
		elif UID009A=="向后转":
			UID4534=np.array(["moveto"],dtype="S")
			UID4512=np.array(["turnB"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID4512
			UID00CE=UID4534
		elif UID009A=="向右转":
			UID3F10=np.array(["moveto"],dtype="S")
			UID3E7D=np.array(["turnR"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID3E7D
			UID00CE=UID3F10
		elif UID009A=="向右走":
			UID48B4=np.array(["moveto"],dtype="S")
			UID4875=np.array(["moveR"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID4875
			UID00CE=UID48B4
		elif UID009A=="小齐小齐":
			Constant_UID0B41="Stand"
			UID17CC=np.array(["xunfei"],dtype="S")
			UID0102=False
			UID2A5F=UID023A[2]
			UID0A92=UID023A[7]
			UID297B=UID023A[8]
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID019E
			UID00CE=UID17CC
			try:
				UID0A7A=UID0A92
				UID0A92.unsubscribe(UID0136)
				UID0AB4=[False,0,""]
			except Exception, errorMsg:
				UID0AB4=[True,1,str(errorMsg)]
				UID0A7A=0
			if UID0AB4[0]== False:
				try:
					UID0AB7=0.800000
					UID29A3=UID297B
					UID0AA1=UID297B.goToPosture(Constant_UID0B41,UID0AB7)
					UID2A56=UID0AB4
				except Exception, errorMsg:
					UID2A56=[True,1,str(errorMsg)]
					UID0AA1=False
					UID29A3=0
			else:
				UID2A56=UID0AB4
				UID0AA1=False
				UID29A3=0
			if UID2A56[0]== False:
				try:
					UID2A46=UID2A5F
					if False==True:
						UID2A5F.post.say("您好！","contextual")
					else:
						UID2A5F.say("您好！","contextual")
					UID299A=UID2A56
				except Exception, errorMsg:
					UID299A=[True,1,str(errorMsg)]
					UID2A46=0
			else:
				UID299A=UID2A56
				UID2A46=0
			if UID299A[0]== False:
				UID299D=0.800000
				UID298A=UID29A3
				UID2987=UID29A3.goToPosture(Constant_UID0B41,UID299D)
		elif UID009A=="gangnam style" or UID009A=="韩国舞" or UID009A=="江南style" or UID009A=="骑马舞":
			UID4FD3=np.array(["gangnamstyle"],dtype="S")
			UID5269=np.array(["dance"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID4FD3
			UID00CE=UID5269
		elif UID009A=="小苹果" or UID009A=="小苹果舞":
			UID5417=np.array(["littleapple"],dtype="S")
			UID5577=np.array(["dance"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID5417
			UID00CE=UID5577
		elif UID009A=="太极" or UID009A=="太极舞" or UID009A=="中国舞":
			UID343E=np.array(["taiji"],dtype="S")
			UID347C=np.array(["dance"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID343E
			UID00CE=UID347C
		elif UID009A=="Michael Jackson" or UID009A=="Thriller" or UID009A=="惊悚" or UID009A=="太空舞":
			UID416E=np.array(["dance"],dtype="S")
			UID56A0=np.array(["thriller"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID56A0
			UID00CE=UID416E
		elif UID009A=="飞鹰舞":
			UID5758=np.array(["eagledance"],dtype="S")
			UID1D03=np.array(["dance"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID5758
			UID00CE=UID1D03
		elif UID009A=="快乐的心":
			UID4A31=np.array(["happyheart"],dtype="S")
			UID4A0E=np.array(["dance"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID4A31
			UID00CE=UID4A0E
		elif UID009A=="大篷车" or UID009A=="大鹏车":
			UID4CA1=np.array(["caravanpalace"],dtype="S")
			UID4C6A=np.array(["dance"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID4CA1
			UID00CE=UID4C6A
		elif UID009A=="新小苹果":
			UID44F5=np.array(["littleapple2"],dtype="S")
			UID465F=np.array(["dance"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID44F5
			UID00CE=UID465F
		elif UID009A=="鼓掌":
			UID54F0=np.array(["applaud"],dtype="S")
			UID54CD=np.array(["dance"],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID54F0
			UID00CE=UID54CD
		elif UID009A=="坐下":
			UID0102=False
			UID4A57=np.array(["RerunVoicecloud"])
			UID4089=UID023A[8]
			UID393A=UID023A[7]
			UID38A9=UID023A[6]
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID019E
			try:
				UID38D5=UID393A
				UID393A.unsubscribe(UID0136)
				UID4077=[False,0,""]
			except Exception, errorMsg:
				UID4077=[True,1,str(errorMsg)]
				UID38D5=0
			UID00CE=UID4A57
			if UID4077[0]== False:
				UID407D=0.800000
				UID4060=UID4089
				UID405B=UID4089.goToPosture("Sit",UID407D)
		elif UID009A=="蹲下" or UID009A=="休息":
			UID016A=np.array([],dtype="S")
			UID0102=False
			UID4DCF=UID023A[7]
			UID4F42=UID023A[6]
			UID4AF4=np.array(["RerunVoicecloud"])
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			try:
				UID4DB7=UID4DCF
				UID4DCF.unsubscribe(UID0136)
				UID4F39=[False,0,""]
			except Exception, errorMsg:
				UID4F39=[True,1,str(errorMsg)]
				UID4DB7=0
			UID00CE=UID4AF4
			if UID4F39[0]== False:
				UID4F2A=UID4F42
				UID4F42.rest()
		elif UID009A=="你叫什么" or UID009A=="你叫什么名字" or UID009A=="你是谁":
			UID016A=np.array([],dtype="S")
			UID0102=False
			UID58FE=np.array(["RerunVoicecloud"])
			UID6121=UID023A[3]
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID6109=UID6121
			UID6121.say("我是小齐，很高兴遇见你")
			UID00CE=UID58FE
		elif UID009A=="声音开大点":
			UID016A=np.array([],dtype="S")
			UID0102=False
			UID5C50=np.array(["RerunVoicecloud"])
			UID6270=UID023A[4]
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID6258=UID6270
			UID6270.setOutputVolume(95)
			UID00CE=UID5C50
		elif UID009A=="声音开小点":
			UID016A=np.array([],dtype="S")
			UID0102=False
			UID5D7F=np.array(["RerunVoicecloud"])
			UID3FDD=UID023A[4]
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID3E23=UID3FDD
			UID3FDD.setOutputVolume(50)
			UID00CE=UID5D7F
		elif UID009A=="立正" or UID009A=="站起来":
			UID0102=False
			UID5759=UID023A[8]
			UID59C8=UID023A[7]
			UID55A0=UID023A[6]
			UID521B=np.array(["RerunVoicecloud"])
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID019E
			try:
				UID59B0=UID59C8
				UID59C8.unsubscribe(UID0136)
				UID5597=[False,0,""]
			except Exception, errorMsg:
				UID5597=[True,1,str(errorMsg)]
				UID59B0=0
			UID00CE=UID521B
			if UID5597[0]== False:
				try:
					UID5588=UID55A0
					UID55A0.wakeUp()
					UID5736=UID5597
				except Exception, errorMsg:
					UID5736=[True,1,str(errorMsg)]
					UID5588=0
			else:
				UID5736=UID5597
				UID5588=0
			if UID5736[0]== False:
				UID5739=0.800000
				UID5727=UID5759
				UID5724=UID5759.goToPosture("Stand",UID5739)
		elif UID009A=="xunfei":
			UID0102=False
			UID1BB8=UID023A[14]
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID1BB5=[False,0,""]
			UID093C=NAO_ASR.main(UID1BB5,UID1BB8,UID1C60)
			UID1B9D=UID093C[0]
			UID1BA6=UID093C[1]
			UID0256=""==UID1BA6
			UID021E=UID1B9D[0]
			UID1D7E=UID0256|UID021E
			UID02F4=UID1BA6
			UID1F8F=UID1B9D
			UID1D6E=UID019E
			if UID1D7E==True:
				UID051C=np.array(["RerunVoicecloud"],dtype="S")
				UID1D19=UID1D6E
				UID1E5B=UID051C
			else: 
				if UID1F8F[0]== False:
					try:
						UID1F1E=json.loads(UID02F4)
						UID1F2D=0
						UID1F2A=0
						UID0394=UID1F8F
					except Exception, errorMsg:
						UID0394=[True,1,str(errorMsg)]
						UID1F2A=0
						UID1F2D=0
						UID1F1E=None
				else:
					UID0394=UID1F8F
					UID1F2A=0
					UID1F2D=0
					UID1F1E=None
				UID00BF=semantic_getResult.main(UID0394,UID1F1E)
				UID2004=UID00BF[0]
				UID0364=UID00BF[1]
				UID1D31=UID1D6E
				if UID2004[0]==True:
					UID0AE0=np.array(["RerunVoicecloud"],dtype="S")
					UID1D2E=UID1D31
					UID2280=UID0AE0
				else: 
					UID182D=UID0364[0]
					UID1DF8=UID0364
					if UID182D==1 or UID182D==2 or UID182D==4:
						UID19B9=np.array(["AnimatedSay","RerunVoicecloud"],dtype="S")
						UID1CD6=UID1DF8[4]
						UID1B8B=UID19B9
						UID1CCA=[False,0,""]
						UID1C98=tuling3.main(UID1CCA,UID1CD6,"36f566b00576f4037bfca354e1af6555")
						UID1CA0=UID1C98[0]
						UID1920=UID1C98[1]
						UID1CA9=UID1C98[2]
						UID1D41=np.array([UID1920])
						UID1D49=UID1D41
					else: 
						UID1E1D=UID1DF8[2]
						UID1D3D=UID1DF8[3]
						UID1676=len(UID1E1D)
						UID1D49=UID1D3D
						UID1DBA=UID1676==0
						UID1DDE=UID1E1D
						if UID1DBA==True:
							UID1E82=np.array(["RerunVoicecloud"],dtype="S")
							UID1DD2=UID1E82
						else: 
							UID1DD2=UID1DDE
						UID1B8B=UID1DD2
					UID1D2E=UID1D49
					UID2280=UID1B8B
				UID1D19=UID1D2E
				UID1E5B=UID2280
			UID016A=UID1D19
			UID00CE=UID1E5B
		elif UID009A=="song_search":
			Constant_UID2876="Stand"
			UID0102=False
			AnimatedSpeechRef_2B54=UID023A[2]
			UID278B=UID023A[8]
			try:
				UID2B5F=UID019E[0]
			except:
				UID2B5F=""
			try:
				UID2CDB=UID019E[1]
			except:
				UID2CDB=""
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			UID00CE=UID2DC3
			try:
				UID2781=0.800000
				UID1F5A=UID278B
				UID274B=UID278B.goToPosture(Constant_UID2876,UID2781)
				UID273A=[False,0,""]
			except Exception, errorMsg:
				UID273A=[True,1,str(errorMsg)]
				UID274B=False
				UID1F5A=0
			ErrorOut_2D65=UID273A
			queue_ErrorOut_2E85=Queue.Queue()
			thread.start_new_thread(UID2B35,(AnimatedSpeechRef_2B54,UID2B5F,ErrorOut_2D65,queue_ErrorOut_2E85,))
			ErrorOut_2D30=UID273A
			queue_error_out_2E2F=Queue.Queue()
			queue_songInfo_2C6D=Queue.Queue()
			thread.start_new_thread(UID2C87,(UID2CDB,ErrorOut_2D30,queue_error_out_2E2F,queue_songInfo_2C6D,))
			ErrorOut_2E85=queue_ErrorOut_2E85.get()
			queue_ErrorOut_2E85.put(ErrorOut_2E85)
			error_out_2E2F=queue_error_out_2E2F.get()
			queue_error_out_2E2F.put(error_out_2E2F)
			UID2EAF_Errors=[ErrorOut_2E85,error_out_2E2F]
			Error00D3=UID2EAF_Errors
			Error013C=-1
			Error01A6_Stop=False
			Error012A_IndexsIn=[]
			Error012A_IndexsIn.append(len(Error00D3))
			Error012A_Indexmin=min(Error012A_IndexsIn)
			Error012A_count=Error012A_Indexmin
			while Error01A6_Stop==False and Error013C<Error012A_count-1:
				Error013C=Error013C+1
				Error00E7=Error00D3[Error013C][0]
				Error0190=Error00D3[Error013C]
				Error01A6_Stop=Error00E7
			UID1F51=Error0190
			songInfo_2C6D=queue_songInfo_2C6D.get()
			queue_songInfo_2C6D.put(songInfo_2C6D)
			UID1DD8=songInfo_2C6D[5]
			UID1B6B=songInfo_2C6D[6]
			UID1B59=np.array([UID1DD8])
			if UID1F51[0]== False:
				UID1F54=0.800000
				UID1F1A=UID1F5A
				UID1F17=UID1F5A.goToPosture(Constant_UID2876,UID1F54)
			UID030A=UID1B6B
			UID016A=UID1B59
		elif UID009A=="song_search_artist_song":
			Constant_UID3995="Stand"
			UID0102=False
			AnimatedSpeechRef_39C3=UID023A[2]
			UID3990=UID023A[8]
			try:
				UID39CF=UID019E[0]
			except:
				UID39CF=""
			try:
				UID2720=UID019E[1]
			except:
				UID2720=""
			try:
				UID28A6=UID019E[2]
			except:
				UID28A6=""
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			UID00CE=UID2DC3
			try:
				UID398A=0.800000
				UID3BA0=UID3990
				UID20F4=UID3990.goToPosture(Constant_UID3995,UID398A)
				UID20E2=[False,0,""]
			except Exception, errorMsg:
				UID20E2=[True,1,str(errorMsg)]
				UID20F4=False
				UID3BA0=0
			ErrorOut_39D8=UID20E2
			queue_ErrorOut_39DE=Queue.Queue()
			thread.start_new_thread(UID39C1,(AnimatedSpeechRef_39C3,UID39CF,ErrorOut_39D8,queue_ErrorOut_39DE,))
			ErrorOut_3AA8=UID20E2
			queue_error_out_3AB1=Queue.Queue()
			queue_songInfo_2CE6=Queue.Queue()
			thread.start_new_thread(UID3A99,(ErrorOut_3AA8,queue_error_out_3AB1,UID2720,UID28A6,queue_songInfo_2CE6,))
			ErrorOut_39DE=queue_ErrorOut_39DE.get()
			queue_ErrorOut_39DE.put(ErrorOut_39DE)
			error_out_3AB1=queue_error_out_3AB1.get()
			queue_error_out_3AB1.put(error_out_3AB1)
			UID3B67_Errors=[ErrorOut_39DE,error_out_3AB1]
			Error00D3=UID3B67_Errors
			Error013C=-1
			Error01A6_Stop=False
			Error012A_IndexsIn=[]
			Error012A_IndexsIn.append(len(Error00D3))
			Error012A_Indexmin=min(Error012A_IndexsIn)
			Error012A_count=Error012A_Indexmin
			while Error01A6_Stop==False and Error013C<Error012A_count-1:
				Error013C=Error013C+1
				Error00E7=Error00D3[Error013C][0]
				Error0190=Error00D3[Error013C]
				Error01A6_Stop=Error00E7
			UID3B97=Error0190
			songInfo_2CE6=queue_songInfo_2CE6.get()
			queue_songInfo_2CE6.put(songInfo_2CE6)
			UID3B78=songInfo_2CE6[5]
			UID38B7=songInfo_2CE6[6]
			UID38A5=np.array([UID3B78])
			if UID3B97[0]== False:
				UID3B9A=0.800000
				UID3B88=UID3BA0
				UID3B85=UID3BA0.goToPosture(Constant_UID3995,UID3B9A)
			UID030A=UID38B7
			UID016A=UID38A5
		elif UID009A=="song_search_random":
			Constant_UID3686="Stand"
			UID030A=0
			UID0102=False
			AnimatedSpeechRef_36BA=UID023A[2]
			UID3681=UID023A[8]
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			UID00CE=UID2DC3
			try:
				UID367B=0.800000
				UID3FB5=UID3681
				UID3660=UID3681.goToPosture(Constant_UID3686,UID367B)
				UID3658=[False,0,""]
			except Exception, errorMsg:
				UID3658=[True,1,str(errorMsg)]
				UID3660=False
				UID3FB5=0
			ErrorOut_36CB=UID3658
			queue_ErrorOut_36DD=Queue.Queue()
			thread.start_new_thread(UID36B4,(AnimatedSpeechRef_36BA,ErrorOut_36CB,queue_ErrorOut_36DD,))
			ErrorOut_3812=UID3658
			queue_error_out_3833=Queue.Queue()
			queue_UID383A=Queue.Queue()
			thread.start_new_thread(UID3808,(ErrorOut_3812,queue_error_out_3833,queue_UID383A,))
			ErrorOut_36DD=queue_ErrorOut_36DD.get()
			queue_ErrorOut_36DD.put(ErrorOut_36DD)
			error_out_3833=queue_error_out_3833.get()
			queue_error_out_3833.put(error_out_3833)
			UID3F52_Errors=[ErrorOut_36DD,error_out_3833]
			Error00D3=UID3F52_Errors
			Error013C=-1
			Error01A6_Stop=False
			Error012A_IndexsIn=[]
			Error012A_IndexsIn.append(len(Error00D3))
			Error012A_Indexmin=min(Error012A_IndexsIn)
			Error012A_count=Error012A_Indexmin
			while Error01A6_Stop==False and Error013C<Error012A_count-1:
				Error013C=Error013C+1
				Error00E7=Error00D3[Error013C][0]
				Error0190=Error00D3[Error013C]
				Error01A6_Stop=Error00E7
			UID3FAC=Error0190
			UID383A=queue_UID383A.get()
			queue_UID383A.put(UID383A)
			UID016A=UID383A
			if UID3FAC[0]== False:
				UID3FAF=0.800000
				UID3F9D=UID3FB5
				UID3F9A=UID3FB5.goToPosture(Constant_UID3686,UID3FAF)
		elif UID009A=="song_search_tinguid":
			Constant_UID2034="Stand"
			UID030A=0
			UID0102=False
			AnimatedSpeechRef_2224=UID023A[2]
			UID1FDE=UID023A[8]
			try:
				UID224F=UID019E[0]
			except:
				UID224F=""
			try:
				UID2429=UID019E[1]
			except:
				UID2429=""
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			UID00CE=UID2DC3
			try:
				UID1FD7=0.800000
				UID2C23=UID1FDE
				UID1FBE=UID1FDE.goToPosture(Constant_UID2034,UID1FD7)
				UID1FB5=[False,0,""]
			except Exception, errorMsg:
				UID1FB5=[True,1,str(errorMsg)]
				UID1FBE=False
				UID2C23=0
			ErrorOut_225C=UID1FB5
			queue_ErrorOut_2262=Queue.Queue()
			thread.start_new_thread(UID2220,(AnimatedSpeechRef_2224,UID224F,ErrorOut_225C,queue_ErrorOut_2262,))
			ErrorOut_242F=UID1FB5
			queue_error_out_2433=Queue.Queue()
			queue_UID4434=Queue.Queue()
			thread.start_new_thread(UID2423,(UID2429,ErrorOut_242F,queue_error_out_2433,queue_UID4434,))
			ErrorOut_2262=queue_ErrorOut_2262.get()
			queue_ErrorOut_2262.put(ErrorOut_2262)
			error_out_2433=queue_error_out_2433.get()
			queue_error_out_2433.put(error_out_2433)
			UID2BE3_Errors=[ErrorOut_2262,error_out_2433]
			Error00D3=UID2BE3_Errors
			Error013C=-1
			Error01A6_Stop=False
			Error012A_IndexsIn=[]
			Error012A_IndexsIn.append(len(Error00D3))
			Error012A_Indexmin=min(Error012A_IndexsIn)
			Error012A_count=Error012A_Indexmin
			while Error01A6_Stop==False and Error013C<Error012A_count-1:
				Error013C=Error013C+1
				Error00E7=Error00D3[Error013C][0]
				Error0190=Error00D3[Error013C]
				Error01A6_Stop=Error00E7
			UID2C16=Error0190
			UID4434=queue_UID4434.get()
			queue_UID4434.put(UID4434)
			UID016A=UID4434
			if UID2C16[0]== False:
				UID2C1A=0.800000
				UID2C05=UID2C23
				UID2C02=UID2C23.goToPosture(Constant_UID2034,UID2C1A)
		elif UID009A=="song_search_artist":
			Constant_UID323A="Stand"
			UID0102=False
			AnimatedSpeechRef_3268=UID023A[2]
			UID3235=UID023A[8]
			try:
				UID326C=UID019E[0]
			except:
				UID326C=""
			try:
				UID38FC=UID019E[1]
			except:
				UID38FC=""
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID00CE=UID2DC3
			try:
				UID322D=0.800000
				UID35C4=UID3235
				UID3211=UID3235.goToPosture(Constant_UID323A,UID322D)
				UID320B=[False,0,""]
			except Exception, errorMsg:
				UID320B=[True,1,str(errorMsg)]
				UID3211=False
				UID35C4=0
			ErrorOut_3270=UID320B
			queue_ErrorOut_3274=Queue.Queue()
			thread.start_new_thread(UID3266,(AnimatedSpeechRef_3268,UID326C,ErrorOut_3270,queue_ErrorOut_3274,))
			ErrorOut_3906=UID320B
			queue_error_out_390C=Queue.Queue()
			queue_UID3914=Queue.Queue()
			thread.start_new_thread(UID38DC,(UID38FC,ErrorOut_3906,queue_error_out_390C,queue_UID3914,))
			ErrorOut_3274=queue_ErrorOut_3274.get()
			queue_ErrorOut_3274.put(ErrorOut_3274)
			error_out_390C=queue_error_out_390C.get()
			queue_error_out_390C.put(error_out_390C)
			UID358B_Errors=[ErrorOut_3274,error_out_390C]
			Error00D3=UID358B_Errors
			Error013C=-1
			Error01A6_Stop=False
			Error012A_IndexsIn=[]
			Error012A_IndexsIn.append(len(Error00D3))
			Error012A_Indexmin=min(Error012A_IndexsIn)
			Error012A_count=Error012A_Indexmin
			while Error01A6_Stop==False and Error013C<Error012A_count-1:
				Error013C=Error013C+1
				Error00E7=Error00D3[Error013C][0]
				Error0190=Error00D3[Error013C]
				Error01A6_Stop=Error00E7
			UID35BB=Error0190
			UID3914=queue_UID3914.get()
			queue_UID3914.put(UID3914)
			UID016A=UID3914
			if UID35BB[0]== False:
				UID35BE=0.800000
				UID35AC=UID35C4
				UID35A9=UID35C4.goToPosture(Constant_UID323A,UID35BE)
		elif UID009A=="song_play":
			UID0102=False
			try:
				UID283D=UID019E[0]
			except:
				UID283D=""
			UID3669=UID023A[2]
			UID3600=UID023A[6]
			UID35CC=UID023A[5]
			UID3445=UID023A[9]
			UID3342=UID023A[8]
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID016A=UID019E
			UID00CE=UID2DC3
			UID341B=UID283D==""
			UID345A=UID033E
			UID35F1=UID0206
			UID360C=UID283D
			if UID341B==True:
				UID36B8=False
				UID1C68=UID3669
				if UID36B8==True:
					UID3669.post.say("抱歉，未能找到相应歌曲","contextual")
				else:
					UID3669.say("抱歉，未能找到相应歌曲","contextual")
			else: 
				UID2D0F=np.array(["move1.py","move2.py","move3.py","move4.py"],dtype="S")
				try:
					UID2031=UID3445
					if True==True:
						UID3445.post.playWebStream(UID360C,1.000000,0.000000)
					else:
						UID3445.playWebStream(UID360C,1.000000,0.000000)
					UID223A=[False,0,""]
				except Exception, errorMsg:
					UID223A=[True,1,str(errorMsg)]
					UID2031=0
				appended_path_2AA9=os.path.join(UID35F1,"movements")
				UID29DD=1000*UID345A
				
				UID241B=int(time.time()*1000)
				UID2421=UID241B
				UID232E=UID223A
				ErrorOut_322C=UID232E
				millisecond_timer_value_2794=UID2421
				ALMemoryRef_2CCF=UID35CC
				UID2D91=UID2D0F
				ALMotionRef_3101=UID3600
				queue_ErrorOut_322C=Queue.Queue()
				thread.start_new_thread(UID247D,(millisecond_timer_value_2794,UID29DD,ALMemoryRef_2CCF,appended_path_2AA9,UID2D91,ALMotionRef_3101,ErrorOut_322C,queue_ErrorOut_322C,))
				ErrorOut_322C=queue_ErrorOut_322C.get()
				queue_ErrorOut_322C.put(ErrorOut_322C)
				UID07E7=0
				UID042D=Clear_Errors.main(ErrorOut_322C,UID07E7)
				UID2027=UID042D[0]
				UID0794=UID042D[1]
				if UID2027[0]== False:
					try:
						UID1FF2=UID2031
						UID2031.stopAll()
						UID2296=UID2027
					except Exception, errorMsg:
						UID2296=[True,1,str(errorMsg)]
						UID1FF2=0
				else:
					UID2296=UID2027
					UID1FF2=0
				UID22A5=0
				UID2277=Clear_Errors.main(UID2296,UID22A5)
				UID31A0=UID2277[0]
				UID2290=UID2277[1]
				if UID31A0[0]== False:
					UID31A8=0.800000
					UID317B=UID3342
					UID3171=UID3342.goToPosture("Stand",UID31A8)
		elif UID009A=="song_play_all":
			UID016A=np.array([],dtype="S")
			UID0102=False
			UID2A0E=UID023A[2]
			ALMotionRef_47F9=UID023A[6]
			ALMemoryRef_482D=UID023A[5]
			AudioPlayer_4857=UID023A[9]
			ALPostureRef_3E08=UID023A[8]
			appended_path_44F6=os.path.join(UID0206,"movements")
			UID03DA=UID040E
			UID03A6=UID0372
			UID030A=UID033E
			UID02D6=UID02A2
			UID00CE=UID2DC3
			UID4EAE=UID019E
			i_3156=-1
			ForS_D1S_ADS_BBS_B7_330D_Stop=False
			ForS_D1S_ADS_BBS_B7_3142_IndexsIn=[]
			ForS_D1S_ADS_BBS_B7_3142_IndexsIn.append(len(UID4EAE))
			ForS_D1S_ADS_BBS_B7_3142_Indexmin=min(ForS_D1S_ADS_BBS_B7_3142_IndexsIn)
			ForS_D1S_ADS_BBS_B7_3142_count=ForS_D1S_ADS_BBS_B7_3142_Indexmin
			while ForS_D1S_ADS_BBS_B7_330D_Stop==False and i_3156<ForS_D1S_ADS_BBS_B7_3142_count-1:
				i_3156=i_3156+1
				UID3A9C=[False,0,""]
				UID394C=BaiduMusic_GetLink.main(UID3A9C,UID4EAE[i_3156])
				UID395A=UID394C[0]
				UID3EB9=UID394C[1]
				UID4701=UID3EB9[5]
				UID4951=UID3EB9[6]
				try:
					UID4923=AudioPlayer_4857
					if True==True:
						AudioPlayer_4857.post.playWebStream(UID4701,1.000000,0.000000)
					else:
						AudioPlayer_4857.playWebStream(UID4701,1.000000,0.000000)
					UID4709=[False,0,""]
				except Exception, errorMsg:
					UID4709=[True,1,str(errorMsg)]
					UID4923=0
				UID472F=1000*UID4951
				
				UID4714=int(time.time()*1000)
				UID4711=UID4714
				UID470D=UID4709
				ALMotionRef_474A=ALMotionRef_47F9
				ALMemoryRef_4734=ALMemoryRef_482D
				ErrorOut_4739=UID470D
				millisecond_timer_value_472A=UID4711
				appended_path_44E7=appended_path_44F6
				queue_UID335F=Queue.Queue()
				queue_ErrorOut_4739=Queue.Queue()
				thread.start_new_thread(UID4728,(millisecond_timer_value_472A,UID472F,ALMemoryRef_4734,ALMotionRef_474A,queue_UID335F,appended_path_44E7,ErrorOut_4739,queue_ErrorOut_4739,))
				ErrorOut_4739=queue_ErrorOut_4739.get()
				queue_ErrorOut_4739.put(ErrorOut_4739)
				UID4973=0
				UID4957=Clear_Errors.main(ErrorOut_4739,UID4973)
				UID491A=UID4957[0]
				UID4964=UID4957[1]
				UID335F=queue_UID335F.get()
				queue_UID335F.put(UID335F)
				ForS_D1S_ADS_BBS_B7_330D_Stop=UID335F
				if UID491A[0]== False:
					try:
						UID490A=UID4923
						UID4923.stopAll()
						UID4935=UID491A
					except Exception, errorMsg:
						UID4935=[True,1,str(errorMsg)]
						UID490A=0
				else:
					UID4935=UID491A
					UID490A=0
				UID493E=0
				UID4926=Clear_Errors.main(UID4935,UID493E)
				UID3BA9=UID4926[0]
				UID4932=UID4926[1]
				if UID3BA9[0]== False:
					UID3BAE=0.800000
					UID3B8A=ALPostureRef_3E08
					UID3B81=ALPostureRef_3E08.goToPosture("Stand",UID3BAE)
		elif UID009A=="请退出程序":
			UID030A=0
			UID016A=np.array([],dtype="S")
			UID37D4=UID023A[11]
			UID3786=UID023A[10]
			UID37FB=UID023A[6]
			UID374D=UID023A[7]
			UID0100=np.array([""])
			UID03DA=UID040E
			UID03A6=UID0372
			UID02D6=UID02A2
			UID0102=True
			try:
				UID3735=UID374D
				UID374D.unsubscribe(UID0136)
				UID37F2=[False,0,""]
			except Exception, errorMsg:
				UID37F2=[True,1,str(errorMsg)]
				UID3735=0
			UID00CE=UID0100
			if UID37F2[0]== False:
				try:
					UID37E3=UID37FB
					UID37FB.rest()
					UID377D=UID37F2
				except Exception, errorMsg:
					UID377D=[True,1,str(errorMsg)]
					UID37E3=0
			else:
				UID377D=UID37F2
				UID37E3=0
			if UID377D[0]== False:
				try:
					UID376E=UID3786
					UID3786.unsubscribe(UID0136)
					UID37CB=UID377D
				except Exception, errorMsg:
					UID37CB=[True,1,str(errorMsg)]
					UID376E=0
			else:
				UID37CB=UID377D
				UID376E=0
			if UID37CB[0]== False:
				try:
					UID37AD=UID37D4
					UID37D4.stopTracker()
					UID37A4=UID37CB
				except Exception, errorMsg:
					UID37A4=[True,1,str(errorMsg)]
					UID37AD=0
			else:
				UID37A4=UID37CB
				UID37AD=0
			if UID37A4[0]== False:
				try:
					UID3795=UID37AD
					UID37AD.unregisterAllTargets()
					UID1CB8=UID37A4
				except Exception, errorMsg:
					UID1CB8=[True,1,str(errorMsg)]
					UID3795=0
			else:
				UID1CB8=UID37A4
				UID3795=0
			UID1CC1=0
			UID07AE=Clear_Errors.main(UID1CB8,UID1CC1)
			UID1F04=UID07AE[0]
			UID1CB5=UID07AE[1]
			if UID1F04[0]== False:
				try:
					UID1EF5=xfdll.MSPLogout()
					UID1FF3=UID1F04
				except Exception, errorMsg:
					UID1FF3=[True,1,str(errorMsg)]
					UID1EF5=0
			else:
				UID1FF3=UID1F04
				UID1EF5=0
			UID1FFC=0
			UID00BB=Clear_Errors.main(UID1FF3,UID1FFC)
			UID01F2=UID00BB[0]
			UID1FF0=UID00BB[1]
		else: 
			UID29BC=np.array(["Listen"],dtype="S")
			UID030A=0
			UID02D6=np.array([],dtype="S")
			UID0102=False
			UID03DA=UID040E
			UID03A6=UID0372
			UID016A=UID019E
			UID00CE=UID29BC
		While_Loop_0089_Stop=UID0102
		millisecond_timer_value_0075=UID03DA
		
		UID006C=UID03A6
		
		UID0063=UID030A
		
		UID005A=UID02D6
		
		UID0041=UID016A
		
		UID0034=UID00CE
		
	queue_UID002B.put(1)
def UID127D(ALMemoryRef_1280,ErrorOut_1288,queue_UID127D,):
	i_1294=-1
	While_Loop_1297_Stop=False
	while While_Loop_1297_Stop==False:
		UID129A=np.array(["Device/SubDeviceList/Head/Touch/Front/Sensor/Value","Device/SubDeviceList/Head/Touch/Rear/Sensor/Value","Device/SubDeviceList/Head/Touch/Middle/Sensor/Value"],dtype="S")
		time.sleep((500-int(time.time()*1000)%500)/1000.0)
		if ErrorOut_1288[0]== False:
			try:
				UID1337=ALMemoryRef_1280
				UID1308=np.array(ALMemoryRef_1280.getListData(UID129A.tolist()))
				UID132E=ErrorOut_1288
			except Exception, errorMsg:
				UID132E=[True,1,str(errorMsg)]
				UID1308=np.array([],dtype="float64")
				UID1337=0
		else:
			UID132E=ErrorOut_1288
			UID1308=np.array([],dtype="float64")
			UID1337=0
		UID1310=np.sum(UID1308)
		if UID132E[0]== False:
			UID131F=UID1337
			UID134B=UID1337.getData("ALTextToSpeech/CurrentSentence")
		UID1356=UID1310>0
		UID1353=UID134B==""
		While_Loop_1297=UID1356|UID1353
		While_Loop_1297_Stop=While_Loop_1297
	queue_UID127D.put(1)
def UID14F0(ALMemoryRef_14F3,queue_ErrorOut_14F7,ErrorOut_14FB,):
	i_1507=-1
	While_Loop_150A_Stop=False
	while While_Loop_150A_Stop==False:
		UID150D=np.array(["Device/SubDeviceList/Head/Touch/Front/Sensor/Value","Device/SubDeviceList/Head/Touch/Rear/Sensor/Value","Device/SubDeviceList/Head/Touch/Middle/Sensor/Value"],dtype="S")
		time.sleep((500-int(time.time()*1000)%500)/1000.0)
		if ErrorOut_14FB[0]== False:
			try:
				UID15AA=ALMemoryRef_14F3
				UID157B=np.array(ALMemoryRef_14F3.getListData(UID150D.tolist()))
				UID15A1=ErrorOut_14FB
			except Exception, errorMsg:
				UID15A1=[True,1,str(errorMsg)]
				UID157B=np.array([],dtype="float64")
				UID15AA=0
		else:
			UID15A1=ErrorOut_14FB
			UID157B=np.array([],dtype="float64")
			UID15AA=0
		UID1583=np.sum(UID157B)
		if UID15A1[0]== False:
			try:
				UID1592=UID15AA
				UID15BE=UID15AA.getData("ALTextToSpeech/CurrentSentence")
				UID14FA=UID15A1
			except Exception, errorMsg:
				UID14FA=[True,1,str(errorMsg)]
				UID15BE=""
				UID1592=0
		else:
			UID14FA=UID15A1
			UID15BE=""
			UID1592=0
		UID15C9=UID1583>0
		UID15C6=UID15BE==""
		ErrorOut_14F7=UID14FA
		While_Loop_150A=UID15C9|UID15C6
		While_Loop_150A_Stop=While_Loop_150A
	queue_ErrorOut_14F7.put(ErrorOut_14F7)
def UID2315(queue_UID2318,millisecond_timer_value_231C,UID2320,ALMotionRef_2324,ErrorOut_2328,queue_ErrorOut_232C,):
	i_2338=-1
	While_Loop_233B_Stop=False
	while While_Loop_233B_Stop==False:
		UID234A=np.array(["RHipYawPitch"],dtype="S")
		UID23F6=int(time.time()*1000)
		time.sleep((1000-int(time.time()*1000)%1000)/1000.0)
		UID23AC=ALMotionRef_2324
		UID23C9=np.array(ALMotionRef_2324.getStiffnesses(UID234A.tolist()))
		UID2401=UID23F6-millisecond_timer_value_231C
		ErrorOut_232C=ErrorOut_2328
		try:
			UID23DB=UID23C9[0+0]
		except:
			UID23DB=0.000000
		UID23E3=UID2401>=UID2320
		UID23D5=UID23DB<=0.400000
		While_Loop_233B=UID23D5|UID23E3
		UID2318=UID23D5
		While_Loop_233B_Stop=While_Loop_233B
	queue_UID2318.put(UID2318)
	queue_ErrorOut_232C.put(ErrorOut_232C)
def UID2B35(AnimatedSpeechRef_2B54,UID2B5F,ErrorOut_2D65,queue_ErrorOut_2E85,):
	i_2B47=-1
	WhileS_D1S_ADS_BBS_B7_2B4A_Stop=False
	while WhileS_D1S_ADS_BBS_B7_2B4A_Stop==False:
		WhileS_D1S_ADS_BBS_B7_2B4A_Stop=True
		if ErrorOut_2D65[0]== False:
			try:
				UID21D7=False
				UID21B7=AnimatedSpeechRef_2B54
				if UID21D7==True:
					AnimatedSpeechRef_2B54.post.say(UID2B5F,"contextual")
				else:
					AnimatedSpeechRef_2B54.say(UID2B5F,"contextual")
				UID2E81=ErrorOut_2D65
			except Exception, errorMsg:
				UID2E81=[True,1,str(errorMsg)]
				UID21B7=0
		else:
			UID2E81=ErrorOut_2D65
			UID21B7=0
		ErrorOut_2E85=UID2E81
	queue_ErrorOut_2E85.put(ErrorOut_2E85)
def UID2C87(UID2CDB,ErrorOut_2D30,queue_error_out_2E2F,queue_songInfo_2C6D,):
	i_2C99=-1
	WhileS_D1S_ADS_BBS_B7_2C9C_Stop=False
	while WhileS_D1S_ADS_BBS_B7_2C9C_Stop==False:
		WhileS_D1S_ADS_BBS_B7_2C9C_Stop=True
		UID194E=BaiduMusic_KeyWords.main(ErrorOut_2D30,UID2CDB)
		UID2D89=UID194E[0]
		UID2DA2=UID194E[1]
		if UID2D89[0]==True:
			UID2F6E=[False,0,""]
			UID2DE0=["","","","","","",0,""]
			UID2DCE=UID2F6E
		else: 
			try:
				UID2FEE=UID2DA2[0]
			except:
				UID2FEE=["","",""]
			UID388D=UID2FEE[0]
			UID3848=BaiduMusic_GetLink.main(UID2D89,UID388D)
			UID2DCA=UID3848[0]
			UID2DDF=UID3848[1]
			UID2DE0=UID2DDF
			UID2DCE=UID2DCA
		songInfo_2C6D=UID2DE0
		error_out_2E2F=UID2DCE
	queue_error_out_2E2F.put(error_out_2E2F)
	queue_songInfo_2C6D.put(songInfo_2C6D)
def UID39C1(AnimatedSpeechRef_39C3,UID39CF,ErrorOut_39D8,queue_ErrorOut_39DE,):
	i_39F0=-1
	WhileS_D1S_ADS_BBS_B7_39F4_Stop=False
	while WhileS_D1S_ADS_BBS_B7_39F4_Stop==False:
		WhileS_D1S_ADS_BBS_B7_39F4_Stop=True
		if ErrorOut_39D8[0]== False:
			try:
				UID3A4D=False
				UID3A2F=AnimatedSpeechRef_39C3
				if UID3A4D==True:
					AnimatedSpeechRef_39C3.post.say(UID39CF,"contextual")
				else:
					AnimatedSpeechRef_39C3.say(UID39CF,"contextual")
				UID39E2=ErrorOut_39D8
			except Exception, errorMsg:
				UID39E2=[True,1,str(errorMsg)]
				UID3A2F=0
		else:
			UID39E2=ErrorOut_39D8
			UID3A2F=0
		ErrorOut_39DE=UID39E2
	queue_ErrorOut_39DE.put(ErrorOut_39DE)
def UID3A99(ErrorOut_3AA8,queue_error_out_3AB1,UID2720,UID28A6,queue_songInfo_2CE6,):
	i_3AC5=-1
	WhileS_D1S_ADS_BBS_B7_3AC8_Stop=False
	while WhileS_D1S_ADS_BBS_B7_3AC8_Stop==False:
		WhileS_D1S_ADS_BBS_B7_3AC8_Stop=True
		UID3AF8=UID2720+" "+UID28A6
		UID3AD4=BaiduMusic_KeyWords.main(ErrorOut_3AA8,UID3AF8)
		UID1F67=UID3AD4[0]
		UID38E9=UID3AD4[1]
		if UID1F67[0]==True:
			UID2163=[False,0,""]
			UID38F5=["","","","","","",0,""]
			UID1F9D=UID2163
		else: 
			try:
				UID3AFD=UID38E9[0]
			except:
				UID3AFD=["","",""]
			UID3B34=UID3AFD[0]
			UID3B10=BaiduMusic_GetLink.main(UID1F67,UID3B34)
			UID1F9C=UID3B10[0]
			UID38F4=UID3B10[1]
			UID38F5=UID38F4
			UID1F9D=UID1F9C
		songInfo_2CE6=UID38F5
		error_out_3AB1=UID1F9D
	queue_error_out_3AB1.put(error_out_3AB1)
	queue_songInfo_2CE6.put(songInfo_2CE6)
def UID36B4(AnimatedSpeechRef_36BA,ErrorOut_36CB,queue_ErrorOut_36DD,):
	i_36F1=-1
	WhileS_D1S_ADS_BBS_B7_36F4_Stop=False
	while WhileS_D1S_ADS_BBS_B7_36F4_Stop==False:
		WhileS_D1S_ADS_BBS_B7_36F4_Stop=True
		if ErrorOut_36CB[0]== False:
			try:
				UID3788=False
				UID3761=AnimatedSpeechRef_36BA
				if UID3788==True:
					AnimatedSpeechRef_36BA.post.say("请欣赏音乐","contextual")
				else:
					AnimatedSpeechRef_36BA.say("请欣赏音乐","contextual")
				UID36E5=ErrorOut_36CB
			except Exception, errorMsg:
				UID36E5=[True,1,str(errorMsg)]
				UID3761=0
		else:
			UID36E5=ErrorOut_36CB
			UID3761=0
		ErrorOut_36DD=UID36E5
	queue_ErrorOut_36DD.put(ErrorOut_36DD)
def UID3808(ErrorOut_3812,queue_error_out_3833,queue_UID383A,):
	i_3849=-1
	WhileS_D1S_ADS_BBS_B7_384D_Stop=False
	while WhileS_D1S_ADS_BBS_B7_384D_Stop==False:
		UID32E9=np.array([1,2,6,7,8,9,11,12,13,14,15,21,23,22],dtype="int32")
		UID4B3B=random.random()
		WhileS_D1S_ADS_BBS_B7_384D_Stop=True
		UID4B3F=len(UID32E9)
		UID4B56=np.floor((int(UID4B3F)*UID4B3B))
		UID410B=int(UID4B56)
		UID4105=0
		UID40D8=BaiduMusic_GetList.main(ErrorOut_3812,UID4105,50,UID410B)
		UID386A=UID40D8[0]
		UID387E=UID40D8[1]
		if UID386A[0]==True:
			UID3ACD=[False,0,""]
			UID3884=np.array([],dtype="S")
			UID3877=UID3ACD
		else: 
			UID3894=np.array([],dtype="S")
			error_IO_38D6=UID386A
			songs_38F7=UID387E
			UID38E4=UID3894
			queue_error_IO_38D6=Queue.Queue()
			queue_UID38E4=Queue.Queue()
			thread.start_new_thread(UID38D1,(error_IO_38D6,queue_error_IO_38D6,UID38E4,queue_UID38E4,songs_38F7,))
			UID38E4=queue_UID38E4.get()
			queue_UID38E4.put(UID38E4)
			UID3884=UID38E4
			error_IO_38D6=queue_error_IO_38D6.get()
			queue_error_IO_38D6.put(error_IO_38D6)
			UID3877=error_IO_38D6
		UID383A=UID3884
		error_out_3833=UID3877
	queue_error_out_3833.put(error_out_3833)
	queue_UID383A.put(UID383A)
def UID2220(AnimatedSpeechRef_2224,UID224F,ErrorOut_225C,queue_ErrorOut_2262,):
	i_2278=-1
	WhileS_D1S_ADS_BBS_B7_227D_Stop=False
	while WhileS_D1S_ADS_BBS_B7_227D_Stop==False:
		WhileS_D1S_ADS_BBS_B7_227D_Stop=True
		if ErrorOut_225C[0]== False:
			try:
				UID23C3=False
				UID2399=AnimatedSpeechRef_2224
				if UID23C3==True:
					AnimatedSpeechRef_2224.post.say(UID224F,"contextual")
				else:
					AnimatedSpeechRef_2224.say(UID224F,"contextual")
				UID2266=ErrorOut_225C
			except Exception, errorMsg:
				UID2266=[True,1,str(errorMsg)]
				UID2399=0
		else:
			UID2266=ErrorOut_225C
			UID2399=0
		ErrorOut_2262=UID2266
	queue_ErrorOut_2262.put(ErrorOut_2262)
def UID2423(UID2429,ErrorOut_242F,queue_error_out_2433,queue_UID4434,):
	i_2473=-1
	WhileS_D1S_ADS_BBS_B7_24A2_Stop=False
	while WhileS_D1S_ADS_BBS_B7_24A2_Stop==False:
		WhileS_D1S_ADS_BBS_B7_24A2_Stop=True
		UID1C6B=BaiduMusic_tagToTinguid.main(UID2429)
		UID3145=UID1C6B[0]
		UID3197=UID1C6B[1]
		UID33DA=UID1C6B[2]
		UID31B9=ErrorOut_242F
		UID31DD=UID2429
		if UID3197=="singer":
			UID1F5E=BaiduMusic_GetSingerInfo.main(UID31B9,UID33DA)
			UID33B6=UID1F5E[0]
			UID3490=UID1F5E[1]
			UID3493=UID1F5E[2]
			UID474E=UID3490<=50
			UID4782=UID3490
			if UID474E==True:
				UID4A3E=0
				UID4910=UID4782
			else: 
				UID4E2E=random.random()
				UID436B=UID4782-50
				UID4368=UID4E2E**5.000000
				UID4910=50
				UID437B=np.floor((int(UID436B)*UID4368))
				UID4A36=int(UID437B)
				UID4A3E=UID4A36
			UID3394=BaiduMusic_GetSingerMusic.main(UID33B6,UID4A3E,UID4910,UID33DA)
			UID31C5=UID3394[0]
			UID31AA=UID3394[1]
			UID31C7=UID31C5
			UID31AB=UID31AA
		elif UID3197=="type":
			UID3623=int(str(UID33DA)[0:])
			UID3618=0
			UID1DE2=BaiduMusic_GetList.main(UID31B9,UID3618,50,UID3623)
			UID33E8=UID1DE2[0]
			UID33E2=UID1DE2[1]
			UID31C7=UID33E8
			UID31AB=UID33E2
		else: 
			UID3129=BaiduMusic_KeyWords.main(UID31B9,UID31DD)
			UID31C4=UID3129[0]
			UID31A9=UID3129[1]
			UID31C7=UID31C4
			UID31AB=UID31A9
		UID2503=UID31AB
		UID24F4=UID31C7
		if UID24F4[0]==True:
			UID2A90=[False,0,""]
			UID4446=np.array([],dtype="S")
			UID24FC=UID2A90
		else: 
			songs_3EEF=UID2503
			UID40BE=np.array([],dtype="S")
			i_3CE7=-1
			ForS_D1S_ADS_BBS_B7_3C98_IndexsIn=[]
			ForS_D1S_ADS_BBS_B7_3C98_IndexsIn.append(len(songs_3EEF))
			ForS_D1S_ADS_BBS_B7_3C98_Indexmin=min(ForS_D1S_ADS_BBS_B7_3C98_IndexsIn)
			ForS_D1S_ADS_BBS_B7_3C98_count=ForS_D1S_ADS_BBS_B7_3C98_Indexmin
			for i in range(0, ForS_D1S_ADS_BBS_B7_3C98_count):
				i_3CE7=i_3CE7+1
				UID40B8=songs_3EEF[i_3CE7][0]
				UID40BE=np.concatenate((UID40BE,[UID40B8]))
			UID24FC=UID24F4
			UID4446=UID40BE
		UID4434=UID4446
		error_out_2433=UID24FC
	queue_error_out_2433.put(error_out_2433)
	queue_UID4434.put(UID4434)
def UID3266(AnimatedSpeechRef_3268,UID326C,ErrorOut_3270,queue_ErrorOut_3274,):
	i_3281=-1
	WhileS_D1S_ADS_BBS_B7_3284_Stop=False
	while WhileS_D1S_ADS_BBS_B7_3284_Stop==False:
		WhileS_D1S_ADS_BBS_B7_3284_Stop=True
		if ErrorOut_3270[0]== False:
			try:
				UID32C4=False
				UID32B7=AnimatedSpeechRef_3268
				if UID32C4==True:
					AnimatedSpeechRef_3268.post.say(UID326C,"contextual")
				else:
					AnimatedSpeechRef_3268.say(UID326C,"contextual")
				UID3277=ErrorOut_3270
			except Exception, errorMsg:
				UID3277=[True,1,str(errorMsg)]
				UID32B7=0
		else:
			UID3277=ErrorOut_3270
			UID32B7=0
		ErrorOut_3274=UID3277
	queue_ErrorOut_3274.put(ErrorOut_3274)
def UID38DC(UID38FC,ErrorOut_3906,queue_error_out_390C,queue_UID3914,):
	i_3933=-1
	WhileS_D1S_ADS_BBS_B7_393C_Stop=False
	while WhileS_D1S_ADS_BBS_B7_393C_Stop==False:
		WhileS_D1S_ADS_BBS_B7_393C_Stop=True
		UID3DBF=BaiduMusic_tagToTinguid.main(UID38FC)
		UID22F4=UID3DBF[0]
		UID3DD2=UID3DBF[1]
		UID24D9=UID3DBF[2]
		UID249D=ErrorOut_3906
		UID2CBE=UID38FC
		if UID22F4==True:
			UID4000=BaiduMusic_GetSingerMusic.main(UID249D,0,50,UID24D9)
			UID24B5=UID4000[0]
			UID2482=UID4000[1]
			UID24B8=UID24B5
			UID2487=UID2482
		else: 
			UID27BC=BaiduMusic_KeyWords.main(UID249D,UID2CBE)
			UID24B3=UID27BC[0]
			UID247B=UID27BC[1]
			UID24B8=UID24B3
			UID2487=UID247B
		UID398F=UID2487
		UID3967=UID24B8
		if UID3967[0]==True:
			UID3D1A=[False,0,""]
			UID39B0=np.array([],dtype="S")
			UID3976=UID3D1A
		else: 
			UID3A13=np.array([],dtype="S")
			error_IO_3AC1=UID3967
			songInfos_3B2D=UID398F
			UID3AFA=UID3A13
			queue_error_IO_3AC1=Queue.Queue()
			queue_UID3AFA=Queue.Queue()
			thread.start_new_thread(UID3ABD,(error_IO_3AC1,queue_error_IO_3AC1,UID3AFA,queue_UID3AFA,songInfos_3B2D,))
			UID3AFA=queue_UID3AFA.get()
			queue_UID3AFA.put(UID3AFA)
			UID39B0=UID3AFA
			error_IO_3AC1=queue_error_IO_3AC1.get()
			queue_error_IO_3AC1.put(error_IO_3AC1)
			UID3976=error_IO_3AC1
		UID3914=UID39B0
		error_out_390C=UID3976
	queue_error_out_390C.put(error_out_390C)
	queue_UID3914.put(UID3914)
def UID247D(millisecond_timer_value_2794,UID29DD,ALMemoryRef_2CCF,appended_path_2AA9,UID2D91,ALMotionRef_3101,ErrorOut_322C,queue_ErrorOut_322C,):
	i_2497=-1
	WhileS_D1S_ADS_BBS_B7_249A_Stop=False
	while WhileS_D1S_ADS_BBS_B7_249A_Stop==False:
		UID2BBE=np.array(["Device/SubDeviceList/Head/Touch/Front/Sensor/Value","Device/SubDeviceList/Head/Touch/Rear/Sensor/Value","Device/SubDeviceList/Head/Touch/Middle/Sensor/Value"],dtype="S")
		UID2699=int(time.time()*1000)
		i_2497=i_2497+1
		UID291B=UID2699-millisecond_timer_value_2794
		UID2B74=i_2497//4
		UID2B6E=i_2497%4
		UID3367=UID291B>UID29DD
		try:
			UID2B60=UID2D91[UID2B6E+0]
		except:
			UID2B60=""
		UID2B03=os.path.join(appended_path_2AA9,UID2B60)
		if ErrorOut_322C[0]== False:
			try:
				pythonmodulefolder,pythonmodepath=os.path.split(UID2B03)
				pythonmodule=pythonmodepath[:pythonmodepath.find(".")]
				imp_bbb=pythonmodulefolder+"/"+pythonmodule
				imp_ccc=imp.find_module(pythonmodule,[pythonmodulefolder])
				imp_ddd=imp.load_module(imp_bbb,imp_ccc[0],imp_ccc[1],imp_ccc[2])
				imp_eee=imp_ddd.main()
				UID2AE5=imp_eee[0]
				UID2AE8=imp_eee[1]
				UID2B30=imp_eee[2]
				UID2B2A=ErrorOut_322C
			except Exception, errorMsg:
				UID2B2A=[True,1,str(errorMsg)]
				UID2AE5=""
				UID2AE8=0
				UID2B30=[]
		else:
			UID2B2A=ErrorOut_322C
			UID2AE5=""
			UID2AE8=0
			UID2B30=[]
		if UID2B2A[0]== False:
			try:
				UID2B1B=ALMotionRef_3101
				UID2B30_names=[]
				UID2B30_time=[]
				UID2B30_angle=[]
				for i in UID2B30:
					UID2B30_names.append(i[0])
					UID2B30_time_one=[]
					UID2B30_angle_one=[]
					for j in i[1]:
						UID2B30_time_one.append(j[0])
						UID2B30_angle_one.append([j[1],j[2],j[3]])
					UID2B30_time.append(UID2B30_time_one)
					UID2B30_angle.append(UID2B30_angle_one)
				if False==True:
					ALMotionRef_3101.post.angleInterpolationBezier(UID2B30_names,UID2B30_time,UID2B30_angle)
				else:
					ALMotionRef_3101.angleInterpolationBezier(UID2B30_names,UID2B30_time,UID2B30_angle)
				UID2E32=UID2B2A
			except Exception, errorMsg:
				UID2E32=[True,1,str(errorMsg)]
				UID2B1B=0
		else:
			UID2E32=UID2B2A
			UID2B1B=0
		if UID2E32[0]== False:
			try:
				UID2E1F=ALMemoryRef_2CCF
				UID2F3F=np.array(ALMemoryRef_2CCF.getListData(UID2BBE.tolist()))
				UID2E15=UID2E32
			except Exception, errorMsg:
				UID2E15=[True,1,str(errorMsg)]
				UID2F3F=np.array([],dtype="float64")
				UID2E1F=0
		else:
			UID2E15=UID2E32
			UID2F3F=np.array([],dtype="float64")
			UID2E1F=0
		try:
			UID307F=UID2F3F.tolist().index(1.000000)
		except:
			UID307F=-1
		UID2ACE=UID2E15[0]
		ErrorOut_322C=UID2E15
		
		UID336A=UID307F>=0
		UID2AD3=UID336A|UID3367
		WhileS_D1S_ADS_BBS_B7_249A=UID2AD3|UID2ACE
		WhileS_D1S_ADS_BBS_B7_249A_Stop=WhileS_D1S_ADS_BBS_B7_249A
	ErrorOut_322C=ErrorOut_322C
	queue_ErrorOut_322C.put(ErrorOut_322C)
def UID4728(millisecond_timer_value_472A,UID472F,ALMemoryRef_4734,ALMotionRef_474A,queue_UID335F,appended_path_44E7,ErrorOut_4739,queue_ErrorOut_4739,):
	i_4756=-1
	WhileS_D1S_ADS_BBS_B7_4759_Stop=False
	while WhileS_D1S_ADS_BBS_B7_4759_Stop==False:
					UID475C=np.array(["Device/SubDeviceList/Head/Touch/Front/Sensor/Value","Device/SubDeviceList/Head/Touch/Rear/Sensor/Value","Device/SubDeviceList/Head/Touch/Middle/Sensor/Value"],dtype="S")
					UID46B0=np.array(["move1.py","move2.py","move3.py","move4.py"],dtype="S")
					UID47B2=int(time.time()*1000)
					i_4756=i_4756+1
					UID47BD=UID47B2-millisecond_timer_value_472A
					UID4819=i_4756//4
					UID4811=i_4756%4
					UID4802=UID47BD>UID472F
					try:
						UID4887=UID46B0[UID4811+0]
					except:
						UID4887=""
					UID4849=os.path.join(appended_path_44E7,UID4887)
					if ErrorOut_4739[0]== False:
						try:
							pythonmodulefolder,pythonmodepath=os.path.split(UID4849)
							pythonmodule=pythonmodepath[:pythonmodepath.find(".")]
							imp_bbb=pythonmodulefolder+"/"+pythonmodule
							imp_ccc=imp.find_module(pythonmodule,[pythonmodulefolder])
							imp_ddd=imp.load_module(imp_bbb,imp_ccc[0],imp_ccc[1],imp_ccc[2])
							imp_eee=imp_ddd.main()
							UID482B=imp_eee[0]
							UID482E=imp_eee[1]
							UID486E=imp_eee[2]
							UID4867=ErrorOut_4739
						except Exception, errorMsg:
							UID4867=[True,1,str(errorMsg)]
							UID482B=""
							UID482E=0
							UID486E=[]
					else:
						UID4867=ErrorOut_4739
						UID482B=""
						UID482E=0
						UID486E=[]
					if UID4867[0]== False:
						try:
							UID4858=ALMotionRef_474A
							UID486E_names=[]
							UID486E_time=[]
							UID486E_angle=[]
							for i in UID486E:
								UID486E_names.append(i[0])
								UID486E_time_one=[]
								UID486E_angle_one=[]
								for j in i[1]:
									UID486E_time_one.append(j[0])
									UID486E_angle_one.append([j[1],j[2],j[3]])
								UID486E_time.append(UID486E_time_one)
								UID486E_angle.append(UID486E_angle_one)
							if False==True:
								ALMotionRef_474A.post.angleInterpolationBezier(UID486E_names,UID486E_time,UID486E_angle)
							else:
								ALMotionRef_474A.angleInterpolationBezier(UID486E_names,UID486E_time,UID486E_angle)
							UID47DB=UID4867
						except Exception, errorMsg:
							UID47DB=[True,1,str(errorMsg)]
							UID4858=0
					else:
						UID47DB=UID4867
						UID4858=0
					if UID47DB[0]== False:
						try:
							UID47CC=ALMemoryRef_4734
							UID47F2=np.array(ALMemoryRef_4734.getListData(UID475C.tolist()))
							UID47C3=UID47DB
						except Exception, errorMsg:
							UID47C3=[True,1,str(errorMsg)]
							UID47F2=np.array([],dtype="float64")
							UID47CC=0
					else:
						UID47C3=UID47DB
						UID47F2=np.array([],dtype="float64")
						UID47CC=0
					try:
						UID47FA=UID47F2.tolist().index(1.000000)
					except:
						UID47FA=-1
					UID489C=UID47C3[0]
					ErrorOut_4739=UID47C3
					
					UID47F7=UID47FA>=0
					UID489F=UID47F7|UID4802
					UID335F=UID47F7
					WhileS_D1S_ADS_BBS_B7_4759=UID489F|UID489C
					WhileS_D1S_ADS_BBS_B7_4759_Stop=WhileS_D1S_ADS_BBS_B7_4759
	queue_UID335F.put(UID335F)
	ErrorOut_4739=ErrorOut_4739
	queue_ErrorOut_4739.put(ErrorOut_4739)
def UID38D1(error_IO_38D6,queue_error_IO_38D6,UID38E4,queue_UID38E4,songs_38F7,):
	i_390D=-1
	WhileS_D1S_ADS_BBS_B7_3912_Stop=False
	while WhileS_D1S_ADS_BBS_B7_3912_Stop==False:
		UID392C=random.random()
		UID3946=len(songs_38F7)
		
		UID3937=int(UID3946)*UID392C
		WhileS_D1S_ADS_BBS_B7_3912=1>=UID3946
		UID3941=np.floor(UID3937)
		WhileS_D1S_ADS_BBS_B7_3912_Stop=WhileS_D1S_ADS_BBS_B7_3912
		UID3964=int(UID3941)
		songs_38F7=copy.copy(songs_38F7)
		UID396D=songs_38F7.pop(UID3964)
		UID39A9=UID396D[0]
		
		UID38E4=np.concatenate((UID38E4,[UID39A9]))
		
	error_IO_38D6=error_IO_38D6
	UID38E4=UID38E4
	queue_error_IO_38D6.put(error_IO_38D6)
	queue_UID38E4.put(UID38E4)
def UID3ABD(error_IO_3AC1,queue_error_IO_3AC1,UID3AFA,queue_UID3AFA,songInfos_3B2D,):
	i_3B60=-1
	WhileS_D1S_ADS_BBS_B7_3B63_Stop=False
	while WhileS_D1S_ADS_BBS_B7_3B63_Stop==False:
		UID3BCD=random.random()
		UID3BEF=len(songInfos_3B2D)
		
		UID3BE2=int(UID3BEF)*UID3BCD
		WhileS_D1S_ADS_BBS_B7_3B63=1>=UID3BEF
		UID3BEA=np.floor(UID3BE2)
		WhileS_D1S_ADS_BBS_B7_3B63_Stop=WhileS_D1S_ADS_BBS_B7_3B63
		UID3C04=int(UID3BEA)
		songInfos_3B2D=copy.copy(songInfos_3B2D)
		UID3C0E=songInfos_3B2D.pop(UID3C04)
		UID3C38=UID3C0E[0]
		
		UID3AFA=np.concatenate((UID3AFA,[UID3C38]))
		
	error_IO_3AC1=error_IO_3AC1
	UID3AFA=UID3AFA
	queue_error_IO_3AC1.put(error_IO_3AC1)
	queue_UID3AFA.put(UID3AFA)
def main():
    UID3A3A=os.path.realpath(__file__)
    Constant_UID3C96="127.0.0.1"
    UID3F79=np.array([],dtype="S")
    UID1F73=np.array([],dtype="S")
    UID4201=np.array(["小齐小齐","请退出程序"],dtype="S")
    UID4B6F=np.array(["休息","坐下","站起来","立正","蹲下"],dtype="S")
    UID4B93=np.array(["骑马舞","江南style","gangnam style","韩国舞"],dtype="S")
    UID4BBD=np.array(["小苹果","小苹果舞"],dtype="S")
    UID4BDD=np.array(["中国舞","太极","太极舞"],dtype="S")
    UID4BFE=np.array(["太空舞","惊悚","Thriller","Michael Jackson"],dtype="S")
    UID4C1E=np.array(["飞鹰舞"],dtype="S")
    UID4C5F=np.array(["新小苹果"],dtype="S")
    UID5084=np.array(["向左转","向右转","向后转","向前走","向后走","向左走","向右走","鼓掌","你是谁","你叫什么名字","你叫什么","声音开大点","声音开小点"],dtype="S")
    UID4377=np.array(["快乐的心"],dtype="S")
    UID444C=np.array(["大篷车","大鹏车"],dtype="S")
    stripped_path_004E,UID3A40=os.path.split(UID3A3A)
    try:
    	UID3D90=ALProxy("ALAutonomousLife",Constant_UID3C96,9559)
    	UID3E9C=[False,0,""]
    except Exception, errorMsg:
    	UID3E9C=[True,1,str(errorMsg)]
    	UID3D90=0
    UID4D95=np.concatenate((UID4B93,UID4BBD,UID4BDD,UID4BFE,UID4C1E,UID4C5F,UID4377,UID444C))
    UID3EA5=0
    UID3E8D=Clear_Errors.main(UID3E9C,UID3EA5)
    UID3DE5=UID3E8D[0]
    UID3E99=UID3E8D[1]
    UID3523=np.concatenate((UID4201,UID4B6F,UID4D95,UID5084))
    if UID3DE5[0]== False:
    	try:
    		UID3D93=ALProxy("ALBehaviorManager",Constant_UID3C96,9559)
    		UID3D57=UID3DE5
    	except Exception, errorMsg:
    		UID3D57=[True,1,str(errorMsg)]
    		UID3D93=0
    else:
    	UID3D57=UID3DE5
    	UID3D93=0
    if UID3D57[0]== False:
    	try:
    		UID3D96=ALProxy("ALAnimatedSpeech",Constant_UID3C96,9559)
    		UID3C7C=UID3D57
    	except Exception, errorMsg:
    		UID3C7C=[True,1,str(errorMsg)]
    		UID3D96=0
    else:
    	UID3C7C=UID3D57
    	UID3D96=0
    if UID3C7C[0]== False:
    	try:
    		UID3D99=ALProxy("ALTextToSpeech",Constant_UID3C96,9559)
    		UID3D7E=UID3C7C
    	except Exception, errorMsg:
    		UID3D7E=[True,1,str(errorMsg)]
    		UID3D99=0
    else:
    	UID3D7E=UID3C7C
    	UID3D99=0
    if UID3D7E[0]== False:
    	try:
    		UID3D9C=ALProxy("ALAudioDevice",Constant_UID3C96,9559)
    		UID3CBB=UID3D7E
    	except Exception, errorMsg:
    		UID3CBB=[True,1,str(errorMsg)]
    		UID3D9C=0
    else:
    	UID3CBB=UID3D7E
    	UID3D9C=0
    if UID3CBB[0]== False:
    	try:
    		UID3D9F=ALProxy("ALMemory",Constant_UID3C96,9559)
    		UID3D09=UID3CBB
    	except Exception, errorMsg:
    		UID3D09=[True,1,str(errorMsg)]
    		UID3D9F=0
    else:
    	UID3D09=UID3CBB
    	UID3D9F=0
    if UID3D09[0]== False:
    	try:
    		UID3DA2=ALProxy("ALMotion",Constant_UID3C96,9559)
    		UID3C55=UID3D09
    	except Exception, errorMsg:
    		UID3C55=[True,1,str(errorMsg)]
    		UID3DA2=0
    else:
    	UID3C55=UID3D09
    	UID3DA2=0
    if UID3C55[0]== False:
    	try:
    		UID3DA5=ALProxy("ALSpeechRecognition",Constant_UID3C96,9559)
    		UID3CE2=UID3C55
    	except Exception, errorMsg:
    		UID3CE2=[True,1,str(errorMsg)]
    		UID3DA5=0
    else:
    	UID3CE2=UID3C55
    	UID3DA5=0
    if UID3CE2[0]== False:
    	try:
    		UID3DA8=ALProxy("ALRobotPosture",Constant_UID3C96,9559)
    		UID3D30=UID3CE2
    	except Exception, errorMsg:
    		UID3D30=[True,1,str(errorMsg)]
    		UID3DA8=0
    else:
    	UID3D30=UID3CE2
    	UID3DA8=0
    if UID3D30[0]== False:
    	try:
    		UID3DAB=ALProxy("ALAudioPlayer",Constant_UID3C96,9559)
    		UID3E0C=UID3D30
    	except Exception, errorMsg:
    		UID3E0C=[True,1,str(errorMsg)]
    		UID3DAB=0
    else:
    	UID3E0C=UID3D30
    	UID3DAB=0
    if UID3E0C[0]== False:
    	try:
    		UID3DAE=ALProxy("ALFaceDetection",Constant_UID3C96,9559)
    		UID3E33=UID3E0C
    	except Exception, errorMsg:
    		UID3E33=[True,1,str(errorMsg)]
    		UID3DAE=0
    else:
    	UID3E33=UID3E0C
    	UID3DAE=0
    if UID3E33[0]== False:
    	try:
    		UID3DB1=ALProxy("ALTracker",Constant_UID3C96,9559)
    		UID3E5A=UID3E33
    	except Exception, errorMsg:
    		UID3E5A=[True,1,str(errorMsg)]
    		UID3DB1=0
    else:
    	UID3E5A=UID3E33
    	UID3DB1=0
    if UID3E5A[0]== False:
    	try:
    		UID3DB4=ALProxy("ALNavigation",Constant_UID3C96,9559)
    		UID3EC3=UID3E5A
    	except Exception, errorMsg:
    		UID3EC3=[True,1,str(errorMsg)]
    		UID3DB4=0
    else:
    	UID3EC3=UID3E5A
    	UID3DB4=0
    if UID3EC3[0]== False:
    	try:
    		UID3DB7=ALProxy("ALPhotoCapture",Constant_UID3C96,9559)
    		UID3EEA=UID3EC3
    	except Exception, errorMsg:
    		UID3EEA=[True,1,str(errorMsg)]
    		UID3DB7=0
    else:
    	UID3EEA=UID3EC3
    	UID3DB7=0
    if UID3EEA[0]== False:
    	try:
    		UID3DBA=ALProxy("ALLeds",Constant_UID3C96,9559)
    		UID3F11=UID3EEA
    	except Exception, errorMsg:
    		UID3F11=[True,1,str(errorMsg)]
    		UID3DBA=0
    else:
    	UID3F11=UID3EEA
    	UID3DBA=0
    if UID3F11[0]== False:
    	try:
    		UID3DBD=ALProxy("ALBarcodeReader",Constant_UID3C96,9559)
    		UID3F38=UID3F11
    	except Exception, errorMsg:
    		UID3F38=[True,1,str(errorMsg)]
    		UID3DBD=0
    else:
    	UID3F38=UID3F11
    	UID3DBD=0
    if UID3F38[0]== False:
    	try:
    		UID3DC0=ALProxy("ALSonar",Constant_UID3C96,9559)
    		UID3F5F=UID3F38
    	except Exception, errorMsg:
    		UID3F5F=[True,1,str(errorMsg)]
    		UID3DC0=0
    else:
    	UID3F5F=UID3F38
    	UID3DC0=0
    if UID3F5F[0]== False:
    	try:
    		UID3DC3=ALProxy("ALBattery",Constant_UID3C96,9559)
    		UID4406=UID3F5F
    	except Exception, errorMsg:
    		UID4406=[True,1,str(errorMsg)]
    		UID3DC3=0
    else:
    	UID4406=UID3F5F
    	UID3DC3=0
    UID0052=[UID3D90,UID3D93,UID3D96,UID3D99,UID3D9C,UID3D9F,UID3DA2,UID3DA5,UID3DA8,UID3DAB,UID3DAE,UID3DB1,UID3DB4,UID3DB7,UID3DBA,UID3DBD,UID3DC0,UID3DC3]
    if UID4406[0]== False:
    	try:
    		UID440C=""
    		UID440F=""
    		UID43F7=xfdll.MSPLogin(UID440F,UID440C,"appid = 5948e6e8")
    		UID3A51=UID4406
    	except Exception, errorMsg:
    		UID3A51=[True,1,str(errorMsg)]
    		UID43F7=0
    else:
    	UID3A51=UID4406
    	UID43F7=0
    if UID3A51[0]==True:
    	UID3A5A=np.array(["请退出程序"])
    	UID3A56=UID3A5A
    else: 
    	UID3A59=np.array(["Initial"])
    	UID3A56=UID3A59
    UID0034=UID3A56
    name_for_subscribe_003D="xunfei"
    UID0063=0
    UID006C=True
    millisecond_timer_value_0075=0
    UID005A=UID3F79
    pIP_1C71=Constant_UID3C96
    UID0041=UID1F73
    queue_UID002B=Queue.Queue()
    thread.start_new_thread(UID002B,(name_for_subscribe_003D,stripped_path_004E,UID0052,pIP_1C71,UID3523,UID0034,UID0041,UID005A,UID0063,UID006C,millisecond_timer_value_0075,queue_UID002B,))
    queue_UID002B.get()
    
if __name__ == "__main__":
    main()
