<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<body>
<?php
	$juegos_id = $_POST['id'];
	$comentario = $_POST['new_comment'];
	$query = "INSERT INTO tComentarios (id, comentario, usuario_id, juegos_id) VALUES ('".$comentario. "' ,NULL, " . $juegos_id . ",CURDATE())";
	mysqli_query ($db, $query) or die('Error');
	echo "<p>Nuevo comentario ";
	echo mysqli_insert_id($db) ;
	echo " añadido</p>";
	echo "<a href='/detail.php?id=". $juegos_id . "'>Volver</a>";
	mysqli_close ($db);

?>
</body>
</html>
