


function langFun(langItem){
  var d = new Date();
  d.setTime(d.getTime() + (1*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = "Language=" + langItem + ";" + expires + ";path=/";
  document.getElementById("targetLanguage").innerHTML = langItem;
}

function getCookie(cname) {
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function checkCookie() {
  var lang = getCookie("Language");
  if (lang != "") {
    document.getElementById("targetLanguage").innerHTML = lang;
  } else {
    // lang = prompt("Please select a language:", "");
    if (lang != "" && lang != null) {
      setCookie("Language", lang, 365);
    }
  }
}

checkCookie();