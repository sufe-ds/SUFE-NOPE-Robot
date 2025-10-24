# -*- coding: utf-8 -*-
code=1097
error_out=[False,0,""]
error_in__no_error_=[False,0,""]
import copy
def main(code,error_in__no_error_):
    UID00A4=error_in__no_error_[1]
    UID00FC=UID00A4==code
    UID013D=error_in__no_error_
    if UID00FC==True:
    	UID0151=copy.copy(UID013D)
    	UID0151[0]=False
    	UID0155=UID0151
    else: 
    	UID0155=UID013D
    error_out=UID0155
    return error_out
if __name__ == "__main__":
    error_out=main(code,error_in__no_error_)
