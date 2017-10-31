var pirContainer = document.getElementById("pirinfo");
var flameContainer = document.getElementById("flameinfo");
var testContainer = document.getElementById("tabletest");

var pageRequest = new XMLHttpRequest();
pageRequest.open('GET', 'sensordata.json');
pageRequest.onload = function() {
/*
	var myPirData = JSON.parse(pageRequest.responseText);
	renderPIR(myPirData);

	var myFlameData = JSON.parse(pageRequest.responseText);
	renderFlame(myFlameData);
*/
	var myTestData = JSON.parse(pageRequest.responseText);
	renderTest(myTestData);
};
pageRequest.send();

/*
function renderPIR(data) {
	var htmlString1 = "";

	
	for (i = 0; i < data.length; i++) {

		htmlString1 += "<p>" + data[i].sensor + " status is " + data[i].status + ".</p>";

	}


	pirContainer.insertAdjacentHTML('beforeend', htmlString1)
	
}


*/
/*
function renderFlame(data) {
	var htmlString2 = "";

	
	for (x in data) {

		htmlString2 = "<p>" + data[x].sensor + " status is " + data[x].status + ".</p>";

	}


	flameContainer.insertAdjacentHTML('beforeend', htmlString2)
	
}
*/

function renderTest(data) {
	var htmlString3 = "";


	for (i = 0; i < data.length; i++) {


	htmlString3 += "<th>" + data[i].status + "</th>";

		if (data[i].status == 1) {

		document.getElementsByTagName("th")[1].style.backgroundColor = "Yellow";
		document.getElementsByTagName("th")[1].innerHTML = "Varattu";
		
		}


		else {
		document.getElementsByTagName("th")[1].style.backgroundColor = "Green";
		document.getElementsByTagName("th")[1].innerHTML = "Tyhja";
	

	
		}
	}

	testContainer.insertAdjacentHTML('beforeend', htmlString3)
	
}











var mySensors= [

	{

	"sensor": "PIR",
	"status": "1"

	},
	{

	"sensor": "Flame",
	"status": "0"

	}
]

mySensors[1].status

