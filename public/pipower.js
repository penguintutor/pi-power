

// Use global variable for status so we know if we need to send ajax if change
var button_pressed = '';

$(document).ready(function() {
// define handlers
$('#sw_on_1').click(function(){onButtonClicked('1')});
$('#sw_on_2').click(function(){onButtonClicked('2')});
$('#sw_on_3').click(function(){onButtonClicked('3')});
$('#sw_on_4').click(function(){onButtonClicked('4')});
$('#sw_on_all').click(function(){onButtonClicked('0')});

$('#sw_off_1').click(function(){offButtonClicked('1')});
$('#sw_off_2').click(function(){offButtonClicked('2')});
$('#sw_off_3').click(function(){offButtonClicked('3')});
$('#sw_off_4').click(function(){offButtonClicked('4')});
$('#sw_off_all').click(function(){offButtonClicked('0')});


}); // end ready



// handle on button
function onButtonClicked (button) {
    $.get ('/switchon', 'socket='+button, displayResponse);
}


// handle off button
function offButtonClicked (button) {
    $.get ('/switchoff', 'socket='+button, displayResponse);
}


function displayResponse (data) {
    $('#status').html(data);
}
