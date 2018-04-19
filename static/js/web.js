$(document).ready(function(){
	$("#bois").click(function(){
		$("#dog").load("/delete", function(){
		     $(".listing").remove();
	        });
	})
});
