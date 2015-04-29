
function get_List(){
	$.get("available/", { "artist_name" : "", "strength" : ""},
		function(data){
			var data=data.substring(1, data.length-1);
			names=data.split(",")
			$("#availableList li").remove();
			$.each(names, function(index,value)
			{
				$("#availableList").append('<li class="populars">'+value+'</li>');
			});
			
});
};


$(document).ready(function() {
	$("#about").hide()
	$('#loader').hide();
	$('#content').hide();
	get_List();
	window.setInterval(function(){ get_List(); console.log("go");}, 10000);
$('#form-button').click(function() {
	var artist_names=[]
	var listItems=$('#names li input');
	listItems.each(function(input){
		console.log($(this).val());
		artist_names.push($(this).val());
	});
	artist_names=artist_names.join();
	console.log(artist_names)
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
	$.get("generated/", { "artist_names" : artist_names, "strength" : strength},
		function(data){
			var lyrics=data.substring(1, data.length-1);
			if (lyrics.length < 30)
			{
				console.log(data)
				$('#loading-block').html("You are the first person to request a song by " + lyrics +"."  
					+ " Please be patient while we collect lyrical data. Once the data has been collected "
					+ lyrics +" will appear at the top of the popular artists list.")

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

get_List()
});

$('#availableList').on('click','li.populars', function(){
	var name=$(this).text();
	for (i=0;i<3;i++){
		var element="#artist_name"+i.toString();
		if ($(element).val()=="")
		{
			$(element).val(name);
			return
		};
	};
});

	$("#artist_name").each(function(i){
		if ($(this).val()=="")
		{
			$(this).val(name)
			return
		}
	});

$('#artists_number').change(function(){
	$('#names').empty();
	var num=$(this).val();
	for (i=0; i<num; i++)
	{	
		var id="artist_name"+i.toString();
		var input='<li><input id="'+id+'" class="style-1" type="text" name="artist_name"></li>';
		$('#names').append(input);
	}
});
});

