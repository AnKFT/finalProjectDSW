function deletefunction() {
	$("#listingT").load("/deleteListing", {'id':$(".deleteBtn").val()});		
}

