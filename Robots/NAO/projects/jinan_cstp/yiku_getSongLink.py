# -*- coding: utf-8 -*-
import numpy as np
songInfo=["","","","","",0,0]
import copy
source="qianqian"
error_in=[False,0,""]
error_out=[False,0,""]
import json
songID=""
import urllib2
def main(error_in,source,songID):
    UID0BAC=["","","","","",0,0]
    UID0252=np.array(["title","artist","pic","lyric","songLink"],dtype="S")
    UID0043="http://116.198.207.45:8080/services/song/getSongLink?"+"songID="+songID+"&source="+source
    if error_in[0]== False:
    	try:
    		UID0034=0
    		UID0037="<Not A Path>"
    		UID0058=10000
    		UID0040=UID0034
    		if UID0034==0:
    			UID0034_ref=urllib2.urlopen(UID0043,timeout=UID0058/1000.0)
    			UID0107=UID0034_ref.read()
    			UID0046=UID0034_ref.info().dict
    		else:
    			UID0034_req=urllib2.Request(UID0043)
    			UID0034_ref=UID0034.open(UID0034_req,timeout=UID0058/1000.0)
    			UID0107=UID0034_ref.read()
    			UID0046=UID0034_ref.info().dict
    		if UID0037=="" or UID0037=="<Not A Path>":
    			pass
    		else:
    			UID0034_file=open(UID0037,"wb+")
    			UID0034_file.write(UID0107)
    			UID0034_file.close()
    		UID0101=error_in
    	except Exception, errorMsg:
    		UID0101=[True,1,str(errorMsg)]
    		UID0040=0
    		UID0046=""
    		UID0107=""
    else:
    	UID0101=error_in
    	UID0040=0
    	UID0046=""
    	UID0107=""
    if UID0101[0]== False:
    	try:
    		UID0189=json.loads(UID0107)
    		UID00EF=0
    		UID00E6=0
    		UID0180=UID0101
    	except Exception, errorMsg:
    		UID0180=[True,1,str(errorMsg)]
    		UID00E6=0
    		UID00EF=0
    		UID0189=None
    else:
    	UID0180=UID0101
    	UID00E6=0
    	UID00EF=0
    	UID0189=None
    if UID0180[0]== False:
    	try:
    		UID016F=UID0189
    		try:
    			UID016C=UID0189["songInfo"]
    			UID0169=False
    		except:
    			UID016C={}
    			UID0169=True
    		error_out_0234=UID0180
    	except Exception, errorMsg:
    		error_out_0234=[True,1,str(errorMsg)]
    		UID0169=False
    		UID016C=None
    		UID016F=None
    else:
    	error_out_0234=UID0180
    	UID0169=False
    	UID016C=None
    	UID016F=None
    UID04DE=UID0252
    JSON_Object_03F9=UID016C
    UID0602=np.array([],dtype="S")
    i_03D2=-1
    ForS_D1S_ADS_BBS_B7_03B5_IndexsIn=[]
    ForS_D1S_ADS_BBS_B7_03B5_IndexsIn.append(len(UID04DE))
    ForS_D1S_ADS_BBS_B7_03B5_Indexmin=min(ForS_D1S_ADS_BBS_B7_03B5_IndexsIn)
    ForS_D1S_ADS_BBS_B7_03B5_count=ForS_D1S_ADS_BBS_B7_03B5_Indexmin
    for i in range(0, ForS_D1S_ADS_BBS_B7_03B5_count):
    	i_03D2=i_03D2+1
    	if error_out_0234[0]== False:
    		try:
    			UID04C8=""
    			UID04A9=JSON_Object_03F9
    			try:
    				UID0544=JSON_Object_03F9[UID04DE[i_03D2]]
    				UID0497=False
    			except:
    				UID0544=""
    				UID0497=True
    			
    			UID053B=error_out_0234
    		except Exception, errorMsg:
    			UID053B=[True,1,str(errorMsg)]
    			UID0497=False
    			UID0544=""
    			UID04A9=None
    	else:
    		UID053B=error_out_0234
    		UID0497=False
    		UID0544=""
    		UID04A9=None
    	if UID053B[0]== False:
    		try:
    			UID05FE=UID0544.encode("utf-8")
    			error_out_0234=UID053B
    		except Exception, errorMsg:
    			error_out_0234=[True,1,str(errorMsg)]
    			UID05FE=""
    	else:
    		error_out_0234=UID053B
    		UID05FE=""
    	
    	UID0602=np.concatenate((UID0602,[UID05FE]))
    if error_out_0234[0]== False:
    	try:
    		UID0841=0.000000
    		UID0A42=UID016C
    		try:
    			UID038F=UID016C["isVip"]
    			UID0822=False
    		except:
    			UID038F=0
    			UID0822=True
    		
    		UID0A39=error_out_0234
    	except Exception, errorMsg:
    		UID0A39=[True,1,str(errorMsg)]
    		UID0822=False
    		UID038F=0.000000
    		UID0A42=None
    else:
    	UID0A39=error_out_0234
    	UID0822=False
    	UID038F=0.000000
    	UID0A42=None
    try:
    	UID02A2=UID0602[0]
    except:
    	UID02A2=""
    try:
    	UID02DC=UID0602[1]
    except:
    	UID02DC=""
    try:
    	UID02E1=UID0602[2]
    except:
    	UID02E1=""
    try:
    	UID03DE=UID0602[3]
    except:
    	UID03DE=""
    try:
    	UID03E2=UID0602[4]
    except:
    	UID03E2=""
    if UID0A39[0]== False:
    	try:
    		UID0A3C=0.000000
    		UID0A2A=UID0A42
    		try:
    			UID034A=UID0A42["duration"]
    			UID0A24=False
    		except:
    			UID034A=0
    			UID0A24=True
    		
    		UID0AAB=UID0A39
    	except Exception, errorMsg:
    		UID0AAB=[True,1,str(errorMsg)]
    		UID0A24=False
    		UID034A=0.000000
    		UID0A2A=None
    else:
    	UID0AAB=UID0A39
    	UID0A24=False
    	UID034A=0.000000
    	UID0A2A=None
    UID03E7=int(UID038F)
    error_out=UID0AAB
    UID0314=int(UID034A)
    UID0620=copy.copy(UID0BAC)
    UID0620[0]=UID02A2
    UID0620[1]=UID02DC
    UID0620[2]=UID02E1
    UID0620[3]=UID03DE
    UID0620[4]=UID03E2
    UID0620[5]=UID03E7
    UID0620[6]=UID0314
    songInfo=UID0620
    return error_out,songInfo
if __name__ == "__main__":
    error_out,songInfo=main(error_in,source,songID)
