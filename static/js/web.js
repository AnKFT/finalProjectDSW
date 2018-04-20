$(document).ready(function(){
	$(".deleteButton").click(function(){
		$("#listingT").load("/deleteListing", {'id':$(".deleteButton").val()});
	})
	$(".createList").click(function(){
		$("#createListForm").load("/createListing",{'ltitle':$("#ltitle").val(),'ppemail':$("#paypaladdress").val(), 'description': $("#des").val()});
	})
});

$(document).ready(function() {
            namespace = '/'
            var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
			
			//Event handler for the start event
			socket.on('start', function(msg){
				$('#start').text(msg); //display the server data
			});
			
			//Event handler for my_response events
			socket.on('my_response', function(msg){
				$('#log').append('<br>' + msg);
			});
});
