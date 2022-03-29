$(function(){

    $(".nextto2").on('click',function(){
        $(".booking-1st").hide()
        $(".booking-2nd").show()
    })

    $(".nextto4").on('click',function(){
        $(".booking-3rd").hide()
        $(".booking-4th").show()
    })

    $(".nextto5").on('click',function(){
        $(".booking-4th").hide()
        $(".booking-5th").show()
    })

    $("label.radio").on('click',function(){
        $(this).addClass("action").find("input").prop('checked',true).end().siblings().removeClass("action")
    })


    // 設置AJAX送出,使用preventDefault
    $(".AJAXbtn").click(function(evt){
        evt.preventDefault()
        console.log("ajax送出")
        post()
    })
    // 打包表單資料
    function post(){
    var datas = $("form").serializeArray()
    $.ajax({
        url:"http://127.0.0.1:8000/api/Booking/",
        method:"post",
        data:datas,
        success: function(res){
            console.log('ajax result:')
            console.log(res)
            let sex = (res.sex == true)?'先生':'小姐'
            let date = `${res.date.substring(4,6)}/${res.date.substring(6,8)}`
            let time = (res.time == 1)?'午餐時段':'晚餐時段'
            let message = `${res.name} ${sex} <br>
                您在 <span>${date}</span> ${time}<br> 
                預訂了 <span>${res.number}</span> 位用餐<br>
                預約的餐點為：<br>
                牛排 <span>${res.steak}</span> 份、魚排 <span>${res.fish}</span> 份、雞排 <span>${res.chicken}</span> 份<br>
                <h2>已預約成功</h2>
                `
            $(".booking-5th").hide()
            $(".booking-success").html(message).show()
        }
    })
    }
})