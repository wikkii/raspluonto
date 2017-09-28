<?php

$servername = "localhost";
$username = "nuotiovahti";
$password = "salasana";

//Create connection

$conn = new mysqli($servername, $username, $password);

//

if (!$conn) {
    
	die("Connection failed: " . mysqli_connect_error());

}

echo "Connected successfully";

?>
