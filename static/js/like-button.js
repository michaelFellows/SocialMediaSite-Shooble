// $("form.comment-class").on("submit", function (e) {
//     console.log("banana")
//     let dataString = $(this).serialize();
//     let user_id = $(this).closest("form.comment-class").attr('id');
//     user_id = user_id.replace('comment', '')
//     $.ajax({
//         type: "POST",
//         url: "/make-comment/" + user_id,
//         data: dataString,
//     });
//     e.preventDefault();
//     $("#like_button").load(location.href + " #like_button");
//     window.location.reload()
// });

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

