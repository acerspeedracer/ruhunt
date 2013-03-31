
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Home | Scarlet Assassins &middot; Bootstrap</title>
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

<?php

require("navigation.php");

?>
<br><br><br><br>

    <!-- Carousel
    ================================================== -->
    <div id="myCarousel" class="carousel slide">
      <div class="carousel-inner">
        <div class="item active">
          <img src="images/assassin.png" alt="">
          <div class="container">
            <div class="carousel-caption">

              <h1>RU Assassins</h1>
              <p class="lead">Ultimate Rutgers Manhunt.</p>


              <a class="btn btn-large btn-primary" href="rules.php">Sign Up</a>


            </div>
          </div>
        </div>
        <div class="item">
          <img src="images/scarlet.png" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>A New Perspective on<br> Large Scale Gameplay</h1>
              <p class="lead">Engage in a game of skill and wits<br> on a university-wide scale.</p>
              <a class="btn btn-large btn-primary" href="about.php">Learn more</a>
            </div>
          </div>
        </div>
        <!--<div class="item">
          <img src="http://2guystalkingmetsbaseball.com/wp-content/uploads/2012/11/Rutgers_Scarlet_Knights.jpg" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>One more for good measure.</h1>
              <p class="lead">Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.</p>
              <a class="btn btn-large btn-primary" href="#">Browse gallery</a>
            </div>
          </div>
        </div>-->
      </div>
      <a class="left carousel-control" href="#myCarousel" data-slide="prev">&lsaquo;</a>
      <a class="right carousel-control" href="#myCarousel" data-slide="next">&rsaquo;</a>
    </div><!-- /.carousel -->



    <!-- Marketing messaging and featurettes
    ================================================== -->
    <!-- Wrap the rest of the page in another container to center all the content. -->

    <div class="container marketing">

      <!-- Three columns of text below the carousel -->
      <div class="row">
        <div class="span4">
          <img class="img-circle" data-src="holder.js/140x140">
          <h2>Winner of the Previous Game</h2>
			 <p> This player won the previous game with a recorded time of Days:Hours:Minutes:Seconds. There were X number of players in the game. 
			</p>
          <p><a class="btn" href="#">View details &raquo;</a></p>
		  </div><!-- /.span4 -->

        <div class="span4">
          <img class="img-circle" data-src="holder.js/140x140">
          <h2>Winner of the Previous Game</h2>
			 <p> This player won the previous game with a recorded time of Days:Hours:Minutes:Seconds. There were X number of players in the game.
			</p>
          <p><a class="btn" href="#">View details &raquo;</a></p>
        </div><!-- /.span4 -->
        
        <div class="span4">
          <img class="img-circle" data-src="holder.js/140x140">
        
          <h2>Winner of the Previous Game</h2>
			 <p> This player won the previous game with a recorded time of Days:Hours:Minutes:Seconds. There were X number of players in the game.
			</p>
          <p><a class="btn" href="#">View details &raquo;</a></p>
        </div><!-- /.span4 -->
      </div><!-- /.row -->




      <!-- FOOTER -->
      <footer>
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2013 Company, Inc. &middot; <a href="#">Privacy</a> &middot; <a href="#">Terms</a></p>
      </footer>

    </div><!-- /.container -->



    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="../static/js/jquery.js"></script>
    <script src="../static/js/bootstrap-transition.js"></script>
    <script src="../static/js/bootstrap-alert.js"></script>
    <script src="../static/js/bootstrap-modal.js"></script>
    <script src="../static/js/bootstrap-dropdown.js"></script>
    <script src="../static/js/bootstrap-scrollspy.js"></script>
    <script src="../static/js/bootstrap-tab.js"></script>
    <script src="../static/js/bootstrap-tooltip.js"></script>
    <script src="../static/js/bootstrap-popover.js"></script>
    <script src="../static/js/bootstrap-button.js"></script>
    <script src="../static/js/bootstrap-collapse.js"></script>
    <script src="../static/js/bootstrap-carousel.js"></script>
    <script src="../static/js/bootstrap-typeahead.js"></script>
    <script>
      !function ($) {
        $(function(){
          // carousel demo
          $('#myCarousel').carousel()
        })
      }(window.jQuery)
    </script>
    <script src="/static/js/bootstrap-holder.js"></script>
  </body>
</html>
