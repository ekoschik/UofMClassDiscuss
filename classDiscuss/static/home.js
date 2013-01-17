$(document).ready(function(){
	
	departmentlist = new Array();
	//departmentlist.push({label:'Electrical Engineering and Computer Science', value:'EECS'});

	$.ajax({
		url: '/subj_list/',
		type: 'GET',
		success: function(results) {
			console.log(results.length);
			for(var key in results) {
				departmentlist.push({label: results[key].subject, value: results[key].code});
				departmentlist.push({label: results[key].code, value: results[key].code});	
			}
			$('#departmentname').autocomplete({source:departmentlist});
			$('#departmentname').removeClass('unloaded');
			$('#departmentname').addClass('loaded');
				
		}
	})

	


	
	
});
