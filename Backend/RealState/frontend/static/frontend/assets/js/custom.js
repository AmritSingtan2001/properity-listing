$(document).ready(function() {

    // sticky navbar
    // window.onscroll = function() {myFunction()};

    // var header = document.getElementById("header");
    // var sticky = header.offsetTop;

    // function myFunction() {
    //    if (window.pageYOffset > sticky) {
    //       header.classList.add("sticky");
    //    }else{
    //       header.classList.remove("sticky");
    //    }
    // }




   // brand slider
    $('.customer-logos').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1500,
        arrows: false,
        dots: false,
        pauseOnHover: false,
        responsive: [{
            breakpoint: 768,
            settings: {
                slidesToShow: 4
            }
        }, {
            breakpoint: 520,
            settings: {
                slidesToShow: 2
            }
        }]
    });



    $('.moreless-button').click(function() {
  $('.moretext').slideToggle();
  if ($('.moreless-button').text() == "Read More") {
    $(this).text("Read Less")
  } else {
    $(this).text("Read More")
  }
});

    // // advance search
    // $("#formButton").click(function() {
    //     $("#advanceform").toggle();
    // });

     // advance search
     $("#formButton").click(function() {
        $("#form1").toggle();
    });


    // slect2 js
    $('.js-example-basic-single').select2();


    /* Go up */

    $(window).scroll(function () {
        if($(this).scrollTop() > 100 ) {
            $(".go-up").css("right","30px");
        }else {
            $(".go-up").css("right","-60px");
        }
      });

      $(".go-up").click(function(){
          $("html,body").animate({scrollTop:0},500);
          return false;
      });


    // Match-height
    $(function() {
       $('.blog-item').matchHeight();
       $('.sameheight').matchHeight();
       $('.same-height').matchHeight();
    });

});
