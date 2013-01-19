
//Class Picker
//manipulates text inputs #departmentname and #classnumber
//calls SelectClass = function(department, classnum, instructor) 
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
						loadClassData(dep_chosen, ui.item.value);

						//update css for class field to filled
						$('#classnumber').removeClass('loaded');
						$('#classnumber').addClass('filled');
					}});

					var loadClassData = function(department, classnum) {
						$.ajax({
							url: '/class_info/'.concat(department).concat('/').concat(classnum),
							type: 'GET',
							success: function(results) {
								$("#instructorlist").empty();
								$("#classname").empty();

								var flag = true;
								for(var key in results) {

									//Populate the title of the class (only once)
									if(flag){
										$("#classname").append(results[key].title);
										flag = false;
									}

									//Look for a lecture, which contains the instructor name,
									//for each instructor create a button that selects the class
									if(results[key].type == 'LEC') {
										//todo: remove duplicates
										$("#instructorlist").append(
											"<button type='button' class='instructor_selection'>".concat(
												results[key].instructor
											).concat("</button>")
										)
										$('.instructor_selection').unbind('click');
										$('.instructor_selection').click(function(){
											var instructor = $(this).html();
											SelectClass(department, classnum, instructor)
										})
									}
								}
							}
						});
					}
				}
			});//end of call to get class list
		}});//end of responding to a department selection
	}
});//end of setting up class picker


var SelectClass = function(department, classnum, instructor) {
	console.log("Class Selected!");
	console.log(department);
	console.log(classnum);
	console.log(instructor);
}//end of Select Class







$(document).ready(function(){
});
