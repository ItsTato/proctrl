$(document).ready(function () {
    var socket;
    socket = io();

    socket.on('update', function (msg) {
        document.getElementById("pcdata").textContent=`<code>${msg.data}</code>`
        $('update').text = `<code>${msg.data}</code>`;
    });
});