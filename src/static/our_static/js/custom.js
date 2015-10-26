$(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });
});

function my_special_notification_callback(data) {
    for (var i=0; i < data.unread_list.length; i++) {
        msg = data.unread_list[i];
        console.log(msg);
    }
}