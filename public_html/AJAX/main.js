var testContainer = document.getElementById("tabletest");

var pageRequest = new XMLHttpRequest();
pageRequest.open('GET', 'PirSensor.json');
pageRequest.onload = function() {

	var myTestData = JSON.parse(pageRequest.responseText);
	renderTest(myTestData);
};
pageRequest.send();



function renderTest(data) {
	var htmlString3 = "";


	if (data.length > 0) {

		for (i = 0; i < data.length; i++) {
			

			htmlString3 += "<tr><td>" + data[i].location + "</td><td class='AreaStatusNo'>" + data[i].pir_rows + "</td><td>" + data[i].flame_rows + "</td></tr>";

			if (data[i].pir_rows < 5) {
				
				console.log ("yo V1")

				$( "th" ).text("Hello");
				/*$('.AreaStatusNo').replaceWith('.hello');
				$('.hello').text("Hello World!");*/
				//$( ".AreaStatusNo" ).css("background-color", "blue");
				
				$( ".AreaStatusNo" ).css( "color", "red" )
 				.add( "p" )
  				.css( "background", "orange" );				

// https://api.jquery.com/add/
			}


			else	{

				console.log ("yo V2")
			}


			

		}

	console.log ("yo V3" + htmlString3)
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
