
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
                    <h3>已預約成功</h3>
                    `
                $(".booking-5th").hide()
                $(".booking-success").html(message).show()
                getBooking()
            }
        })
    }
    
    function getBooking(){
        var datas = $("form").serializeArray()
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/api/Booking/", 
            success: function(result){
                //console.log(result)
                html = ``
                for(item of result){
                    //console.log(item)
                    let date = `${item.date.substring(4,6)}/${item.date.substring(6,8)}`
                    let time = (item.time == 1)?'午餐時段':'晚餐時段'
                    li = `
                    <li>
                        <span>${item.mobile.substring(0,4)}OOO${item.mobile.substring(7,10)}</span>
                        預訂了 ${date} ${time} ${item.number} 席
                    </li>
                    `
                    html += li
                }
                $("ul").html(html)

                var result2 = $.map(result, function(item, index) {
                    return item.mobile;
                  }).indexOf('0987654321');

                console.log(result[result2])
                searchResult(result)
            }
        });
    }
    getBooking()
    function searchResult(result){
        $(".goto-search").on('click',function(){
            let key = $(".search").val()
            let arr = $.map(result, function(item, index) {
                return item.mobile;
            })
            list = []
            let i = arr.indexOf(key)
            while(i >= 0) {
                console.log(i)
                list.push(i);
                i = arr.indexOf(key, i+1);
            }
            console.log(list)
            html=``
            if(list.length==0){
                $("ul").html(`<li><span>${key}</span> 沒有訂位資料</li>`)
                return
            }
            for(let j=0;j<list.length;j++){
                item = result[list[j]]
                console.log(j)
                let date = `${item.date.substring(4,6)}/${item.date.substring(6,8)}`
                let time = (item.time == 1)?'午餐時段':'晚餐時段'
                li = `
                    <li>
                        <span>${item.mobile}</span>
                        預訂了 ${date} ${time} ${item.number} 席
                    </li>
                `
                html+=li
            }
            $("ul").html(html)
        })
    }
})