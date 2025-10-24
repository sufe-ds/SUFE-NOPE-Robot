# -*- coding: utf-8 -*-
body=""
error_out=[False,0,""]
artistName=""
songs=0
import json
import urllib2
error_in__no_error_=[False,0,""]
ting_uid=""
import imp
import BaiduMusic_Head
imp.reload (BaiduMusic_Head)
def main(error_in__no_error_,ting_uid):
    UID00A8=BaiduMusic_Head.main()
    UID00D5=UID00A8
    UID013F=UID00D5+"baidu.ting.artist.getInfo&format=json&tinguid="+ting_uid
    if error_in__no_error_[0]== False:
    	try:
    		UID0128=0
    		UID012D="<Not A Path>"
    		UID0154=10000
    		UID013C=UID0128
    		if UID0128==0:
    			UID0128_ref=urllib2.urlopen(UID013F,timeout=UID0154/1000.0)
    			UID0148=UID0128_ref.read()
    			UID0142=UID0128_ref.info().dict
    		else:
    			UID0128_req=urllib2.Request(UID013F)
    			UID0128_ref=UID0128.open(UID0128_req,timeout=UID0154/1000.0)
    			UID0148=UID0128_ref.read()
    			UID0142=UID0128_ref.info().dict
    		if UID012D=="" or UID012D=="<Not A Path>":
    			pass
    		else:
    			UID0128_file=open(UID012D,"wb+")
    			UID0128_file.write(UID0148)
    			UID0128_file.close()
    		UID0220=error_in__no_error_
    	except Exception, errorMsg:
    		UID0220=[True,1,str(errorMsg)]
    		UID013C=0
    		UID0142=""
    		UID0148=""
    else:
    	UID0220=error_in__no_error_
    	UID013C=0
    	UID0142=""
    	UID0148=""
    if UID0220[0]== False:
    	try:
    		UID0211=json.loads(UID0148)
    		UID020E=0
    		UID020B=0
    		UID0262=UID0220
    	except Exception, errorMsg:
    		UID0262=[True,1,str(errorMsg)]
    		UID020B=0
    		UID020E=0
    		UID0211=None
    else:
    	UID0262=UID0220
    	UID020B=0
    	UID020E=0
    	UID0211=None
    body=UID0148
    if UID0262[0]== False:
    	try:
    		UID0265=""
    		UID0253=UID0211
    		try:
    			UID01B3=UID0211["name"]
    			UID024D=False
    		except:
    			UID01B3=""
    			UID024D=True
    		
    		UID01AA=UID0262
    	except Exception, errorMsg:
    		UID01AA=[True,1,str(errorMsg)]
    		UID024D=False
    		UID01B3=""
    		UID0253=None
    else:
    	UID01AA=UID0262
    	UID024D=False
    	UID01B3=""
    	UID0253=None
    if UID01AA[0]== False:
    	try:
    		try:
    			UID05B0=UID01B3.encode('utf-8')
    		except:
    			UID05B0=UID01B3
    		UID02DA=UID01AA
    	except Exception, errorMsg:
    		UID02DA=[True,1,str(errorMsg)]
    		UID05B0=""
    else:
    	UID02DA=UID01AA
    	UID05B0=""
    if UID02DA[0]== False:
    	try:
    		UID02CB=UID0211
    		try:
    			UID03F4=UID0211["songs_total"]
    			UID02C5=False
    		except:
    			UID03F4={}
    			UID02C5=True
    		UID03EB=UID02DA
    	except Exception, errorMsg:
    		UID03EB=[True,1,str(errorMsg)]
    		UID02C5=False
    		UID03F4=None
    		UID02CB=None
    else:
    	UID03EB=UID02DA
    	UID02C5=False
    	UID03F4=None
    	UID02CB=None
    artistName=UID05B0
    if UID03EB[0]== False:
    	try:
    		try:
    			UID0894=UID03F4.encode('utf-8')
    		except:
    			UID0894=UID03F4
    		UID03D2=UID03EB
    	except Exception, errorMsg:
    		UID03D2=[True,1,str(errorMsg)]
    		UID0894=""
    else:
    	UID03D2=UID03EB
    	UID0894=""
    error_out=UID03D2
    UID0889=UID03D2
    if UID0889[0]==True:
    	UID08A0=0
    else: 
    	UID089F=int(str(UID0894)[0:])
    	UID08A0=UID089F
    songs=UID08A0
    return error_out,songs,artistName
if __name__ == "__main__":
    error_out,songs,artistName=main(error_in__no_error_,ting_uid)
