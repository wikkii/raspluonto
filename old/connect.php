<?php

// Database and login information

$servername = "localhost";
$database = "nuotiovahti";
$username = "username";
$password = "password";

// Connect to MySQL database

$conn = mysqli_connect($servername, $username, $password, $database);

// Check the connection. Either print "Connection failed" or print "Connected successfully"

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());

}

echo "Connected successfully";

//Close the connection

mysqli_close($conn);
?>
