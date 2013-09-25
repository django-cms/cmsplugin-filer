(function ($) {

    $(document).ready(function () {
        $($('#filerimage_form div fieldset')[2]).find("h2").after('<br><div>Using these fields will override any Image size option specified above in the admin</div><br>');
        $($('#filerimage_form div fieldset')[2]).find("div.field-box.field-horizontal_space p").css('margin-top', '15px').css('margin-left', '-117px');
    });
}(jQuery));