$(document).ready(function () {
    $('.btn_top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 400);
        return false;
    });

    // 항상 버튼을 표시
    $('.btn_top').show();
});


// function showCancellationMessage() {
//     alert('취소되었습니다.');
// }

// // 예약 취소 버튼에 이벤트 리스너 추가
// document.addEventListener('DOMContentLoaded', function () {
//     const cancelButton = document.querySelector('.btn-cancel'); // 버튼 클래스 이름을 실제 사용하는 클래스로 변경

//     if (cancelButton) {
//         cancelButton.addEventListener('click', function (event) {
//             if (!confirm('정말 예약을 취소하시겠습니까?')) {
//                 event.preventDefault(); // 예약 취소 링크를 클릭한 경우 페이지 이동을 막음
//             } else {
//                 showCancellationMessage();
//             }
//         });
//     }
// });

function search_button_mylocation() {
}

function social_sign_in() {
    alert('준비중입니다');
}

function social_sign_up() {
    var userConfirmed = confirm('소셜 계정으로 회원가입 하시겠습니까?');

    if (userConfirmed) {
        alert('준비중입니다');
    }
}

// 비밀번호확인


function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username && !password) {
        alert("비밀번호를 입력해주세요.");
        return false; // 폼 제출 중지
    }
    return true;
}


function checkPasswordMatch() {
    var password = document.getElementById("password").value;
    var password_retype = document.getElementById("password-retype").value;
    var mismatchMessage = document.querySelector(".mismatch-message");

    if (password === password_retype) {
        mismatchMessage.style.display = "none";
    } else {
        mismatchMessage.style.display = "block";
    }
}


