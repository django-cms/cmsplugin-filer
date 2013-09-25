(function($) {

    var super_showRelated = null;
    var super_dismissRelated =null;

    dismissRelatedImageLookupPopupOverriden = function(win, chosenId, chosenThumbnailUrl, chosenDescriptionTxt, alt, caption, credit, width, height) {
        super_dismissRelated(win, chosenId, chosenThumbnailUrl, chosenDescriptionTxt);
        if (! $('#id_alt_text').val()){
            $('#id_alt_text').val(alt != 'None' ? alt : '');
        }

        if (! $('#id_caption_text').val()){
            $('#id_caption_text').val(caption != 'None' ? caption : '');
        }

        if (! $('#id_credit_text').val()){
            $('#id_credit_text').val(credit != 'None' ? credit : '');
        }

        var aspectRatio = width / height;
        $('#id_thumbnail_option option').each(function(index){
            if (this.value) {
                var m = this.text.match(/(\w+) -- (\d+) x (XXX|\d+)/);
                var optionName = m[1];
                var optionWidth = parseInt(m[2]);
                var optionHeight = m[3];
                this.text = optionName + ' -- ' + optionWidth + ' x ' + Math.floor(optionWidth / aspectRatio);
            }
        });
        return false;
    }

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
    window.showRelatedObjectLookupPopup = showRelatedObjectLookupPopupOverriden;

})(jQuery);
