$(document).ready(function(){
    $('.camp_introduce').on('click', function(event){
        event.preventDefault();

        camp_no = document.getElementById('camp_no').value;

        $.ajax({
            type:'get',
            url : "/camping/detail_intro/" + camp_no,
            // data : {'camp_no':7},
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

    $('.camp_guide').on('click', function(event){
        event.preventDefault();

        camp_no = document.getElementById('camp_no').value;

        $.ajax({
            type:'get',
            url : "/camping/detail_text/" + camp_no,
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