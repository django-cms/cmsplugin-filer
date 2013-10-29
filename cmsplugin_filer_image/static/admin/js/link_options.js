(function ($) {

    // show/hide formsets when link_option drop-down is changed

    var formset_divs_cls;

    function show_selected_link_option(value) {
        // for IE compatibility with older jQuery version, we use both item and i (since item is seen as a function object)
        var i = 1;
        for (item in formset_divs_cls) {
            try {
                $(formset_divs_cls[i++]).hide()
            } catch (e) {
            }
        }
        var link_option = (value != null && value != undefined) ? value : $('#id_link_options option[selected="selected"]').val();
        if (link_option != null && link_option != undefined) {
            $(formset_divs_cls[link_option]).show();
        }
    };

    $(document).ready(function () {
        // The "data" attribute (which value is dictionary) is set in cmsplugins.py,
        // FilerImagePluginForm.__init__ method. The keys represents link_options
        // values, and the values are css classes coresponding to the formsets that are
        // shown/hidden. I've choosen this solution in order to avoid hard-coding
        // link-options values.
        formset_divs_cls = JSON.parse($('#id_link_options').attr('data'));
        $('#id_link_options').change(function () {
            show_selected_link_option(this.value);
        });
        show_selected_link_option();

        // remove the + sign next to the drop-down box
        $('div.form-row.field-thumbnail_option a').remove();
    });
}(jQuery));