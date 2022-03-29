$(function(){

    $(".next").on('click',function(){
        $(".booking-3rd").hide()
        $(".booking-4th").show()
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
    //datas.find((obj)=>obj.name=='json').value="true"
    $.ajax({
        url:"http://127.0.0.1:8000/api/Booking/",
        method:"post",
        data:datas,
        success: function(res){
            console.log('ajax result:')
            console.log(res)
            let sex = (res.sex = true)?'先生':'小姐'
            let date = `${res.date.substr(4,6)} / ${res.date.substr(6,8)}`
            let time = (res.time = 1)?'午餐時段':'晚餐時段'
            let message = `${res.name} ${sex} <br>
                您在 ${date} ${time}<br> 
                預訂了 ${res.number} 位用餐<br>
                預約的餐點為：<br>
                牛排 ${res.steak} 份、魚排 ${res.fish} 份、雞排 ${res.chicken} 份<br>
                已預約成功
                `
            $(".booking-4th").hide()
            $(".booking-success").html(message).show()
        }
    })
    }
})