function addgoods(id) {
    // alert(id)
    console.log(id)
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/shopping/addgoods/',
        type: 'POST',
        data: {'goods_id': id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success:function (data) {
            alert('请求成功')
        },
        error:function (data) {
            alert('请求失败')
        }
    })
}
