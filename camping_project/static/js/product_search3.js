$(document).ready(function(){
    $('#prdSearchFrm3').on('submit', function(){
        event.preventDefault();
        
        let formData = $(this).serialize();

        $.ajax({
            type:"post",
            // url:"/product/search2/",
            url:"http://127.0.0.1:8000/product/search3/",
            data:formData,
            datatype:'json',
            success:function(result){
                $('#searchResultBox').html(result);
            },
            error:function(){
                // 오류 발생 시 수행되는 함수
                alert("오류 발생")
            },
            complete:function(){
                // 완료 되었을 때 수행된 함수
            }
        });

    })
});