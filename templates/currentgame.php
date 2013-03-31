<DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Carousel Template &middot; Bootstrap</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="../static/bootstrap.css" rel="stylesheet">
    <link href="../static/bootstrap-responsive.css" rel="stylesheet">
    <link href="../static/manhunt.css" rel="stylesheet">


    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="../assets/js/html5shiv.js"></script>
    <![endif]-->

  </head>

  <body background="images/background.jpg">
  
  <div id="current">

  	<?php

require("navigation.php");

?>

<div class="container marketing">


  <!-- Three columns of text below the carousel -->
  <div class="row">
     
     <br>
     <br>
     <br>
     <center>
       <img src="images/logo.png">
       
          <h2>Currently Playing</h2>
		</center>
<?php

if ($handle = opendir('dynamicimages')) {

 while ( ($entry = readdir($handle)) !== (false)) {
 	if($entry == "." || $entry == ".."){
 		continue;
 	}
	?>
	<div class="figure">
    <?php
        echo "<img src=dynamicimages/$entry>\n";
	?>	
    <p> Firstname Lastname </p>
    </div>
    <?php
}

closedir($handle);

}
else{
 echo "failed to open";
}

?>


	</div>
</div>



  </body>
</html>
