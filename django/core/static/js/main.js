$(document).ready(function(){

    // Anchors must be shown offset from top of screen due to floating nav bar
    function jumpToHash(hash){
    const target = $(hash);
        if (target.length){
            window.scrollTo(0, target.offset().top - 120);
        }
    }
    // Handle clicks
    $('a[href^="#"]').on('click', function(e){
        e.preventDefault();
        jumpToHash(this.hash);
        history.pushState(null, null, this.hash);
    });
    // Handle page load
    $(window).on('load', () => {
        if (window.location.hash) jumpToHash(window.location.hash);
    });

});