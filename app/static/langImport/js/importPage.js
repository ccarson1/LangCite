function displayRadioValue() { 
    var ele = document.getElementsByName('flexRadioDefault'); 
    var url = document.getElementById('ytUrl');
    var output;
    for(i = 0; i < ele.length; i++) { 
        if(ele[i].checked) 
        	output = ele[i].value;
        // alert("Import by: "+ele[i].value); 
    } 

    if(url.style.display == "none"){
    	output = '[{ "method":"' + output + '"}, {"name":"' + 
			document.getElementById('lessonName').value + '"}, {"language":"' +
			getCookie("Language") + '"}, {"genre":"' +
			document.getElementById('genreSelect').value + '"}, {"public":"' +
			document.getElementById("flexCheckChecked").checked + '"}]';
    }
    else{
    	alert(url.value);
    	output = '[{ "method":"' + output + '"}, {"name":"' + 
			document.getElementById('lessonName').value + '"}, {"language":"' +
			getCookie("Language") + '"}, {"genre":"' +
			document.getElementById('genreSelect').value + '"}, {"public":"' +
			document.getElementById("flexCheckChecked").checked + '"}, {"url":"' +
			url.value + '"}]';
    }
   alert(output);
} 

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
