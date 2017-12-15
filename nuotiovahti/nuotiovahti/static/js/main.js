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
	pageRequest.open('GET', '/data');
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
	setInterval( getData, 5000 );


// Add HTML to the page. Array of objects is accessed with "data".
function renderData(data) {
	var htmlString = "";


		// Variables for HTML classes
		var pirhtml = "<td class='AreaStatusNo'>";
		var flamehtml = "<td class='FlameStatusNo'>";


			// If the amount of rows from the PIR sensor is higher than value, then use the HMTL class "AreaStatusYes"
			if (data.pir > 25) {

				pirhtml = "<td class='AreaStatusYes'>";

			}

			// If the amount of rows from the flame sensor is higher than value, then use the HMTL class "AreaStatusYes"
			if (data.flame > 5) {

				flamehtml = "<td class='FlameStatusYes'>";

			}

			// Add elements to htmlString

			htmlString += "<tr><td>" + "Mustalampi" + "</td>"+ pirhtml + data.pir + "</td>" + flamehtml + data.flame + "</td></tr>";




	// Add htmlString as content to HTML

	$("#datatable tbody").html(htmlString);

				// Text values for the classes
				$( ".AreaStatusNo" ).text("Available (detections: " + data.pir + ")");

				$( ".AreaStatusYes" ).text("Occupied (detections: " + data.pir + ")");

				$( ".FlameStatusNo" ).text("No fire (detections: " + data.flame + ")");

				$( ".FlameStatusYes" ).text("Burning (detections: " + data.flame + ")");




} // Function ends here
