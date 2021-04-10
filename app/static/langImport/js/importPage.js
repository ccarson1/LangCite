 
// sets the input as a file uploader or a text input

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


function checkNativeCookie() {
  var n_lang = getCookie("Native");
  if (n_lang != "") {
    
    document.getElementById("userLang").value = n_lang;
  } 
  else {
    // lang = prompt("Please select a language:", "");
    if (n_lang != "" && n_lang != null) {
      langFun("Native", n_lang, 365);
    }
    
  }
  
}

function NoTargetLanguageError(){
	var NLV = document.getElementById("noLangVal");
	if(NLV.innerHTML != "" || null ){
		NLV.className = "alert alert-danger";
	}else{
		NLV.className = "alert alert-light";
	}
}
function NoNativeLanguageError(){
	var NLV = document.getElementById("noNativeVal");
	if(NLV.innerHTML != "" || null ){
		NLV.className = "alert alert-danger";
	}else{
		NLV.className = "alert alert-light";
	}
}
NoTargetLanguageError();
NoNativeLanguageError();
checkCookie();
window.onload = (function(){checkNativeCookie()});
