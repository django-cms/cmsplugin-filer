(function($) {

    // save the reference to the default showRelatedObjectLookupPopup function
    var super_showRelated = null;

    // save the reference to the default dismissRelatedImageLookupPopup function
    var super_dismissRelated = null;

    function windowname_to_id(text) {
        text = text.replace(/__dot__/g, '.');
        text = text.replace(/__dash__/g, '-');
        return text;
    }

    /* This function overrides the one in popup_handling.js from django-filer.
       It performs an extra ajax request in order to fetch the image metadata.
       (alt, caption, credit, width and height).
     */
    dismissRelatedImageLookupPopupOverriden = function(win, chosenId, chosenThumbnailUrl, chosenDescriptionTxt) {
    	var name = windowname_to_id(win.name);
    	var imgChanged = (document.getElementById(name).value != chosenId);
    	super_dismissRelated(win, chosenId, chosenThumbnailUrl, chosenDescriptionTxt);
    	if (imgChanged) {
    		$.ajax({url: '/cmsplugin_filer_image/fetch_image_metadata',
    			data: {id : chosenId},
    			beforeSend : function (xhr, settings) {
    				$('#filerimage_form div.form-row.field-image').after('<div class="form-row temp-text-fetch-meta"><p class="help">Fetching metadata ... </p></div>');
    			},
    			success : function (data) {
    				if (data) {
    					fixMetadata(data.alt, data.caption, data.credit);
    					$('#id_thumbnail_option').html(data.options);
    					fixThumbnailOptionsHeight(data.width, data.height);
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

    function fixMetadata(alt, caption, credit) {
    	$('#id_alt_text').val(alt ? alt : '');
    	$('#id_caption_text').val(caption ? caption : '');
    	$('#id_credit_text').val(credit ? credit : '');
    }

    function fixThumbnailOptionsHeight(image_width, image_height){
        var aspectRatio = image_width / image_height;
        $('#id_thumbnail_option option').each(function(index){
            if (this.value) {
                var m = this.text.match(/(\w+) -- (\d+) x (XXX|\d+)/);
                var optionName = m[1];
                var optionWidth = parseInt(m[2]);
                this.text = optionName + ' -- ' + optionWidth + ' x ' + Math.floor(optionWidth / aspectRatio);
            }
        });
    }

    function showRelatedObjectLookupPopupOverriden(triggeringLink) {
    	window.showRelatedObjectLookupPopup = showRelatedObjectLookupPopupOverriden;
        super_showRelated(triggeringLink);
        if (! super_dismissRelated)
        	super_dismissRelated = window.dismissRelatedImageLookupPopup;
        dismissRelatedImageLookupPopup = dismissRelatedImageLookupPopupOverriden;
        return false;
    }

    if (! super_showRelated) {
        super_showRelated = window.showRelatedObjectLookupPopup;
    }

    // override the default function; it is called when the mangifying glass is clicked.
    // In my implemetation of this function (see showRelatedObjectLookupPopupOverriden
    // from above), I change the default call to opener.dismissRelatedImageLookupPopup
    // (see directory_listing.html from django-filer templates.)
    window.showRelatedObjectLookupPopup = showRelatedObjectLookupPopupOverriden;

    $(document).ready(function () {
        var width, height;
        // look for <option ...>Original -- ...</option>
        // to get the width and height of the original image
        $('#id_thumbnail_option option').each(function(index){
            if (this.value) {
                var m = this.text.match(/Original -- (\d+) x (\d+)/);
                if (m) {
                    width = parseInt(m[1]);
                    height = parseInt(m[2]);
                }
            }
        });
        if (width && height) {
            fixThumbnailOptionsHeight(width, height);
        }
    });
})(jQuery);
