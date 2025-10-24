# -*- coding: utf-8 -*-
source=""
userid=""
import numpy as np
content=np.array([],dtype="S")
action=np.array([],dtype="S")
result=[0,"",np.array([],dtype="S"),np.array([],dtype="S"),""]
import imp
import tuling_v2
imp.reload (tuling_v2)
import Clear_Errors
imp.reload (Clear_Errors)
import yiku_searchSongID
imp.reload (yiku_searchSongID)
import copy
def main(userid,result):
    UID1BB8=result[3]
    UID1BDA=result[4]
    UID1BBE=result[2]
    UID1BD0=len(UID1BB8)
    try:
    	UID271D=UID1BBE[0]
    except:
    	UID271D=""
    UID2742=UID1BD0>0
    UID273F=UID271D=="song_search_random"
    UID1BD5=UID2742|UID273F
    UID1BE9=UID1BB8
    UID1BEE=UID1BBE
    UID1BF3=UID271D
    UID073C=userid
    if UID1BD5==True:
    	UID1CAF=UID1BE9
    	UID1CC1=UID1BEE
    	UID1CA6=UID1BF3
    	UID098C=UID1BDA
    	if UID1CA6=="song_search":
    		try:
    			UID1D25=UID1CAF[0]
    		except:
    			UID1D25=""
    		try:
    			UID06D6=UID1CAF[1]
    		except:
    			UID06D6=""
    		UID06CB=[False,0,""]
    		UID06A1=yiku_searchSongID.main(UID06CB,"song",UID06D6)
    		UID1D16=UID06A1[0]
    		UID1D1B=UID06A1[1]
    		UID0751=UID06A1[2]
    		if UID1D16[0]==True:
    			UID1D24=np.array(["抱歉，未找到相应歌曲。"])
    			UID1D2E=np.array(["AnimatedSay"])
    			UID07D1=""
    			UID1D2A=UID1D2E
    			UID1D20=UID1D24
    		else: 
    			UID1D44=len(UID1D1B)
    			UID1D49=UID1D44>0
    			UID1D53=UID1D1B
    			UID1D5D=UID1D25
    			UID0730=UID0751
    			if UID1D49==True:
    				UID1DA4=np.array(["AnimatedSay","Music"],dtype="S")
    				try:
    					UID1DC5=UID1D53[0]
    				except:
    					UID1DC5=["","",""]
    				UID0770=UID0730
    				UID1D58=UID1DA4
    				UID1DE0=UID1DC5[2]
    				UID1D52=np.concatenate(([UID1D5D],[UID1DE0]))
    				UID1D4E=UID1D52
    			else: 
    				UID1D51=np.array(["抱歉，未找到相应歌曲。"])
    				UID1D5B=np.array(["AnimatedSay"])
    				UID0770=""
    				UID1D58=UID1D5B
    				UID1D4E=UID1D51
    			UID07D1=UID0770
    			UID1D2A=UID1D58
    			UID1D20=UID1D4E
    		UID07BF=UID07D1
    		UID1CCA=UID1D2A
    		UID1CB8=UID1D20
    	elif UID1CA6=="song_search_artist_song":
    		try:
    			UID1E83=UID1CAF[0]
    		except:
    			UID1E83=""
    		try:
    			UID0601=UID1CAF[1]
    		except:
    			UID0601=""
    		try:
    			UID068B=UID1CAF[2]
    		except:
    			UID068B=""
    		UID08E2=UID0601+"_"+UID068B
    		UID08D9=[False,0,""]
    		UID08B8=yiku_searchSongID.main(UID08D9,"artist_song",UID08E2)
    		UID1E79=UID08B8[0]
    		UID1E8D=UID08B8[1]
    		UID0950=UID08B8[2]
    		if UID1E79[0]==True:
    			UID1E82=np.array(["抱歉，未找到相应歌曲。"])
    			UID1E8C=np.array(["AnimatedSay"])
    			UID09BF=""
    			UID1E88=UID1E8C
    			UID1E7E=UID1E82
    		else: 
    			UID1EAC=len(UID1E8D)
    			UID1EB1=UID1EAC>0
    			UID1EC0=UID1E83
    			UID1EC5=UID1E8D
    			UID097E=UID0950
    			if UID1EB1==True:
    				UID1F0C=np.array(["AnimatedSay","Music"],dtype="S")
    				try:
    					UID1F45=UID1EC5[0]
    				except:
    					UID1F45=["","",""]
    				UID09D3=UID097E
    				UID1EBB=UID1F0C
    				UID1F33=UID1F45[2]
    				UID1EBA=np.concatenate(([UID1EC0],[UID1F33]))
    				UID1EB6=UID1EBA
    			else: 
    				UID1EB9=np.array(["抱歉，未找到相应歌曲。"])
    				UID1EBE=np.array(["AnimatedSay"])
    				UID09D3=""
    				UID1EBB=UID1EBE
    				UID1EB6=UID1EB9
    			UID09BF=UID09D3
    			UID1E88=UID1EBB
    			UID1E7E=UID1EB6
    		UID07BF=UID09BF
    		UID1CCA=UID1E88
    		UID1CB8=UID1E7E
    	elif UID1CA6=="song_search_artist":
    		try:
    			UID2054=UID1CAF[0]
    		except:
    			UID2054=""
    		try:
    			UID0AAC=UID1CAF[1]
    		except:
    			UID0AAC=""
    		UID0AA3=[False,0,""]
    		UID033F=yiku_searchSongID.main(UID0AA3,"artist",UID0AAC)
    		UID204A=UID033F[0]
    		UID205E=UID033F[1]
    		UID0B2F=UID033F[2]
    		if UID204A[0]==True:
    			UID2053=np.array(["抱歉，未找到相应歌曲。"])
    			UID205D=np.array(["AnimatedSay"])
    			UID0B8E=""
    			UID2059=UID205D
    			UID204F=UID2053
    		else: 
    			UID2078=len(UID205E)
    			UID207D=UID2078>0
    			UID208C=UID2054
    			UID2091=UID205E
    			UID0B6B=UID0B2F
    			if UID207D==True:
    				UID20D8=np.array(["AnimatedSay","Music"],dtype="S")
    				results_2109=UID2091
    				UID210F=np.array([],dtype="S")
    				i_211D=-1
    				ForS_D1S_ADS_BBS_B7_2103_IndexsIn=[]
    				ForS_D1S_ADS_BBS_B7_2103_IndexsIn.append(len(results_2109))
    				ForS_D1S_ADS_BBS_B7_2103_Indexmin=min(ForS_D1S_ADS_BBS_B7_2103_IndexsIn)
    				ForS_D1S_ADS_BBS_B7_2103_count=ForS_D1S_ADS_BBS_B7_2103_Indexmin
    				for i in range(0, ForS_D1S_ADS_BBS_B7_2103_count):
    					i_211D=i_211D+1
    					UID2112=results_2109[i_211D][2]
    					UID210F=np.concatenate((UID210F,[UID2112]))
    				UID0BA0=UID0B6B
    				UID2087=UID20D8
    				UID2086=np.concatenate(([UID208C],UID210F))
    				UID2082=UID2086
    			else: 
    				UID2085=np.array(["抱歉，未找到相应歌曲。"])
    				UID208A=np.array(["AnimatedSay"])
    				UID0BA0=""
    				UID2087=UID208A
    				UID2082=UID2085
    			UID0B8E=UID0BA0
    			UID2059=UID2087
    			UID204F=UID2082
    		UID07BF=UID0B8E
    		UID1CCA=UID2059
    		UID1CB8=UID204F
    	elif UID1CA6=="song_search_random":
    		UID0C45=[False,0,""]
    		UID0C15=yiku_searchSongID.main(UID0C45,"type","随机")
    		UID2270=UID0C15[0]
    		UID227F=UID0C15[1]
    		UID0D38=UID0C15[2]
    		if UID2270[0]==True:
    			UID2279=np.array(["抱歉，未找到相应歌曲。"])
    			UID227E=np.array(["AnimatedSay"])
    			UID0D78=""
    			UID227A=UID227E
    			UID2275=UID2279
    		else: 
    			UID2299=len(UID227F)
    			UID229E=UID2299>0
    			UID22AD=UID227F
    			UID0D55=UID0D38
    			if UID229E==True:
    				UID22F4=np.array(["AnimatedSay","Music"],dtype="S")
    				results_2330=UID22AD
    				UID2336=np.array([],dtype="S")
    				i_2344=-1
    				ForS_D1S_ADS_BBS_B7_232A_IndexsIn=[]
    				ForS_D1S_ADS_BBS_B7_232A_IndexsIn.append(len(results_2330))
    				ForS_D1S_ADS_BBS_B7_232A_Indexmin=min(ForS_D1S_ADS_BBS_B7_232A_IndexsIn)
    				ForS_D1S_ADS_BBS_B7_232A_count=ForS_D1S_ADS_BBS_B7_232A_Indexmin
    				for i in range(0, ForS_D1S_ADS_BBS_B7_232A_count):
    					i_2344=i_2344+1
    					UID2339=results_2330[i_2344][2]
    					UID2336=np.concatenate((UID2336,[UID2339]))
    				UID0D8A=UID0D55
    				UID22A8=UID22F4
    				UID22A7=np.concatenate((["没具体吗？那就听听我的推荐吧。"],UID2336))
    				UID22A3=UID22A7
    			else: 
    				UID22A6=np.array(["抱歉，未找到相应歌曲。"])
    				UID22AB=np.array(["AnimatedSay"])
    				UID0D8A=""
    				UID22A8=UID22AB
    				UID22A3=UID22A6
    			UID0D78=UID0D8A
    			UID227A=UID22A8
    			UID2275=UID22A3
    		UID07BF=UID0D78
    		UID1CCA=UID227A
    		UID1CB8=UID2275
    	elif UID1CA6=="song_search_tinguid":
    		try:
    			UID2445=UID1CAF[0]
    		except:
    			UID2445=""
    		try:
    			UID0E4B=UID1CAF[1]
    		except:
    			UID0E4B=""
    		UID0E42=[False,0,""]
    		UID0E23=yiku_searchSongID.main(UID0E42,"type",UID0E4B)
    		UID2431=UID0E23[0]
    		UID2440=UID0E23[1]
    		UID0EFA=UID0E23[2]
    		if UID2431[0]==True:
    			UID243A=np.array(["抱歉，未找到相应歌曲。"])
    			UID243F=np.array(["AnimatedSay"])
    			UID0F1D=""
    			UID243B=UID243F
    			UID2436=UID243A
    		else: 
    			UID245F=len(UID2440)
    			UID2464=UID245F>0
    			UID2473=UID2440
    			UID2478=UID2445
    			UID0ECB=UID0EFA
    			if UID2464==True:
    				UID24BF=np.array(["AnimatedSay","Music"],dtype="S")
    				results_24F0=UID2473
    				UID24F6=np.array([],dtype="S")
    				i_2504=-1
    				ForS_D1S_ADS_BBS_B7_24EA_IndexsIn=[]
    				ForS_D1S_ADS_BBS_B7_24EA_IndexsIn.append(len(results_24F0))
    				ForS_D1S_ADS_BBS_B7_24EA_Indexmin=min(ForS_D1S_ADS_BBS_B7_24EA_IndexsIn)
    				ForS_D1S_ADS_BBS_B7_24EA_count=ForS_D1S_ADS_BBS_B7_24EA_Indexmin
    				for i in range(0, ForS_D1S_ADS_BBS_B7_24EA_count):
    					i_2504=i_2504+1
    					UID24F9=results_24F0[i_2504][2]
    					UID24F6=np.concatenate((UID24F6,[UID24F9]))
    				UID0F2F=UID0ECB
    				UID246E=UID24BF
    				UID246D=np.concatenate(([UID2478],UID24F6))
    				UID2469=UID246D
    			else: 
    				UID246C=np.array(["抱歉，未找到相应歌曲。"])
    				UID2471=np.array(["AnimatedSay"])
    				UID0F2F=""
    				UID246E=UID2471
    				UID2469=UID246C
    			UID0F1D=UID0F2F
    			UID243B=UID246E
    			UID2436=UID2469
    		UID07BF=UID0F1D
    		UID1CCA=UID243B
    		UID1CB8=UID2436
    	elif UID1CA6=="Translation_Sentence" or UID1CA6=="Translation_Word":
    		UID09AA=np.array(["AnimatedSay"],dtype="S")
    		try:
    			UID084B=UID1CAF[0]
    		except:
    			UID084B=""
    		try:
    			UID0850=UID1CAF[1]
    		except:
    			UID0850=""
    		UID07BF=""
    		UID1CCA=UID09AA
    		if UID084B=="en":
    			UID0855=UID0850
    		else: 
    			UID0855="这个我不会呀，问我英语吧"
    		UID0623=np.array([UID0855])
    		UID1CB8=UID0623
    	else: 
    		UID069F=UID1CC1[-1:]
    		UID1CD2=np.delete(UID1CC1,np.s_[-1:])
    		UID07BF=""
    		UID1CB8=UID1CAF
    		UID1CCA=UID1CD2
    	UID0798=UID07BF
    	UID1BE4=UID1CCA
    	UID1BDF=UID1CB8
    else: 
    	try:
    		try:
    			UID05F6=UID1BDA.encode('utf-8')
    		except:
    			UID05F6=UID1BDA
    		UID05ED=[False,0,""]
    	except Exception, errorMsg:
    		UID05ED=[True,1,str(errorMsg)]
    		UID05F6=""
    	UID1BE7=np.array(["AnimatedSay"])
    	UID0798=""
    	UID05F0='{"city": "上海","province": "上海","street": "五角场"}'
    	UID05CA=tuling_v2.main("e0bada8cf5fb4afc81292ccc47fef250",UID05ED,UID05F0,UID073C,UID05F6)
    	UID1C68=UID05CA[0]
    	UID1C79=UID05CA[1]
    	UID05DE=UID05CA[2]
    	UID1BE4=UID1BE7
    	UID1C71=0
    	UID1C59=Clear_Errors.main(UID1C68,UID1C71)
    	UID1C5C=UID1C59[0]
    	UID1C65=UID1C59[1]
    	UID1BE2=np.array([UID1C79])
    	UID1BDF=UID1BE2
    UID1B8E=np.concatenate((UID1BE4,["Page"]))
    content=UID1BDF
    source=UID0798
    action=UID1B8E
    return action,source,content
if __name__ == "__main__":
    action,source,content=main(userid,result)
