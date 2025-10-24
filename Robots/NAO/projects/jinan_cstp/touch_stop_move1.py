# -*- coding: utf-8 -*-
touch=False
timeout_s_=0
ErrorOut=[False,0,""]
error_out=[False,0,""]
import numpy as np
movepath=np.array([],dtype="S")
ALMotionRef=0
ALMemoryRef=0
import time
import thread
import Queue
import imp
import os
def UID007F(ALMemoryRef_0081,ALMotionRef_008B,ErrorOut_0091,millisecond_timer_value_009D,UID00A1,UID04EF,movepath_0530,queue_UID01FF,queue_ErrorOut_05A9,timeout_s_,ErrorOut,movepath,ALMotionRef,ALMemoryRef,):
	i_00AD=-1
	WhileS_D1S_ADS_BBS_B7_00B0_Stop=False
	while WhileS_D1S_ADS_BBS_B7_00B0_Stop==False:
		i_00AD=i_00AD+1
		UID00BF=np.array(["Device/SubDeviceList/Head/Touch/Front/Sensor/Value","Device/SubDeviceList/Head/Touch/Rear/Sensor/Value","Device/SubDeviceList/Head/Touch/Middle/Sensor/Value"],dtype="S")
		UID01B3=int(time.time()*1000)
		UID0151=i_00AD//UID04EF
		UID0544=i_00AD%UID04EF
		UID01BE=UID01B3-millisecond_timer_value_009D
		UID0B8B=UID01BE>UID00A1
		try:
			UID010F=movepath_0530[UID0544+0]
		except:
			UID010F=""
		if ErrorOut_0091[0]== False:
			try:
				pythonmodulefolder,pythonmodepath=os.path.split(UID010F)
				pythonmodule=pythonmodepath[:pythonmodepath.find(".")]
				imp_bbb=pythonmodulefolder+"/"+pythonmodule
				imp_ccc=imp.find_module(pythonmodule,[pythonmodulefolder])
				imp_ddd=imp.load_module(imp_bbb,imp_ccc[0],imp_ccc[1],imp_ccc[2])
				imp_eee=imp_ddd.main()
				UID00F1=imp_eee[0]
				UID00F4=imp_eee[1]
				UID0133=imp_eee[2]
				UID012D=ErrorOut_0091
			except Exception, errorMsg:
				UID012D=[True,1,str(errorMsg)]
				UID00F1=""
				UID00F4=0
				UID0133=[]
		else:
			UID012D=ErrorOut_0091
			UID00F1=""
			UID00F4=0
			UID0133=[]
		if UID012D[0]== False:
			try:
				UID0130=False
				UID011E=ALMotionRef_008B
				UID0133_names=[]
				UID0133_time=[]
				UID0133_angle=[]
				for i in UID0133:
					UID0133_names.append(i[0])
					UID0133_time_one=[]
					UID0133_angle_one=[]
					for j in i[1]:
						UID0133_time_one.append(j[0])
						UID0133_angle_one.append([j[1],j[2],j[3]])
					UID0133_time.append(UID0133_time_one)
					UID0133_angle.append(UID0133_angle_one)
				if UID0130==True:
					ALMotionRef_008B.post.angleInterpolationBezier(UID0133_names,UID0133_time,UID0133_angle)
				else:
					ALMotionRef_008B.angleInterpolationBezier(UID0133_names,UID0133_time,UID0133_angle)
				UID0178=UID012D
			except Exception, errorMsg:
				UID0178=[True,1,str(errorMsg)]
				UID011E=0
		else:
			UID0178=UID012D
			UID011E=0
		if UID0178[0]== False:
			try:
				UID028F=ALMemoryRef_0081
				UID018F=np.array(ALMemoryRef_0081.getListData(UID00BF.tolist()))
				UID027D=UID0178
			except Exception, errorMsg:
				UID027D=[True,1,str(errorMsg)]
				UID018F=np.array([],dtype="float64")
				UID028F=0
		else:
			UID027D=UID0178
			UID018F=np.array([],dtype="float64")
			UID028F=0
		try:
			UID0198=UID018F.tolist().index(1.000000)
		except:
			UID0198=-1
		if UID027D[0]== False:
			try:
				UID026D=UID028F
				UID0255=UID028F.getData("VIRobotics_Page")
				UID0264=UID027D
			except Exception, errorMsg:
				UID0264=[True,1,str(errorMsg)]
				UID0255=""
				UID026D=0
		else:
			UID0264=UID027D
			UID0255=""
			UID026D=0
		UID0195=UID0198>=0
		UID051F=UID0264[0]
		if UID0255=="home":
			UID0260=False
		else: 
			UID0260=True
		ErrorOut_05A9=UID0264
		UID0287=UID0B8B|UID0195
		UID01FB=UID0195|UID0260
		UID0522=UID0287|UID0260
		UID01FF=UID01FB
		WhileS_D1S_ADS_BBS_B7_00B0=UID0522|UID051F
		WhileS_D1S_ADS_BBS_B7_00B0_Stop=WhileS_D1S_ADS_BBS_B7_00B0
	queue_UID01FF.put(UID01FF)
	queue_ErrorOut_05A9.put(ErrorOut_05A9)
def main(timeout_s_,ErrorOut,movepath,ALMotionRef,ALMemoryRef):
    millisecond_timer_value_009D=int(time.time()*1000)
    UID04EF=len(movepath)
    UID00A1=1000*timeout_s_
    ALMemoryRef_0081=ALMemoryRef
    ALMotionRef_008B=ALMotionRef
    movepath_0530=movepath
    ErrorOut_0091=ErrorOut
    queue_UID01FF=Queue.Queue()
    queue_ErrorOut_05A9=Queue.Queue()
    thread.start_new_thread(UID007F,(ALMemoryRef_0081,ALMotionRef_008B,ErrorOut_0091,millisecond_timer_value_009D,UID00A1,UID04EF,movepath_0530,queue_UID01FF,queue_ErrorOut_05A9,timeout_s_,ErrorOut,movepath,ALMotionRef,ALMemoryRef,))
    ErrorOut_05A9=queue_ErrorOut_05A9.get()
    queue_ErrorOut_05A9.put(ErrorOut_05A9)
    error_out=ErrorOut_05A9
    UID01FF=queue_UID01FF.get()
    queue_UID01FF.put(UID01FF)
    touch=UID01FF
    return error_out,touch
if __name__ == "__main__":
    error_out,touch=main(timeout_s_,ErrorOut,movepath,ALMotionRef,ALMemoryRef)
