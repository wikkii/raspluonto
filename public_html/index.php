<!doctype html>
<html>
<head>
	<title>Virtuaaliluonto - Nuotiovahti</title>
	<meta charset="utf-8" />
	<meta name="description" content="Check the realtime status of nearby campfires." >
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="shortcut icon" href="favicon.png">
	
	 <!-- Libraries used -->
	
	<link rel="stylesheet" href="styles.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">	
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

</head>
<body>

<!-- Header -->

<div class="container">
	
	<!-- Fixed Navbar -->

    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" id="HeaderNav" href="#">Nuotiovahti</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="https://raspluonto.wordpress.com">About</a></li>
            <li><a href="https://raspluonto.wordpress.com/contact/">Contact</a></li>           
          </ul>
        </div>
      </div>
    </nav>
</div>

<br>

<!-- Fire Picture -->
 
<div class="container" id="picture">	

<br>
	<div class="row">
		<div class="col-xs-12">
		<img src="fireBig.png" id="logo" alt="Fire logo">
		</div>
	</div>
</div>

<!-- Tables for status data -->

<div class="container" id="maincontent">		
	<div class="row">
	
	
	<table class="table table-bordered">
		<thead>
			<tr>
				
				<th>Location:</th>
				<th>Area status:</th>
				<th>Fire status:</th>

			</tr>
		</thead>
		<tbody>
			<tr>
				
				<th>X</th>
				<th id="pir"></th>
				<th id="flame"></th>

			</tr>
		</tbody>
	</table>
	</div>

	<div class="space"></div>
	
<!-- Footer & credits -->
	
	<div class="row">
		
		<p id="tekijä">Markus Pyhäranta - Virtuaaliluonto 2017.</p>
	
	</div>
</div>



<!-- Set table values -->

<script>
function setValue(){
	
	
	<!-- Set value for PIR -->	
	var PirValue = document.getElementById("pir").innerHTML = "1";
	
	<!-- Set value for Flame -->	
	var FlameValue = document.getElementById("flame").innerHTML = "0";

}

<!-- Run script -->
setValue();

</script>

<!-- Change table colors based on their value -->

<script>
function checkValue(){
	
	//Not working atm..
	
	var PirValue = document.getElementById("pir");
	
	<!-- If PIRs value has been defined as 1, then use red color -->
	if (PirValue.value == "1" ) {
		PirValue.style.backgroundColor = "red";

		
	}
	<!-- If PIR's value has been defined as something else than 1, then use green color -->
	else {
		PirValue.style.backgroundColor = "green";
	
	
	}
}

<!-- Run script -->
checkValue();

</script>

</body>
</html>
