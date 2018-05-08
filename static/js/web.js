function deletefunction(e) {
	$("#listingT").load("/deleteListing", {'id':e.target.id});
	$("#refreshDelete").load("/DL");	
}
function searchfunction(){
	$("#refreshDelete").text("/search")
}

function swiab(e) {
	$("#buyinginfo").load("/swiab", {'id':e.id});		
}

function readURL(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $('.imgpreview').attr('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
  }
}

$(document).ready(function(){
	$("#imgtoupload").change(function() {
		readURL(this);
	})
});


