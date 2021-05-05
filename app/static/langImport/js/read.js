checkCookie();

var path = window.location.pathname
var csrf = $("input[name=csrfmiddlewaretoken]").val();
var read_mode = getCookie("read_mode"); 
var page = 0;
var sentence_num;
var read_page;

if(read_mode == "sentence"){
	sentence_num = 1;
}else{
	// sentence_num = getCookie("sentences")
	sentence_num = 1;
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
	position = getCookie("read_page");
	pos = position.split(":_:")
	console.log(pos[1]);

	if(position == ""){
		pos[0] = 0;
	}
	if(store_json.up_title != pos[1] || store_json.uptitle == "undefined"){
		pos[0] = 0;
	}


	

	if(store_json.up_method == "PDF" || store_json.up_method == "Text File" || store_json.up_method == "Image" || store_json.up_method == "Youtube url"){
		if(sentence_num > store_json.lesson_sentences.length ){
			sentence_num = store_json.lesson_sentences.length;
		}
		if(store_json.target_lang == "Russian"){
			for(i = 0; i < sentence_num; i++){
				
				for(j=0; j < store_json.lesson_sentences[pos[0]].sentence_.length; j++){
					
					createReadButtons(store_json.lesson_sentences[pos[0]].sentence_[j].Russian, j, pos[0])

				}
				
			}
			
		}

		if(store_json.target_lang == "French"){
			for(i = 0; i < sentence_num; i++){
				
				for(j=0; j < store_json.lesson_sentences[pos[0]].sentence_.length; j++){

					createReadButtons(store_json.lesson_sentences[pos[0]].sentence_[j].French, j, pos[0])
					
				}		
			}
		}
		if(store_json.target_lang == "Spanish"){
			for(i = 0; i < sentence_num; i++){
				// console.log(store_json.lesson_sentences[i].sentence_.length)
				for(j=0; j < store_json.lesson_sentences[pos[0]].sentence_.length; j++){

					createReadButtons(store_json.lesson_sentences[pos[0]].sentence_[j].Spanish, j, pos[0])
					
				}	
			}
		}

		if(store_json.target_lang == "English"){
			for(i = 0; i < sentence_num; i++){
				
				// console.log(store_json.lesson_sentences[i].sentence_.length)
				for(j=0; j < store_json.lesson_sentences[pos[0]].sentence_.length; j++){
					
					createReadButtons(store_json.lesson_sentences[pos[0]].sentence_[j].English, j, pos[0])
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
		var att8 = document.createAttribute("onclick");
		
		
		att.value = "btn btn-light";
		att2.value = sent_pos + "_" +word_pos;
		att3.value = "body";
		att4.value = "popover";
		att5.value = "bottom";
		att6.value = "word";
		att7.value = sent_pos;
		att8.value = "click_word('"+ word +"','"+ att2.value +"')";
		
		
		btn.setAttributeNode(att);
		btn.setAttributeNode(att2);
		btn.setAttributeNode(att3);
		btn.setAttributeNode(att4);
		btn.setAttributeNode(att5);
		btn.setAttributeNode(att6);
		btn.setAttributeNode(att7);
		btn.setAttributeNode(att8);
		
		
		document.getElementById("json_lesson").appendChild(btn);
		
	}


	
}

function click_word(btn_word, btn_id){

	
		if(store_json.up_method == "PDF" || store_json.up_method == "Text File" || store_json.up_method == "Image" || store_json.up_method == "Youtube url"){
			
			bust = btn_id.split("_");
			// console.log("sentence " + bust[0] + " on word " + bust[1] + " = " + store_json.lesson_sentences[bust[0]].sentence_[bust[1]].Russian);
			
			// document.getElementById("target_def").innerHTML = bust;
			if(store_json.native_lang == 'English'){
				var en_word = store_json.lesson_sentences[bust[0]].sentence_[bust[1]].English;
				if(en_word != ""){
					document.getElementById("target_def").innerHTML = en_word;
				}
				else{
					document.getElementById("target_def").innerHTML = "";
				}
			}
			if(store_json.native_lang == 'Russian'){
				var en_word = store_json.lesson_sentences[bust[0]].sentence_[bust[1]].Russian;
				if(en_word != ""){
					document.getElementById("target_def").innerHTML = en_word;
				}
				else{
					document.getElementById("target_def").innerHTML = "";
				}
			}
			if(store_json.native_lang == 'French'){
				var en_word = store_json.lesson_sentences[bust[0]].sentence_[bust[1]].French;
				if(en_word != ""){
					document.getElementById("target_def").innerHTML = en_word;
				}
				else{
					document.getElementById("target_def").innerHTML = "";
				}
			}
			if(store_json.native_lang == 'Spanish'){
				var en_word = store_json.lesson_sentences[bust[0]].sentence_[bust[1]].Spanish;
				if(en_word != ""){
					document.getElementById("target_def").innerHTML = en_word;
				}
				else{
					document.getElementById("target_def").innerHTML = "";
				}
			}

		}else{
			console.log("sentence " + bust[0] + " on word " + bust[1] + " = " );
		}
		document.getElementById("target_word").innerHTML = btn_word;
		
		

		if(document.getElementById("target_def").innerHTML == ""){
			$.ajax({
				type: "POST",
				url: path,
				data: {
					'btn_word': btn_word,
					'btn_target': store_json.target_lang,
					'btn_native': getCookie("Native"),
					'csrfmiddlewaretoken': csrf
				},
				success: function(response){
					console.log(response.native_word);
					new_word = response.native_word;
					
					// if(new_word != null){
					// 	if(store_json.native_lang == "English")
					// 		  store_json.lesson_sentences[bust[0]].sentence_[bust[1]].English = new_word;
					// 		  var w = new Date();
					// 		  w.setTime(w.getTime() + (1*24*60*60*1000));
					// 		  var expires = "expires="+ w.toUTCString();
					// 		  document.cookie = "json=" + JSON.stringify(store_json) + ";" + expires + ";path=/";
							  
					// }
					

					var w = new Date();
					w.setTime(w.getTime() + (1*24*60*60*1000));
					var expires = "expires="+ w.toUTCString();
					document.cookie = "trans_word=" + new_word + ";" + expires + ";path=/";
					document.getElementById("target_def").innerHTML = new_word;
					
					
				}


			});
		}

}
	// sends the word to the server using ajax
	// for(var i =0; i < document.getElementsByClassName("btn btn-light").length; i++){
	// 	document.getElementsByClassName("btn btn-light")[i].addEventListener("click", function(){
			
	// 		btn_word = this.innerHTML;
	// 		if(store_json.up_method == "PDF" || store_json.up_method == "Text File" || store_json.up_method == "Image" || store_json.up_method == "Youtube url"){
				
	// 			bust = this.id.split("_");
	// 			console.log("sentence " + bust[0] + " on word " + bust[1] + " = " + store_json.lesson_sentences[bust[0]].sentence_[bust[1]].Russian);
				
	// 			// document.getElementById("target_def").innerHTML = bust;
	// 			if(store_json.native_lang == 'English'){
	// 				var en_word = store_json.lesson_sentences[bust[0]].sentence_[bust[1]].English;
	// 				if(en_word != ""){
	// 					document.getElementById("target_def").innerHTML = en_word;
	// 				}
	// 				else{
	// 					document.getElementById("target_def").innerHTML = "";
	// 				}
	// 			}
	// 			if(store_json.native_lang == 'Russian'){
	// 				var en_word = store_json.lesson_sentences[bust[0]].sentence_[bust[1]].Russian;
	// 				if(en_word != ""){
	// 					document.getElementById("target_def").innerHTML = en_word;
	// 				}
	// 				else{
	// 					document.getElementById("target_def").innerHTML = "";
	// 				}
	// 			}
	// 			if(store_json.native_lang == 'French'){
	// 				var en_word = store_json.lesson_sentences[bust[0]].sentence_[bust[1]].French;
	// 				if(en_word != ""){
	// 					document.getElementById("target_def").innerHTML = en_word;
	// 				}
	// 				else{
	// 					document.getElementById("target_def").innerHTML = "";
	// 				}
	// 			}
	// 			if(store_json.native_lang == 'Spanish'){
	// 				var en_word = store_json.lesson_sentences[bust[0]].sentence_[bust[1]].Spanish;
	// 				if(en_word != ""){
	// 					document.getElementById("target_def").innerHTML = en_word;
	// 				}
	// 				else{
	// 					document.getElementById("target_def").innerHTML = "";
	// 				}
	// 			}

	// 		}else{
	// 			console.log("sentence " + bust[0] + " on word " + bust[1] + " = " );
	// 		}
	// 		document.getElementById("target_word").innerHTML = this.innerHTML;
			
			

	// 		if(document.getElementById("target_def").innerHTML == ""){
	// 			$.ajax({
	// 				type: "POST",
	// 				url: path,
	// 				data: {
	// 					'btn_word': btn_word,
	// 					'btn_target': store_json.target_lang,
	// 					'btn_native': store_json.native_lang,
	// 					'csrfmiddlewaretoken': csrf
	// 				},
	// 				success: function(response){
	// 					console.log(response.native_word);
	// 					new_word = response.native_word;

	// 					var w = new Date();
	// 					w.setTime(w.getTime() + (1*24*60*60*1000));
	// 					var expires = "expires="+ w.toUTCString();
	// 					document.cookie = "trans_word=" + new_word + ";" + expires + ";path=/";
	// 					document.getElementById("target_def").innerHTML = new_word;
						
						
	// 				}


	// 			});
	// 		}
			
			
	// 		new_word = getCookie("trans_word");
	// 		///set second parameter with the defition from server////
	// 		this.setAttribute("data-bs-content", new_word);
			
	// 		return false;
	// 	});
		
	// }

//turns the pages andsets the page number as well as the progress bar
//variables for turning pages
var btn_left = document.getElementById("btn_left");
var btn_right = document.getElementById("btn_right");
var percent_bar = document.getElementById("read_bar");
var container = document.getElementById("json_lesson");
var percent = 0;

var pageNum = Math.ceil(store_json.lesson_sentences.length/sentence_num); 
var inc = 100/pageNum;


btn_left.addEventListener("click", function(){
	document.getElementById("json_lesson").innerHTML = "";
	if(page == 0 || page < 0){
		page = 0;
	}
	else{
		page--;
	}
	percent = (inc * page)
	
	percent_bar.style.width =  percent + "%";
	percent_bar.innerHTML = (Math.round(percent)) + "%";
	console.log(sentence_num *page)
	console.log("sentence_num = " + sentence_num)
	console.log("pageNum = " + pageNum)

	read_page = sentence_num * page;

	var n = store_json.up_title;
	var d = new Date();
	d.setTime(d.getTime() + (1*24*60*60*1000));
	var expires = "expires="+ d.toUTCString();
	document.cookie ="read_page=" + read_page + ":_:" + n +  ";" + expires + ";path=/";

	populate_words();
});

btn_right.addEventListener("click", function(){
	document.getElementById("json_lesson").innerHTML = "";
	if(page == pageNum || page > pageNum){
		page = pageNum;
	}
	else{
		page++;
	}
	percent = (inc * page);
	if(percent > 100){
		percent = 100;
	}
	percent_bar.style.width =  percent + "%";
	percent_bar.innerHTML = (Math.round(percent)) + "%";
	console.log(sentence_num *page)
	console.log("sentence_num = " + sentence_num)
	console.log("pageNum = " + pageNum)

	read_page = sentence_num * page;

	var n = store_json.up_title;
	var d = new Date();
	d.setTime(d.getTime() + (1*24*60*60*1000));
	var expires = "expires="+ d.toUTCString();
	document.cookie = "read_page=" + read_page + ":_:" + n + ";" + expires + ";path=/";

	populate_words();
});



function playAudio(){
	var speak = new p5.Speech();

	if(store_json.target_lang == "Russian"){
		speak.setLang("ru-RU");
	}
	else if(store_json.target_lang == "French"){
		speak.setLang("fr-FR");
	}
	else if(store_json.target_lang == "Spanish"){
		speak.setLang("es-ES");
	}
	else if(store_json.target_lang == "English"){
		speak.setLang("en-US");
	}

	
	var word = document.getElementById("target_word").innerHTML;
	speak.speak(word);
}
