function addDiv(department, classNum, classTitle){
	var div =  "<div class=\"course\">" + department + " " + classNum + "<br/>" + classTitle + "</div>";
	$("#classesTaken").append(div);
}