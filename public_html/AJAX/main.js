var testContainer = document.getElementById("tabletest");

var pageRequest = new XMLHttpRequest();
pageRequest.open('GET', 'PirSensor.json');
//pageRequest.open('GET', 'FlameSensor.json');
pageRequest.onload = function() {

	var myTestData = JSON.parse(pageRequest.responseText);
	renderTest(myTestData);
};
pageRequest.send();



function renderTest(data) {
	var htmlString3 = "";



	if (data.length > 0) {

		for (i = 0; i < data.length; i++) {
			
			
			//j = 0

			//if (data[i].pir_rows > 3) {

				//j = 1
			//}


			htmlString3 += "<tr><td>" + data[i].location + "</td><td>" + data[i].pir_rows + "</td><td>" + data[i].flame_rows + "</td></tr>";

			if (data[i].pir_rows < 10) {
				document.getElementsByTagName("td")[1].innerHTML = "Varattu";
				
		}

		}

	console.log ("yo" + htmlString3)
	testContainer.insertAdjacentHTML('beforeend', htmlString3)


	}


}




	//htmlString3 += "<tr>" + data[i] + "</tr>";






/*

if (data[i].status == 1) {

		document.getElementsByTagName("th")[1].style.backgroundColor = "Yellow";
		document.getElementsByTagName("th")[1].innerHTML = "Varattu";
		
		}


		else {
		document.getElementsByTagName("th")[1].style.backgroundColor = "orange";
		document.getElementsByTagName("th")[1].innerHTML = "Tyhja";
	
	
		}
	}

	testContainer.insertAdjacentHTML('beforeend', htmlString3)
	
}


*/

