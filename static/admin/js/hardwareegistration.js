var lastMsg;
var lastMsg_ident;
var socketio = null;
var namespace = "/workhardware";
function showImg() {
    $.get( location.protocol + '//' + document.domain + ':' + 5000 + "/img", function( data ) {
        if (data != '')
            $( "#imgResult" ).html( "<img src='data:image/png;base64, " + data + "' width='150'>");
    });
}

function connect() {

    socketio = io.connect(
        location.protocol + '//' + document.domain + ':' + 5000 + namespace
    );
    socketio.off().on("re_connect_hardware", function(msg) {
        console.log("Соединение с UHF сканером установлено");
        showStartBtn();
        $(".report").html(msg.msg + "<br />");
    });
}

function start() {
    socketio.emit("start_hardware");
    showStopBtn();
}

function stop() {
    socketio.emit("stop_hardware");
    showStartBtn();
}

function showStartBtn() {
    $(".socket_control_start, .socket_control_stop").remove();
    $("<a class='button socket_control_start' style='padding: 15px; display: block; width: 425px; text-align: center;' onclick='start()'>Сканировать метку</a>").insertAfter( "#id_rfid_id" );
}
function showStopBtn() {
    $(".socket_control_start, .socket_control_stop").remove();
    $("<a class='button socket_control_stop' style='padding: 15px; display: block; width: 425px; text-align: center; background-color: #ba2121;' onclick='stop()'>Остановить сканирование</a>").insertAfter( "#id_rfid_id" );
}

$(document).ready(function() {

    $("<p class='report'>Установка соединения со сканером меток...</p>").insertAfter( "#id_rfid_id" );

   connect();
   socketio.on("update", function(msg) {
            //console.log(msg.user_id);

            if (msg.uhf_id !== undefined) {
                if (msg.uhf_id !== "") {
                    $("#id_rfid_id").val(msg.uhf_id);
                } else {
                    $("#id_rfid_id").val('');
                }
            }
            $(".report").html(msg.msg + "<br />");

            if (msg.cardNum !== undefined) {
                if (msg.cardNum !== "") {
                    if (parseInt(msg.cardNum) > 1) {
                        $(".report").html(msg.msg + "<br /><b>ВНИМАНИЕ!</b> Обнаружено несколько меток. Возможны ошибки при определении серийного номера.");
                    }
                }
            }

        //}
    });



});