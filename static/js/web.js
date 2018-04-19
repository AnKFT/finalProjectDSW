$(document).ready(function(){
	$("#bois").click(function(){
		$("#dog").load("/delete", function(){
		     $("#h2t").replaceWith("<h2>==>This text is updated</h2>");
	        });
	})
});
