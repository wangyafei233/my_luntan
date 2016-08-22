/**
 * Created by peter on 2016/8/19.
 */
$(function () {
    $("#box_id").append("<input type='hidden' id='id_user' name='QuestionAuthor'>");
    $("#button-id-ajax").on('click', function () {
        $('#id_QuestionAuthor').val("{{ request.user.id }}");
    });
})