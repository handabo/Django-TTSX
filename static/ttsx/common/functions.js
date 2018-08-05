// 增加商品数量
function addgoods(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/shopping/addgoods/',
        type: 'POST',
        data: {'goods_id': id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success:function (data) {
            if (data.code == '200'){
                $('.num_show_'+ id).val(data.count)
            }
        },
        error:function (data) {
            console.log(data)

        }
    })
}


// 减少商品数量
function subgoods(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url:'/shopping/subgoods/',
        type:'POST',
        data:{'goods_id':id},
        dataType:'json',
        headers:{'X-CSRFToken':csrf},
        success:function (data) {
            if (data.code == '200') {
                $('.num_show_'+ id).val(data.count)
            }
        },
        error:function (data) {
            console.log(data)
        }
    })
}


// 刷新商品数量
$.get('/shopping/goodsnum/', function (data) {
    if (data.code == '200'){
        console.log(data)
        for (var i=0; i<data.carts.length; i++){
            $('.num_show_'+ data.carts[i].goods_id).val(data.carts[i].count)
        }
    }
});















