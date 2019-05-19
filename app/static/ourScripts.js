$(document).ready(function () {
    $(".sampleTopic").each(function () {
        $(this).mouseenter(function () {
            $(this).css("background-color", "#E8E8E8");
        })
        $(this).mouseleave(function () {
            $(this).css("background-color", "#F8F8F8");
        })
    })

    $(".comment").each(function () {
        $(this).mouseenter(function () {
            $(this).css("background-color", "#E8E8E8");
        })
        $(this).mouseleave(function () {
            $(this).css("background-color", "#F8F8F8");
        })
    })

    $(".sampleTopic").each(function () {
        $(this).mouseenter(function () {
            $(this).find('.hoverOnly').css('display','block');
        })
        $(this).mouseleave(function () {
            $(this).find('.hoverOnly').css('display','none');
        })
    })
    

////////////////////////////////////////////////////////////////
    $(this).submit(function (e) {
       
       var username = $('#username').val();
        var email = $('#email').val();
        var password = $('#password').val();
        var password2 = $('#password2').val();
        var title = $('#title').val();
        var text = $('#text').val();
       var subject = $('#subject').val();

    $(".error").remove();

        if (username.length < 1) {
            $('#username').after('<span class="error">(Required, page not loaded until this field is filled.)</span>');
            e.preventDefault();
        }
        if (password.length < 1) {
            $('#password').after('<span class="error">(Required, page not loaded until this field is filled.)</span>');
            e.preventDefault();
        }

        if (password2.length < 1) {
            $('#password2').after('<span class="error">(Required, page not loaded until this field is filled.)</span>');
            e.preventDefault();
        }

        if (email.length < 1) {
            $('#email').after('<span class="error">(Required, page not loaded until this field is filled.)</span>');
            e.preventDefault();
        }

        if (title.length < 1) {
            $('#title').after('<span class="error">(Required, page not loaded until this field is filled.)</span>');
            e.preventDefault();
        }

        if (text.length < 1) {
            $('#text').after('<span class="error">(Required, page not loaded until this field is filled.)</span>');
            e.preventDefault();
        }

        if (subject.length < 1) {
            $('#subject').after('<span class="error">(Required, page not loaded until this field is filled.)</span>');
            e.preventDefault();
        }
    })
  

});
