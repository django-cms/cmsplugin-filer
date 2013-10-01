(function($) {

    // save the reference to the default showRelatedObjectLookupPopup function
    var super_showRelated = null;

    // save the reference to the default dismissRelatedImageLookupPopup function
    var super_dismissRelated =null;

    /* This function overrides the one in popup_handling.js from django-filer.
       It performs an extra ajax request in order to fetch the image metadata.
       (alt, caption, credit, width and height).
     */
    dismissRelatedImageLookupPopupOverriden = function(win, chosenId, chosenThumbnailUrl, chosenDescriptionTxt) {
        super_dismissRelated(win, chosenId, chosenThumbnailUrl, chosenDescriptionTxt);
        if (!$('#id_alt_text').val() || !$('#id_caption_text').val() || !$('#id_credit_text').val()) {
            $.ajax({url: '/cmsplugin_filer_image/fetch_image_metadata',
                    data: {id : chosenId},
                    beforeSend : function (xhr, settings) {
                        $('#filerimage_form div.form-row.field-image').after('<div class="form-row temp-text-fetch-meta"><p class="help">Fetching metadata ... </p></div>');
                    },
                    success : function (data) {
                        if (data){
                            if (! $('#id_alt_text').val()){
                                $('#id_alt_text').val(data.alt != 'None' ? data.alt : '');
                            }

                            if (! $('#id_caption_text').val()){
                                $('#id_caption_text').val(data.caption != 'None' ? data.caption : '');
                            }

                            if (! $('#id_credit_text').val()){
                                $('#id_credit_text').val(data.credit != 'None' ? data.credit : '');
                            }

                            var aspectRatio = data.width / data.height;
                            $('#id_thumbnail_option option').each(function(index){
                                if (this.value) {
                                    var m = this.text.match(/(\w+) -- (\d+) x (XXX|\d+)/);
                                    var optionName = m[1];
                                    var optionWidth = parseInt(m[2]);
                                    var optionHeight = m[3];
                                    this.text = optionName + ' -- ' + optionWidth + ' x ' + Math.floor(optionWidth / aspectRatio);
                                }
                            });
                            $('#filerimage_form div.form-row.temp-text-fetch-meta').remove();
                        }
                    },
                    error: function(xhr){
                        $('#filerimage_form div.form-row.temp-text-fetch-meta').remove();
                    },
                   });
        }
        return false;
    };

    function showRelatedObjectLookupPopupOverriden(triggeringLink) {
        super_showRelated(triggeringLink);
        if (!super_dismissRelated){
            super_dismissRelated = window.dismissRelatedImageLookupPopup;
        }
        dismissRelatedImageLookupPopup = dismissRelatedImageLookupPopupOverriden;
        return false;
    }

    if (! super_showRelated){
        super_showRelated = window.showRelatedObjectLookupPopup;
    }

    // override the default function; it is called when the mangifying glass is clicked.
    // In my implemetation of this function (see showRelatedObjectLookupPopupOverriden
    // from above), I change the default call to opener.dismissRelatedImageLookupPopup
    // (see directory_listing.html from django-filer templates.)
    window.showRelatedObjectLookupPopup = showRelatedObjectLookupPopupOverriden;

})(jQuery);
