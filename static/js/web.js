function deletefunction() {
	$("#listingT").load("/deleteListing", {'id':$(".deleteBtn").val()});		
}

function swiab() {
	$("#buyinginfo").load("/swiab", {'id':$(".buying").val()});		
}

function readURL(input) {

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $('#imgpreview').attr('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
  }
}

$(document).ready(function(){
	$("#imgtoupload").change(function() {
		readURL(this);
	})
});
	

