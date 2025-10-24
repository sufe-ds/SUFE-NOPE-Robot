# -*- coding: utf-8 -*-
String=""
import numpy as np
Action=np.array([],dtype="S")
Array=np.array([],dtype="S")
error_out=[False,0,""]
JSON_Tree=None
error_in__no_error_=[False,0,""]
import random
def main(error_in__no_error_,JSON_Tree):
    if error_in__no_error_[0]== False:
    	try:
    		UID022C=JSON_Tree
    		try:
    			UID039E=JSON_Tree["semantic"]
    			UID0226=False
    		except:
    			UID039E={}
    			UID0226=True
    		UID0395=error_in__no_error_
    	except Exception, errorMsg:
    		UID0395=[True,1,str(errorMsg)]
    		UID0226=False
    		UID039E=None
    		UID022C=None
    else:
    	UID0395=error_in__no_error_
    	UID0226=False
    	UID039E=None
    	UID022C=None
    if UID0395[0]== False:
    	try:
    		UID0386=UID039E
    		UID04A0=UID039E[0]
    		UID0380=False
    		UID0495=UID0395
    	except Exception, errorMsg:
    		UID0495=[True,1,str(errorMsg)]
    		UID0380=False
    		UID04A0=None
    		UID0386=None
    else:
    	UID0495=UID0395
    	UID0380=False
    	UID04A0=None
    	UID0386=None
    if UID0495[0]== False:
    	try:
    		UID0486=UID04A0
    		try:
    			UID0530=UID04A0["slots"]
    			UID0480=False
    		except:
    			UID0530={}
    			UID0480=True
    		UID0527=UID0495
    	except Exception, errorMsg:
    		UID0527=[True,1,str(errorMsg)]
    		UID0480=False
    		UID0530=None
    		UID0486=None
    else:
    	UID0527=UID0495
    	UID0480=False
    	UID0530=None
    	UID0486=None
    if UID0527[0]== False:
    	try:
    		JSON_Tree_Passthrough__JSON_Array__0996=UID0530
    		ForS_D1S_ADS_BBS_B7_0937=len(UID0530)
    		error_out_096A=UID0527
    	except Exception, errorMsg:
    		error_out_096A=[True,1,str(errorMsg)]
    		ForS_D1S_ADS_BBS_B7_0937=0
    		JSON_Tree_Passthrough__JSON_Array__0996=None
    else:
    	error_out_096A=UID0527
    	ForS_D1S_ADS_BBS_B7_0937=0
    	JSON_Tree_Passthrough__JSON_Array__0996=None
    UID0C3A=""
    i_0933=-1
    ForS_D1S_ADS_BBS_B7_0921_count=ForS_D1S_ADS_BBS_B7_0937
    for i in range(0, ForS_D1S_ADS_BBS_B7_0921_count):
    	i_0933=i_0933+1
    	if error_out_096A[0]== False:
    		try:
    			UID09B1=JSON_Tree_Passthrough__JSON_Array__0996
    			UID0A40=JSON_Tree_Passthrough__JSON_Array__0996[i_0933]
    			UID09AB=False
    			UID0A37=error_out_096A
    		except Exception, errorMsg:
    			UID0A37=[True,1,str(errorMsg)]
    			UID09AB=False
    			UID0A40=None
    			UID09B1=None
    	else:
    		UID0A37=error_out_096A
    		UID09AB=False
    		UID0A40=None
    		UID09B1=None
    	if UID0A37[0]== False:
    		try:
    			UID0A28=UID0A40
    			try:
    				UID0AB9=UID0A40["name"]
    				UID0A22=False
    			except:
    				UID0AB9={}
    				UID0A22=True
    			UID0AB3=UID0A37
    		except Exception, errorMsg:
    			UID0AB3=[True,1,str(errorMsg)]
    			UID0A22=False
    			UID0AB9=None
    			UID0A28=None
    	else:
    		UID0AB3=UID0A37
    		UID0A22=False
    		UID0AB9=None
    		UID0A28=None
    	if UID0AB3[0]== False:
    		try:
    			UID0B3B=str(UID0AB9)
    			error_out_096A=UID0AB3
    		except Exception, errorMsg:
    			error_out_096A=[True,1,str(errorMsg)]
    			UID0B3B=""
    	else:
    		error_out_096A=UID0AB3
    		UID0B3B=""
    	UID0C3A=UID0C3A+UID0B3B+"_"
    	
    	
    UID0E1E=JSON_Tree
    UID0DD5=UID0C3A
    UID0DFE=error_out_096A
    if UID0DD5=="keyword_queryField_":
    	UID0360=np.array(["AnimatedSay","RerunVoicecloud"],dtype="S")
    	if UID0DFE[0]== False:
    		try:
    			UID0037=UID0E1E
    			try:
    				UID008B=UID0E1E["data"]
    				UID0031=False
    			except:
    				UID008B={}
    				UID0031=True
    			UID0082=UID0DFE
    		except Exception, errorMsg:
    			UID0082=[True,1,str(errorMsg)]
    			UID0031=False
    			UID008B=None
    			UID0037=None
    	else:
    		UID0082=UID0DFE
    		UID0031=False
    		UID008B=None
    		UID0037=None
    	UID0CE5=UID0360
    	if UID0082[0]== False:
    		try:
    			UID0073=UID008B
    			try:
    				UID030D=UID008B["result"]
    				UID006D=False
    			except:
    				UID030D={}
    				UID006D=True
    			UID0304=UID0082
    		except Exception, errorMsg:
    			UID0304=[True,1,str(errorMsg)]
    			UID006D=False
    			UID030D=None
    			UID0073=None
    	else:
    		UID0304=UID0082
    		UID006D=False
    		UID030D=None
    		UID0073=None
    	if UID0304[0]== False:
    		try:
    			UID02F5=UID030D
    			UID041E=UID030D[0]
    			UID02EF=False
    			UID0415=UID0304
    		except Exception, errorMsg:
    			UID0415=[True,1,str(errorMsg)]
    			UID02EF=False
    			UID041E=None
    			UID02F5=None
    	else:
    		UID0415=UID0304
    		UID02EF=False
    		UID041E=None
    		UID02F5=None
    	if UID0415[0]== False:
    		try:
    			UID0406=UID041E
    			try:
    				UID0504=UID041E["showContent"]
    				UID0400=False
    			except:
    				UID0504={}
    				UID0400=True
    			UID04FB=UID0415
    		except Exception, errorMsg:
    			UID04FB=[True,1,str(errorMsg)]
    			UID0400=False
    			UID0504=None
    			UID0406=None
    	else:
    		UID04FB=UID0415
    		UID0400=False
    		UID0504=None
    		UID0406=None
    	if UID04FB[0]== False:
    		try:
    			try:
    				UID04BF=UID0504.encode('utf-8')
    			except:
    				UID04BF=UID0504
    			UID0FCC=UID04FB
    		except Exception, errorMsg:
    			UID0FCC=[True,1,str(errorMsg)]
    			UID04BF=""
    	else:
    		UID0FCC=UID04FB
    		UID04BF=""
    	UID02AB=np.array([UID04BF])
    	UID0FD0=UID0FCC
    	UID02AE=UID02AB
    elif UID0DD5=="" or UID0DD5=="author_" or UID0DD5=="author_dynasty_" or UID0DD5=="author_queried_" or UID0DD5=="dynasty_" or UID0DD5=="name_":
    	UID08A2=random.random()
    	UID0AD5=np.array(["title","author","content"],dtype="S")
    	UID03ED=np.array(["AnimatedSay","AnimatedSay","RerunVoicecloud"],dtype="S")
    	if UID0DFE[0]== False:
    		try:
    			UID06AF=UID0E1E
    			try:
    				UID1065=UID0E1E["data"]
    				UID06A9=False
    			except:
    				UID1065={}
    				UID06A9=True
    			UID105C=UID0DFE
    		except Exception, errorMsg:
    			UID105C=[True,1,str(errorMsg)]
    			UID06A9=False
    			UID1065=None
    			UID06AF=None
    	else:
    		UID105C=UID0DFE
    		UID06A9=False
    		UID1065=None
    		UID06AF=None
    	UID0CE5=UID03ED
    	if UID105C[0]== False:
    		try:
    			UID104D=UID1065
    			try:
    				UID1296=UID1065["result"]
    				UID1047=False
    			except:
    				UID1296={}
    				UID1047=True
    			UID128A=UID105C
    		except Exception, errorMsg:
    			UID128A=[True,1,str(errorMsg)]
    			UID1047=False
    			UID1296=None
    			UID104D=None
    	else:
    		UID128A=UID105C
    		UID1047=False
    		UID1296=None
    		UID104D=None
    	if UID128A[0]== False:
    		try:
    			UID1172=UID1296
    			UID08A5=len(UID1296)
    			UID1160=UID128A
    		except Exception, errorMsg:
    			UID1160=[True,1,str(errorMsg)]
    			UID08A5=0
    			UID1172=None
    	else:
    		UID1160=UID128A
    		UID08A5=0
    		UID1172=None
    	UID0971=np.floor((int(UID08A5)*UID08A2))
    	UID1166=int(UID0971)
    	if UID1160[0]== False:
    		try:
    			UID1151=UID1172
    			JSON_Object_12CE=UID1172[UID1166]
    			UID1133=False
    			error_out_12E0=UID1160
    		except Exception, errorMsg:
    			error_out_12E0=[True,1,str(errorMsg)]
    			UID1133=False
    			JSON_Object_12CE=None
    			UID1151=None
    	else:
    		error_out_12E0=UID1160
    		UID1133=False
    		JSON_Object_12CE=None
    		UID1151=None
    	UID12D4=UID0AD5
    	UID12DA=np.array([],dtype="S")
    	i_12F2=-1
    	ForS_D1S_ADS_BBS_B7_0A77_IndexsIn=[]
    	ForS_D1S_ADS_BBS_B7_0A77_IndexsIn.append(len(UID12D4))
    	ForS_D1S_ADS_BBS_B7_0A77_Indexmin=min(ForS_D1S_ADS_BBS_B7_0A77_IndexsIn)
    	ForS_D1S_ADS_BBS_B7_0A77_count=ForS_D1S_ADS_BBS_B7_0A77_Indexmin
    	for i in range(0, ForS_D1S_ADS_BBS_B7_0A77_count):
    		i_12F2=i_12F2+1
    		if error_out_12E0[0]== False:
    			try:
    				UID1301=JSON_Object_12CE
    				try:
    					UID1349=JSON_Object_12CE[UID12D4[i_12F2]]
    					UID12FB=False
    				except:
    					UID1349={}
    					UID12FB=True
    				UID1340=error_out_12E0
    			except Exception, errorMsg:
    				UID1340=[True,1,str(errorMsg)]
    				UID12FB=False
    				UID1349=None
    				UID1301=None
    		else:
    			UID1340=error_out_12E0
    			UID12FB=False
    			UID1349=None
    			UID1301=None
    		if UID1340[0]== False:
    			try:
    				try:
    					UID12DD=UID1349.encode('utf-8')
    				except:
    					UID12DD=UID1349
    				error_out_12E0=UID1340
    			except Exception, errorMsg:
    				error_out_12E0=[True,1,str(errorMsg)]
    				UID12DD=""
    		else:
    			error_out_12E0=UID1340
    			UID12DD=""
    		
    		UID12DA=np.concatenate((UID12DA,[UID12DD]))
    	try:
    		UID14FD=UID12DA[0]
    	except:
    		UID14FD=""
    	try:
    		UID14F7=UID12DA[1]
    	except:
    		UID14F7=""
    	try:
    		UID1517=UID12DA[2]
    	except:
    		UID1517=""
    	UID0FD0=error_out_12E0
    	UID1514="为您阅读"+UID14F7+"的"+UID14FD
    	UID0666=np.concatenate(([UID1514],[UID1517]))
    	UID02AE=UID0666
    elif UID0DD5=="author_name_":
    	UID086A=np.array(["title","author","content"],dtype="S")
    	UID0DB5=np.array(["AnimatedSay","AnimatedSay","RerunVoicecloud"],dtype="S")
    	if UID0DFE[0]== False:
    		try:
    			UID0597=UID0E1E
    			try:
    				UID10CB=UID0E1E["data"]
    				UID0585=False
    			except:
    				UID10CB={}
    				UID0585=True
    			UID10C2=UID0DFE
    		except Exception, errorMsg:
    			UID10C2=[True,1,str(errorMsg)]
    			UID0585=False
    			UID10CB=None
    			UID0597=None
    	else:
    		UID10C2=UID0DFE
    		UID0585=False
    		UID10CB=None
    		UID0597=None
    	UID0CE5=UID0DB5
    	if UID10C2[0]== False:
    		try:
    			UID10B3=UID10CB
    			try:
    				UID1107=UID10CB["result"]
    				UID10AD=False
    			except:
    				UID1107={}
    				UID10AD=True
    			UID10FE=UID10C2
    		except Exception, errorMsg:
    			UID10FE=[True,1,str(errorMsg)]
    			UID10AD=False
    			UID1107=None
    			UID10B3=None
    	else:
    		UID10FE=UID10C2
    		UID10AD=False
    		UID1107=None
    		UID10B3=None
    	if UID10FE[0]== False:
    		try:
    			UID10EF=UID1107
    			JSON_Object_083A=UID1107[0]
    			UID10E9=False
    			error_out_1139=UID10FE
    		except Exception, errorMsg:
    			error_out_1139=[True,1,str(errorMsg)]
    			UID10E9=False
    			JSON_Object_083A=None
    			UID10EF=None
    	else:
    		error_out_1139=UID10FE
    		UID10E9=False
    		JSON_Object_083A=None
    		UID10EF=None
    	UID0954=UID086A
    	UID0988=np.array([],dtype="S")
    	i_082C=-1
    	ForS_D1S_ADS_BBS_B7_05E0_IndexsIn=[]
    	ForS_D1S_ADS_BBS_B7_05E0_IndexsIn.append(len(UID0954))
    	ForS_D1S_ADS_BBS_B7_05E0_Indexmin=min(ForS_D1S_ADS_BBS_B7_05E0_IndexsIn)
    	ForS_D1S_ADS_BBS_B7_05E0_count=ForS_D1S_ADS_BBS_B7_05E0_Indexmin
    	for i in range(0, ForS_D1S_ADS_BBS_B7_05E0_count):
    		i_082C=i_082C+1
    		if error_out_1139[0]== False:
    			try:
    				UID112B=JSON_Object_083A
    				try:
    					UID118B=JSON_Object_083A[UID0954[i_082C]]
    					UID1125=False
    				except:
    					UID118B={}
    					UID1125=True
    				UID1182=error_out_1139
    			except Exception, errorMsg:
    				UID1182=[True,1,str(errorMsg)]
    				UID1125=False
    				UID118B=None
    				UID112B=None
    		else:
    			UID1182=error_out_1139
    			UID1125=False
    			UID118B=None
    			UID112B=None
    		if UID1182[0]== False:
    			try:
    				try:
    					UID0984=UID118B.encode('utf-8')
    				except:
    					UID0984=UID118B
    				error_out_1139=UID1182
    			except Exception, errorMsg:
    				error_out_1139=[True,1,str(errorMsg)]
    				UID0984=""
    		else:
    			error_out_1139=UID1182
    			UID0984=""
    		
    		UID0988=np.concatenate((UID0988,[UID0984]))
    	try:
    		UID0A72=UID0988[0]
    	except:
    		UID0A72=""
    	try:
    		UID0AEA=UID0988[1]
    	except:
    		UID0AEA=""
    	try:
    		UID0B45=UID0988[2]
    	except:
    		UID0B45=""
    	UID0FD0=error_out_1139
    	UID0B1F=UID0A72+","+UID0AEA
    	UID050B=np.concatenate(([UID0B1F],[UID0B45]))
    	UID02AE=UID050B
    elif UID0DD5=="keyword_queried_" or UID0DD5=="name_queried_":
    	UID0D85=np.array(["AnimatedSay","RerunVoicecloud"],dtype="S")
    	if UID0DFE[0]== False:
    		try:
    			UID0603=UID0E1E
    			try:
    				UID0E64=UID0E1E["data"]
    				UID05CA=False
    			except:
    				UID0E64={}
    				UID05CA=True
    			UID0E59=UID0DFE
    		except Exception, errorMsg:
    			UID0E59=[True,1,str(errorMsg)]
    			UID05CA=False
    			UID0E64=None
    			UID0603=None
    	else:
    		UID0E59=UID0DFE
    		UID05CA=False
    		UID0E64=None
    		UID0603=None
    	UID0CE5=UID0D85
    	if UID0E59[0]== False:
    		try:
    			UID0E4A=UID0E64
    			try:
    				UID0FD5=UID0E64["result"]
    				UID0E43=False
    			except:
    				UID0FD5={}
    				UID0E43=True
    			UID0FC9=UID0E59
    		except Exception, errorMsg:
    			UID0FC9=[True,1,str(errorMsg)]
    			UID0E43=False
    			UID0FD5=None
    			UID0E4A=None
    	else:
    		UID0FC9=UID0E59
    		UID0E43=False
    		UID0FD5=None
    		UID0E4A=None
    	if UID0FC9[0]== False:
    		try:
    			UID0F1C=UID0FD5
    			UID0FB6=len(UID0FD5)
    			UID0F28=UID0FC9
    		except Exception, errorMsg:
    			UID0F28=[True,1,str(errorMsg)]
    			UID0FB6=0
    			UID0F1C=None
    	else:
    		UID0F28=UID0FC9
    		UID0FB6=0
    		UID0F1C=None
    	UID0F0B=1==UID0FB6
    	UID0F4F=UID0FB6
    	if UID0F0B==True:
    		UID1251=np.array(["dynasty","author"],dtype="S")
    		if UID0F28[0]== False:
    			try:
    				UID1216=UID0F1C
    				JSON_Object_1274=UID0F1C[0]
    				UID120F=False
    				error_out_1286=UID0F28
    			except Exception, errorMsg:
    				error_out_1286=[True,1,str(errorMsg)]
    				UID120F=False
    				JSON_Object_1274=None
    				UID1216=None
    		else:
    			error_out_1286=UID0F28
    			UID120F=False
    			JSON_Object_1274=None
    			UID1216=None
    		UID127A=UID1251
    		UID1280=np.array([],dtype="S")
    		i_12A0=-1
    		ForS_D1S_ADS_BBS_B7_126E_IndexsIn=[]
    		ForS_D1S_ADS_BBS_B7_126E_IndexsIn.append(len(UID127A))
    		ForS_D1S_ADS_BBS_B7_126E_Indexmin=min(ForS_D1S_ADS_BBS_B7_126E_IndexsIn)
    		ForS_D1S_ADS_BBS_B7_126E_count=ForS_D1S_ADS_BBS_B7_126E_Indexmin
    		for i in range(0, ForS_D1S_ADS_BBS_B7_126E_count):
    			i_12A0=i_12A0+1
    			if error_out_1286[0]== False:
    				try:
    					UID12B5=JSON_Object_1274
    					try:
    						UID1354=JSON_Object_1274[UID127A[i_12A0]]
    						UID12A9=False
    					except:
    						UID1354={}
    						UID12A9=True
    					UID1342=error_out_1286
    				except Exception, errorMsg:
    					UID1342=[True,1,str(errorMsg)]
    					UID12A9=False
    					UID1354=None
    					UID12B5=None
    			else:
    				UID1342=error_out_1286
    				UID12A9=False
    				UID1354=None
    				UID12B5=None
    			if UID1342[0]== False:
    				try:
    					try:
    						UID1283=UID1354.encode('utf-8')
    					except:
    						UID1283=UID1354
    					error_out_1286=UID1342
    				except Exception, errorMsg:
    					error_out_1286=[True,1,str(errorMsg)]
    					UID1283=""
    			else:
    				error_out_1286=UID1342
    				UID1283=""
    			
    			UID1280=np.concatenate((UID1280,[UID1283]))
    		try:
    			UID1377=UID1280[0]
    		except:
    			UID1377=""
    		try:
    			UID140D=UID1280[1]
    		except:
    			UID140D=""
    		UID0F34=error_out_1286
    		UID139A=len(UID1377)
    		UID13AC=UID139A<=3
    		UID13B1=UID1377
    		if UID13AC==True:
    			UID13BA=UID13B1+"代"
    			UID13B6=UID13BA
    		else: 
    			UID13B6=UID13B1
    		UID1433="它是"+UID13B6+"的"+UID140D+"写的"
    		UID0F41=np.array([UID1433])
    		UID0F43=UID0F41
    	else: 
    		JSON_Tree_Passthrough__JSON_Array__07F0=UID0F1C
    		error_out_0884=UID0F28
    		UID153E=""
    		ForS_D1S_ADS_BBS_B7_077C=UID0F4F
    		i_0778=-1
    		ForS_D1S_ADS_BBS_B7_0749_count=ForS_D1S_ADS_BBS_B7_077C
    		for i in range(0, ForS_D1S_ADS_BBS_B7_0749_count):
    			i_0778=i_0778+1
    			if error_out_0884[0]== False:
    				try:
    					UID08CF=JSON_Tree_Passthrough__JSON_Array__07F0
    					UID11D1=JSON_Tree_Passthrough__JSON_Array__07F0[i_0778]
    					UID08C9=False
    					UID11BC=error_out_0884
    				except Exception, errorMsg:
    					UID11BC=[True,1,str(errorMsg)]
    					UID08C9=False
    					UID11D1=None
    					UID08CF=None
    			else:
    				UID11BC=error_out_0884
    				UID08C9=False
    				UID11D1=None
    				UID08CF=None
    			if UID11BC[0]== False:
    				try:
    					UID0A5F=UID11D1
    					try:
    						UID164A=UID11D1["author"]
    						UID0A59=False
    					except:
    						UID164A={}
    						UID0A59=True
    					UID1641=UID11BC
    				except Exception, errorMsg:
    					UID1641=[True,1,str(errorMsg)]
    					UID0A59=False
    					UID164A=None
    					UID0A5F=None
    			else:
    				UID1641=UID11BC
    				UID0A59=False
    				UID164A=None
    				UID0A5F=None
    			if UID1641[0]== False:
    				try:
    					try:
    						UID0C64=UID164A.encode('utf-8')
    					except:
    						UID0C64=UID164A
    					error_out_0884=UID1641
    				except Exception, errorMsg:
    					error_out_0884=[True,1,str(errorMsg)]
    					UID0C64=""
    			else:
    				error_out_0884=UID1641
    				UID0C64=""
    			UID153E=UID153E+UID0C64+","
    			
    			
    		UID0F42=np.array([UID153E])
    		UID0F34=error_out_0884
    		UID0F43=UID0F42
    	UID02AE=UID0F43
    	UID0FD0=UID0F34
    elif UID0DD5=="author_name_queried_":
    	UID0BE7=np.array(["AnimatedSay","RerunVoicecloud"],dtype="S")
    	UID1616=np.array(["dynasty","author"],dtype="S")
    	if UID0DFE[0]== False:
    		try:
    			UID0961=UID0E1E
    			try:
    				UID09F3=UID0E1E["data"]
    				UID0957=False
    			except:
    				UID09F3={}
    				UID0957=True
    			UID09E9=UID0DFE
    		except Exception, errorMsg:
    			UID09E9=[True,1,str(errorMsg)]
    			UID0957=False
    			UID09F3=None
    			UID0961=None
    	else:
    		UID09E9=UID0DFE
    		UID0957=False
    		UID09F3=None
    		UID0961=None
    	UID0CE5=UID0BE7
    	if UID09E9[0]== False:
    		try:
    			UID09D6=UID09F3
    			try:
    				UID0B0F=UID09F3["result"]
    				UID09C8=False
    			except:
    				UID0B0F={}
    				UID09C8=True
    			UID0B06=UID09E9
    		except Exception, errorMsg:
    			UID0B06=[True,1,str(errorMsg)]
    			UID09C8=False
    			UID0B0F=None
    			UID09D6=None
    	else:
    		UID0B06=UID09E9
    		UID09C8=False
    		UID0B0F=None
    		UID09D6=None
    	if UID0B06[0]== False:
    		try:
    			UID0AEF=UID0B0F
    			JSON_Object_17BF=UID0B0F[0]
    			UID0AE6=False
    			error_out_19FE=UID0B06
    		except Exception, errorMsg:
    			error_out_19FE=[True,1,str(errorMsg)]
    			UID0AE6=False
    			JSON_Object_17BF=None
    			UID0AEF=None
    	else:
    		error_out_19FE=UID0B06
    		UID0AE6=False
    		JSON_Object_17BF=None
    		UID0AEF=None
    	UID1808=UID1616
    	UID1930=np.array([],dtype="S")
    	i_17A1=-1
    	ForS_D1S_ADS_BBS_B7_178F_IndexsIn=[]
    	ForS_D1S_ADS_BBS_B7_178F_IndexsIn.append(len(UID1808))
    	ForS_D1S_ADS_BBS_B7_178F_Indexmin=min(ForS_D1S_ADS_BBS_B7_178F_IndexsIn)
    	ForS_D1S_ADS_BBS_B7_178F_count=ForS_D1S_ADS_BBS_B7_178F_Indexmin
    	for i in range(0, ForS_D1S_ADS_BBS_B7_178F_count):
    		i_17A1=i_17A1+1
    		if error_out_19FE[0]== False:
    			try:
    				UID0B2D=JSON_Object_17BF
    				try:
    					UID0B8D=JSON_Object_17BF[UID1808[i_17A1]]
    					UID0B27=False
    				except:
    					UID0B8D={}
    					UID0B27=True
    				UID0B84=error_out_19FE
    			except Exception, errorMsg:
    				UID0B84=[True,1,str(errorMsg)]
    				UID0B27=False
    				UID0B8D=None
    				UID0B2D=None
    		else:
    			UID0B84=error_out_19FE
    			UID0B27=False
    			UID0B8D=None
    			UID0B2D=None
    		if UID0B84[0]== False:
    			try:
    				try:
    					UID1924=UID0B8D.encode('utf-8')
    				except:
    					UID1924=UID0B8D
    				error_out_19FE=UID0B84
    			except Exception, errorMsg:
    				error_out_19FE=[True,1,str(errorMsg)]
    				UID1924=""
    		else:
    			error_out_19FE=UID0B84
    			UID1924=""
    		
    		UID1930=np.concatenate((UID1930,[UID1924]))
    	try:
    		UID1C25=UID1930[0]
    	except:
    		UID1C25=""
    	try:
    		UID1FD6=UID1930[1]
    	except:
    		UID1FD6=""
    	UID0FD0=error_out_19FE
    	UID1D0F=len(UID1C25)
    	UID1DF4=UID1D0F<=3
    	UID1E7A=UID1C25
    	if UID1DF4==True:
    		UID201E=UID1E7A+"代"
    		UID2021=UID201E
    	else: 
    		UID2021=UID1E7A
    	UID23A5="它是"+UID2021+"的"+UID1FD6+"写的"
    	UID08BE=np.array([UID23A5])
    	UID02AE=UID08BE
    else: 
    	UID1C47=np.array(["RerunVoicecloud"],dtype="S")
    	UID02AE=np.array([],dtype="S")
    	UID0CE5=UID1C47
    	UID0FD0=UID0DFE
    String=UID0C3A
    error_out=UID0FD0
    Array=UID02AE
    Action=UID0CE5
    return error_out,Action,Array
if __name__ == "__main__":
    error_out,Action,Array=main(error_in__no_error_,JSON_Tree)
