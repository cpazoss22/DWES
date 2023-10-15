<html>
<body>
	<h1>Jubilación</h1>
	<?php
	$edad=$_GET("edad");
	
	function edad_en_7_anhos($edad) {

	return $edad +7;
	}
	if (edad_en_7_anhos($edad) > 65){

	echo "En 7 años tendrás edad de jubilación";
	}else{
	echo "Disfruta de tu tiempo";
	}
	?>
	<table>
	<tr>
		<th>Edad</th>
		<th>Info</th>
	</tr>

	<?php
	$lista = array (57,58,59,60,61);
	foreach ($lista as $valor)
	echo "<tr>";
	echo "<td>", $valor."</td>";
	echo "<td>" mensaje ($valor). "</td>"
	echo"</tr>"
</body>
</html>
