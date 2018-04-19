$(document).ready(function(){
	$(".deleteButton").click(function(){
		$("#listingT").load("/deleteListing", {'id':$(".deleteButton").val()});
	})
	$(".createList").click(function(){
		$("#createListForm").load("/createListing",{'ltitle':$("#ltitle").val(),'ppemail':$("#paypaladdress").val()});
	})
});
