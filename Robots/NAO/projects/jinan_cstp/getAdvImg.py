# -*- coding: utf-8 -*-
index=""
url=""
RobotID=""
error_out=[False,0,""]
ErrorIn=[False,0,""]
def main(ErrorIn,index,RobotID):
    UID0180="http://116.198.207.45:8080/naoservice/advertisement/getadvimg?robotid="+RobotID+"&advindex="+index
    error_out=ErrorIn
    url=UID0180
    return error_out,url
if __name__ == "__main__":
    error_out,url=main(ErrorIn,index,RobotID)
