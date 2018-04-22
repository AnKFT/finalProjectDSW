$(document).ready(function(){
	$(".deleteButton").click(function(){
		$("#listingT").load("/deleteListing #listingT", {'id':$(".deleteButton").val()});
	})
});
