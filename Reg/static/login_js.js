// <<<<<<< HEAD
const username = document.getElementById("username").value;
const password = document.getElementById("password").value;

$(document).ready(function(){

	const URL = "https://127.0.0.1:8000/login"; //server
	$('#submit').click(function(){

		var data = JSON.stringify({"username": username, "password": password});

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

$(document).ready(function(){

	const URL = "https://127.0.0.1:8000/"; //server
	$('#submit').click(function(){

		var data = JSON.stringify({"username": username, "password": password});

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
