$(document).ready(function() {
$('#undo-button').click(function(){
	$('#song').hide();
	$('#loading-block').html("Our webscraper is young and disobedient at times. Please feel free to try again.");
	var artist_names=[]
	var listItems=$('#names li input');
	listItems.each(function(input){
		console.log($(this).val());
		artist_names.push($(this).val());
	});
	artist_names=artist_names.join();
	$.get("undo-model/", { 'artist_names' : artist_names},
		function(data){
			return 
	});
});
});