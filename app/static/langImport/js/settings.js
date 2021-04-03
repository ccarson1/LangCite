
function navLang(langItem){
  var d = new Date();
  d.setTime(d.getTime() + (1*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = "Native=" + langItem + ";" + expires + ";path=/";
 
}

function setNativeLang() { 
    var ele = document.getElementsByName('btnradio'); 
    var output;
    for(i = 0; i < ele.length; i++) { 
        if(ele[i].checked) 
        	output = ele[i].value;
        
    } 
    alert(output);
    navLang(output);
}