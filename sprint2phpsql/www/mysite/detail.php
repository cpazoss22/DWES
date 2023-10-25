<html>
<head>
<?php
  $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
</head>
  <body>
    <?php
	if (!isset($_GET['id'])) {
	 die('No se ha especificado un juego');
	}
	$id = $_GET['id'];
	$query = 'SELECT * FROM tJuegos WHERE id='.$id;
	$result = mysqli_query($db, $query) or die('Query error');
	$only_row = mysqli_fetch_array($result);
	echo '<img src="'  . $only_row['url_imagen'] .'" id="game-image"/>';
	echo '<h1>'  . $only_row['nombre']  . '</h1>';
    	echo '<p>' . $only_row['genero'] . '</p>';
	echo '<p>' . $only_row['precio'] . '</p>';
	?>
    <h3>Comentarios:</h3>
    <ul>
      <?php
	$query2 = "SELECT * FROM tComentarios WHERE juegos_id=".$id;
	$result2 = mysqli_query($db, $query2) or die("Query error");
	while ($row = mysqli_fetch_array($result2)) {
	  echo "<li>".$row["comentario"]."</li>";
      }
      mysqli_close($db);
      ?>
    </ul>
  </body>
</html>
