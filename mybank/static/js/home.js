function doFirst(){
	//先跟HTML畫面產生關聯
	var div_mic = document.getElementById('div_mic');
	var mic = document.getElementById('mic');
	//建立事件聆聽的功能
	
	div_mic.addEventListener('mouseover', mic_none, false);
	div_mic.addEventListener('mouseout', mic_on, false);
}
function mic_none(){
	mic.src = '/static/img/mic_none.svg';
}
function mic_on(){
	mic.src = '/static/img/mic.svg';
}
window.addEventListener('load', doFirst, false);