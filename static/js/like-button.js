$("form.like_button_class").on("submit", function (e) {
    let dataString = $(this).serialize();
    let user_id = $(this).closest("form.like_button_class").attr('id');
    $.ajax({
        type: "POST",
        url: "/liked/" + user_id,
        data: dataString,
    });
    e.preventDefault();
    $("#like_button").load(location.href + " #like_button");
    window.location.reload()
});