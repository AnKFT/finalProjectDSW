$(document).ready(function(){
	$(".deleteButton").click(function(){
		$("#listingT").load("/deleteListing", $(".deleteButton").val());
	})
});
