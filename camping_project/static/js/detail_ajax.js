$(document).ready(function(){
    $('.camp_introduce').on('click', function(event){
        event.preventDefault();

        $.ajax({
            type:'get',
            url : "/camping/detail_intro/",
            // dataType: 'html',
            success: function(result){
                $('#resultbox').html(result); 
            },
            error: function(){
                // 오류 발생 시 수행되는 함수
                alert('오류 발생');
            },
            complete: function(){
                // 완료 되었을 때 수행된 함수
            }
        });
    });
});