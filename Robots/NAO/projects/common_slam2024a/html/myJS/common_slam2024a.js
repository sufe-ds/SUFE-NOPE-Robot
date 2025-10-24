
"use strict";

//兼容算法：PC端用IP地址作为host，机器人平板电脑则无需host（置为false即可）
var local = window.location.host;
var IP = "192.168.1.42";
var host = local ? false:IP;

function ipCheck(ip_str){
	return /^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$/.test(ip_str);
}
//记录最近的点击时间，用于计算超时无点击
var lastClick = new Date().getTime();
document.onclick = function(){
	lastClick = new Date().getTime();
};

var backhome;
var autoclose;
var autoNextNav;
var waitForNearTask;

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
		
		session.service("ALMotion").then(function (mot) {
			window.mot = mot;
			window.mot.setIdlePostureEnabled("Head",true);
		},function (error) {
			console.log("Fail to Create ALMotion:" +  error);
		});
		
		session.service("ALAudioDevice").then(function (aud) {
			window.aud = aud;
		},function (error) {
			console.log("Fail to Create ALAudioDevice:" +  error);
		});
		
		session.service("ALTabletService").then(function (tab) {
			window.tab = tab;	
		},function (error) {
			console.log("Fail to Create ALTabletService:" +  error);
		});
		
		session.service("ALVideoDevice").then(function (vid) {
			window.vid = vid;
			window.vid.setParameter(0,11,1);
		},function (error) {
			console.log("Fail to Create ALVideoDevice:" +  error);
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
			window.basA.setStimulusDetectionEnabled("Movement",false);
			window.basA.setStimulusDetectionEnabled("NavigationMotion",false);
			
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
	//clickSound("sounds/click1.mp3");
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
	//clickSound("sounds/click3.mp3");
	var tips = document.getElementById("tips");
	var buttons = document.getElementById("buttons");
	var notice = document.getElementById("notice");
	tips.style.display = "none";
	buttons.style.display = "block";
	notice.style.display = "none";
}

function openVideo(video_name){
	if(window.mem){
		clickSound("sounds/click1.mp3");
		window.mem.insertData("VIRobotics_video_name",video_name).then(function(){
			setPage("video");
		});
	}
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


function getSlamIP(){
	if(window.mem){
		window.mem.getData("VIRobotics_settings").then(function(data){
			var list = data.replace(/\r/g,"").split("\n");
			for(var i=0;i<list.length;i++){
				var item = list[i].split("\t");
				if(item[0]=="底盘IP"){
					if(ipCheck(item[1])){
						window.slamIP = item[1];
						document.getElementById("slam_ip").innerHTML = item[1] + "（手动）";
					}
					else{
						auto_get_slamIP();
					}
					return
				}
			}
		});
	}
	else{
		setTimeout(function(){getSlamIP();},100);
	}
}

function openNav(timeout){
	//clickSound("sounds/click1.mp3");
	var buttons = document.getElementById("buttons");
	var nav = document.getElementById("nav");
	var navList = document.getElementById("navList");
	
	navList.innerHTML = "<br><font style='font-size:40px'>地点</font><br>";
	buttons.style.display = "none";
	nav.style.display = "block";
	
	loadNavTargets();
	
	autoclose = setInterval(function(){
		var currentTime = new Date().getTime();
		if(currentTime - lastClick>timeout){
			clearInterval(autoclose);
			closeNav();
		}
	},1000);
}

function closeNav(){
	clearInterval(autoclose);
	//clickSound("sounds/click3.mp3");
	var nav = document.getElementById("nav");
	var buttons = document.getElementById("buttons");
	nav.style.display = "none";
	buttons.style.display = "block";
}

function loadNavTargets(){
	if(window.mem){
		window.mem.getData("VIRobotics_nav").then(function(data){
			var list = data.replace(/\r/g,"").split("\n");
			for(var i=0;i<list.length;i++){
				if(list[i]==""){
					return;
				}
				var item = list[i].split("\t");
				addNavTarget(item[0]);
			}
		});
	}
	else{
		setTimeout(function(){loadNavTargets();},100);
	}
}

function addNavTarget(name){
	var navList = document.getElementById("navList");
	var navB = document.createElement("button");
	navB.innerHTML = name;
	navB.onclick = function(){setNavDest(name)};
	navList.appendChild(navB);
}

function setNavDest(name){
	
	clearInterval(autoclose);
	var nav = document.getElementById("nav");
	nav.style.display = "none";
	
	openSlide();
	window.mem.insertData("VIRobotics_nav_button",name).then(function(){
		setPage("nav");
	});
}


//定义openSlide
function openSlide(){
	clickSound("sounds/click1.mp3");
	var slides = document.getElementById("slides");
	slides.style.display = "block";
}

//定义closeSlide
function closeSlide(){
	clickSound("sounds/click3.mp3");
	var slides = document.getElementById("slides");
	slides.style.display = "none";
}

//定义changeSlide
function changeSlide(title,pic_path,txt){	
	var slide_title = document.getElementById("slide_title");
	var slide_txt = document.getElementById("slide_txt");
	var slide_pic123 = document.getElementById("slide_pic123");
	
	slide_title.innerHTML = title;
	slide_txt.innerHTML = txt;
	slide_pic123.src = pic_path + "?time=" + new Date().getTime();
}

function navigationTo(pos){
	if(window.slamIP&&window.mem){
		window.mem.getData("Device/SubDeviceList/Battery/Current/Sensor/Value").then(function(current){
			
			if(current>-1.3){
				robotSay("请先拔出我的充电线缆！");
				setTimeout(function(){setPage("home");},3500);
				return
			}
			else{
				var req;
				var url = "http://"+window.slamIP+"/cmd/nav";
				if (window.XMLHttpRequest)
				{
					req = new XMLHttpRequest();
				}
				else
				{
					req = new ActiveXObject("Microsoft.XMLHTTP");
				}
				
				req.open("POST",url);
				
				req.onreadystatechange = function(){
					if (req.readyState == 4 && req.status == 200){
						
					}
				}
				var obj = {"x":parseFloat(pos.x),"y":parseFloat(pos.y),"theta":parseFloat(pos.theta)*3.14/180};
				req.send(JSON.stringify(obj));
			}
		});
		
	}
}

function goToRecharge(node){
	if(window.slamIP&&window.mem){
		blink(node);
		window.mem.getData("Device/SubDeviceList/Battery/Current/Sensor/Value").then(function(current){
			if(current>-1.3){
				return
			}
			else{
				var req;
				var url = "http://"+window.slamIP+"/cmd/charge";
				if (window.XMLHttpRequest)
				{
					req = new XMLHttpRequest();
				}
				else
				{
					req = new ActiveXObject("Microsoft.XMLHTTP");
				}
				
				req.open("POST",url);
				
				req.onreadystatechange = function(){
					if (req.readyState == 4 && req.status == 200){
						
					}
				}
				// var obj = {"type":1,"point":"充电桩"};
				var obj = {"type":2,"point":"充电桩"}; //参数已经更改，1为取消充电
				req.send(JSON.stringify(obj));
			}
		});
	}
}

function navigationByName(TargetName){
	if(window.slamIP){
		if(TargetName!=""){
			
			var req;
			var url = "http://"+window.slamIP+"/reeman/position";
			// var url = "http://"+window.slamIP+"/reeman/android_target";
			if (window.XMLHttpRequest)
			{
				req = new XMLHttpRequest();
			}
			else
			{
				req = new ActiveXObject("Microsoft.XMLHTTP");
			}
			
			req.open("GET",url);
			console.log(req);
			
			// req.onreadystatechange = function(){
			// 	if (req.readyState == 4 && req.status == 200){
			// 		if (req.responseText!=""){
			// 			var targets = JSON.parse(req.responseText);
			// 			for(var name in targets){
			// 				if(name==TargetName){
			// 					navigationTo(targets[name]);
			// 					return
			// 				}
			// 			}
			// 		}
			// 	}
			// }
			req.onreadystatechange = function() {
				if (req.readyState == 4 && req.status == 200) {
					if (req.responseText != "") {
						var responseObj = JSON.parse(req.responseText);
						var waypoints = responseObj.waypoints;
						for (var i = 0; i < waypoints.length; i++) {
							if (waypoints[i].name == TargetName) {
								// 找到匹配的目标，提取pose信息
								navigationTo(waypoints[i].pose);
								return
							}
						}
					}
				}
			}
			req.send();	
		}
	}
}

function cancelNav(node){
	if(window.slamIP){
		blink(node);
		var req;
		var url = "http://"+window.slamIP+"/cmd/cancel_goal";
		if (window.XMLHttpRequest)
		{
			req = new XMLHttpRequest();
		}
		else
		{
			req = new ActiveXObject("Microsoft.XMLHTTP");
		}
		
		req.open("POST",url);
		
		req.onreadystatechange = function(){
			if (req.readyState == 4 && req.status == 200){
				
			}
		}
		var obj = {};
		req.send(JSON.stringify(obj));
	}
}


function blink(node){
	clickSound("sounds/click1.mp3");
	if(node){
		node.style.backgroundColor = "rgba(255,201,14,1)";
		setTimeout(function(){node.style.backgroundColor="rgba(0,0,0,0.5)";},500);
	}
}

function backToHome(){
	window.location.reload();
}


function openPhoto(timeout){
	setPage("wait");
	clickSound("sounds/click1.mp3");
	var group_photo = document.getElementById("group_photo");
	
	var buttons = document.getElementById("buttons");
	
	buttons.style.display = "none";
	group_photo.style.display = "block";
	
	var video = document.getElementById("video");
	video.src = "http://198.18.0.1:8000/video";
	riseHead();
	autoBack(timeout);
}

function riseHead(){
	if(window.mot&&window.basA){
		window.basA.setEnabled(false).then(function(){
			window.mot.setIdlePostureEnabled("Head",false).then(function(){
				window.mot.setAngles(["HeadYaw","HeadPitch"],[0,-0.2],0.2).then(function(){
					robotSay("我来为您拍照吧");
				});
			});
		});
	}
	else{
		setTimeout(function(){riseHead();},100);
	}
}

function takePhoto(){
	clickSound("sounds/click1.mp3");
	var photo = document.getElementById("photo");
	photo.style.display = "none";
	var count = document.getElementById("qrcode");
	count.innerHTML = "";
	var photo_ctrl = document.getElementById("photo_ctrl");
	photo_ctrl.style.display="none";
	countDown();
}

function countDown(){
	var count = document.getElementById("qrcode");
	count.innerHTML="";
	var i = 5;
	var loop = setInterval(function(){		
		if(i>0){
			count.innerHTML = String(i);
			robotSay(String(i));
			i--;
		}
		else{
			setPage("photo");
			clearInterval(loop);
		}		
	},1000);
}

function showPhoto(url){
	var photo = document.getElementById("photo");
	var photo_ctrl = document.getElementById("photo_ctrl");
	var takePhoto = document.getElementById("takePhoto");
	var qrcode = document.getElementById("qrcode");
	
	photo.src = "pictures/photo.jpg?time="+new Date().getTime();
	photo.onclick = function(){mysign()};			
	takePhoto.innerHTML = "重拍";	
	photo.style.display = "block";
	photo_ctrl.style.display="block";
	
	openQR(url);
	robotSay("拍好了！请扫描二维码，获取照片。");
}

function openQR(url){
	document.getElementById('qrcode').innerHTML = "";
	
	var qrcode = new QRCode(document.getElementById('qrcode'),{
		text: url,
		width: 300,
		height: 300,
		colorDark : "#000000",
		colorLight : "white",
		correctLevel : QRCode.CorrectLevel.L			
	});
}

function openSettings(timeout){
	//clickSound("sounds/click1.mp3");
	getSettingsData();
	var settings = document.getElementById("settings");
	var buttons = document.getElementById("buttons");
	settings.style.display = "block";
	buttons.style.display = "none";

	autoclose = setInterval(function(){
		var currentTime = new Date().getTime();
		if(currentTime - lastClick>timeout){
			clearInterval(autoclose);
			closeSettings();
		}
	},1000);
}

function closeSettings(){
	clearInterval(autoclose);
	//clickSound("sounds/click3.mp3");
	var settings = document.getElementById("settings");
	var buttons = document.getElementById("buttons");
	settings.style.display = "none";
	buttons.style.display = "block";
}

function getSettingsData(){
	if(window.mem&&window.aud&&window.tab){
		window.aud.getOutputVolume().then(function (volume) {
			document.getElementById("volume").innerHTML = volume;						
		});	
		window.tab.getBrightness().then(function (brightness) {
			document.getElementById("brightness").innerHTML = parseInt(brightness*100);						
		});	
		
		var keylist = ["BatteryChargeChanged",
					   "Device/SubDeviceList/Head/Temperature/Sensor/Value",
					   "RobotConfig/Head/FullHeadId"
					   ];
		window.mem.getListData(keylist).then(function(list){
			document.getElementById("pepperBattery").innerHTML = list[0]+"%";
			document.getElementById("cpuTemperature").innerHTML = list[1]+"℃";
			document.getElementById("headID").innerHTML = list[2];
		});
		getSlamBattery();
		getTalkEnable();
	}
	else{
		setTimeout(function(){getSettingsData()},100);
	}
}

function getSlamBattery(){
	if(window.slamIP){
		var req;
		var url = "http://"+window.slamIP+"/reeman/base_encode";
		if (window.XMLHttpRequest)
		{
			req = new XMLHttpRequest();
		}
		else
		{
			req = new ActiveXObject("Microsoft.XMLHTTP");
		}
		
		req.open("GET",url);
		
		req.onreadystatechange = function(){
			if (req.readyState == 4 && req.status == 200){
				if (req.responseText!=""){
					var obj = JSON.parse(req.responseText);
					document.getElementById("slamBattery").innerHTML = obj["battery"] + "%";
				}
			}
		}
		req.send();	
	}
	else{
		setTimeout(function(){getSlamBattery()},100);
	}
}

function changeRobotVolume(adjust){
	if (window.aud){
		var volume = document.getElementById("volume");
		var vol = parseInt(volume.innerHTML) + adjust;
		vol = vol>100?100:vol;
		vol = vol<0?0:vol;
		window.aud.setOutputVolume(vol).then(function(){
			volume.innerHTML = vol;
		});
	}
	else{
		setTimeout(function(){changeRobotVolume(adjust);},100);
	}
}

function changeTabletBrightness(adjust){
	if (window.tab){
		var brightness = document.getElementById("brightness");
		var bri = parseInt(brightness.innerHTML) + adjust;
		bri = bri>100?100:bri;
		bri = bri<0?0:bri;
		window.tab.setBrightness(bri/100.0).then(function(){
			brightness.innerHTML = bri;
		});
	}
	else{
		setTimeout(function(){changeTabletBrightness(adjust);},100);
	}
}

function setRouteList(list){	
	clearInterval(autoclose);
	clearInterval(backhome);
	
	var nav = document.getElementById("nav");
	nav.style.display = "none";
	var customerRoute = document.getElementById("customerRoute");
	customerRoute.style.display = "none";
	
	openSlide();
	
	window.mem.insertData("VIRobotics_route",list).then(function(){
		setPage("route");
	});
}

function routeOne(){
	if(window.mem){	
		window.mem.getData("Device/SubDeviceList/Battery/Current/Sensor/Value").then(function(current){
			if(current>-1.3){
				setPage("wait");
				robotSay("请先拔出我的充电线缆！");
				setTimeout(function(){setPage("home");},3500);
				return
			}
			else{
				window.mem.getData("VIRobotics_settings").then(function(data){
					var list = data.replace(/\r/g,"").split("\n");
					for(var i=0;i<list.length;i++){
						var item = list[i].split("\t");
						if(item[0]=="路线1"){
							setRouteList(item[1]);
							return
						}
					}
				});
			}
		});
	}
}

function routeTwo(){
	if(window.mem){	
		window.mem.getData("Device/SubDeviceList/Battery/Current/Sensor/Value").then(function(current){
			if(current>-1.3){
				setPage("wait");
				robotSay("请先拔出我的充电线缆！");
				setTimeout(function(){setPage("home");},3500);
				return
			}
			else{
				window.mem.getData("VIRobotics_settings").then(function(data){
					var list = data.replace(/\r/g,"").split("\n");
					for(var i=0;i<list.length;i++){
						var item = list[i].split("\t");
						if(item[0]=="路线2"){
							setRouteList(item[1]);
							return
						}
					}
				});
			}
		});
	}
}

function openFeedback(){
	robotSay("请为我的服务评分吧！");
	var slides = document.getElementById("slides");
	var feedback = document.getElementById("feedback");
	slides.style.display = "none";
	feedback.style.display = "block";
	
	lastClick = new Date().getTime();
	autoBack(60000);
}

function setScore(num){
	var feedbackScore = document.getElementById("feedbackScore");
	feedbackScore.setAttribute('data-score',String(num));
	activeFeedback();
	var stars = feedbackScore.children;
	for(var i=0;i<stars.length;i++){
		if(i<=num-1){
			stars[i].style.color = "yellow";
			stars[i].innerHTML = "&#9733;";
		}
		else{
			stars[i].style.color = "white";
			stars[i].innerHTML = "&#9734;";
		}
	}
}

function activeFeedback(){
	var feedbackSubmit = document.getElementById("feedbackSubmit");
	feedbackSubmit.onclick = function(){submitFeedback()};
	feedbackSubmit.style.backgroundColor = "orange";
}

function submitFeedback(){
	var feedbackButton = document.getElementById("feedbackButton");
	var feedbackScore = document.getElementById("feedbackScore");
	var feedbackTxt = document.getElementById("feedbackTxt");
	var feedbackThanks = document.getElementById("feedbackThanks");
	
	feedbackButton.style.display = "none";
	feedbackScore.style.display = "none";
	feedbackTxt.style.display = "none";
	feedbackThanks.style.display = "block";
	
	var score = feedbackScore.getAttribute('data-score');
	var txt = feedbackTxt.value;
	
	//console.log(score+"\t"+txt);
	//暂时不提交用户反馈数据，有需求可以定制
	
	robotSay("谢谢！");
	setTimeout(function(){backToHome()},2000);
}

function openCustomerRoute(timeout){
	clearInterval(autoclose);
	clickSound("sounds/click1.mp3");
	loadNavTargets2();
	var nav = document.getElementById("nav");
	var customerRoute = document.getElementById("customerRoute");
	
	nav.style.display = "none";
	customerRoute.style.display = "block";
	autoBack(timeout);
}

function loadNavTargets2(){
	if(window.mem){
		window.mem.getData("VIRobotics_nav").then(function(data){
			var list = data.replace(/\r/g,"").split("\n");
			for(var i=0;i<list.length;i++){
				if(list[i]==""){
					return;
				}
				var item = list[i].split("\t");
				addNavTarget2(item[0]);
			}
		});
	}
	else{
		setTimeout(function(){loadNavTargets2();},100);
	}
}

function addNavTarget2(name){
	var allNav = document.getElementById("allNav");
	var navB = document.createElement("button");
	navB.innerHTML = name;
	navB.onclick = function(){selectNav(name)};
	allNav.appendChild(navB);
}

function selectNav(name){
	var selectedNavList = document.getElementById("selectedNavList");
	var count = selectedNavList.children.length;
	
	for(var i=0;i<count;i++){
		if(selectedNavList.children[i].children[0].getAttribute('data-name')==name){
			return;
		}
	}
	
	var newtr = document.createElement("tr");
	newtr.innerHTML = "<td data-name=\""+name+"\" >"+ name +"</td><td width=50 onclick='deleteNav(this)'>X</td>";
	selectedNavList.appendChild(newtr);
	
	var selectedNavScroll = document.getElementById("selectedNavScroll");
	selectedNavScroll.scrollTop = selectedNavScroll.scrollHeight;
	
}

function deleteNav(node){
	var deltr = node.parentNode;
	var	table = deltr.parentNode;
	table.removeChild(deltr);
}

function customerRoute(){
	var selectedNavList = document.getElementById("selectedNavList");
	var count = selectedNavList.children.length;
	var text = "";
	for(var i=0;i<count;i++){
		text += selectedNavList.children[i].children[0].getAttribute('data-name') +",";
		if(i+1==count){
			setRouteList(text);
		}
	}
}

function tryWakeUp(){
	if(window.mot){
		clickSound("sounds/click1.mp3");
		window.mot.wakeUp().then(function(){
				
		},function (error) {
			robotSay("太热了！请让我休息一会儿吧。");
		});
	}
}

function rest(){
	if(window.mot){
		clickSound("sounds/click1.mp3");
		window.mot.rest();
	}
}

function setTerminate(){
	stopRobotSay();
	cancelNav(null);
	setPage("home");
}

function waitForNextNav(timeout){
	if(timeout){
		var nextNav = document.getElementById("nextNav");
		
		var i = timeout;
		nextNav.innerHTML = "下一站("+String(i)+"s)";
		nextNav.style.display = "block";
		
		autoNextNav = setInterval(function(){
			if(i>0){
				i--;
				nextNav.innerHTML = "下一站("+String(i)+"s)";
			}
			else{
				goNextNav();
			}
			
		},1000);
	}
	else{
		goNextNav();
	}
}

function goNextNav(){
	clearInterval(autoNextNav);
	clickSound("sounds/click1.mp3");
	var nextNav = document.getElementById("nextNav");
	nextNav.style.display = "none";
	
	window.mem.insertData("VIRobotics_route_pause","0");
}


function waitForNear(TargetName,distance){
	if(window.slamIP){
		if(TargetName!=""){
			var req;
			var url = "http://"+window.slamIP+"/reeman/position";
			if (window.XMLHttpRequest)
			{
				req = new XMLHttpRequest();
			}
			else
			{
				req = new ActiveXObject("Microsoft.XMLHTTP");
			}
			
			req.open("GET",url);
				
			// req.onreadystatechange = function(){
			// 	if (req.readyState == 4 && req.status == 200){
			// 		if (req.responseText!=""){
			// 			var targets = JSON.parse(req.responseText);
			// 			for(var name in targets){
			// 				if(name==TargetName){
			// 					waitForNearTask = setInterval(function(){	
			// 						isNearPos(targets[name],distance);
			// 					},500);
			// 					return
			// 				}
			// 			}
			// 		}
			// 	}
			// }
			req.onreadystatechange = function() {
				if (req.readyState == 4 && req.status == 200) {
					if (req.responseText != "") {
						var responseObj = JSON.parse(req.responseText);
						var waypoints = responseObj.waypoints;
						for (var i = 0; i < waypoints.length; i++){
							if (waypoints[i].name == TargetName) {
								waitForNearTask = setInterval(function(){	
									isNearPos(waypoints[i].pose,distance);
								},500);
							// if (waypoints[i].name == TargetName) {
							// 	// 找到匹配的目标，提取pose信息
							// 	var targetPose = waypoints[i].pose;
							// 	// 调用navigationTo函数，并传入目标的pose信息
							// 	navigationTo(targetPose);
							
								return
							}
						}
					}
				}
			}
			req.send();	
		}
	}
}

function isNearPos(pos,distance){
	var req;
	var url = "http://"+window.slamIP+"/reeman/pose";
	if (window.XMLHttpRequest)
	{
		req = new XMLHttpRequest();
	}
	else
	{
		req = new ActiveXObject("Microsoft.XMLHTTP");
	}
	req.open("GET",url);
	req.onreadystatechange = function(){
		if (req.readyState == 4 && req.status == 200){
			if (req.responseText!=""){
				var nowPos = JSON.parse(req.responseText);
				if((Math.pow(nowPos["x"] - parseFloat(pos.x),2)+Math.pow(nowPos["y"] - parseFloat(pos.y),2))<=Math.pow(distance,2)){
					stopWaitForNear();
				}
			}
		}
	}
	req.send();
}

function stopWaitForNear(){
	clearInterval(waitForNearTask);
	window.mem.insertData("VIRobotics_nav_busy","0");
}

function openNetwork(device){
	if(device=="head"){
		//window.open("http://198.18.0.1");
		openWebSetting();
	}
	else if(device=="tablet"){
		window.tab._launchApk("com.android.settings");
	}
}

function autoRecharge(low,period){
	setInterval(function(){
		if (window.slamIP){
			var req;
			var url = "http://"+window.slamIP+"/reeman/base_encode";
			if (window.XMLHttpRequest)
			{
				req = new XMLHttpRequest();
			}
			else
			{
				req = new ActiveXObject("Microsoft.XMLHTTP");
			}
			
			req.open("GET",url);
			
			req.onreadystatechange = function(){
				if (req.readyState == 4 && req.status == 200){
					if (req.responseText!=""){
						var obj = JSON.parse(req.responseText);
						var battery = obj["battery"];
						var chargeFlag = obj["chargeFlag"];
						if(battery<=low&&chargeFlag==1){
							tryRecharge();
						}
					}
				}
			}
			req.send();		
		}
	},period);
}

function tryRecharge(){
	if(window.mem){
		window.mem.getData("VIRobotics_Page").then(function (page){
			if(page=="home"){
				robotSay("底盘电量低，我要去充电了！");
				goToRecharge();
			}
		});
	}
}

function getTalkEnable(){
	if(window.mem){
		var talkEnable = document.getElementById("talkEnable");
		window.mem.getData("VIRobotics_enableTalk").then(function (enable){
			if(enable=="1"){
				talkEnable.style.backgroundColor = "rgba(255,201,14,1)";
				talkEnable.innerHTML = "对话(开)";
				talkEnable.onclick = function(){setTalkEnable(false)};
			}
			else{
				talkEnable.style.backgroundColor = "transparent";
				talkEnable.innerHTML = "对话(关)";
				talkEnable.onclick = function(){setTalkEnable(true)};
			}
		});
	}
}

function setTalkEnable(enable){
	if(window.mem){
		var talkEnable = document.getElementById("talkEnable");
		if(enable){
			window.mem.insertData("VIRobotics_enableTalk","1");
			talkEnable.style.backgroundColor = "rgba(255,201,14,1)";
			talkEnable.innerHTML = "对话(开)";
			talkEnable.onclick = function(){setTalkEnable(false)};
		}
		else{
			window.mem.insertData("VIRobotics_enableTalk","0");
			talkEnable.style.backgroundColor = "transparent";
			talkEnable.innerHTML = "对话(关)";
			talkEnable.onclick = function(){setTalkEnable(true)};
		}
	}
}

function changeExposure(exposure){
	if(window.vid){
		window.vid.setParameter(0,11,1);
		if(exposure==0){
			window.vid.setParameter(0,40,1);
		}
		else{
			window.vid.setParameter(0,11,0).then(function(){
				window.vid.setParameter(0,17,exposure);
			});
		}
	}
}

function changeHeadPitch(adjust){
	if(window.mot){
		window.mot.getAngles(["HeadPitch"],false).then(function(data){
			var angle = data[0];
			angle = angle + adjust;
			angle = angle>0.3?0.3:angle;
			angle = angle<-0.4?-0.4:angle;
			window.mot.setAngles(["HeadYaw","HeadPitch"],[0,angle],0.1);
		});
	}
}

function openWebSetting(){
	var subPage = document.getElementById("subPage");
	subPage.style.display = "block";
	var subPageContent = document.getElementById("subPageContent");
	subPageContent.innerHTML = "<object type='text/html' data='http://198.18.0.1/#/menu/network/list' width='100%' height='100%'></object>"
}

function closeWebSetting(){
	var subPage = document.getElementById("subPage");
	subPage.style.display = "none";
}

function exit_program(node){
	blink(node);
	setPage("exit");
}

function auto_get_slamIP(){
	var try_ip_list = ["192.168.0.100",
					   "192.168.0.101",
					   "192.168.0.102",
					   "192.168.0.103",
					   "192.168.0.104",
					   "192.168.0.105",
					   "192.168.0.106",
					   "192.168.0.107",
					   "192.168.1.108"];
	for(var i=0;i<try_ip_list.length;i++){
		test_slamIP(try_ip_list[i]);
	}
	setTimeout(function(){auto_get_slamIP();},5000);
}

function test_slamIP(try_ip){
	var req;
	var url = "http://"+try_ip+"/reeman/get_mode";
	if (window.XMLHttpRequest)
	{
		req = new XMLHttpRequest();
	}
	else
	{
		req = new ActiveXObject("Microsoft.XMLHTTP");
	}			
	req.open("GET",url);			
	req.onreadystatechange = function(){
		if (req.readyState == 4 && req.status == 200){
			window.slamIP = try_ip;
			document.getElementById("slam_ip").innerHTML = try_ip + "（自动）";
		}
	}
	req.send();
}