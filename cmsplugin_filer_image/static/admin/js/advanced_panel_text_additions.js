(function ($) {

    /* put the unusual help texts in Advanced formset*/
    $(document).ready(function () {
        $($('#filerimage_form div fieldset')[2]).find("h2").after('<br><div>Using these fields will override any Image size option specified above in the admin</div><br>');
        $($('#filerimage_form div fieldset')[2]).find("div.field-box.field-horizontal_space p").css('margin-top', '15px').css('margin-left', '-117px');

        $('#filerimage_form #id_enable_event_tracking')
        .parent()
        .before('<h1>Event Tracking Options</h1><p>This section allows you to enable Google Analytics event tracking for images linked to other pages. You must select labels for event category and event action; event labels are optional. These events will be reported to the Google Analytics account you are using to track this site. You must have Google Analytics applied to this site for this feature to work. Please visit <a href="https://support.google.com/analytics/answer/1033068?hl=en&ref_topic=1033067">support.google.com/analytics</a> for more information on event tracking.</p>');
    });
}(jQuery));