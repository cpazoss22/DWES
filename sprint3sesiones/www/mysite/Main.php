<html>
<head>
<style>
h1{
font-size:40px;
font-family:Arial Black, Gadget, sans-serif;
text-align:center;
}

table{
font-family:Arial, sans-serif;
border-collapse: collapse;
width: 235%;
borde: 2px solid #dddd;
}

th,td{
border:2px solid #dddd;
text-align:left;
padding:15px;
}

th{
	background-color:#f5f2f3;
}
.game-image{
max-width: 260px;
}
</style>
<?php
	$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
</head>
<body>
<h1>Juegos molones para mi profe molón</h1>
<table>
<tr>
<th>ID</th>
<th>Nombre</th>
<th>Imagen</th>
<th>Empresa</th>
<th>Precio</th>
</tr>
	 <?php
	  // Lanzar una query
	  $query = 'SELECT * FROM tJuegos';
	  $result = mysqli_query($db, $query) or die('Query error');
	  // Recorrer el resultado
	  while ($row = mysqli_fetch_array($result)) {
		echo '<tr>';
		echo '<td>' . $row['id'] . '</td>';
		echo '<td><a href="detail.php?id=' . $row['nombre'] . '</a></td>'
		echo '<td><img src="' . $row['url_imagen'] . '"class=image-game"></td>';
		echo '<td>' . $row['empresa'] . '</td>';
		echo '<td>' . $row['precio'] . '€' . '</td>';
	}
mysqli_close($db);
?>
</table>
</body>
</html>
