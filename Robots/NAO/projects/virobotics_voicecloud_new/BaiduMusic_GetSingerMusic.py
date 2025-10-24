# -*- coding: utf-8 -*-
tinguid="707709"
import json
import urllib2
RequestUrl=""
offset=0
error_out=[False,0,""]
songInfos=[]
limits=10
error_in__no_error_=[False,0,""]
import imp
import BaiduMusic_Head
imp.reload (BaiduMusic_Head)
import copy
def main(error_in__no_error_,offset,limits,tinguid):
    UID00A8=BaiduMusic_Head.main()
    UID00D5=UID00A8
    UID0384=" "*(0-len('%d' %limits))+'%d' %limits
    UID06FE=" "*(0-len('%d' %offset))+'%d' %offset
    UID0681=UID00D5+"baidu.ting.artist.getSongList&format=json&tinguid="+tinguid+"&limits="+UID0384+"&offset="+UID06FE
    if error_in__no_error_[0]== False:
    	try:
    		UID0672=0
    		UID0675="<Not A Path>"
    		UID0696=10000
    		UID067E=UID0672
    		if UID0672==0:
    			UID0672_ref=urllib2.urlopen(UID0681,timeout=UID0696/1000.0)
    			UID068A=UID0672_ref.read()
    			UID0684=UID0672_ref.info().dict
    		else:
    			UID0672_req=urllib2.Request(UID0681)
    			UID0672_ref=UID0672.open(UID0672_req,timeout=UID0696/1000.0)
    			UID068A=UID0672_ref.read()
    			UID0684=UID0672_ref.info().dict
    		if UID0675=="" or UID0675=="<Not A Path>":
    			pass
    		else:
    			UID0672_file=open(UID0675,"wb+")
    			UID0672_file.write(UID068A)
    			UID0672_file.close()
    		UID0715=error_in__no_error_
    	except Exception, errorMsg:
    		UID0715=[True,1,str(errorMsg)]
    		UID067E=0
    		UID0684=""
    		UID068A=""
    else:
    	UID0715=error_in__no_error_
    	UID067E=0
    	UID0684=""
    	UID068A=""
    RequestUrl=UID068A
    if UID0715[0]== False:
    	try:
    		UID0705=json.loads(UID068A)
    		UID0702=0
    		UID06FF=0
    		UID0741=UID0715
    	except Exception, errorMsg:
    		UID0741=[True,1,str(errorMsg)]
    		UID06FF=0
    		UID0702=0
    		UID0705=None
    else:
    	UID0741=UID0715
    	UID06FF=0
    	UID0702=0
    	UID0705=None
    if UID0741[0]== False:
    	try:
    		UID0731=UID0705
    		try:
    			UID072E=UID0705["songlist"]
    			UID072B=False
    		except:
    			UID072E={}
    			UID072B=True
    		UID077F=UID0741
    	except Exception, errorMsg:
    		UID077F=[True,1,str(errorMsg)]
    		UID072B=False
    		UID072E=None
    		UID0731=None
    else:
    	UID077F=UID0741
    	UID072B=False
    	UID072E=None
    	UID0731=None
    if UID077F[0]== False:
    	try:
    		UID0770=UID072E
    		ForS_D1S_ADS_BBS_B7_078D=len(UID072E)
    		error_out_07A3=UID077F
    	except Exception, errorMsg:
    		error_out_07A3=[True,1,str(errorMsg)]
    		ForS_D1S_ADS_BBS_B7_078D=0
    		UID0770=None
    else:
    	error_out_07A3=UID077F
    	ForS_D1S_ADS_BBS_B7_078D=0
    	UID0770=None
    JSON_Tree_0791=UID0705
    JSON_Object_0797=UID072E
    UID079D=[]
    i_07B4=-1
    ForS_D1S_ADS_BBS_B7_078B_count=ForS_D1S_ADS_BBS_B7_078D
    for i in range(0, ForS_D1S_ADS_BBS_B7_078B_count):
    	UID0A5B=["","",""]
    	i_07B4=i_07B4+1
    	UID0794=JSON_Tree_0791
    	UID0841=JSON_Object_0797
    	UID083E=JSON_Object_0797[i_07B4]
    	UID083B=False
    	if error_out_07A3[0]== False:
    		try:
    			UID0883=""
    			UID0871=UID083E
    			try:
    				UID08F2=UID083E["song_id"]
    				UID086B=False
    			except:
    				UID08F2=""
    				UID086B=True
    			
    			UID08B0=error_out_07A3
    		except Exception, errorMsg:
    			UID08B0=[True,1,str(errorMsg)]
    			UID086B=False
    			UID08F2=""
    			UID0871=None
    	else:
    		UID08B0=error_out_07A3
    		UID086B=False
    		UID08F2=""
    		UID0871=None
    	if UID08B0[0]== False:
    		try:
    			UID08A1=UID083E
    			try:
    				UID08E9=UID083E["title"]
    				UID089B=False
    			except:
    				UID08E9={}
    				UID089B=True
    			UID08E0=UID08B0
    		except Exception, errorMsg:
    			UID08E0=[True,1,str(errorMsg)]
    			UID089B=False
    			UID08E9=None
    			UID08A1=None
    	else:
    		UID08E0=UID08B0
    		UID089B=False
    		UID08E9=None
    		UID08A1=None
    	if UID08E0[0]== False:
    		try:
    			UID08F5=UID08E9.encode("utf-8")
    			UID09CE=UID08E0
    		except Exception, errorMsg:
    			UID09CE=[True,1,str(errorMsg)]
    			UID08F5=""
    	else:
    		UID09CE=UID08E0
    		UID08F5=""
    	if UID09CE[0]== False:
    		try:
    			UID09BF=UID083E
    			try:
    				UID09B0=UID083E["author"]
    				UID09B9=False
    			except:
    				UID09B0={}
    				UID09B9=True
    			UID09A7=UID09CE
    		except Exception, errorMsg:
    			UID09A7=[True,1,str(errorMsg)]
    			UID09B9=False
    			UID09B0=None
    			UID09BF=None
    	else:
    		UID09A7=UID09CE
    		UID09B9=False
    		UID09B0=None
    		UID09BF=None
    	if UID09A7[0]== False:
    		try:
    			UID08FE=UID09B0.encode("utf-8")
    			error_out_07A3=UID09A7
    		except Exception, errorMsg:
    			error_out_07A3=[True,1,str(errorMsg)]
    			UID08FE=""
    	else:
    		error_out_07A3=UID09A7
    		UID08FE=""
    	UID07A0=copy.copy(UID0A5B)
    	UID07A0[0]=UID08F2
    	UID07A0[1]=UID08F5
    	UID07A0[2]=UID08FE
    	
    	UID079D.append(UID07A0)
    songInfos=UID079D
    error_out=error_out_07A3
    return error_out,songInfos
if __name__ == "__main__":
    error_out,songInfos=main(error_in__no_error_,offset,limits,tinguid)
