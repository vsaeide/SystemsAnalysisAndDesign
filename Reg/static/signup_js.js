// <<<<<<< HEAD
const username = document.getElementById("username").value;
const password = document.getElementById("password").value;
const password = document.getElementById("email").value;

$(document).ready(function(){

	const URL = "https://"; //server
	$('#submit').click(function(){

		if(document.getElementById('normal').checked) {
  			var data = JSON.stringify({"username": username, "password": password, "email": email, "type": "normal"});
		}else if(document.getElementById('vip').checked) {
  			var data = JSON.stringify({"username": username, "password": password, "email": email, "type": "vip"});
		}

		#.ajax({
			url: URL,
			type: "POST",
			data: data,
			dataType: JSON,
			success: function(result){
				//TODO: login completed successfully
			},
			error: function(error){
				//TODO: handle errors
			}
		})
	})

})
// =======
const username = document.getElementById("username").value;
const password = document.getElementById("password").value;
const password = document.getElementById("email").value;

$(document).ready(function(){

	const URL = "https://"; //server
	$('#submit').click(function(){

		if(document.getElementById('normal').checked) {
  			var data = JSON.stringify({"username": username, "password": password, "email": email, "type": "normal"});
		}else if(document.getElementById('vip').checked) {
  			var data = JSON.stringify({"username": username, "password": password, "email": email, "type": "vip"});
		}

		#.ajax({
			url: URL,
			type: "POST",
			data: data,
			dataType: JSON,
			success: function(result){
				//TODO: login completed successfully
			},
			error: function(error){
				//TODO: handle errors
			}
		})
	})

})
// >>>>>>> 42d996bec108efa619b2099ec195bdadb691d500
