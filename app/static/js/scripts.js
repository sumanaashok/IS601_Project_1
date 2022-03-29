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