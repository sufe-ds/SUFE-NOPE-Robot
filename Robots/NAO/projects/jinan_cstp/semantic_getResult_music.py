# -*- coding: utf-8 -*-
String=""
import numpy as np
Action=np.array([],dtype="S")
Array=np.array([],dtype="S")
error_out=[False,0,""]
JSON_Tree=None
error_in__no_error_=[False,0,""]
import re
def main(error_in__no_error_,JSON_Tree):
    if error_in__no_error_[0]== False:
    	try:
    		UID0570=JSON_Tree
    		try:
    			UID05CE=JSON_Tree["semantic"]
    			UID056A=False
    		except:
    			UID05CE={}
    			UID056A=True
    		UID05C5=error_in__no_error_
    	except Exception, errorMsg:
    		UID05C5=[True,1,str(errorMsg)]
    		UID056A=False
    		UID05CE=None
    		UID0570=None
    else:
    	UID05C5=error_in__no_error_
    	UID056A=False
    	UID05CE=None
    	UID0570=None
    if UID05C5[0]== False:
    	try:
    		UID05B6=UID05CE
    		UID060A=UID05CE[0]
    		UID05B0=False
    		UID0601=UID05C5
    	except Exception, errorMsg:
    		UID0601=[True,1,str(errorMsg)]
    		UID05B0=False
    		UID060A=None
    		UID05B6=None
    else:
    	UID0601=UID05C5
    	UID05B0=False
    	UID060A=None
    	UID05B6=None
    if UID0601[0]== False:
    	try:
    		UID05F2=UID060A
    		try:
    			UID0646=UID060A["slots"]
    			UID05EC=False
    		except:
    			UID0646={}
    			UID05EC=True
    		UID063D=UID0601
    	except Exception, errorMsg:
    		UID063D=[True,1,str(errorMsg)]
    		UID05EC=False
    		UID0646=None
    		UID05F2=None
    else:
    	UID063D=UID0601
    	UID05EC=False
    	UID0646=None
    	UID05F2=None
    if UID063D[0]== False:
    	try:
    		UID062E=UID0646
    		ForS_D1S_ADS_BBS_B7_064B=len(UID0646)
    		error_out_064F=UID063D
    	except Exception, errorMsg:
    		error_out_064F=[True,1,str(errorMsg)]
    		ForS_D1S_ADS_BBS_B7_064B=0
    		UID062E=None
    else:
    	error_out_064F=UID063D
    	ForS_D1S_ADS_BBS_B7_064B=0
    	UID062E=None
    UID065E=""
    JSON_Tree_Passthrough__JSON_Array__0658=UID062E
    i_066F=-1
    ForS_D1S_ADS_BBS_B7_0649_count=ForS_D1S_ADS_BBS_B7_064B
    for i in range(0, ForS_D1S_ADS_BBS_B7_0649_count):
    	i_066F=i_066F+1
    	if error_out_064F[0]== False:
    		try:
    			UID06A1=JSON_Tree_Passthrough__JSON_Array__0658
    			UID06E9=JSON_Tree_Passthrough__JSON_Array__0658[i_066F]
    			UID069B=False
    			UID06E0=error_out_064F
    		except Exception, errorMsg:
    			UID06E0=[True,1,str(errorMsg)]
    			UID069B=False
    			UID06E9=None
    			UID06A1=None
    	else:
    		UID06E0=error_out_064F
    		UID069B=False
    		UID06E9=None
    		UID06A1=None
    	if UID06E0[0]== False:
    		try:
    			UID06D1=UID06E9
    			try:
    				UID06FD=UID06E9["name"]
    				UID06CB=False
    			except:
    				UID06FD={}
    				UID06CB=True
    			UID06F7=UID06E0
    		except Exception, errorMsg:
    			UID06F7=[True,1,str(errorMsg)]
    			UID06CB=False
    			UID06FD=None
    			UID06D1=None
    	else:
    		UID06F7=UID06E0
    		UID06CB=False
    		UID06FD=None
    		UID06D1=None
    	if UID06F7[0]== False:
    		try:
    			UID070E=str(UID06FD)
    			error_out_064F=UID06F7
    		except Exception, errorMsg:
    			error_out_064F=[True,1,str(errorMsg)]
    			UID070E=""
    	else:
    		error_out_064F=UID06F7
    		UID070E=""
    	UID065E=UID065E+UID070E+"_"
    	
    	
    UID0769=UID065E
    UID0772=error_out_064F
    UID1810=UID062E
    UID0A23=JSON_Tree
    if UID0769=="":
    	UID07A7=np.array(["song_search_random","song_play_all","RerunVoicecloud"],dtype="S")
    	UID0C5E=np.array([],dtype="S")
    	UID0796=UID07A7
    	UID078D=UID0C5E
    	UID0784=UID0772
    elif UID0769=="song_" or UID0769=="source_":
    	UID1F40=np.array(["song_search","song_play","RerunVoicecloud"],dtype="S")
    	if UID0772[0]== False:
    		try:
    			UID1943=UID1810
    			UID19A2=UID1810[0]
    			UID193D=False
    			UID1998=UID0772
    		except Exception, errorMsg:
    			UID1998=[True,1,str(errorMsg)]
    			UID193D=False
    			UID19A2=None
    			UID1943=None
    	else:
    		UID1998=UID0772
    		UID193D=False
    		UID19A2=None
    		UID1943=None
    	UID0796=UID1F40
    	if UID1998[0]== False:
    		try:
    			UID1986=UID19A2
    			try:
    				UID1A0E=UID19A2["value"]
    				UID197E=False
    			except:
    				UID1A0E={}
    				UID197E=True
    			UID1A03=UID1998
    		except Exception, errorMsg:
    			UID1A03=[True,1,str(errorMsg)]
    			UID197E=False
    			UID1A0E=None
    			UID1986=None
    	else:
    		UID1A03=UID1998
    		UID197E=False
    		UID1A0E=None
    		UID1986=None
    	if UID1A03[0]== False:
    		try:
    			try:
    				UID19BC=UID1A0E.encode('utf-8')
    			except:
    				UID19BC=UID1A0E
    			UID0789=UID1A03
    		except Exception, errorMsg:
    			UID0789=[True,1,str(errorMsg)]
    			UID19BC=""
    	else:
    		UID0789=UID1A03
    		UID19BC=""
    	UID1A9A="请欣赏"+UID19BC
    	UID0784=UID0789
    	UID0792=np.concatenate(([UID1A9A],[UID19BC]))
    	UID078D=UID0792
    elif UID0769=="artist_song_":
    	UID160F=np.array(["song_search_artist_song","song_play","RerunVoicecloud"],dtype="S")
    	JSON_Tree_Passthrough__JSON_Array__23DA=UID1810
    	error_out_23D1=UID0772
    	ForS_D1S_ADS_BBS_B7_23CD=2
    	UID03EF=np.array([],dtype="S")
    	i_23F1=-1
    	ForS_D1S_ADS_BBS_B7_23C7_count=ForS_D1S_ADS_BBS_B7_23CD
    	for i in range(0, ForS_D1S_ADS_BBS_B7_23C7_count):
    		i_23F1=i_23F1+1
    		if error_out_23D1[0]== False:
    			try:
    				UID2423=JSON_Tree_Passthrough__JSON_Array__23DA
    				UID246B=JSON_Tree_Passthrough__JSON_Array__23DA[i_23F1]
    				UID241D=False
    				UID2462=error_out_23D1
    			except Exception, errorMsg:
    				UID2462=[True,1,str(errorMsg)]
    				UID241D=False
    				UID246B=None
    				UID2423=None
    		else:
    			UID2462=error_out_23D1
    			UID241D=False
    			UID246B=None
    			UID2423=None
    		if UID2462[0]== False:
    			try:
    				UID2453=UID246B
    				try:
    					UID0271=UID246B["value"]
    					UID244D=False
    				except:
    					UID0271={}
    					UID244D=True
    				UID0266=UID2462
    			except Exception, errorMsg:
    				UID0266=[True,1,str(errorMsg)]
    				UID244D=False
    				UID0271=None
    				UID2453=None
    		else:
    			UID0266=UID2462
    			UID244D=False
    			UID0271=None
    			UID2453=None
    		if UID0266[0]== False:
    			try:
    				try:
    					UID03EB=UID0271.encode('utf-8')
    				except:
    					UID03EB=UID0271
    				error_out_23D1=UID0266
    			except Exception, errorMsg:
    				error_out_23D1=[True,1,str(errorMsg)]
    				UID03EB=""
    		else:
    			error_out_23D1=UID0266
    			UID03EB=""
    		
    		UID03EF=np.concatenate((UID03EF,[UID03EB]))
    	UID0796=UID160F
    	try:
    		UID047E=UID03EF[0]
    	except:
    		UID047E=""
    	try:
    		UID09D0=UID03EF[1]
    	except:
    		UID09D0=""
    	UID0784=error_out_23D1
    	UID14E6="请欣赏"+UID047E+"的"+UID09D0
    	UID1690=np.concatenate(([UID14E6],[UID047E],[UID09D0]))
    	UID078D=UID1690
    elif UID0769=="artist_":
    	UID2228=np.array(["song_search_artist","song_play_all","RerunVoicecloud"],dtype="S")
    	if UID0772[0]== False:
    		try:
    			UID188B=UID1810
    			UID19EF=UID1810[0]
    			UID1885=False
    			UID19E4=UID0772
    		except Exception, errorMsg:
    			UID19E4=[True,1,str(errorMsg)]
    			UID1885=False
    			UID19EF=None
    			UID188B=None
    	else:
    		UID19E4=UID0772
    		UID1885=False
    		UID19EF=None
    		UID188B=None
    	UID0796=UID2228
    	if UID19E4[0]== False:
    		try:
    			UID19D1=UID19EF
    			try:
    				UID1D5C=UID19EF["value"]
    				UID19CA=False
    			except:
    				UID1D5C={}
    				UID19CA=True
    			UID1D53=UID19E4
    		except Exception, errorMsg:
    			UID1D53=[True,1,str(errorMsg)]
    			UID19CA=False
    			UID1D5C=None
    			UID19D1=None
    	else:
    		UID1D53=UID19E4
    		UID19CA=False
    		UID1D5C=None
    		UID19D1=None
    	if UID1D53[0]== False:
    		try:
    			try:
    				UID1D44=UID1D5C.encode('utf-8')
    			except:
    				UID1D44=UID1D5C
    			UID1723=UID1D53
    		except Exception, errorMsg:
    			UID1723=[True,1,str(errorMsg)]
    			UID1D44=""
    	else:
    		UID1723=UID1D53
    		UID1D44=""
    	UID209A="请欣赏"+UID1D44+"的音乐"
    	UID0784=UID1723
    	UID1727=np.concatenate(([UID209A],[UID1D44]))
    	UID078D=UID1727
    elif UID0769=="genre_" or UID0769=="tags_" or UID0769=="tags_theme_":
    	UID0FC1=np.array(["song_search_tinguid","song_play_all","RerunVoicecloud"],dtype="S")
    	if UID0772[0]== False:
    		try:
    			UID039F=UID1810
    			UID0415=UID1810[0]
    			UID0399=False
    			UID040C=UID0772
    		except Exception, errorMsg:
    			UID040C=[True,1,str(errorMsg)]
    			UID0399=False
    			UID0415=None
    			UID039F=None
    	else:
    		UID040C=UID0772
    		UID0399=False
    		UID0415=None
    		UID039F=None
    	UID0796=UID0FC1
    	if UID040C[0]== False:
    		try:
    			UID03FD=UID0415
    			try:
    				UID0464=UID0415["value"]
    				UID03F7=False
    			except:
    				UID0464={}
    				UID03F7=True
    			UID045B=UID040C
    		except Exception, errorMsg:
    			UID045B=[True,1,str(errorMsg)]
    			UID03F7=False
    			UID0464=None
    			UID03FD=None
    	else:
    		UID045B=UID040C
    		UID03F7=False
    		UID0464=None
    		UID03FD=None
    	if UID045B[0]== False:
    		try:
    			try:
    				UID0C5B=UID0464.encode('utf-8')
    			except:
    				UID0C5B=UID0464
    			UID0C6A=UID045B
    		except Exception, errorMsg:
    			UID0C6A=[True,1,str(errorMsg)]
    			UID0C5B=""
    	else:
    		UID0C6A=UID045B
    		UID0C5B=""
    	UID0C71=UID0A23
    	if UID0C5B=="儿歌":
    		UID0C99=np.array(["儿童歌曲","少儿歌曲","儿歌","摇篮曲","钢琴曲"],dtype="S")
    		if UID0C6A[0]== False:
    			try:
    				UID0CD8=UID0C71
    				try:
    					UID0D26=UID0C71["text"]
    					UID0CD1=False
    				except:
    					UID0D26={}
    					UID0CD1=True
    				UID0D1D=UID0C6A
    			except Exception, errorMsg:
    				UID0D1D=[True,1,str(errorMsg)]
    				UID0CD1=False
    				UID0D26=None
    				UID0CD8=None
    		else:
    			UID0D1D=UID0C6A
    			UID0CD1=False
    			UID0D26=None
    			UID0CD8=None
    		if UID0D1D[0]== False:
    			try:
    				try:
    					gbkstring_0D3E=UID0D26.encode('utf-8')
    				except:
    					gbkstring_0D3E=UID0D26
    				error_out_0D35=UID0D1D
    			except Exception, errorMsg:
    				error_out_0D35=[True,1,str(errorMsg)]
    				gbkstring_0D3E=""
    		else:
    			error_out_0D35=UID0D1D
    			gbkstring_0D3E=""
    		UID0D2F=UID0C99
    		i_0D50=-1
    		ForS_D1S_ADS_BBS_B7_0D53_Stop=False
    		ForS_D1S_ADS_BBS_B7_0D29_IndexsIn=[]
    		ForS_D1S_ADS_BBS_B7_0D29_IndexsIn.append(len(UID0D2F))
    		ForS_D1S_ADS_BBS_B7_0D29_Indexmin=min(ForS_D1S_ADS_BBS_B7_0D29_IndexsIn)
    		ForS_D1S_ADS_BBS_B7_0D29_count=ForS_D1S_ADS_BBS_B7_0D29_Indexmin
    		while ForS_D1S_ADS_BBS_B7_0D53_Stop==False and i_0D50<ForS_D1S_ADS_BBS_B7_0D29_count-1:
    			i_0D50=i_0D50+1
    			UID0D56_result=re.split(UID0D2F[i_0D50],gbkstring_0D3E[0:],1)
    			UID0D61=gbkstring_0D3E[:0]+UID0D56_result[0]
    			if len(UID0D56_result)==2:
    				UID0D65=UID0D2F[i_0D50]
    				UID0D68=UID0D56_result[1]
    				UID0D6C=len(UID0D61)+len(UID0D2F[i_0D50])
    			else:
    				UID0D65=""
    				UID0D68=""
    				UID0D6C=-1
    			
    			ForS_D1S_ADS_BBS_B7_0D53=UID0D2F[i_0D50]==UID0D65
    			gbkstring_0D44=UID0D65
    			ForS_D1S_ADS_BBS_B7_0D53_Stop=ForS_D1S_ADS_BBS_B7_0D53
    		UID0C7D=gbkstring_0D44
    		UID0C77=error_out_0D35
    	elif UID0C5B=="钢琴曲":
    		UID0C7D=UID0C5B
    		UID0C77=UID0C6A
    	else: 
    		UID0C7D=UID0C5B
    		UID0C77=UID0C6A
    	UID11BE="请欣赏"+UID0C7D
    	UID0784=UID0C77
    	UID2346=np.concatenate(([UID11BE],[UID0C7D]))
    	UID078D=UID2346
    elif UID0769=="artist_tags_":
    	UID1390=np.array(["song_search","song_play","RerunVoicecloud"],dtype="S")
    	JSON_Tree_Passthrough__JSON_Array__15A1=UID1810
    	error_out_15CF=UID0772
    	ForS_D1S_ADS_BBS_B7_156C=2
    	UID0A77=np.array([],dtype="S")
    	i_1568=-1
    	ForS_D1S_ADS_BBS_B7_0938_count=ForS_D1S_ADS_BBS_B7_156C
    	for i in range(0, ForS_D1S_ADS_BBS_B7_0938_count):
    		i_1568=i_1568+1
    		if error_out_15CF[0]== False:
    			try:
    				UID0751=JSON_Tree_Passthrough__JSON_Array__15A1
    				UID07F1=JSON_Tree_Passthrough__JSON_Array__15A1[i_1568]
    				UID074A=False
    				UID07E8=error_out_15CF
    			except Exception, errorMsg:
    				UID07E8=[True,1,str(errorMsg)]
    				UID074A=False
    				UID07F1=None
    				UID0751=None
    		else:
    			UID07E8=error_out_15CF
    			UID074A=False
    			UID07F1=None
    			UID0751=None
    		if UID07E8[0]== False:
    			try:
    				UID07D9=UID07F1
    				try:
    					UID082E=UID07F1["value"]
    					UID07D3=False
    				except:
    					UID082E={}
    					UID07D3=True
    				UID0825=UID07E8
    			except Exception, errorMsg:
    				UID0825=[True,1,str(errorMsg)]
    				UID07D3=False
    				UID082E=None
    				UID07D9=None
    		else:
    			UID0825=UID07E8
    			UID07D3=False
    			UID082E=None
    			UID07D9=None
    		if UID0825[0]== False:
    			try:
    				try:
    					UID0A73=UID082E.encode('utf-8')
    				except:
    					UID0A73=UID082E
    				error_out_15CF=UID0825
    			except Exception, errorMsg:
    				error_out_15CF=[True,1,str(errorMsg)]
    				UID0A73=""
    		else:
    			error_out_15CF=UID0825
    			UID0A73=""
    		
    		UID0A77=np.concatenate((UID0A77,[UID0A73]))
    	UID0796=UID1390
    	try:
    		UID0A11=UID0A77[0]
    	except:
    		UID0A11=""
    	try:
    		UID0833=UID0A77[1]
    	except:
    		UID0833=""
    	UID0839=error_out_15CF
    	UID083F=UID0A23
    	if UID0833=="儿歌":
    		UID1282=np.array(["儿童歌曲","少儿歌曲","儿歌","摇篮曲"],dtype="S")
    		if UID0839[0]== False:
    			try:
    				UID12B8=UID083F
    				try:
    					UID1300=UID083F["text"]
    					UID12B2=False
    				except:
    					UID1300={}
    					UID12B2=True
    				UID12F7=UID0839
    			except Exception, errorMsg:
    				UID12F7=[True,1,str(errorMsg)]
    				UID12B2=False
    				UID1300=None
    				UID12B8=None
    		else:
    			UID12F7=UID0839
    			UID12B2=False
    			UID1300=None
    			UID12B8=None
    		if UID12F7[0]== False:
    			try:
    				try:
    					gbkstring_1318=UID1300.encode('utf-8')
    				except:
    					gbkstring_1318=UID1300
    				error_out_130F=UID12F7
    			except Exception, errorMsg:
    				error_out_130F=[True,1,str(errorMsg)]
    				gbkstring_1318=""
    		else:
    			error_out_130F=UID12F7
    			gbkstring_1318=""
    		UID1309=UID1282
    		i_132A=-1
    		ForS_D1S_ADS_BBS_B7_132D_Stop=False
    		ForS_D1S_ADS_BBS_B7_1303_IndexsIn=[]
    		ForS_D1S_ADS_BBS_B7_1303_IndexsIn.append(len(UID1309))
    		ForS_D1S_ADS_BBS_B7_1303_Indexmin=min(ForS_D1S_ADS_BBS_B7_1303_IndexsIn)
    		ForS_D1S_ADS_BBS_B7_1303_count=ForS_D1S_ADS_BBS_B7_1303_Indexmin
    		while ForS_D1S_ADS_BBS_B7_132D_Stop==False and i_132A<ForS_D1S_ADS_BBS_B7_1303_count-1:
    			i_132A=i_132A+1
    			UID1330_result=re.split(UID1309[i_132A],gbkstring_1318[0:],1)
    			UID133B=gbkstring_1318[:0]+UID1330_result[0]
    			if len(UID1330_result)==2:
    				UID133E=UID1309[i_132A]
    				UID1341=UID1330_result[1]
    				UID1344=len(UID133B)+len(UID1309[i_132A])
    			else:
    				UID133E=""
    				UID1341=""
    				UID1344=-1
    			
    			ForS_D1S_ADS_BBS_B7_132D=UID1309[i_132A]==UID133E
    			gbkstring_131E=UID133E
    			ForS_D1S_ADS_BBS_B7_132D_Stop=ForS_D1S_ADS_BBS_B7_132D
    		UID084B=gbkstring_131E
    		UID0845=error_out_130F
    	elif UID0833=="钢琴曲":
    		UID084B=UID0833
    		UID0845=UID0839
    	else: 
    		UID084B=UID0833
    		UID0845=UID0839
    	UID13B4="请欣赏"+UID0A11+"的"+UID084B
    	UID0784=UID0845
    	UID06B8=np.concatenate(([UID13B4],[UID0A11],[UID084B]))
    	UID078D=UID06B8
    else: 
    	UID0A47=np.array([],dtype="S")
    	UID0AAA=np.array([],dtype="S")
    	UID0796=UID0A47
    	UID078D=UID0AAA
    	UID0784=UID0772
    String=UID065E
    error_out=UID0784
    Array=UID078D
    Action=UID0796
    return error_out,Action,Array
if __name__ == "__main__":
    error_out,Action,Array=main(error_in__no_error_,JSON_Tree)
