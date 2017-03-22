/**
 * Created by J_hao on 2016/12/13.
 */
(function ($) {
    if (!!window.ActiveXObject && !window.XMLHttpRequest) return;
    $(function () {
        nav();
        systole();

        var img = document.createElement("img");
    });


    function nav() {
        var $liCur = $(".nav-box ul li.cur"),
            curP = $liCur.position().left,
            curW = $liCur.outerWidth(true),
            $slider = $(".nav-line"),
            $targetEle = $(".nav-box ul li:not('.last') a"),
            $navBox = $(".nav-box");
        $slider.stop(true, true).animate({
            "left": curP,
            "width": curW
        });
        $targetEle.mouseenter(function () {
            var $_parent = $(this).parent(),
                _width = $_parent.outerWidth(true),
                posL = $_parent.position().left;
            $slider.stop(true, true).animate({
                "left": posL,
                "width": _width
            }, "fast");
        });
        $navBox.mouseleave(function (cur, wid) {
            cur = curP;
            wid = curW;
            $slider.stop(true, true).animate({
                "left": cur,
                "width": wid
            }, "fast");
        });
    }

    ;

    function systole() {
        if (!$(".history").length) {
            return;
        }
        var $warpEle = $(".history-date"),
            $targetA = $warpEle.find("h2 a"),
            parentH,
            eleTop = [];
        parentH = $warpEle.parent().height();
        $warpEle.parent().css({
            "height": 59
        });
        setTimeout(function () {

            $warpEle.find("ul").children(":not('h2:first')").each(function (idx) {
                eleTop.push($(this).position().top);
                $(this).css({
                    "margin-top": -eleTop[idx]
                }).children().hide();
            }).animate({
                "margin-top": 0
            }, 1600).children().fadeIn();
            $warpEle.parent().animate({
                "height": parentH
            }, 2600);

            $warpEle.find("ul").children(":not('h2:first')").addClass("bounceInDown").css({
                "-webkit-animation-duration": "2s",
                "-webkit-animation-delay": "0",
                "-webkit-animation-timing-function": "ease",
                "-webkit-animation-fill-mode": "both"
            }).end().children("h2").css({
                "position": "relative"
            });
        }, 600);

        $targetA.click(function () {
            $(this).parent().css({
                "position": "relative"
            });
            $(this).parent().siblings().slideToggle();
            $warpEle.parent().removeAttr("style");
            return false;
        });

    }

    ;


})(jQuery);