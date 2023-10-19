// slideShow.js

// 축약 형태
$(function() {
    // 이동한 이미지의 index 값을 저장하기 위한 변수 (현재 위치)
    let movedIndex  = 0;

    // 슬라이드 패널을 움직이는 함수
    function moveSlide(index) {
        // 전달 받은 index 값을 현재 위치 변수에 저장
        movedIndex = index;

        // 슬라이드 이동
        let moveLeft = -(index * 1280); // 왼쪽으로 이동 거리
        $('#slidePanel').animate({'left': moveLeft}, 'slow');
    }

    // prevButton 클릭했을 때 
    $('#prevButton').on('click', function() {
        if(movedIndex != 0) {
            movedIndex = movedIndex - 1;
        }

        moveSlide(movedIndex);        
    });

    // nextButton 클릭했을 때 
    $('#nextButton').on('click', function() {
        if(movedIndex != 3) {
            movedIndex = movedIndex + 1;
        }

        moveSlide(movedIndex);        
    });

    // 초기 슬라이드 이미지 랜덤하게 출력
    let randomNum = Math.floor(Math.random() * 4);
    moveSlide(randomNum);   

}); 