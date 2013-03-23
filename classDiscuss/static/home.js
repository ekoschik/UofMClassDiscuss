function hideBoxes(){
	$("#classBlurb").hide();
	$("#classInputButton").hide();
}
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
								//$("#className").empty();

								var flag = true;
								for(var key in results) {
									//Look for a lecture, which contains the instructor name,
									//for each instructor create a button that selects the class
									if(results[key].type == 'LEC' || results[key].type == 'SEM') {
										//todo: remove duplicates
										//Populate the title of the class (only once)
										var department = results[key].code;
										var classNum = results[key].number;
										var classTitle = results[key].title;

										document.getElementById("classBlurb").innerText = classTitle;
										//$("#classBlurb").html(classBlurbString);
										$("#classInputButton").unbind("click");
										$("#classInputButton").click(function(){SelectClass(department, classNum, classTitle)});

										$("#classBlurb").show();
										$("#classInputButton").show();
										/*
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
										*/
										break;
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

var SelectClass = function(department, classNum, className) {
	console.log("Class Selected!");
	/*
	console.log(department);
	console.log(classnum);
	console.log(instructor);
	*/
	

	$.ajax({
		type:"POST",
		url:"/addclass/",
		data: {
			"depcode":department,
			"classnum":classNum,
			"classname":className,
		},
		async:true,
		success: function(data) {
			//add to the right
			if(data == "success")
				addDiv(department, classNum, className);
			else if(data == "duplicate")
				alert("Class is a duplicate entry");
			console.log(data);
		},
		error: function(data, status, xhr){
			alert(data);
			alert(status);
			alert(xhr);
		},
	});
}//end of Select Class

function addDiv(department, classNum, classTitle){
	var div =  "<div class=\"course\"> <div class=\"courseInfo\">" + department + " " + classNum + "<br/>" + classTitle + "</div></div>";
	$("#classesTaken").append(div);
}

function showOnLeft(department, classNum, classTitle, classComments){
	selectedDept = department;
	selectedClass = classNum;
	//var comment
	document.getElementById("selectedClassName").innerText = department + " " + classNum;
	document.getElementById("selectedClassTitle").innerText = classTitle;
	document.getElementById("selectedClassCommentArea").placeholder = "Please enter your thoughts on this class.";
	$("#selectedClassCommentArea").val(classComments);
	$("#selectedClass").show();
}

var selectedDept, selectedClass;

function updateComment(){
	var comment = $("#selectedClassCommentArea").val();
	if(comment == "")
		alert("Please enter a comment to be saved.");
	else {
		$.ajax({
			type:"POST",
			url:"/updatecomment/",
			data: {
				"depcode":selectedDept,
				"classnum":selectedClass,
				"text":comment,
			},
			async:true,
			success: function(data) {
				//add to the right
				if(data == "success"){
					alert("Comment saved");
					$("selectedClass").hide();
				}
				console.log(data);
			},
			error: function(data, status, xhr){
				alert(data);
				alert(status);
				alert(xhr);
			},
		});
	}
}
