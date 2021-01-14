$("#request").submit(function() {
    var oData = {
        'first_name': $('#request').find('[name="first_name"]').val(),
        'last_name': $('#request').find('[name="last_name"]').val(),
        'email': $('#request').find('[name="email"]').val(),
        'phone': $('#request').find('[name="phone"]').val(),
        'message': $('#request').find('[name="message"]').val(),
        'csrfmiddlewaretoken': $('#request').find('[name="csrfmiddlewaretoken"]').val()
    };
    $.ajax({
        type: "POST",
        url: '/contact/',
        dataType: 'html',
        data: oData,
        success: function(){
            alert("Успешно отправлено!");
        }
    })

return false;
});