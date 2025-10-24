#!/usr/bin/python
#-*- coding:utf-8 -*-

import time
import cv2
import numpy as np
from naoqi import ALProxy
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn

class NaoCamera:
    def __init__(self,ip="127.0.0.1",index=0,resolution=1,fps=30):
        self.__vid = ALProxy("ALVideoDevice",ip,9559)
        self.__name = "virobotics"+str(time.time())
        self.__handle = self.__vid.subscribeCamera(self.__name,index,resolution,13,fps)

    def read(self):
        data = self.__vid.getImageRemote(self.__handle)
        width = data[0]
        height = data[1]
        img_str = data[6]       
        img = np.fromstring(img_str,dtype=np.uint8).reshape((height,width,3))
        return img

    def read_jpg(self):      
        img = self.read()
        jpg = cv2.imencode(".jpg",img)[1].tostring()
        return jpg

    def release(self):
        self.__vid.unsubscribe(self.__handle)

    def __del__(self):
        self.release()

def decodeUrl(path):
    loc_and_reqs = path.split('?')   
    loc = loc_and_reqs[0]
    reqs = {}  
    if len(loc_and_reqs) > 1:
        params = loc_and_reqs[1].split('&')
        for p in params:
            kv = p.split('=')
            if len(kv) > 1:
                reqs[kv[0]] = kv[1]
    return loc,reqs

class HTTPHandle(BaseHTTPRequestHandler):

    # empty this func in order to prompt send_response(200)
    def log_request(self, code='-', size='-'):
        pass
    
    def do_GET(self):
        if self.path != "/favicon.ico":
            loc,reqs = decodeUrl(self.path)
            if loc == "/video":
                try:
                    index = reqs.get("index") if reqs.get("index") else 0
                    resolution = reqs.get("resolution") if reqs.get("resolution") else 1
                    
                    cap = NaoCamera(index=int(index),resolution=int(resolution))
                    self.protocol_version = "HTTP/1.1"
                    self.send_response(200)
                   
                    self.wfile.write("Content-type: multipart/x-mixed-replace; boundary=--videoboundary") 
                    self.wfile.write("\r\n\r\n")

                    while 1:
                        jpg = cap.read_jpg()
                        self.wfile.write("--videoboundary\r\n")
                        self.wfile.write("Content-Type: image/jpeg\r\n")
                        self.wfile.write("Content-length: "+str(len(jpg))+"\r\n\r\n" )
                        self.wfile.write(jpg)
                        self.wfile.write("\r\n\r\n\r\n")

                except:
                    pass

            else:
                self.send_error(404, "Not Found")
                        
    def do_POST(self):
        loc,reqs = decodeUrl(self.path)
        postDatas = self.rfile.read(int(self.headers['content-length']))
        
        self.protocol_version = "HTTP/1.1"      
        self.send_response(200)       
        self.send_header("Content-type", "application/json") 
        self.end_headers()    
        self.wfile.write(postDatas)


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass


def main():
    server = ThreadingHTTPServer(("", 8000), HTTPHandle)
    print("start http server")
    server.serve_forever()
    
if __name__ == '__main__':
    main()
    

    
