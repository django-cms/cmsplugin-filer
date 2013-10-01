(function ($) {

    // show/hide formsets when link_option drop-down is changed

    var formset_divs_cls;

    function show_selected_link_option(value) {
        for (item in formset_divs_cls) {
            $(formset_divs_cls[item]).hide();
        }
        var link_option = value ? value : $('#id_link_options option[selected="selected"]').val();
        $(formset_divs_cls[link_option]).show();
    };

    $(document).ready(function () {
        // The "data" attribute (which value is dictionary) is set in cmsplugins.py,
        // FilerImagePluginForm.__init__ method. The keys represents link_options
        // values, and the values are css classes coresponding to the formsets that are
        // shown/hidden. I've choosen this solution in order to avoid hard-coding
        // link-options values.
        formset_divs_cls = JSON.parse($('#id_link_options').attr('data'));
        $('#id_link_options').change(function(){
            show_selected_link_option(this.value);
        });
        show_selected_link_option();
    });
}(jQuery));