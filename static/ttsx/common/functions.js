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
                console.log(data);
                $('.num_show_'+ id).val(data.count)
                $('#price'+ id).html(data.goods_price)
            }
            tatal_price();
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
                if (data.count >= 1){
                    $('.num_show_'+ id).val(data.count)
                    $('#price'+ id).html(data.goods_price)
                }else {
                    alert('亲! 生活不易啊, 至少买一个吧!')
                }
                tatal_price();
                console.log(data);
            }
        },
        error:function (data) {
            console.log(data)
        }
    })
}


// 刷新商品数量, 单个商品总价
$.get('/shopping/goodsnum/', function (data) {
    if (data.code == '200'){
        console.log(data); //测试
        for (var i=0; i<data.carts.length; i++){
            $('.num_show_'+ data.carts[i].goods_id).val(data.carts[i].count);
            $('#price'+ data.carts[i].goods_id).html(data.carts[i].goods_price)
        }
    }
});


// 计算商品总价
function tatal_price() {
    $.get('/shopping/tatalprice/', function (data) {
        console.log(data);
        if (data.code == '200'){
            console.log(data)
            $('#tatal_price').html(data.tatal_price);
            $('#all_num').html(data.num);
            $('#all_num1').html(data.num)
        }
    })
}
tatal_price();











