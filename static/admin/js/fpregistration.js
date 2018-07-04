function PopupCenter(url, title, w, h) {
    // Fixes dual-screen position                         Most browsers      Firefox
    var dualScreenLeft = window.screenLeft != undefined ? window.screenLeft : screen.left;
    var dualScreenTop = window.screenTop != undefined ? window.screenTop : screen.top;

    width = window.innerWidth ? window.innerWidth : document.documentElement.clientWidth ? document.documentElement.clientWidth : screen.width;
    height = window.innerHeight ? window.innerHeight : document.documentElement.clientHeight ? document.documentElement.clientHeight : screen.height;

    var left = ((width / 2) - (w / 2)) + dualScreenLeft;
    var top = ((height / 2) - (h / 2)) + dualScreenTop;
    var newWindow = window.open(url, title, 'scrollbars=yes, width=' + w + ', height=' + h + ', top=' + top + ', left=' + left);

    // Puts focus on the newWindow
    if (window.focus) {
        newWindow.focus();
    }
    return newWindow;
}

function fp_modal_open() {
    var newWin = PopupCenter('/fpregistration','Регистрация отпечатка','900','500');
    // newWin.document.write("Привет, мир!");
}

function setTemplate(templateNumber, templateText) {
    $(".field-template" + templateNumber + " textarea").val(templateText);
    checkFPexist();
}

function clearFP() {
    $(".field-template1 textarea").val('');
    $(".fpnote").remove();
    checkFPexist();
}

function checkFPexist() {
    $(".fpnote, .setfp").remove();

    if ($(".field-template1 textarea").val() !== '')
        $("<span class='errornote fpnote' style='padding: 15px; display: block; width: 425px; text-align: center; color: #337927; border: 1px solid #337927;'>Отпечаток пальца зарегистрирован<br><a class='deletelink' style='color: #CC3434;cursor: pointer;' onclick='clearFP()'>Очистить</a></span>").insertBefore( ".field-template1" );
    else {
        $("<a class='button setfp' style='padding: 15px; display: block; width: 425px; text-align: center;' onclick='fp_modal_open();'>Установить отпечаток пальца</a>").insertBefore( ".field-template1" );
        $("<span class='errornote fpnote' style='padding: 15px; display: block; width: 425px; text-align: center;'>Отпечаток пальца не зарегистрирован</span>").insertBefore( ".field-template1" );
    }
}

$(document).ready(function() {
    for (i=1; i<=10; i++)
        $(".field-template"+i).hide();

    checkFPexist();

});