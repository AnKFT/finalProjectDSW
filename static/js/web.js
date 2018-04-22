$(document).ready(function(){
	$(".deleteButton").click(function(){
               $("#listingT").load("/deleteListing", {'id':$(".deleteButton").val()});
	})
});
