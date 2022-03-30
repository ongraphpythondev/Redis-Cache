window.onload=function(){
    value = $("#filter_query").val();
    if (value){
        $.ajax({
        type: 'POST',
        url: "/home/",
        data: {'value': value},
        success: function (response) {

        },
        error: function (response) {
        }
    })
    }
}