 
#sets the input as a file uploader or a text input

document.getElementById("flexRadioDefault4").addEventListener("click", function(){
	document.getElementById("fileChoice").style.display = "none";
	document.getElementById("ytUrl").style.display = "block";
	
});

document.getElementById("flexRadioDefault1").addEventListener("click", function(){
	document.getElementById("fileChoice").style.display = "block";
	document.getElementById("ytUrl").style.display = "none";
	
});
document.getElementById("flexRadioDefault2").addEventListener("click", function(){
	document.getElementById("fileChoice").style.display = "block";
	document.getElementById("ytUrl").style.display = "none";
	
});
document.getElementById("flexRadioDefault3").addEventListener("click", function(){
	document.getElementById("fileChoice").style.display = "block";
	document.getElementById("ytUrl").style.display = "none";
	
});

document.getElementById("fileChoice").addEventListener("click", function(){
	event.target.files;
	console.log(document.getElementById("fileChoice"));
});

//sets the lesson language as the cookie language
document.getElementById("lessonLang").textContent = getCookie("Language");
document.getElementById("lessonLang").value = getCookie("Language");
document.getElementById("userLang").value = getCookie("Native");



checkCookie();
