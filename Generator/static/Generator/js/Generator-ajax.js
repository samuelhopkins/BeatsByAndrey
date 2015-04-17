
$(document).ready(function() {
	$("#about").hide()
	$('#loader').hide();
	$('#content').hide();
$('#form-button').click(function() {
	var artist= $('#artist_name').val();
	var strength= $('#strength').val();
	$('#song').hide();
	$('#info').fadeOut(400,function(){
		$('#content').fadeIn(400);
	})
	$('#form-button').prop("disabled", true);
	$('#loading-block').html("Please be patient while we generate a song.");
	$('#loader').show();
	$('#back').prop("disabled",true);
	$.get("generated/", { "artist_name" : artist, "strength" : strength},
		function(data){
			var lyrics=data.substring(1, data.length-1);
			if (lyrics.length < 30)
			{
				console.log(data)
				$('#loading-block').html("You are the first person to request a song by " + lyrics +"."  
					+ " Please be patient while we collect lyrical data. Once the data has been collected "
					+ lyrics +" will appear in the popular artists list upon refreshing the page.")

			}
			else
			{
			split=lyrics.split(" ");
			var section=split.length/4;
			var chorus=section/2;
			$('#loading-block').html("");
			$('#block-1').html(split.slice(0,section).join(" "));
			$('#chorus-block').html("[Chorus]");
			$('#block-2').html(split.slice(section,section+chorus).join(" "));
			$('#chorus').html("[Chorus x2]");
			$('#block-3').html(split.slice(section+chorus,section*3).join(" "));
			$('#block-4').html(split.slice(section*3,section*4).join(" "));
			$('#song').show()
		}
		$('#back').prop("disabled",false);
		$('#form-button').prop("disabled", false);
		$('#loader').hide();
		});
});

$('#about-click').click(function(){
	$("#about").fadeToggle()
});

$('#back').click(function(){
	$('#info').show();
	$('#content').fadeOut(400,function(){
		$('#info').fadeIn(400);
	});


});

});
