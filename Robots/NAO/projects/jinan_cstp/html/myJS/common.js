
"use strict";
//兼容算法：PC端用IP地址作为host，机器人平板电脑则无需host（置为false即可）
var local = window.location.host;
var IP = "192.168.43.111";
var host = local ? false:IP;


//记录最近的点击时间，用于计算超时无点击
var lastClick = new Date().getTime();
document.onclick = function(){
	lastClick = new Date().getTime();
};

var backhome;
var autoclose;

//定义createProxies
function createProxies(){
	QiSession(function (session) {
		console.log("connected!");
		
		session.service("ALMemory").then(function (mem) {
			window.mem = mem;	
		},function (error) {
			console.log("Fail to Create ALMemory:" +  error);
		});
		
		session.service("ALAnimatedSpeech").then(function (ani) {
			window.ani = ani;
		},function (error) {
			console.log("Fail to Create ALAnimatedSpeech:" +  error);
		});
		
		session.service("ALTextToSpeech").then(function (tts) {
			window.tts = tts;
		},function (error) {
			console.log("Fail to Create ALTextToSpeech:" +  error);
		});
		
		session.service("ALBasicAwareness").then(function (basA) {
			window.basA = basA;
		},function (error) {
			console.log("Fail to Create ALBasicAwareness:" +  error);
		});
		
	}, function () {
		console.log("disconnected");
	},host);
}

function BasicAwaress(enable){
	if(window.basA){
		if (enable){
			window.basA.setParameter("LookStimulusSpeed",0.22);
			window.basA.setParameter("LookBackSpeed",0.17);
			window.basA.setTrackingMode("Head");
			window.basA.setStimulusDetectionEnabled("TabletTouch",false);
			window.basA.setStimulusDetectionEnabled("Sound",false);
			window.basA.setEnabled(true);
		}
		else{
			window.basA.setEnabled(false);
		}
	}
	else{
		setTimeout(function(){BasicAwaress(enable);},100);
	}
}

//定义setPage，变量VIRobotics_Page是Html与LabVIEW沟通的重要标识
function setPage(name){
	if (window.mem){
		window.mem.insertData("VIRobotics_Page",name);
	}
	else{
		setTimeout(function(){setPage(name);},100);
	}		
}

//定义robotSay
function robotSay(sentence,config){
	if (window.ani){
		var config = config?config:"disabled";
		window.ani.say(sentence,{"bodyLanguageMode":config});	
	}
	else{
		setTimeout(function(){robotSay(sentence,config);},100);
	}		
}

//定义stopRobotSay()
function stopRobotSay(){
	if (window.tts){
		window.tts.stopAll();
	}
	else{
		setTimeout(function(){stopRobotSay();},100);
	}		
}


//定义clickSound
function clickSound(file){
	document.getElementById('sound').src = file;
	document.getElementById('sound').play();
}


//定义refreshQA
function refreshQA(period){
	setInterval(function(){
		if (window.mem){
			window.mem.getData("VIRobotics_question").then(function (question){
				document.getElementById("human").innerHTML = question;
			});
			window.mem.getData("VIRobotics_answer").then(function (answer){
				document.getElementById("robot").innerHTML = answer;
			});
		}
	},period);	
}

function openTips(timeout){
	clickSound("sounds/click1.mp3");
	var tips = document.getElementById("tips");
	var buttons = document.getElementById("buttons");
	var notice = document.getElementById("notice");
	tips.style.display = "block";
	buttons.style.display = "none";
	notice.style.display = "block";
	
	autoclose = setInterval(function(){
		var currentTime = new Date().getTime();
		if(currentTime - lastClick>timeout){
			clearInterval(autoclose);
			closeTips();
		}
	},1000);

}

function closeTips(){
	clearInterval(autoclose);
	clickSound("sounds/click3.mp3");
	var tips = document.getElementById("tips");
	var buttons = document.getElementById("buttons");
	var notice = document.getElementById("notice");
	tips.style.display = "none";
	buttons.style.display = "block";
	notice.style.display = "none";
}


//超时无点击，返回首页
function autoBack(timeout){
	backhome = setInterval(function(){
		var currentTime = new Date().getTime();
		if(currentTime - lastClick>timeout){
			clearInterval(backhome);
			backToHome();
		}
	},1000);
}

function showADV(img){
	var ADV = document.getElementById("ADV");
	var ADV_img = document.getElementById("ADV_img");
	ADV_img.src = img;
	ADV.style.display = "block";
}

function closeADV(){
	var ADV = document.getElementById("ADV");
	ADV.style.display = "none";
}

function backToHome(){
	window.location.reload();
}
