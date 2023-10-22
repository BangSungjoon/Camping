$(document).ready(function(){
    $('.camp_introduce').on('click', function(event){
        event.preventDefault();

        $.ajax({
            url: "{% url 'detail_intro' camping.camp_no %}",  // URL 패턴의 이름을 사용하여 URL을 생성
            dataType: 'html',
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