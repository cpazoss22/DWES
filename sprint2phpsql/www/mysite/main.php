<html>
<head>
<?php
	$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
</head>
	<body>
	 <h1>Conexión establecida</h1>
	 <?php
	  // Lanzar una query
	  $query = 'SELECT * FROM tJuegos';
	  $result = mysqli_query($db, $query) or die('Query error');
	  // Recorrer el resultado
	  while ($row = mysqli_fetch_array($result)) {
		echo $row['nombre'];
		echo '<br>';
		echo $row[2];
		echo '<br>';
	}
mysqli_close($db);
?>
</body>
</html>
