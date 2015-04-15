$(document).ready(function() {
$('#undo-button').click(function(){
	$('#song').hide();
	$('#loading-block').html("Our webscraper is young and disobedient at times. Please feel free to try again.");
	var artist = $('#artist_name').val();
	console.log(artist);
	$.get("undo-model/", { 'artist_name' : artist},
		function(data){
			return 
	});
});
});