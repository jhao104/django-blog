/**
 * Created by Administrator on 2016/11/5.
 */


/**
 * 自动生成目录
 */
function GenerateContentList() {
    $(".post-content").find("h2,h3").each(function (i, item) {
        var tag = $(item).get(0).localName;
        $(item).attr("id", "wow" + i);
        $("#AnchorContent").append('<li><a class="new' + tag + ' anchor-link"  href="#wow' + i + '">' + $(this).text() + '</a></li>');
        $(".newh2").css("margin-left", 0);
        $(".newh3").css("margin-left", 20);
        $(".newh4").css("margin-left", 40);
        $(".newh5").css("margin-left", 60);
        $(".newh6").css("margin-left", 80);
    });
    $("#AnchorContentToggle").click(function () {
        var text = $(this).html();
        if (text == "目录[-]") {
            $(this).html("目录[+]");
            $(this).attr({"title": "展开"});
        } else {
            $(this).html("目录[-]");
            $(this).attr({"title": "收起"});
        }
        $("#AnchorContent").toggle();
    });
}

/**
 * 回到顶部功能.
 */
function backToTop() {
    $(document).ready(function () {
        //首先将#back-to-top隐藏
        $("#back-to-top").hide();
        //当滚动条的位置处于距顶部100像素以下时，跳转链接出现，否则消失
        $(function () {
            $(window).scroll(function () {
                if ($(window).scrollTop() > 500) {
                    $("#back-to-top").fadeIn(1500);
                }
                else {
                    $("#back-to-top").fadeOut(1500);
                }
            });
            //当点击跳转链接后，回到页面顶部位置
            $("#back-to-top").click(function () {
                $('body,html').animate({scrollTop: 0}, 1000);
                return false;
            });
        });
    });
}



