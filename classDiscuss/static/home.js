
function getSubjectList() {
	subjects = new Array();
	subjects.push('Apple');
	subjects.push('Blueberry');
	subjects.push('Strawberry');
	subjects.push('Pare');
	subjects.push('Poop');
	return subjects;

/*
	$.get("/subj_list/", function(data) {
		for (var key in data) {
			subjects.push(data[key].code);
		}
		alert(subjects.length);
		return subjects; 
	});
*/
}

$(document).ready(function(){
	
	var countries = [
	   { value: 'Andorra', data: 'AD' },
	   { value: 'Zimbabwe', data: 'ZZ' }
	];

	$('#subj_selector').autocomplete({
	    lookup: countries,
	    onSelect: function (suggestion) {
	        alert('You selected: ' + suggestion.value + ', ' + suggestion.data);
	    }
	});

/*
	$("#subj_selector").autocomplete({
		serviceUrl : getSubjectList(),
		onSelect : function(suggestion) {
			alert("Your Selection was " + suggestion.value + "{" + suggestion.data + "}");
		}
	});
*/
	
});