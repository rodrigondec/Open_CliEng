/* off-canvas sidebar toggle */
//$('[data-toggle=offcanvas]').click(function() {
//    $('.row-offcanvas').toggleClass('active');
//    $('.collapse').toggleClass('in').toggleClass('hidden-xs').toggleClass('visible-xs');
//});

/*Menu-toggle*/
$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("active");
});