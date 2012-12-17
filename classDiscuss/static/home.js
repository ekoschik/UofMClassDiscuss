
function getSubjectList() {
	$.get("/subj_list/",
		function(data) {
			alert('got subject list') 
		}
	);
}


$(document).ready(function(){
	
	subjects = getSubjectList();

	/*
	$("#subj_selector").autocomplete({
		
		//source:["Kenny", "Cartman", "Kyle", "Stan", "Randy"],
		source:subject_list,
		select: function(event, ui) {
			alert(ui.item);
		}
	});
	*/

});