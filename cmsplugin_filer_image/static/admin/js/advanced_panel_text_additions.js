(function ($) {

    /* put the unusual help texts in Advanced formset*/
    $(document).ready(function () {
        $($('#filerimage_form div fieldset')[2]).find("h2").after('<br><div>Using these fields will override any Image size option specified above in the admin</div><br>');
        $($('#filerimage_form div fieldset')[2]).find("div.field-box.field-horizontal_space p").css('margin-top', '15px').css('margin-left', '-117px');
        $('div.form-row.field-caption_text.field-show_caption div').removeClass("field-box");
        $('div.form-row div.field-caption_text input').css('width', '60em');
    });
}(jQuery));