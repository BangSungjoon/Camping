// $(document).ready(function() {
//     // 오류 메시지를 숨깁니다.
//     $(".messages .error").hide();

//     // 이전에 입력한 데이터 복원
//     restoreFormData();

//     document.getElementById("submit_button").addEventListener("click", function(event) {

//         // 폼 데이터 검증
//         var username = document.querySelector("input[name='username']").value;
//         var password = document.querySelector("input[name='password']").value;
//         var user_name = document.querySelector("input[name='user_name']").value;
//         var user_gender = document.querySelector("input[name='user_gender']:checked");
//         var user_tel = document.querySelector("input[name='user_tel']").value;
//         var email = document.querySelector("input[name='email']").value;
//         var formData = new FormData(document.querySelector('form'));

//         var usernameRegex = /^[a-zA-Z0-9]{4,12}$/;
//         var passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,12}$/;
//         // var telRegex = /^[0-9]+$/;
//         var emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
//         var password = document.querySelector("input[name='password']").value;


//         // if (!username.match(usernameRegex) || !password.match(passwordRegex) || password !== passwordConfirm || !user_name || !user_gender || !user_tel.match(telRegex) || !email.match(emailRegex)) {
//         // if (!username || !password || !user_name || !user_gender || !user_tel || !email || password !== passwordConfirm) {
//         if (!username.match(usernameRegex) || !password || !user_name || !user_gender || !user_tel || !email) {            
//             alert("필수 항목을 바르게 기입해주세요.");
//             event.preventDefault();
//         }
        
//         else if (!email.match(emailRegex)) {
//         alert("유효한 이메일 주소를 입력해주세요.");
//         event.preventDefault();

//         }else { 
//             // 유효한 데이터인 경우 폼 데이터를 저장
            
//             saveFormData();
//             alert("회원가입에 성공하였습니다. 캠핑어때를 선택해 주셔서 감사합니다!");

//         // ajax
//         $.ajax({
//             type: "POST",
//             url: "/users_app/sign_up.html",  // 올바른 URL 패턴으로 수정
//             data: formData,
//             processData: false,
//             contentType: false,
//             headers: { "X-CSRFToken": getCookie("csrftoken") },
//             success: function(response) {
//                     if (response.success) {
//                                 alert("회원 가입이 성공적으로 완료되었습니다.");
//                         window.location.href = "{% url 'sign_in' %}";
//                     } else {
//                         var errors = response.errors;
//                         var errorMessage = "회원 가입에 실패했습니다. 오류:\n";
//                         for (var field in errors) {
//                             errorMessage += field + ": " + errors[field].join(", ") + "\n";
//                         }
//                         alert(errorMessage);
//                     }
//                 },
//                     error: function(xhr, status, error) {
//                     alert("오류가 발생했습니다. 관리자에게 문의해주세요.\nStatus: " + status + "\nError: " + error);
//                 }
//             });
//         }
//     });

//     // 폼 데이터를 세션 스토리지에 저장하는 함수
//     function saveFormData() {
//         var formData = {
//             username: document.querySelector("input[name='username']").value,
//             password: document.querySelector("input[name='password']").value,
//             user_name: document.querySelector("input[name='user_name']").value,
//             user_gender: document.querySelector("input[name='user_gender']:checked").value,
//             user_tel: document.querySelector("input[name='user_tel']").value,
//             user_address: document.querySelector("input[name='user_address']").value,
//             email: document.querySelector("input[name='email']").value
//         };
//         sessionStorage.setItem("signupFormData", JSON.stringify(formData));
//     }

//     // 이전에 입력한 데이터를 세션 스토리지에서 복원하는 함수
//     function restoreFormData() {
//         var savedData = sessionStorage.getItem("signupFormData");
//         if (savedData) {
//             savedData = JSON.parse(savedData);
//             document.querySelector("input[name='username']").value = savedData.username;
//             document.querySelector("input[name='password']").value = savedData.password;
//             document.querySelector("input[name='user_name']").value = savedData.user_name;
//             document.querySelector("input[name='user_gender'][value='" + savedData.user_gender + "']").checked = true;
//             document.querySelector("input[name='user_tel']").value = savedData.user_tel;
//             document.querySelector("input[name='user_address']").value = savedData.user_address;
//             document.querySelector("input[name='email']").value = savedData.email;
//         }
//     }

//     // 페이지 이동 시 세션 데이터 초기화
//     window.onbeforeunload = clearFormData;
//     function clearFormData() {
//         sessionStorage.removeItem("signupFormData");
//     }
    
//     // 페이지 이동 시 세션 데이터 초기화
//     window.onbeforeunload = clearFormData;


//     // CSRF 토큰을 가져오기 위한 함수
//     function getCookie(name) {
//         var cookieValue = null;
//         if (document.cookie && document.cookie !== "") {
//             var cookies = document.cookie.split(";");
//             for (var i = 0; i < cookies.length; i++) {
//                 var cookie = cookies[i].trim();
//                 if (cookie.substring(0, name.length + 1) === name + "=") {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }
// });

// // 링크 클릭 이벤트 핸들러
// document.querySelector('#usertype_change a').addEventListener('click', function(event) {
//     // 링크 클릭 이벤트의 기본 동작(페이지 리디렉션) 막기
//     event.preventDefault();
    
//     // 경고 메시지 표시
//     alert('먼저 로그인해주세요.');

//     var signInURL = "/users/sign_in";  // 로그인 페이지 URL을 여기에 입력
//     window.location.href = signInURL;

// });
