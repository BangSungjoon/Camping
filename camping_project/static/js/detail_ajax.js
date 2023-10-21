$(document).ready(function(){
    $('.camp_introduce').on('click', function(event){
        event.preventDefault(); // 기본 링크 동작을 막습니다.

        // AJAX 요청을 수행하여 "detail_intro.html" 파일의 내용을 가져오기
        $.ajax({
            url: 'detail_intro.html', // 파일의 경로를 수정하세요.
            dataType: 'html',
            success: function(result){
                $('#resultbox').html(result); // 결과를 resultbox에 삽입
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