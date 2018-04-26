function deletefunction() {
	$("#listingT").load("/deleteListing", {'id':$(".deleteBtn").val()});		
}

function clickme(){
	$("#buyinginfo").load("/showWUB",{'id':$(".buying").val()});
}

