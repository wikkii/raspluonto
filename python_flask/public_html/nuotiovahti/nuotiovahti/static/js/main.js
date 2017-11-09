/*
============================================
JavaScript for AJAX request.
Gets and handles JSON data from the server.
Virtuaaliluonto 3.11.2017
============================================
*/


// Points to a table class in HTML

function getData () {


	// Request & receive JSON Data
	var pageRequest = new XMLHttpRequest();
	pageRequest.open('GET', '/temp/sensor_data.json');
	pageRequest.onload = function() {
	
	
		
		// Save JSON data to a variable
		var mySensorData = JSON.parse(pageRequest.responseText);

		// Call the renderTest function and pass it to mySensorData variable
		renderData(mySensorData);
	};


// Send the request
pageRequest.send();

} // Function ends here
 
	// Call function before setting an interval
	getData();
	// Set Interval. Last argument is in milliseconds NOTE: setInterval() keeps triggering expression again and again unless you tell it to stop
	setInterval( getData, 10000 ); // Try setTimeout as well.


// Add HTML to the page. Array of objects is accessed with "data".
function renderData(data) {
	
	var htmlString = "";

	if (data.length > 0) {

		for (i = 0; i < data.length; i++) {
		

		// Variables for HTML classes
		var pirhtml = "<td class='AreaStatusNo'>"
		var flamehtml = "<td class='FlameStatusNo'>"


			// If the amount of rows from the PIR sensor is higher than 5, then use the HMTL class "AreaStatusYes"
			if (data[i].pir_rows > 5) {
				
				pirhtml = "<td class='AreaStatusYes'>"

			}
			
			// If the amount of rows from the flame sensor is higher than 5, then use the HMTL class "AreaStatusYes"
			if (data[i].flame_rows > 2) {
				
				flamehtml = "<td class='FlameStatusYes'>"

			}

			// Add elements to htmlString
			htmlString += "<tr><td>" + data[i].location + "</td>"+ pirhtml + data[i].pir_rows + "</td>" + flamehtml + data[i].flame_rows + "</td></tr>";


		}

	// Add htmlString as content to HTML

	$("#datatable tbody").html(htmlString);
				
				// Text values for the classes
				$( ".AreaStatusNo" ).text("Available");

				$( ".AreaStatusYes" ).text("Occupied");

 			
				$( ".FlameStatusNo" ).text("No fire");

				$( ".FlameStatusYes" ).text("Fire!");


	}

} // Function ends here
