<html>
<body>
	<h1>Conversor de longitudes</h1>
	<p>Convierte de la unidad específica a metros</p>
	<p>
	<?php
	 if (isset($_POST["funidad"]) && isset($_POST["fcantidad"])) {
	 $cantidad =$_POST["fcantidad"];
	   if ($_POST["funidad"] == "pulgada"){
		$metros= $cantidad * 0.0254;
		$v_metros = $v_pulgadas * 0.0254;
		echo $cantidad."pulgadas=".$metros."metros(s)";
		}elseif ($_POST["funidad"]=="pie"){
		$metros =$cantidad * 0.3048;
		echo $cantidad."pies= ".$metros."metros";
		}else{ "Unidad no soportada";
	}
}
	?>
	</p>
	<p>Realiza una nueva conversión:</p>
	<form action= "/conversor2.php" method="post">
		<label for="cantidad_input">Cantidad:</label><br>
		<input type="text" id="cantidad_input" name="fcantidad"><br>
		<input type="radio" id="pulgada_input" name="funidad" value="pulgada">
		<label for="pulgada_input">Pulgada(s)</label><br>
		<input type="radio" id="pie_input" name="funidad" value="pie">
		<label for="pie_input">PIE</label><br>
		<input type="radio" id="otro_input" name="funidad" value="otro">
		<label for="otro_input">Otro</label><br>

		<input type="submit" value="Convertir">
	</form>
</body>
</html>

