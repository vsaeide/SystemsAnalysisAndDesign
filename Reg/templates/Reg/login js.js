<<<<<<< HEAD
const username = document.getElementById("username").value;
const password = document.getElementById("password").value;

$(document).ready(function(){
	
	const URL = "https://"; //server
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
=======
const username = document.getElementById("username").value;
const password = document.getElementById("password").value;

$(document).ready(function(){
	
	const URL = "https://"; //server
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
>>>>>>> 42d996bec108efa619b2099ec195bdadb691d500
