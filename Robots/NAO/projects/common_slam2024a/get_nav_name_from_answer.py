# -*- coding: utf-8 -*-
ErrorIn=[False,0,""]
ErrorOut=[False,0,""]
nav_name=""
success=False
input_string=""
import re
def main(ErrorIn,input_string):
    Constant_UID00E4="nav="
    UID002B_result=re.split(Constant_UID00E4,input_string[0:],1)
    UID003C=input_string[:0]+UID002B_result[0]
    if len(UID002B_result)==2:
    	UID016A=Constant_UID00E4
    	UID024A=UID002B_result[1]
    	UID0045=len(UID003C)+len(Constant_UID00E4)
    else:
    	UID016A=""
    	UID024A=""
    	UID0045=-1
    ErrorOut=ErrorIn
    UID01E9=UID016A==Constant_UID00E4
    nav_name=UID024A
    success=UID01E9
    return ErrorOut,success,nav_name
if __name__ == "__main__":
    ErrorOut,success,nav_name=main(ErrorIn,input_string)
