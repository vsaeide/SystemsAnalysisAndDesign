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
