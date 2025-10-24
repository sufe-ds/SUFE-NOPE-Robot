# -*- coding: utf-8 -*-
concatenated_string=""
body=""
error_out=[False,0,""]
error_in__no_error_=[False,0,""]
songInfo=["","","","","","",0,""]
import numpy as np
import copy
songID="564102115"
import json
import urllib2
import imp
import Clear_Errors
imp.reload (Clear_Errors)
def main(error_in__no_error_,songID):
    UID01D9=np.array(["data","songList","0"],dtype="S")
    UID01FA=np.array([0,0,1],dtype="uint16")
    UID03C4=np.array(["songPicBig","songPicRadio","lrcLink","songLink","artistId"],dtype="S")
    UID09BA=["","","","","","",0,""]
    UID030F="http://music.qianqian.com/data/music/fmlink?songIds="+songID
    if error_in__no_error_[0]== False:
        try:
            UID0034=0
            UID0037="<Not A Path>"
            UID0058=10000
            UID0040=UID0034
            if UID0034==0:
                UID0034_ref=urllib2.urlopen(UID030F,timeout=UID0058/1000.0)
                UID004C=UID0034_ref.read()
                UID0046=UID0034_ref.info().dict
            else:
                UID0034_req=urllib2.Request(UID030F)
                UID0034_ref=UID0034.open(UID0034_req,timeout=UID0058/1000.0)
                UID004C=UID0034_ref.read()
                UID0046=UID0034_ref.info().dict
            if UID0037=="" or UID0037=="<Not A Path>":
                pass
            else:
                UID0034_file=open(UID0037,"wb+")
                UID0034_file.write(UID004C)
                UID0034_file.close()
            UID00E0=error_in__no_error_
        except Exception, errorMsg:
            UID00E0=[True,1,str(errorMsg)]
            UID0040=0
            UID0046=""
            UID004C=""
    else:
        UID00E0=error_in__no_error_
        UID0040=0
        UID0046=""
        UID004C=""
    concatenated_string=UID030F
    if UID00E0[0]== False:
        try:
            UID01D4=json.loads(UID004C)
            UID00CE=0
            UID00CB=0
            UID01CB=UID00E0
        except Exception, errorMsg:
            UID01CB=[True,1,str(errorMsg)]
            UID00CB=0
            UID00CE=0
            UID01D4=None
    else:
        UID01CB=UID00E0
        UID00CB=0
        UID00CE=0
        UID01D4=None
    body=UID004C
    if UID01CB[0]== False:
        try:
            UID01BC=UID01D4
            UID01FA_number=0
            for i in UID01D9:
                if UID01FA[UID01FA_number]==0:
                    UID01BC=UID01BC[i]
                else:
                    UID01BC=UID01BC[int(i)]
                UID01FA_number=UID01FA_number+1
            UID048B=UID01CB
        except Exception, errorMsg:
            UID048B=[True,1,str(errorMsg)]
            UID01BC=None
    else:
        UID048B=UID01CB
        UID01BC=None
    if UID048B[0]== False:
        try:
            UID047B=UID01BC
            try:
                UID0501=UID01BC["songName"]
                UID0470=False
            except:
                UID0501={}
                UID0470=True
            UID04F8=UID048B
        except Exception, errorMsg:
            UID04F8=[True,1,str(errorMsg)]
            UID0470=False
            UID0501=None
            UID047B=None
    else:
        UID04F8=UID048B
        UID0470=False
        UID0501=None
        UID047B=None
    if UID04F8[0]== False:
        try:
            UID063B=UID0501.encode("utf-8")
            UID05CC=UID04F8
        except Exception, errorMsg:
            UID05CC=[True,1,str(errorMsg)]
            UID063B=""
    else:
        UID05CC=UID04F8
        UID063B=""
    if UID05CC[0]== False:
        try:
            UID05BD=UID01BC
            try:
                UID06B7=UID01BC["artistName"]
                UID05B7=False
            except:
                UID06B7={}
                UID05B7=True
            UID06AE=UID05CC
        except Exception, errorMsg:
            UID06AE=[True,1,str(errorMsg)]
            UID05B7=False
            UID06B7=None
            UID05BD=None
    else:
        UID06AE=UID05CC
        UID05B7=False
        UID06B7=None
        UID05BD=None
    if UID06AE[0]== False:
        try:
            UID0687=UID06B7.encode("utf-8")
            error_out_0B9D=UID06AE
        except Exception, errorMsg:
            error_out_0B9D=[True,1,str(errorMsg)]
            UID0687=""
    else:
        error_out_0B9D=UID06AE
        UID0687=""
    UID0517=UID03C4
    JsonOut_045A=UID01BC
    UID0B91=np.array([],dtype="S")
    i_03B5=-1
    ForS_D1S_ADS_BBS_B7_00B8_IndexsIn=[]
    ForS_D1S_ADS_BBS_B7_00B8_IndexsIn.append(len(UID0517))
    ForS_D1S_ADS_BBS_B7_00B8_Indexmin=min(ForS_D1S_ADS_BBS_B7_00B8_IndexsIn)
    ForS_D1S_ADS_BBS_B7_00B8_count=ForS_D1S_ADS_BBS_B7_00B8_Indexmin
    for i in range(0, ForS_D1S_ADS_BBS_B7_00B8_count):
        i_03B5=i_03B5+1
        if error_out_0B9D[0]== False:
            try:
                UID0762=JsonOut_045A
                try:
                    UID0803=JsonOut_045A[UID0517[i_03B5]]
                    UID075C=False
                except:
                    UID0803={}
                    UID075C=True
                UID07FD=error_out_0B9D
            except Exception, errorMsg:
                UID07FD=[True,1,str(errorMsg)]
                UID075C=False
                UID0803=None
                UID0762=None
        else:
            UID07FD=error_out_0B9D
            UID075C=False
            UID0803=None
            UID0762=None
        if UID07FD[0]== False:
            try:
                UID058E=str(UID0803)
                UID02E4=UID07FD
            except Exception, errorMsg:
                UID02E4=[True,1,str(errorMsg)]
                UID058E=""
        else:
            UID02E4=UID07FD
            UID058E=""
        UID02ED=0
        UID00B9=Clear_Errors.main(UID02E4,UID02ED)
        error_out_0B9D=UID00B9[0]
        UID02E1=UID00B9[1]
        UID0B91=np.concatenate((UID0B91,[UID058E]))
        
    try:
        UID0C39=UID0B91[0]
    except:
        UID0C39=""
    try:
        UID0C3C=UID0B91[1]
    except:
        UID0C3C=""
    try:
        UID0C3F=UID0B91[2]
    except:
        UID0C3F=""
    try:
        UID0286=UID0B91[3]
    except:
        UID0286=""
    try:
        UID0585=UID0B91[4]
    except:
        UID0585=""
    if error_out_0B9D[0]== False:
        try:
            UID08BA=0.000000
            UID08A8=UID01BC
            try:
                UID02AF=UID01BC["time"]
                UID08A2=False
            except:
                UID02AF=0
                UID08A2=True
            
            UID0B1C=error_out_0B9D
        except Exception, errorMsg:
            UID0B1C=[True,1,str(errorMsg)]
            UID08A2=False
            UID02AF=0.000000
            UID08A8=None
    else:
        UID0B1C=error_out_0B9D
        UID08A2=False
        UID02AF=0.000000
        UID08A8=None
    error_out=UID0B1C
    UID0113=int(UID02AF)
    UID0D5E=copy.copy(UID09BA)
    UID0D5E[0]=UID063B
    UID0D5E[1]=UID0687
    UID0D5E[2]=UID0C39
    UID0D5E[3]=UID0C3C
    UID0D5E[4]=UID0C3F
    UID0D5E[5]=UID0286
    UID0D5E[6]=UID0113
    UID0D5E[7]=UID0585
    songInfo=UID0D5E
    return error_out,songInfo
if __name__ == "__main__":
    error_out,songInfo=main(error_in__no_error_,songID)
