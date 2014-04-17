(function($){
    $(document).ready(function(){
        //set checkbox to toggle
        $('#id_enable_event_tracking').parent().append('<div class="toggle toggle-modern"></div>');
        $('#id_enable_event_tracking').parent().find('.toggle').toggles({
            drag: true, // can the toggle be dragged
            click: true, // can it be clicked to toggle
            text: {
              on: 'ON', // text for the ON position
              off: 'OFF' // and off
            },
            on: $('#id_enable_event_tracking').is(':checked'), // is the toggle ON on init
            animate: 250, // animation time
            transition: 'ease-in-out', // animation transition,
            checkbox: null, // the checkbox to toggle (for use in forms)
            clicker: null, // element that can be clicked on to toggle. removes binding from the toggle itself (use nesting)
            width: 50, // width used if not set in css
            height: 20 // height if not set in css
        })
        .on('toggle', function (e, active) {
            if (active) {
                $('.field-event_category, .field-event_action, .field-event_label').show();
                $('#id_enable_event_tracking').prop('checked', true);
            } else {
                $('.field-event_category, .field-event_action, .field-event_label').hide();
                $('#id_enable_event_tracking').prop('checked', false);
            }
        });

        $('#id_enable_event_tracking').hide();

        if($('#id_enable_event_tracking').is(':checked')){
            $('.field-event_category, .field-event_action, .field-event_label').show();
        }else{
            $('.field-event_category, .field-event_action, .field-event_label').hide();
        }

        $('#filerimage_form').on('submit', function(){
            //turn off event tracking if the image is not clickable
            if($('#id_link_options option[selected="selected"]').text() === "No link"){
                $('#id_enable_event_tracking').prop('checked', false);
            }
        });
    });
}(jQuery));