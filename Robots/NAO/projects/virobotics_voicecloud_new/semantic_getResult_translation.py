# -*- coding: utf-8 -*-
import numpy as np
Parameter=np.array([],dtype="S")
Action=np.array([],dtype="S")
error_in__no_error_=[False,0,""]
error_out=[False,0,""]
JSON_Tree=None
import imp
import Clear_Errors
imp.reload (Clear_Errors)
def main(error_in__no_error_,JSON_Tree):
    if error_in__no_error_[0]== False:
    	try:
    		UID0107=JSON_Tree
    		try:
    			UID015C=JSON_Tree["data"]
    			UID0101=False
    		except:
    			UID015C={}
    			UID0101=True
    		UID0153=error_in__no_error_
    	except Exception, errorMsg:
    		UID0153=[True,1,str(errorMsg)]
    		UID0101=False
    		UID015C=None
    		UID0107=None
    else:
    	UID0153=error_in__no_error_
    	UID0101=False
    	UID015C=None
    	UID0107=None
    if UID0153[0]== False:
    	try:
    		UID0144=UID015C
    		try:
    			UID01DA=UID015C["result"]
    			UID013E=False
    		except:
    			UID01DA={}
    			UID013E=True
    		UID01D1=UID0153
    	except Exception, errorMsg:
    		UID01D1=[True,1,str(errorMsg)]
    		UID013E=False
    		UID01DA=None
    		UID0144=None
    else:
    	UID01D1=UID0153
    	UID013E=False
    	UID01DA=None
    	UID0144=None
    if UID01D1[0]== False:
    	try:
    		UID01C2=UID01DA
    		UID01BF=UID01DA[0]
    		UID01BC=False
    		UID0201=UID01D1
    	except Exception, errorMsg:
    		UID0201=[True,1,str(errorMsg)]
    		UID01BC=False
    		UID01BF=None
    		UID01C2=None
    else:
    	UID0201=UID01D1
    	UID01BC=False
    	UID01BF=None
    	UID01C2=None
    if UID0201[0]== False:
    	try:
    		UID01F2=UID01BF
    		try:
    			UID023A=UID01BF["translated"]
    			UID01EC=False
    		except:
    			UID023A={}
    			UID01EC=True
    		UID0231=UID0201
    	except Exception, errorMsg:
    		UID0231=[True,1,str(errorMsg)]
    		UID01EC=False
    		UID023A=None
    		UID01F2=None
    else:
    	UID0231=UID0201
    	UID01EC=False
    	UID023A=None
    	UID01F2=None
    if UID0231[0]== False:
    	try:
    		try:
    			UID0222=UID023A.encode('utf-8')
    		except:
    			UID0222=UID023A
    		UID0219=UID0231
    	except Exception, errorMsg:
    		UID0219=[True,1,str(errorMsg)]
    		UID0222=""
    else:
    	UID0219=UID0231
    	UID0222=""
    UID043D=UID0219[0]
    UID04BB=len(UID0222)
    UID0417=UID04BB<=1
    UID034C=((UID0417)|(UID043D))
    UID078C=JSON_Tree
    UID0C90=UID01BF
    UID0253=UID0219
    UID03AC=UID0222
    if UID034C==True:
    	UID0882=0
    	UID0866=Clear_Errors.main(UID0253,UID0882)
    	UID0761=UID0866[0]
    	UID0876=UID0866[1]
    	UID035C="Translation_Sentence"
    	if UID0761[0]== False:
    		try:
    			UID0752=UID078C
    			try:
    				UID090C=UID078C["semantic"]
    				UID074C=False
    			except:
    				UID090C={}
    				UID074C=True
    			UID0903=UID0761
    		except Exception, errorMsg:
    			UID0903=[True,1,str(errorMsg)]
    			UID074C=False
    			UID090C=None
    			UID0752=None
    	else:
    		UID0903=UID0761
    		UID074C=False
    		UID090C=None
    		UID0752=None
    	if UID0903[0]== False:
    		try:
    			UID08F4=UID090C
    			UID0971=UID090C[0]
    			UID08EE=False
    			UID0968=UID0903
    		except Exception, errorMsg:
    			UID0968=[True,1,str(errorMsg)]
    			UID08EE=False
    			UID0971=None
    			UID08F4=None
    	else:
    		UID0968=UID0903
    		UID08EE=False
    		UID0971=None
    		UID08F4=None
    	if UID0968[0]== False:
    		try:
    			UID0959=UID0971
    			try:
    				UID0956=UID0971["slots"]
    				UID0953=False
    			except:
    				UID0956={}
    				UID0953=True
    			UID0AC0=UID0968
    		except Exception, errorMsg:
    			UID0AC0=[True,1,str(errorMsg)]
    			UID0953=False
    			UID0956=None
    			UID0959=None
    	else:
    		UID0AC0=UID0968
    		UID0953=False
    		UID0956=None
    		UID0959=None
    	if UID0AC0[0]== False:
    		try:
    			UID0AB1=UID0956
    			ForS_D1S_ADS_BBS_B7_0A56=len(UID0956)
    			error_out_035E=UID0AC0
    		except Exception, errorMsg:
    			error_out_035E=[True,1,str(errorMsg)]
    			ForS_D1S_ADS_BBS_B7_0A56=0
    			UID0AB1=None
    	else:
    		error_out_035E=UID0AC0
    		ForS_D1S_ADS_BBS_B7_0A56=0
    		UID0AB1=None
    	JSON_Object_0A66=UID0956
    	UID0986=np.array([],dtype="S")
    	i_0A52=-1
    	ForS_D1S_ADS_BBS_B7_0A40_count=ForS_D1S_ADS_BBS_B7_0A56
    	for i in range(0, ForS_D1S_ADS_BBS_B7_0A40_count):
    		i_0A52=i_0A52+1
    		if error_out_035E[0]== False:
    			try:
    				UID09E1=JSON_Object_0A66
    				UID09DE=JSON_Object_0A66[i_0A52]
    				UID09DB=False
    				UID0B72=error_out_035E
    			except Exception, errorMsg:
    				UID0B72=[True,1,str(errorMsg)]
    				UID09DB=False
    				UID09DE=None
    				UID09E1=None
    		else:
    			UID0B72=error_out_035E
    			UID09DB=False
    			UID09DE=None
    			UID09E1=None
    		if UID0B72[0]== False:
    			try:
    				UID0B63=UID09DE
    				try:
    					UID0C52=UID09DE["name"]
    					UID0B5D=False
    				except:
    					UID0C52={}
    					UID0B5D=True
    				UID0C49=UID0B72
    			except Exception, errorMsg:
    				UID0C49=[True,1,str(errorMsg)]
    				UID0B5D=False
    				UID0C52=None
    				UID0B63=None
    		else:
    			UID0C49=UID0B72
    			UID0B5D=False
    			UID0C52=None
    			UID0B63=None
    		if UID0C49[0]== False:
    			try:
    				try:
    					UID0713=UID0C52.encode('utf-8')
    				except:
    					UID0713=UID0C52
    				UID0D6B=UID0C49
    			except Exception, errorMsg:
    				UID0D6B=[True,1,str(errorMsg)]
    				UID0713=""
    		else:
    			UID0D6B=UID0C49
    			UID0713=""
    		if UID0D6B[0]== False:
    			try:
    				UID0D5C=UID09DE
    				try:
    					UID0DF1=UID09DE["value"]
    					UID0D56=False
    				except:
    					UID0DF1={}
    					UID0D56=True
    				UID0DE8=UID0D6B
    			except Exception, errorMsg:
    				UID0DE8=[True,1,str(errorMsg)]
    				UID0D56=False
    				UID0DF1=None
    				UID0D5C=None
    		else:
    			UID0DE8=UID0D6B
    			UID0D56=False
    			UID0DF1=None
    			UID0D5C=None
    		if UID0DE8[0]== False:
    			try:
    				try:
    					UID0613=UID0DF1.encode('utf-8')
    				except:
    					UID0613=UID0DF1
    				error_out_035E=UID0DE8
    			except Exception, errorMsg:
    				error_out_035E=[True,1,str(errorMsg)]
    				UID0613=""
    		else:
    			error_out_035E=UID0DE8
    			UID0613=""
    		UID0981=UID0713+"_"+UID0613
    		
    		UID0986=np.concatenate((UID0986,[UID0981]))
    	UID07D2=UID0986
    	UID1331=error_out_035E
    else: 
    	if UID0253[0]== False:
    		try:
    			UID0C03=UID0C90
    			try:
    				UID1AC5=UID0C90["transLangCountry"]
    				UID0BE5=False
    			except:
    				UID1AC5={}
    				UID0BE5=True
    			UID1ABC=UID0253
    		except Exception, errorMsg:
    			UID1ABC=[True,1,str(errorMsg)]
    			UID0BE5=False
    			UID1AC5=None
    			UID0C03=None
    	else:
    		UID1ABC=UID0253
    		UID0BE5=False
    		UID1AC5=None
    		UID0C03=None
    	UID035C="Translation_Word"
    	if UID1ABC[0]== False:
    		try:
    			try:
    				UID0E0D=UID1AC5.encode('utf-8')
    			except:
    				UID0E0D=UID1AC5
    			UID0385=UID1ABC
    		except Exception, errorMsg:
    			UID0385=[True,1,str(errorMsg)]
    			UID0E0D=""
    	else:
    		UID0385=UID1ABC
    		UID0E0D=""
    	UID07CA=np.concatenate(([UID0E0D],[UID03AC]))
    	UID1331=UID0385
    	UID07D2=UID07CA
    error_out=UID1331
    Parameter=UID07D2
    UID00D6=np.concatenate(([UID035C],["RerunVoicecloud"]))
    Action=UID00D6
    return error_out,Parameter,Action
if __name__ == "__main__":
    error_out,Parameter,Action=main(error_in__no_error_,JSON_Tree)
