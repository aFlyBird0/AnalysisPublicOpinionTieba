$(document).ready(function () {
    // 页面刚开始隐藏搜索结果的部分
    $("#resultSection").hide();

    $("#readMoreSection").hide();

    // id为searchInfo的按钮按下触发searchInfo()方法
    $("#searchInfo").click(function () {
        searchInfo(
            page = $("#page").val(),
            keyword = $("#keyword").val());
    });

});


// 在按下enter键的时候就搜索
$(document).keyup(function (event) {
    if (event.keyCode == 13) {
        searchInfo(
            page = $("#page").val(),
            keyword = $("#keyword").val());
    }
});

function searchInfo(page, keyword) {
    // 首先清空result中的内容以便内容填入
    $("#result").empty();
    $.ajax({
        url: "http://localhost:5000/info?page=" + page + "&keyword=" + keyword ,
        //url: "http://localhost:5000/info_new?page=" + page + "&keyword=" + keyword ,
        //url: "http://localhost:5000/info",
        type: "GET",
        dataType: "json",
        success: function (result) {
            // 循环输出json对象result中的键值对
            $.each(result, function (i) {
                // 将返回的结果包装成HTML
                resultItem =
                    `
                        <div class='col-md-12 mb-4'>
                            <div class='card mb-12 shadow-sm'>
                                <div class='card-body'>
                                    <h5>` + result[i].title + `
                                        <small style='margin-left: 10px'>` + result[i].emotion + `</small> 
                                        <small style='margin-left: 10px'>` + result[i].emotion_type + `</small>
                                    <h5>
                                    <p class='text-muted' style='margin-bottom: 0.5em'>` + result[i].href + `</p>
                                    <p class='card-text'>` + result[i].firstFloorContent + `</p>
                                </div>
                            </div>
                        </div>
                    `;
                // 插入HTML到result中
                $("#result").append(resultItem);
            });

            // 搜索完以后让搜索框移上去，带有动画效果
            $("section.jumbotron").animate({
                margin: "0"
            });

            // 显示搜索结果的部分
            $("#resultSection").show();

            $("#readMoreSection").show();

            // error: function (error) {
            //     console.log(error)
            // }

        }
    });
}
