
document.getElementById("targetLanguage").addEventListener("change", function(){
	location.reload();
});

// sets the input as a file uploader or a text input on the form

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
// function logSubmit(event) {
//   var content = `Form Submitted! Time stamp: ${event.timeStamp}`;
//   console.log(content);
//   event.preventDefault();
// }

// const form = document.getElementById('form');
// document.getElementById("spinner").display = block;
// form.addEventListener('submit', logSubmit);

// document.getElementById("btn_upload").addEventListener("click", function(){

// 	$('#spinner').show();

// });

// function spinner(){
// 	alert("import");
// }




function checkTarget(){
	alert("Please select a target language in the languages tab!");
	if(document.getElementById("lessonLang").value == "" || document.getElementById("lessonLang").value == null){
		alert("Please select a target language in the languages tab!");
	}
};

var u = document.getElementById("userLang");
var t = document.getElementById("lessonLang");
var b = document.getElementById("btn_upload")
if(u.value == "" && t.value == ""){
	alert("Specify a native language and a target language before proceeding!");
	b.style.display = "none";
}
else if(u.value == ""){
	alert("Specify a native language before proceeding!");
	b.style.display = "none";
}
else if(t.value == ""){
	alert("Specify a target language before proceeding!");
	b.style.display = "none";
}



checkCookie();
window.onload = (function(){checkNativeCookie()});
