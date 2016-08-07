$(document).ready(function() {
    // define handlers
    $('span[data-cmd]').click(function(){
        var commands = $(this).data().cmd;
        console.log(commands, typeof commands);
        for (var i = 0; i < commands.length; i++) {
            buttonClicked(commands[i][0], commands[i][1]);
        }
    });
}); // end ready

function buttonClicked (type, button) {
    $.get ('/switch'+type, 'socket='+button, displayResponse);
}

function displayResponse (data) {
    $('#status').html(data);
}
