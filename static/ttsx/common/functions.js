// 增加商品数量
function addgoods(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
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
            console.log(data)
        },
        error:function (data) {
            alert('请求失败')
        }
    })
}

