$(document).ready(function(){
	$(".deleteButton").click(function(){
		$("#listingT").replaceWith(function(){
		     $("#listingT").load("/deleteListing", {'id':$(".deleteButton").val()});
		})
	})
});
