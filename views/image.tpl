<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Pi-power - socket control</title>
<link href="/public/image_{{theme}}/pipower.css" rel="stylesheet" type="text/css">
<!-- Add Jquery -->
<script type="text/javascript" src="/public/jquery.min.js"></script>
<script type="text/javascript" src="/public/pipower.js"></script>
</head>
<body>

<p><a href="{{homelink}}">{{hometitle}}</a></p>

<div id="centre">

<h1 id="title">Pi power web control</h1>

<div class="container">
  <div class="box" id="image01">
    <img class="imgonbutton" id="sw_on_1" src="/public/image_{{theme}}/onbutton.png" alt="On"><br />
    <img class="imgoffbutton" id="sw_off_1" src="/public/image_{{theme}}/offbutton.png" alt="Off">
  </div>
  <div class="box" id="image02">
  <img class="imgonbutton" id="sw_on_2" src="/public/image_{{theme}}/onbutton.png" alt="On"><br />
    <img class="imgoffbutton" id="sw_off_2" src="/public/image_{{theme}}/offbutton.png" alt="Off">
  </div>
  <div class="box" id="image03">
  <img class="imgonbutton" id="sw_on_3" src="/public/image_{{theme}}/onbutton.png" alt="On"><br />
    <img class="imgoffbutton" id="sw_off_3" src="/public/image_{{theme}}/offbutton.png" alt="Off">
  </div>
  <div class="box" id="image04">
  <img class="imgonbutton" id="sw_on_4" src="/public/image_{{theme}}/onbutton.png" alt="On"><br />
    <img class="imgoffbutton" id="sw_off_4" src="/public/image_{{theme}}/offbutton.png" alt="Off">
  </div>
</div>



<p>Cmd status : <span id="status">...</span></p>

</div>



</body>
</html>
