# -*- coding: utf-8 -*-
enable=False
error_out=[False,0,""]
error_in=[False,0,""]
IP="127.0.0.1"
from naoqi import ALProxy
def main(error_in,enable,IP):
    if error_in[0]== False:
    	try:
    		
    		ba = ALProxy("ALBasicAwareness",IP,9559)
    		if enable:
    						    ba.setParameter("LookStimulusSpeed",0.22)
    						    ba.setParameter("LookBackSpeed",0.17)
    						    ba.setTrackingMode("Head")
    						    ba.setStimulusDetectionEnabled("TabletTouch",False)
    						    ba.setStimulusDetectionEnabled("Sound",False)
    						    ba.setStimulusDetectionEnabled("Movement",False)
    						    ba.setStimulusDetectionEnabled("NavigationMotion",False)
    		ba.setEnabled(enable)
    		
    		UID02E1=error_in
    	except Exception, errorMsg:
    		UID02E1=[True,1,str(errorMsg)]
    else:
    	UID02E1=error_in
    error_out=UID02E1
    return error_out
if __name__ == "__main__":
    error_out=main(error_in,enable,IP)
