$(document).ready(function(){

	//Class Picker
	//manipulates text inputs #departmentname and #classnumber
	//upon selection calls function SelectClass(department, classnum) 
	$.ajax({
		url: '/department_list/',//Load the Department List
		type: 'GET',
		success: function(results) {

			//Add subject list to the department list's autocomplete
			departmentlist = new Array();
			for(var key in results) {
				departmentlist.push({label: results[key].subject, value: results[key].code});
				departmentlist.push({label: results[key].code, value: results[key].code});	
			}
			$('#departmentname').autocomplete({source:departmentlist});

			//Department Name is now loaded, update css
			$('#departmentname').removeClass('unloaded');
			$('#departmentname').addClass('loaded');

			
			//Sets behavior for when when selection is made
			$('#departmentname').autocomplete({select:function(event, ui) {
				
				//Department Name is now filled, update css
				$('#departmentname').removeClass('loaded');
				$('#departmentname').addClass('filled');
				$('#classnumber').focus();

				//Load the class selection possibilities
				var dep_chosen = ui.item.value; 
				$.ajax({
					url: '/class_list/'.concat(dep_chosen),
					type: 'GET',
					success: function(class_list_raw) {

						//Create an autocomplete for the class number (and description)
						classNumberList = new Array();
						for(var key in class_list_raw) {
							classNumberList.push({label: class_list_raw[key].number, value: class_list_raw[key].number});
							
							//to add descriptions as ways of identifying a class
							//classNumberList.push({label: class_list_raw[key].title, value: class_list_raw[key].number});
						}
						$('#classnumber').autocomplete({source:classNumberList});

						//Set css for class field to loaded
						$('#classnumber').removeClass('unloaded');
						$('#classnumber').addClass('loaded');
						
						//Set success behavior for the class field
						$('#classnumber').autocomplete({select:function(event, ui) {
							var classNum = ui.item.value; //note, still have dep_chosen
							SelectClass(dep_chosen, ui.item.value);

							//update css for class field to filled
							$('#classnumber').removeClass('loaded');
							$('#classnumber').addClass('filled');
						}});
					}
			});//end of call to get class list
		}});//end of responding to a department selection
	}});//end of setting up class picker


	var SelectClass = function(department, classnum) {
		$.ajax({
			url: '/class_info/'.concat(department).concat('/').concat(classnum),
			type: 'GET',
			success: function(results) {
				alert(results.length);
		}});


	}



});//end of document ready function
