$(document).ready(function(){
    $('#get_data_btn').on('click', function(){

        $.ajax({
            url:"/product/get_data/",
            datatype:'json',
            success:function(result){
                console.log(result)
                console.log(result.name)
                // 반환된 결과를 받아서 result_box 에 출력
                $('#result_box').text(result.name)
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