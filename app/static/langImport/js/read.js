checkCookie();

var path = window.location.pathname
var csrf = $("input[name=csrfmiddlewaretoken]").val();
var read_mode = getCookie("read_mode"); 
var page = 0;
var sentence_num;

if(read_mode == "sentence"){
	sentence_num = 1;
}else{
	sentence_num = getCookie("sentences")
}
try{
	var lesson_json = document.getElementById("json_lesson").innerHTML;
	document.getElementById("json_lesson").innerHTML = ""
	document.getElementById("json_lesson").className = "container";
}
catch(err){
	alert(err);

}

// var d = new Date();
// d.setTime(d.getTime() + (1*24*60*60*1000));
// var expires = "expires="+ d.toUTCString();
// document.cookie = "lesson_json=" + lesson_json + ";" + expires + ";path=/";
// var store_json = JSON.parse(lesson_json);
var store_json = JSON.parse(lesson_json);


function set_mode(mode){
	

	var d = new Date();
	d.setTime(d.getTime() + (1*24*60*60*1000));
	var expires = "expires="+ d.toUTCString();
	document.cookie = "read_mode=" + mode + ";" + expires + ";path=/";
	

	location.reload();
	populate_words();

}

function populate_words(){
	if(store_json.up_method == "PDF" || store_json.up_method == "Text File" || store_json.up_method == "Image"){
		if(sentence_num > store_json.lesson_sentences.length ){
			sentence_num = store_json.lesson_sentences.length;
		}
		if(store_json.target_lang == "Russian"){
			for(i = 0; i < sentence_num; i++){
				for(j=0; j < store_json.lesson_sentences[i].sentence_.length; j++){

					createReadButtons(store_json.lesson_sentences[i].sentence_[j].Russian, j, i)
				}
				
			}
			
		}

		if(store_json.target_lang == "French"){
			for(i = 0; i < sentence_num; i++){
				
				for(j=0; j < store_json.lesson_sentences[i].sentence_.length; j++){

					createReadButtons(store_json.lesson_sentences[i].sentence_[j].French, j, i)
					
				}		
			}
		}
		if(store_json.target_lang == "Spanish"){
			for(i = 0; i < sentence_num; i++){
				// console.log(store_json.lesson_sentences[i].sentence_.length)
				for(j=0; j < store_json.lesson_sentences[i].sentence_.length; j++){

					createReadButtons(store_json.lesson_sentences[page].sentence_[j].Spanish, j, i)
					
				}	
			}
		}

		if(store_json.target_lang == "English"){
			for(i = 0; i < sentence_num; i++){
				// console.log(store_json.lesson_sentences[i].sentence_.length)
				for(j=0; j < store_json.lesson_sentences[i].sentence_.length; j++){

					createReadButtons(store_json.lesson_sentences[i].sentence_[j].English, j, i)
				}
			}
		}
	}else{
		var y_text = '';

		if(sentence_num > store_json.length ){
			sentence_num = store_json.length;
		}

		for(i = 0; i < sentence_num; i++){
			y_text += store_json[i].text + " ";
		}
		y_words = y_text.split(" ");
		for(x= 0; x < y_words.length; x++){
			

			createReadButtons(y_words[x], x);
		}
	}

}

populate_words();


console.log(store_json.target_lang);


function createReadButtons(word, word_pos, sent_pos){
	
	if(word != ""){
		var btn = document.createElement("div");
		btn.innerHTML = word;
		var att = document.createAttribute("class");
		var att2 = document.createAttribute("id");
		var att3 = document.createAttribute("data-bs-container");
		var att4 = document.createAttribute("data-toggle");
		var att5 = document.createAttribute("data-bs-placement");
		var att6 = document.createAttribute("data-bs-content");
		var att7 = document.createAttribute("name");
		
		
		att.value = "btn btn-light";
		att2.value = sent_pos + "_" +word_pos;
		att3.value = "body";
		att4.value = "popover";
		att5.value = "bottom";
		att6.value = "word";
		att7.value = sent_pos;
		
		
		btn.setAttributeNode(att);
		btn.setAttributeNode(att2);
		btn.setAttributeNode(att3);
		btn.setAttributeNode(att4);
		btn.setAttributeNode(att5);
		btn.setAttributeNode(att6);
		btn.setAttributeNode(att7);
		
		
		document.getElementById("json_lesson").appendChild(btn);
		
	}
	
}

// sends the word to the server using ajax
for(var i =0; i < document.getElementsByClassName("btn btn-light").length; i++){
	document.getElementsByClassName("btn btn-light")[i].addEventListener("click", function(){
		var new_word ='dddd'
		btn_word = this.innerHTML;
		if(store_json.up_method == "PDF" || store_json.up_method == "Text File" || store_json.up_method == "Image"){
			
			bust = this.id.split("_");
			console.log("sentence " + bust[0] + " on word " + bust[1] + " = " + store_json.lesson_sentences[bust[0]].sentence_[bust[1]].English);
			
			document.getElementById("target_def").innerHTML = bust;
		}else{
			console.log("sentence " + bust[0] + " on word " + bust[1] + " = " );
		}
		document.getElementById("target_word").innerHTML = this.innerHTML;
		
		


		$.ajax({
			type: "POST",
			url: path,
			data: {
				'btn_word': btn_word,
				'btn_target': store_json.target_lang,
				'btn_native': store_json.native_lang,
				'csrfmiddlewaretoken': csrf
			},
			success: function(response){
				console.log(response.native_word);
				new_word = response.native_word;

				var w = new Date();
				w.setTime(w.getTime() + (1*24*60*60*1000));
				var expires = "expires="+ w.toUTCString();
				document.cookie = "trans_word=" + new_word + ";" + expires + ";path=/";
				
				
				
			}


		});
		
		new_word = getCookie("trans_word");
		///set second parameter with the defition from server////
		this.setAttribute("data-bs-content", new_word);
		
		return false;
	});
	
}



