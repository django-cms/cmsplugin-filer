(function ($) {

    // show/hide formsets when link_option drop-down is changed

    var formset_divs_cls;

    function show_selected_link_option(value) {
        for (item in formset_divs_cls) {
            $(formset_divs_cls[item]).hide();
        }
        var option = value ? value : $('#id_link_options option[selected="selected"]').val();
        $(formset_divs_cls[option]).show();
    };

    $(document).ready(function () {
        formset_divs_cls = JSON.parse($('#id_link_options').attr('data'));
        $('#id_link_options').change(function(){
            show_selected_link_option(this.value);
        });
        show_selected_link_option();
    });
}(jQuery));