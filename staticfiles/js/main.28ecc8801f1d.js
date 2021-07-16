$( document ).ready(function() {

    var html = $("html");

    $('.my-tweets-button').on('click', function(event){
            event.preventDefault();
            html.animate({scrollTop: $("#my-timeline").offset().top}, '800');
    });

});