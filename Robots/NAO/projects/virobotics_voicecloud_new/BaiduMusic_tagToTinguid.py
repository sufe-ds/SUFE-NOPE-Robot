# -*- coding: utf-8 -*-
exist=False
import numpy as np
type=""
tinguid=""
tag=""
def main(tag):
    UID00BC=np.array([["儿童歌曲","707709","singer"],["少儿歌曲","553065","singer"],["儿歌","139588613","singer"],["摇篮曲","","song"],["钢琴曲","90656493","singer"],["新歌","1","type"],["经典老歌","22","type"],["热歌","2","type"],["林志炫","83561","singer"],["陈奕迅","1077","singer"],["凤凰传奇","1490","singer"],["周杰伦","7994","singer"],["张学友","2507","singer"],["王菲","45561","singer"],["那英","1076","singer"],["张惠妹","1071","singer"],["黄绮珊","10687666","singer"],["梁静茹","1095","singer"],["羽泉","1389","singer"],["薛之谦","2517","singer"],["杨宗纬","8477","singer"],["林俊杰","1052","singer"],["汪峰","1157","singer"],["曲婉婷","687850","singer"],["刘德华","1224","singer"],["沙宝亮","1114","singer"],["彭佳慧","1425","singer"],["邓丽君","1091","singer"],["辛晓琪","1233","singer"],["王力宏","1107","singer"],["小蓓蕾组合","707709","singer"],["张信哲","1118","singer"],["王麟","1842","singer"],["五月天","1098","singer"],["刘若英","1067","singer"],["周晓鸥","7639","singer"],["齐秦","1117","singer"],["Beyond","1100","singer"],["莫文蔚","1116","singer"],["张国荣","1092","singer"],["孙燕姿","1030","singer"],["李健","1383","singer"],["蔡依林","1034","singer"],["周华健","1097","singer"],["许嵩","1557","singer"],["陈慧娴","11699","singer"],["张靓颖","1026","singer"],["Taylor Swift","9319","singer"],["任贤齐","1094","singer"],["张宇","1210","singer"],["S.H.E","2511","singer"],["林忆莲","1133","singer"],["尚雯婕","1032","singer"],["张震岳","1142","singer"],["萧敬腾","9257","singer"],["萧亚轩","1060","singer"],["李代沫","12889380","singer"],["侃侃","1640","singer"],["许巍","1226","singer"],["范玮琪","1119","singer"],["张杰","1035","singer"],["周传雄","6919","singer"],["张韶涵","1069","singer"],["冷漠","1629","singer"],["杨坤","1380","singer"],["曹格","1292","singer"],["姚贝娜","8007","singer"],["PSY","18104396","singer"],["徐良","211426","singer"],["林海","1740","singer"],["孟庭苇","1191","singer"],["张雨生","8559","singer"],["王若琳","5984","singer"],["郑源","1086","singer"],["陈淑桦","1228","singer"],["王心凌","1063","singer"],["郭静","1401","singer"],["孙俪","1042","singer"],["杨丞琳","82366","singer"],["杨钰莹","1451","singer"],["小沈阳","55198","singer"],["Maroon 5","55191","singer"],["陈明","1212","singer"],["平安","12892072","singer"],["迪克牛仔","1127","singer"],["Rihanna","11703","singer"],["林宥嘉","1454","singer"],["金莎","1079","singer"],["林凡","1911","singer"],["安与骑兵","2327240","singer"],["陈慧琳","82402","singer"],["小虎队","1489","singer"],["李玉刚","1078","singer"],["汪苏泷","211833","singer"],["崔子格","1224778","singer"],["陶","1104","singer"],["梅艳芳","1101","singer"],["吉克隽逸","16541885","singer"],["李宗盛","1925","singer"],["丁当","1400","singer"],["光良","1112","singer"],["Adele","172072","singer"],["Avril Lavigne","11701","singer"],["杜德伟","1183","singer"],["费玉清","1254","singer"],["张敬轩","17301","singer"],["庾澄庆","1139","singer"],["朴树","1151","singer"],["王杰","1090","singer"]],dtype="S")
    UID02DF=UID00BC.transpose()[0]
    try:
    	UID02D6=UID02DF.tolist().index(tag)
    except:
    	UID02D6=-1
    UID014E=UID02D6>=0
    exist=UID014E
    UID025B=UID00BC
    UID0268=UID02D6
    UID0220=UID014E
    UID0139=tag
    if UID0220==True:
    	UID03F5=UID025B.transpose()[1]
    	UID045A=UID025B.transpose()[2]
    	try:
    		UID0241=UID03F5[UID0268+0]
    	except:
    		UID0241=""
    	try:
    		UID024D=UID045A[UID0268+0]
    	except:
    		UID024D=""
    	UID024E=UID024D
    	UID0242=UID0241
    else: 
    	UID024E=""
    	UID0242=""
    tinguid=UID0242
    type=UID024E
    return exist,type,tinguid
if __name__ == "__main__":
    exist,type,tinguid=main(tag)
