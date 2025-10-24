# -*- coding: utf-8 -*-
JSON_Tree=None
import numpy as np
result=[0,"",np.array([],dtype="S"),np.array([],dtype="S"),""]
import copy
error_IO=[False,0,""]
error_in__no_error_=[False,0,""]
import imp
import semantic_getResult_openQA
imp.reload (semantic_getResult_openQA)
import semantic_getResult_weather
imp.reload (semantic_getResult_weather)
import semantic_getResult_poetry
imp.reload (semantic_getResult_poetry)
import semantic_getResult_music
imp.reload (semantic_getResult_music)
import semantic_getResult_restaurant
imp.reload (semantic_getResult_restaurant)
import semantic_getResult_schedule
imp.reload (semantic_getResult_schedule)
import semantic_getResult_translation
imp.reload (semantic_getResult_translation)
import semantic_getResult_joke
imp.reload (semantic_getResult_joke)
import semantic_getResult_news
imp.reload (semantic_getResult_news)
import semantic_getResult_SAMPLERATE_sensor
imp.reload (semantic_getResult_SAMPLERATE_sensor)
import semantic_getResult_SAMPLERATE_robot_arm
imp.reload (semantic_getResult_SAMPLERATE_robot_arm)
def main(error_in__no_error_,JSON_Tree):
    UID00FA=[0,"",np.array([],dtype="S"),np.array([],dtype="S"),""]
    if error_in__no_error_[0]== False:
    	try:
    		UID00AC=0.000000
    		UID009A=JSON_Tree
    		try:
    			UID00CF=JSON_Tree["rc"]
    			UID0094=False
    		except:
    			UID00CF=0
    			UID0094=True
    		
    		UID006D=error_in__no_error_
    	except Exception, errorMsg:
    		UID006D=[True,1,str(errorMsg)]
    		UID0094=False
    		UID00CF=0.000000
    		UID009A=None
    else:
    	UID006D=error_in__no_error_
    	UID0094=False
    	UID00CF=0.000000
    	UID009A=None
    if UID006D[0]== False:
    	try:
    		UID0070=""
    		UID005E=JSON_Tree
    		try:
    			UID0482=JSON_Tree["text"]
    			UID0058=False
    		except:
    			UID0482=""
    			UID0058=True
    		
    		UID0464=UID006D
    	except Exception, errorMsg:
    		UID0464=[True,1,str(errorMsg)]
    		UID0058=False
    		UID0482=""
    		UID005E=None
    else:
    	UID0464=UID006D
    	UID0058=False
    	UID0482=""
    	UID005E=None
    UID00CC=int(UID00CF)
    UID0882=copy.copy(UID00FA)
    UID0882[0]=UID00CC
    UID049B=UID00CC
    UID048F=JSON_Tree
    if UID0464[0]==True:
    	UID0476=[0,"",np.array([],dtype="S"),np.array([],dtype="S"),""]
    	UID0704=UID0464
    else: 
    	try:
    		UID035B=UID0482.encode('utf-8')
    	except:
    		UID035B=UID0482
    	UID015F=copy.copy(UID0882)
    	UID015F[4]=UID035B
    	UID0155=UID048F
    	UID0649=UID0464
    	UID0150=UID049B
    	if UID0150==0 or UID0150==3:
    		if UID0649[0]== False:
    			try:
    				UID018E=UID0155
    				try:
    					UID09DD=UID0155["service"]
    					UID0188=False
    				except:
    					UID09DD={}
    					UID0188=True
    				UID09D2=UID0649
    			except Exception, errorMsg:
    				UID09D2=[True,1,str(errorMsg)]
    				UID0188=False
    				UID09DD=None
    				UID018E=None
    		else:
    			UID09D2=UID0649
    			UID0188=False
    			UID09DD=None
    			UID018E=None
    		if UID09D2[0]== False:
    			try:
    				try:
    					UID09C2=UID09DD.encode('utf-8')
    				except:
    					UID09C2=UID09DD
    				UID068F=UID09D2
    			except Exception, errorMsg:
    				UID068F=[True,1,str(errorMsg)]
    				UID09C2=""
    		else:
    			UID068F=UID09D2
    			UID09C2=""
    		UID01CC=copy.copy(UID015F)
    		UID01CC[1]=UID09C2
    		UID01BC=UID0155
    		UID01B4=UID09C2
    		if UID01B4=="False":
    			UID073C=UID068F
    			UID01D4=UID01CC
    		elif UID01B4=="openQA":
    			UID093B=semantic_getResult_openQA.main(UID068F,UID01BC)
    			UID084E=UID093B[0]
    			UID09E5=UID093B[1]
    			UID09E2=UID093B[2]
    			UID0836=copy.copy(UID01CC)
    			UID0836[2]=UID09E2
    			UID0836[3]=UID09E5
    			UID073C=UID084E
    			UID01D4=UID0836
    		elif UID01B4=="weather":
    			UID0743=semantic_getResult_weather.main(UID068F,UID01BC)
    			UID0728=UID0743[0]
    			UID0610=UID0743[1]
    			UID0523=np.concatenate((["AnimatedSay"],["RerunVoicecloud"]))
    			UID01D9=copy.copy(UID01CC)
    			UID01D9[1]="weather"
    			UID01D9[2]=UID0523
    			UID01D9[3]=UID0610
    			UID073C=UID0728
    			UID01D4=UID01D9
    		elif UID01B4=="poetry":
    			UID076E=semantic_getResult_poetry.main(UID068F,UID01BC)
    			UID0646=UID076E[0]
    			UID068E=UID076E[1]
    			UID0BB5=UID076E[2]
    			UID063B=copy.copy(UID01CC)
    			UID063B[3]=UID0BB5
    			UID063B[2]=UID068E
    			UID073C=UID0646
    			UID01D4=UID063B
    		elif UID01B4=="musicX":
    			UID013C=semantic_getResult_music.main(UID068F,UID01BC)
    			UID072C=UID013C[0]
    			UID02EA=UID013C[1]
    			UID097F=UID013C[2]
    			UID01DA=copy.copy(UID01CC)
    			UID01DA[2]=UID02EA
    			UID01DA[3]=UID097F
    			UID073C=UID072C
    			UID01D4=UID01DA
    		elif UID01B4=="restaurant":
    			UID05A1=semantic_getResult_restaurant.main(UID068F,UID01BC)
    			UID0730=UID05A1[0]
    			UID040C=UID05A1[1]
    			UID0312=np.concatenate((["restaurant"],["RerunVoicecloud"]))
    			UID01DB=copy.copy(UID01CC)
    			UID01DB[2]=UID0312
    			UID01DB[3]=UID040C
    			UID073C=UID0730
    			UID01D4=UID01DB
    		elif UID01B4=="Ctripflight":
    			if UID068F[0]== False:
    				try:
    					UID07CB=UID01BC
    					try:
    						UID097D=UID01BC["webPage"]
    						UID07C0=False
    					except:
    						UID097D={}
    						UID07C0=True
    					UID0973=UID068F
    				except Exception, errorMsg:
    					UID0973=[True,1,str(errorMsg)]
    					UID07C0=False
    					UID097D=None
    					UID07CB=None
    			else:
    				UID0973=UID068F
    				UID07C0=False
    				UID097D=None
    				UID07CB=None
    			UID0608=np.concatenate((["Ctripflight"],["RerunVoicecloud"]))
    			if UID0973[0]== False:
    				try:
    					UID0976=""
    					UID0964=UID097D
    					try:
    						UID0C9E=UID097D["url"]
    						UID095E=False
    					except:
    						UID0C9E=""
    						UID095E=True
    					
    					UID056A=UID0973
    				except Exception, errorMsg:
    					UID056A=[True,1,str(errorMsg)]
    					UID095E=False
    					UID0C9E=""
    					UID0964=None
    			else:
    				UID056A=UID0973
    				UID095E=False
    				UID0C9E=""
    				UID0964=None
    			try:
    				UID0D40=UID0C9E.encode('utf-8')
    			except:
    				UID0D40=UID0C9E
    			UID073C=UID056A
    			UID078A=np.array([UID0D40])
    			UID0554=copy.copy(UID01CC)
    			UID0554[2]=UID0608
    			UID0554[3]=UID078A
    			UID01D4=UID0554
    		elif UID01B4=="telephone":
    			UID073C=UID068F
    			UID01D4=UID01CC
    		elif UID01B4=="airControl":
    			UID073C=UID068F
    			UID01D4=UID01CC
    		elif UID01B4=="tv":
    			UID073C=UID068F
    			UID01D4=UID01CC
    		elif UID01B4=="websearch":
    			if UID068F[0]== False:
    				try:
    					UID0E46=UID01BC
    					try:
    						UID0E9F=UID01BC["webPage"]
    						UID0E40=False
    					except:
    						UID0E9F={}
    						UID0E40=True
    					UID0E96=UID068F
    				except Exception, errorMsg:
    					UID0E96=[True,1,str(errorMsg)]
    					UID0E40=False
    					UID0E9F=None
    					UID0E46=None
    			else:
    				UID0E96=UID068F
    				UID0E40=False
    				UID0E9F=None
    				UID0E46=None
    			UID1155=np.concatenate((["websearch"],["RerunVoicecloud"]))
    			if UID0E96[0]== False:
    				try:
    					UID0E99=""
    					UID0E87=UID0E9F
    					try:
    						UID0EBC=UID0E9F["url"]
    						UID0E81=False
    					except:
    						UID0EBC=""
    						UID0E81=True
    					
    					UID0DAA=UID0E96
    				except Exception, errorMsg:
    					UID0DAA=[True,1,str(errorMsg)]
    					UID0E81=False
    					UID0EBC=""
    					UID0E87=None
    			else:
    				UID0DAA=UID0E96
    				UID0E81=False
    				UID0EBC=""
    				UID0E87=None
    			UID1007=np.array([UID0EBC])
    			UID073C=UID0DAA
    			UID0DA4=copy.copy(UID01CC)
    			UID0DA4[2]=UID1155
    			UID0DA4[3]=UID1007
    			UID01D4=UID0DA4
    		elif UID01B4=="stock":
    			if UID068F[0]== False:
    				try:
    					UID122B=UID01BC
    					try:
    						UID1284=UID01BC["webPage"]
    						UID1225=False
    					except:
    						UID1284={}
    						UID1225=True
    					UID127B=UID068F
    				except Exception, errorMsg:
    					UID127B=[True,1,str(errorMsg)]
    					UID1225=False
    					UID1284=None
    					UID122B=None
    			else:
    				UID127B=UID068F
    				UID1225=False
    				UID1284=None
    				UID122B=None
    			UID12AB=np.concatenate((["stock"],["RerunVoicecloud"]))
    			if UID127B[0]== False:
    				try:
    					UID127E=""
    					UID126C=UID1284
    					try:
    						UID12A1=UID1284["url"]
    						UID1266=False
    					except:
    						UID12A1=""
    						UID1266=True
    					
    					UID11F6=UID127B
    				except Exception, errorMsg:
    					UID11F6=[True,1,str(errorMsg)]
    					UID1266=False
    					UID12A1=""
    					UID126C=None
    			else:
    				UID11F6=UID127B
    				UID1266=False
    				UID12A1=""
    				UID126C=None
    			UID12AE=np.array([UID12A1])
    			UID073C=UID11F6
    			UID11F0=copy.copy(UID01CC)
    			UID11F0[2]=UID12AB
    			UID11F0[3]=UID12AE
    			UID01D4=UID11F0
    		elif UID01B4=="schedule":
    			UID090E=semantic_getResult_schedule.main(UID068F,UID01BC)
    			UID07BE=UID090E[0]
    			UID07E2=UID090E[1]
    			UID0D0E=UID090E[2]
    			UID0CAB=UID090E[3]
    			UID0803=UID090E[4]
    			UID0BD6=np.concatenate((["schedule"],["RerunVoicecloud"]))
    			UID0A81=np.concatenate(([UID0CAB],[UID0D0E],[UID07E2],[UID0803]))
    			UID073C=UID07BE
    			UID07B4=copy.copy(UID01CC)
    			UID07B4[2]=UID0BD6
    			UID07B4[3]=UID0A81
    			UID01D4=UID07B4
    		elif UID01B4=="translation":
    			UID0C4D=semantic_getResult_translation.main(UID068F,UID01BC)
    			UID05E6=UID0C4D[0]
    			UID0B45=UID0C4D[1]
    			UID0A12=UID0C4D[2]
    			UID05DF=copy.copy(UID01CC)
    			UID05DF[2]=UID0A12
    			UID05DF[3]=UID0B45
    			UID073C=UID05E6
    			UID01D4=UID05DF
    		elif UID01B4=="joke":
    			UID0E3A=semantic_getResult_joke.main(UID068F,UID01BC)
    			UID0EFC=UID0E3A[0]
    			UID11A1=UID0E3A[1]
    			UID10F8=UID0E3A[2]
    			UID0EF6=copy.copy(UID01CC)
    			UID0EF6[2]=UID10F8
    			UID0EF6[3]=UID11A1
    			UID073C=UID0EFC
    			UID01D4=UID0EF6
    		elif UID01B4=="news":
    			UID0892=semantic_getResult_news.main(UID068F,UID01BC)
    			UID081B=UID0892[0]
    			UID0A37=UID0892[1]
    			UID0B1E=UID0892[2]
    			UID07C2=copy.copy(UID01CC)
    			UID07C2[2]=UID0B1E
    			UID07C2[3]=UID0A37
    			UID073C=UID081B
    			UID01D4=UID07C2
    		elif UID01B4=="SAMPLERATE.sensor":
    			UID09F8=semantic_getResult_SAMPLERATE_sensor.main(UID068F,UID01BC)
    			UID08DB=UID09F8[0]
    			UID0B4A=UID09F8[1]
    			UID0C50=UID09F8[2]
    			UID08D4=copy.copy(UID01CC)
    			UID08D4[2]=UID0B4A
    			UID08D4[3]=UID0C50
    			UID073C=UID08DB
    			UID01D4=UID08D4
    		elif UID01B4=="SAMPLERATE.robot_arm":
    			UID08CD=semantic_getResult_SAMPLERATE_robot_arm.main(UID068F,UID01BC)
    			UID08E7=UID08CD[0]
    			UID0B55=UID08CD[1]
    			UID09F7=UID08CD[2]
    			UID08E1=copy.copy(UID01CC)
    			UID08E1[2]=UID09F7
    			UID08E1[3]=UID0B55
    			UID073C=UID08E7
    			UID01D4=UID08E1
    		else: 
    			if UID068F[0]== False:
    				try:
    					UID0228=UID01BC
    					try:
    						UID0270=UID01BC["answer"]
    						UID0222=False
    					except:
    						UID0270={}
    						UID0222=True
    					UID0267=UID068F
    				except Exception, errorMsg:
    					UID0267=[True,1,str(errorMsg)]
    					UID0222=False
    					UID0270=None
    					UID0228=None
    			else:
    				UID0267=UID068F
    				UID0222=False
    				UID0270=None
    				UID0228=None
    			UID0282=np.concatenate((["AnimatedSay"],["RerunVoicecloud"]))
    			if UID0267[0]== False:
    				try:
    					UID026A=""
    					UID0258=UID0270
    					try:
    						UID0514=UID0270["text"]
    						UID0252=False
    					except:
    						UID0514=""
    						UID0252=True
    					
    					UID0724=UID0267
    				except Exception, errorMsg:
    					UID0724=[True,1,str(errorMsg)]
    					UID0252=False
    					UID0514=""
    					UID0258=None
    			else:
    				UID0724=UID0267
    				UID0252=False
    				UID0514=""
    				UID0258=None
    			try:
    				UID0407=UID0514.encode('utf-8')
    			except:
    				UID0407=UID0514
    			UID073C=UID0724
    			UID0285=np.array([UID0407])
    			UID01D8=copy.copy(UID01CC)
    			UID01D8[2]=UID0282
    			UID01D8[3]=UID0285
    			UID01D4=UID01D8
    		UID0716=UID073C
    		UID0164=UID01D4
    	else: 
    		UID0716=UID0649
    		UID0164=UID015F
    	UID0704=UID0716
    	UID0476=UID0164
    error_IO=UID0704
    result=UID0476
    return error_IO,result
if __name__ == "__main__":
    error_IO,result=main(error_in__no_error_,JSON_Tree)
