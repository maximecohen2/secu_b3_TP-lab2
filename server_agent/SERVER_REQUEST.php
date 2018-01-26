<?php

//

$order = $_POST['ORDER'];
$value = $_POST['VALUE'];
$ip = $_SERVER['REMOTE_ADDR'];

$mysqli = new mysqli("localhost","root","WRK97mnt","status");

/* Vérificartion de la connexion */
if (mysql_connect_errno()) {
	printf("Echec de la connexion: %s\n", mysqli_connect_error());
	exit();
}

/*Requête 'Select' retourne un jeu de résultat */
$query1 = mysqli->query("INSERT INTO test set CHAMP='$status1'");
mysqli_query($mysqli, $query1);

$query2 = mysqli->query("INSERT INTO test set CHAMP='$status2'");
mysqli_query($mysqli, $query2);

$query3 = mysqli->query("INSERT INTO test set CHAMP='$status3'");
mysqli_query($mysqli, $query3);

$query4 = mysqli->query("INSERT INTO test set CHAMP='$status4'");
mysqli_query($mysqli, $query4);

/* LIbération du jeu de résulat */
$result->close($mysqli);

?>