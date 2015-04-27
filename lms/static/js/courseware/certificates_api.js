$(document).ready(function() {
    'use strict';

    $(".generate_certs").click(function(e){
        e.preventDefault();
        var post_url = $(".generate_certs").data("endpoint");
        $(this).prop("disabled", true);
        $.ajax({
            type: "POST",
            url: post_url,
            dataType: 'text',
            success: function () {
                location.reload();
            },
            error: function(jqXHR, textStatus, errorThrown) {
                $('#errors-info').html(jqXHR.responseText);
                $('.generate_certs').prop("disabled", false);
            }
        });
    });
});
