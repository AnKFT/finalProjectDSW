$(document).ready(function(){
	$(".deleteButton").click(function(){
		$("#listingT").load("/deleteListing", {'id':$(".deleteButton").val()});
	})
	$('#createListForm').on('submit', function() {
            $('#myModal').modal('show');
        })
});
