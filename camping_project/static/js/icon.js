
      window.onload = function() {
      function clip(){
        var url = '';
        var textarea = document.createElement("textarea");
        document.body.appendChild(textarea);
        url = window.document.location.href;
        textarea.value = url;
        textarea.select();
        document.execCommand("copy");
        document.body.removeChild(textarea);
        alert("URL이 복사되었습니다.")
      };
    // "camp_item_box" 클래스 하위에 있는 li 요소를 가져옵니다.
    var listItems = document.querySelectorAll(".camp_item_g li i");
    // 각 li 요소에 대한 반복문
    listItems.forEach(function (i) {
        var text = i.textContent.trim(); // 텍스트 내용 가져오기 (앞뒤 공백 제거)
        switch (text) {
            case "전기":
                i.className = "ico_volt";
                break;
            case "와이파이":
                i.className = "ico_wifi";
                break;
            case "장작판매":
                i.className = "ico_wood";
                break;
            case "온수":
                i.className = "ico_hotwater";
                break;
            case "물놀이장":
                i.className = "ico_pool";
                break;
            case "놀이터":
                i.className = "ico_playzone";
                break;
            case "운동시설":
                i.className = "ico_ico_sports";
                break;
            case "운동장":
                i.className = "ico_ground";
                break;
            case "산책로":
                i.className = "ico_walk";
                break;
            case "마트.편의점":
                i.className = "ico_mart";
                break;
            case "트렘폴린":
                i.className = "ico_ico_ico_tramp";
                break;
            default:
                // 기본 클래스 설정 (매칭되는 것이 없을 경우)
                i.className = "ico_tramp";
                break;
        }
    });
};