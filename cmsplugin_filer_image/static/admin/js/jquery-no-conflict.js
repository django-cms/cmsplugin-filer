try{
    window['jQuery'+jQuery.fn.jquery.split('.').join('')] = jQuery.noConflict();
}catch(e){
    console.error(e);
}