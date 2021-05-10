



function sent_in_par(num_sent){
  var d = new Date();
  d.setTime(d.getTime() + (1*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = "sentences=" + num_sent + ";" + expires + ";path=/";
}

function setNativeLang() { 
    var ele = document.getElementsByName('btnradio'); 
    // var sent = document.getElementById('sent_num').value;
    var sent = 1;

    
    var output;
    for(i = 0; i < ele.length; i++) { 
        if(ele[i].checked) 
        	output = ele[i].value;
        
    } 
    alert(output + " " + sent);
    navLang(output);
    sent_in_par(sent);
    // num_sent()
}