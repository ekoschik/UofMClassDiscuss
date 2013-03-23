
//Class Picker
//manipulates text inputs #departmentName and #classNumber
//calls SelectClass
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
		$('#departmentName').autocomplete({source:departmentlist});

		//Department Name is now loaded, update css
		$('#departmentName').removeClass('unloaded');
		$('#departmentName').addClass('loaded');

		//Sets behavior for when when selection is made
		$('#departmentName').autocomplete({select:function(event, ui) {

			//Department Name is now filled, update css
			$('#departmentName').removeClass('loaded');
			$('#departmentName').addClass('filled');
			$('#classNumber').focus();

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
						classNumberList.push({label: class_list_raw[key].title, value: class_list_raw[key].number});
					}
					$('#classNumber').autocomplete({source:classNumberList});

					//Set css for class field to loaded
					$('#classNumber').removeClass('unloaded');
					$('#classNumber').addClass('loaded');

					//Set success behavior for the class field
					$('#classNumber').autocomplete({select:function(event, ui) {
						var classNum = ui.item.value; //note, still have dep_chosen
						loadClassData(dep_chosen, ui.item.value);

						//update css for class field to filled
						$('#classNumber').removeClass('loaded');
						$('#classNumber').addClass('filled');
					}});

					var loadClassData = function(department, classnum) {
						$.ajax({
							url: '/class_info/'.concat(department).concat('/').concat(classnum),
							type: 'GET',
							success: function(results) {
								$("#instructorList").empty();
								$("#className").empty();

								var flag = true;
								for(var key in results) {

									//Populate the title of the class (only once)
									if(flag){
										$("#className").append(results[key].title);
										flag = false;
									}

									//Look for a lecture, which contains the instructor name,
									//for each instructor create a button that selects the class
									if(results[key].type == 'LEC' || results[key].type == 'SEM') {
										//todo: remove duplicates
										$("#instructorList").append(
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

var SelectClass = function(department, classnum, className, year, semester) {
	console.log("Class Selected!");
	console.log(department);
	console.log(classnum);
	console.log(instructor);
	/*
	$.ajax(
		type:"POST",
		url:"/addclass/",
		data: {
			"depcode":department,
			"classnum":classnum,
			"className":,className,
			"year":year,
			"semester":,semester,
		},
		async:true,
		success function(response) {
			console.log(response);
		},
		dataType:"json",
	});
	*/
}//end of Select Class


