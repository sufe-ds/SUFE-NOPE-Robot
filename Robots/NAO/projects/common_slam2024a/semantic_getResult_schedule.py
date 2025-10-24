# -*- coding: utf-8 -*-
content=""
name=""
error_out=[False,0,""]
date=""
time=""
error_in__no_error_=[False,0,""]
JSON_Tree=None
def main(error_in__no_error_,JSON_Tree):
    if error_in__no_error_[0]== False:
    	try:
    		UID03C1=JSON_Tree
    		try:
    			UID0468=JSON_Tree["semantic"]
    			UID03BB=False
    		except:
    			UID0468={}
    			UID03BB=True
    		UID045F=error_in__no_error_
    	except Exception, errorMsg:
    		UID045F=[True,1,str(errorMsg)]
    		UID03BB=False
    		UID0468=None
    		UID03C1=None
    else:
    	UID045F=error_in__no_error_
    	UID03BB=False
    	UID0468=None
    	UID03C1=None
    if UID045F[0]== False:
    	try:
    		UID0450=UID0468
    		try:
    			UID044D=UID0468["slots"]
    			UID044A=False
    		except:
    			UID044D={}
    			UID044A=True
    		UID088C=UID045F
    	except Exception, errorMsg:
    		UID088C=[True,1,str(errorMsg)]
    		UID044A=False
    		UID044D=None
    		UID0450=None
    else:
    	UID088C=UID045F
    	UID044A=False
    	UID044D=None
    	UID0450=None
    if UID088C[0]== False:
    	try:
    		UID087D=UID044D
    		try:
    			UID087A=UID044D["datetime"]
    			UID0877=False
    		except:
    			UID087A={}
    			UID0877=True
    		UID0AE3=UID088C
    	except Exception, errorMsg:
    		UID0AE3=[True,1,str(errorMsg)]
    		UID0877=False
    		UID087A=None
    		UID087D=None
    else:
    	UID0AE3=UID088C
    	UID0877=False
    	UID087A=None
    	UID087D=None
    if UID0AE3[0]== False:
    	try:
    		UID0AE8=""
    		UID0ACC=UID087A
    		try:
    			UID0C0F=UID087A["date"]
    			UID0AC6=False
    		except:
    			UID0C0F=""
    			UID0AC6=True
    		
    		UID0C06=UID0AE3
    	except Exception, errorMsg:
    		UID0C06=[True,1,str(errorMsg)]
    		UID0AC6=False
    		UID0C0F=""
    		UID0ACC=None
    else:
    	UID0C06=UID0AE3
    	UID0AC6=False
    	UID0C0F=""
    	UID0ACC=None
    if UID0C06[0]== False:
    	try:
    		try:
    			UID0B9C=UID0C0F.encode('utf-8')
    		except:
    			UID0B9C=UID0C0F
    		UID0506=UID0C06
    	except Exception, errorMsg:
    		UID0506=[True,1,str(errorMsg)]
    		UID0B9C=""
    else:
    	UID0506=UID0C06
    	UID0B9C=""
    if UID0506[0]== False:
    	try:
    		UID0509=""
    		UID04F7=UID087A
    		try:
    			UID090F=UID087A["time"]
    			UID04F1=False
    		except:
    			UID090F=""
    			UID04F1=True
    		
    		UID06E1=UID0506
    	except Exception, errorMsg:
    		UID06E1=[True,1,str(errorMsg)]
    		UID04F1=False
    		UID090F=""
    		UID04F7=None
    else:
    	UID06E1=UID0506
    	UID04F1=False
    	UID090F=""
    	UID04F7=None
    date=UID0B9C
    if UID06E1[0]== False:
    	try:
    		try:
    			UID0A6B=UID090F.encode('utf-8')
    		except:
    			UID0A6B=UID090F
    		UID012E=UID06E1
    	except Exception, errorMsg:
    		UID012E=[True,1,str(errorMsg)]
    		UID0A6B=""
    else:
    	UID012E=UID06E1
    	UID0A6B=""
    time=UID0A6B
    if UID012E[0]== False:
    	try:
    		UID0131=""
    		UID011F=UID044D
    		try:
    			UID016A=UID044D["name"]
    			UID0119=False
    		except:
    			UID016A=""
    			UID0119=True
    		
    		UID0161=UID012E
    	except Exception, errorMsg:
    		UID0161=[True,1,str(errorMsg)]
    		UID0119=False
    		UID016A=""
    		UID011F=None
    else:
    	UID0161=UID012E
    	UID0119=False
    	UID016A=""
    	UID011F=None
    if UID0161[0]== False:
    	try:
    		try:
    			UID05FD=UID016A.encode('utf-8')
    		except:
    			UID05FD=UID016A
    		UID0241=UID0161
    	except Exception, errorMsg:
    		UID0241=[True,1,str(errorMsg)]
    		UID05FD=""
    else:
    	UID0241=UID0161
    	UID05FD=""
    if UID0241[0]== False:
    	try:
    		UID0244=""
    		UID0232=UID044D
    		try:
    			UID027D=UID044D["content"]
    			UID022C=False
    		except:
    			UID027D=""
    			UID022C=True
    		
    		UID0274=UID0241
    	except Exception, errorMsg:
    		UID0274=[True,1,str(errorMsg)]
    		UID022C=False
    		UID027D=""
    		UID0232=None
    else:
    	UID0274=UID0241
    	UID022C=False
    	UID027D=""
    	UID0232=None
    name=UID05FD
    if UID0274[0]== False:
    	try:
    		try:
    			UID064A=UID027D.encode('utf-8')
    		except:
    			UID064A=UID027D
    		UID0F99=UID0274
    	except Exception, errorMsg:
    		UID0F99=[True,1,str(errorMsg)]
    		UID064A=""
    else:
    	UID0F99=UID0274
    	UID064A=""
    error_out=UID0F99
    content=UID064A
    return error_out,name,time,date,content
if __name__ == "__main__":
    error_out,name,time,date,content=main(error_in__no_error_,JSON_Tree)
