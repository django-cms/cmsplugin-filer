(function ($) {

    formset_divs_cls = {
        1: 'None',
        2: '.form-row.field-free_link.field-target_blank',
        3: '.form-row.field-page_link',
        4: '.form-row.field-file_link',
    };

    function show_selected_link_option(value) {
        for (item in formset_divs_cls) {
            $(formset_divs_cls[item]).hide();
        }
        var option = value ? value : $('#id_link_options option[selected="selected"]').val();
        $(formset_divs_cls[option]).show();
    };

    $(document).ready(function () {
        $('#id_link_options').change(function(){
            show_selected_link_option(this.value);
        });
        show_selected_link_option();
    });
}(jQuery));