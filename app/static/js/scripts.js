// $('.nav-item a').click(function(e) {
//     $('.nav-item a').removeClass('nav_item_clicked');
//     $(this).addClass('nav_item_clicked');
//
// });


// var btns =
//     $(".navbar-nav .nav-link");
//
// for (var i = 0; i < btns.length; i++) {
//     btns[i].addEventListener("click",
//         function () {
//             var current = document
//                 .getElementsByClassName("active");
//
//             current[0].className = current[0]
//                 .className.replace(" active", "");
//
//             this.className += " active";
//         });
// }


// let current = 0;
// for (let i = 0; i < document.links.length; i++) {
//     if (document.links[i].href === document.URL) {
//         current = i;
//     }
// }
// document.links[current].className = 'current';


// $(document).ready(function () {
//     $('li').click(function (e) {
//         console.log("hiiiiiii");
//         $('li').removeClass('current');
//         $(this).addClass('current');
//     });
//
// });


$(document).ready(function () {
    AddActive();
});

function AddActive() {

    var pageUrl = location.href.split(location.host)[1].replace(/^\//, '');

    $(".navbar-nav li").each(function (index) {
        var divId = jQuery(this).attr("id");
        if (pageUrl) {
            if (pageUrl.startsWith(divId)) {

                $(this).addClass("current");
                return false;
            }
        } else {
            $('#home').addClass("current");
            return false;
        }
    })
}