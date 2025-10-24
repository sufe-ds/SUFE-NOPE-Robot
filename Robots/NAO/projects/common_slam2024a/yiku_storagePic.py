# -*- coding: utf-8 -*-
userId="common"
url=""
error_out=[False,0,""]
error_in=[False,0,""]
import json
FilePath="/home/nao/abc.jpg"
import imp
import file_to_base64
imp.reload (file_to_base64)
import urllib
import urllib2
def main(error_in,userId,FilePath):
    UID012B=file_to_base64.main(error_in,FilePath)
    UID05E0=UID012B[0]
    UID05EA=UID012B[1]
    if UID05E0[0]== False:
    	try:
    		UID031C=urllib.quote(UID05EA)
    		UID00A1=UID05E0
    	except Exception, errorMsg:
    		UID00A1=[True,1,str(errorMsg)]
    		UID031C=""
    else:
    	UID00A1=UID05E0
    	UID031C=""
    UID0095='{"userId":"'+userId+'","image":"'+UID031C+'"}'
    if UID00A1[0]== False:
    	try:
    		UID0080=0
    		UID0083="<Not A Path>"
    		UID00A4=10000
    		UID008C=UID0080
    		if UID0080==0:
    			UID0080_ref=urllib2.urlopen("http://116.198.207.45:8080/services/storage/upload_picture",UID0095,timeout=UID00A4/1000.0)
    			UID0531=UID0080_ref.read()
    			UID0092=UID0080_ref.info().dict
    		else:
    			UID0080_req=urllib2.Request("http://116.198.207.45:8080/services/storage/upload_picture")
    			UID0080_ref=UID0080.open(UID0080_req,UID0095,timeout=UID00A4/1000.0)
    			UID0531=UID0080_ref.read()
    			UID0092=UID0080_ref.info().dict
    		if UID0083=="" or UID0083=="<Not A Path>":
    			pass
    		else:
    			UID0080_file=open(UID0083,"wb+")
    			UID0080_file.write(UID0531)
    			UID0080_file.close()
    		UID052B=UID00A1
    	except Exception, errorMsg:
    		UID052B=[True,1,str(errorMsg)]
    		UID008C=0
    		UID0092=""
    		UID0531=""
    else:
    	UID052B=UID00A1
    	UID008C=0
    	UID0092=""
    	UID0531=""
    if UID052B[0]== False:
    	try:
    		UID05FA=json.loads(UID0531)
    		UID0519=0
    		UID0516=0
    		UID05F1=UID052B
    	except Exception, errorMsg:
    		UID05F1=[True,1,str(errorMsg)]
    		UID0516=0
    		UID0519=0
    		UID05FA=None
    else:
    	UID05F1=UID052B
    	UID0516=0
    	UID0519=0
    	UID05FA=None
    if UID05F1[0]== False:
    	try:
    		UID05F4=""
    		UID05D0=UID05FA
    		try:
    			UID0132=UID05FA["url"]
    			UID05C3=False
    		except:
    			UID0132=""
    			UID05C3=True
    		
    		UID08C6=UID05F1
    	except Exception, errorMsg:
    		UID08C6=[True,1,str(errorMsg)]
    		UID05C3=False
    		UID0132=""
    		UID05D0=None
    else:
    	UID08C6=UID05F1
    	UID05C3=False
    	UID0132=""
    	UID05D0=None
    error_out=UID08C6
    try:
    	UID01EB=UID0132.encode('utf-8')
    except:
    	UID01EB=UID0132
    url=UID01EB
    return error_out,url
if __name__ == "__main__":
    error_out,url=main(error_in,userId,FilePath)
