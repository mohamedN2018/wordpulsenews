(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Main News carousel
    $(".main-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        center: true,
    });


    // Tranding carousel
    $(".tranding-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 2000,
        items: 1,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="fa fa-angle-left"></i>',
            '<i class="fa fa-angle-right"></i>'
        ]
    });


    // Carousel item 1
    $(".carousel-item-1").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ]
    });

    // Carousel item 2
    $(".carousel-item-2").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 30,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            }
        }
    });


    // Carousel item 3
    $(".carousel-item-3").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 30,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });
    

    // Carousel item 4
    $(".carousel-item-4").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 30,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            },
            1200:{
                items:4
            }
        }
    });
    
})(jQuery);

(function () {
  "use strict";

  // helper: safe console
  var log = function () {
    if (window.console && console.log) {
      console.log.apply(console, arguments);
    }
  };

  // wait for DOM
  function onReady(fn) {
    if (document.readyState !== "loading") {
      fn();
    } else {
      document.addEventListener("DOMContentLoaded", fn);
    }
  }

  onReady(function () {
    // ======= basic checks =======
    if (typeof jQuery === "undefined") {
      log("ERROR: jQuery not found — please include jQuery before main.js");
      return;
    }

    var $ = jQuery;

    if (typeof $.fn === "undefined" || typeof $.fn.owlCarousel === "undefined") {
      log("ERROR: Owl Carousel plugin not found — include owl.carousel.min.js before main.js");
      return;
    }

    // detect RTL from <html dir> or lang
    var isRTL = (document.documentElement.getAttribute("dir") || "").toLowerCase() === "rtl";

    // ======= main slider (single item) =======
    if ($("#mainNewsSlider").length) {
      try {
        $("#mainNewsSlider").owlCarousel({
          rtl: isRTL,
          items: 1,
          loop: true,
          margin: 0,
          nav: true,
          dots: true,
          autoplay: true,
          autoplayTimeout: 5000,
          autoplayHoverPause: true,
          navText: ['‹', '›'],
          smartSpeed: 600,
          responsiveRefreshRate: 200,
          lazyLoad: true // if you use data-src lazy images
        });
      } catch (e) {
        log("Owl init error (mainNewsSlider):", e);
      }
    }

    // ======= generic carousels with class .news-carousel =======
    $(".news-carousel").each(function () {
      var $el = $(this);
      try {
        $el.owlCarousel({
          rtl: isRTL,
          loop: true,
          margin: 20,
          nav: true,
          dots: false,
          autoplay: true,
          autoplayTimeout: 4000,
          autoplayHoverPause: true,
          navText: ['‹', '›'],
          smartSpeed: 600,
          responsive: {
            0: { items: 1 },
            576: { items: 1 },
            768: { items: 2 },
            992: { items: 3 },
            1200: { items: 4 }
          }
        });
      } catch (e) {
        log("Owl init error (news-carousel):", e);
      }
    });

    // ======= small helper: update carousels on direction change =======
    // if you toggle RTL dynamically, call $(...).trigger('refresh.owl.carousel') on the carousel element.

    // ======= optional: back-to-top behavior (if present) =======
    var $back = $(".back-to-top");
    if ($back.length) {
      $(window).on("scroll", function () {
        if ($(window).scrollTop() > 300) $back.addClass("show");
        else $back.removeClass("show");
      });
      $back.on("click", function (e) {
        e.preventDefault();
        $("html, body").animate({ scrollTop: 0 }, 600);
      });
    }

    log("main.js loaded — jQuery & Owl OK, RTL:", isRTL);
  });
})();