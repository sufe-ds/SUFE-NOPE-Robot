# -*- coding: utf-8 -*-
specific_error_cleared_=False
specific_error_code_to_clear__0__all_=0
error_out=[False,0,""]
error_in__no_error_=[False,0,""]
def main(error_in__no_error_,specific_error_code_to_clear__0__all_):
    UID0223=specific_error_code_to_clear__0__all_
    UID022B=error_in__no_error_
    if UID0223==0:
    	UID023F=[False,0,""]
    	UID047F=False
    	UID0285=UID023F
    else: 
    	UID031F=[False,0,""]
    	UID02BE=UID022B[1]
    	UID02BB=UID0223==UID02BE
    	if UID02BB:
    		UID0281=UID031F
    	else:
    		UID0281=UID022B
    	UID047F=UID02BB
    	UID0285=UID0281
    error_out=UID0285
    specific_error_cleared_=UID047F
    return error_out,specific_error_cleared_
if __name__ == "__main__":
    error_out,specific_error_cleared_=main(error_in__no_error_,specific_error_code_to_clear__0__all_)
