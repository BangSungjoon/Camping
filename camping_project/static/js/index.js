function updateSubregions() {
  var regionSelect = document.getElementById("c_do");
  var subregionSelect = document.getElementById("c_signgu");
  subregionSelect.innerHTML = ''; // 서브지역 목록 초기화

  var region = regionSelect.value;

  var option = document.createElement("option");
  option.value = "";
  option.text = "전체/시/군";
  subregionSelect.add(option);

  // 각 지역에 따른 서브지역 옵션을 동적으로 생성
  if (region === "서울") {
      var seoulSubregions = ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"];
      for (var i = 0; i < seoulSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = seoulSubregions[i];
          option.text = seoulSubregions[i];
          subregionSelect.add(option);
      }
  } else if (region === "부산") {
      var busanSubregions = ["강서구", "금정구", "기장군", "남구", "동구", "동래구", "부산진구", "북구", "사상구", "사하구", "서구", "수영구", "연제구", "영도구", "중구", "해운대구"];
      for (var i = 0; i < busanSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = busanSubregions[i];
          option.text = busanSubregions[i];
          subregionSelect.add(option);
      }
    } else if (region === "대구") {
      var daeguSubregions = ["남구","달서구","달성군","동구","북구","상주","서구","수성구","중구","군위군"];
      for (var i = 0; i < daeguSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = daeguSubregions[i];
          option.text = daeguSubregions[i];
          subregionSelect.add(option);
      }
    
  } else if (region === "인천") {
      var incheonSubregions = ["강화군","계양구","남구","남동구","동구","부평구","서구","연수구","옹진군","중구"];
      for (var i = 0; i < incheonSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = incheonSubregions[i];
          option.text = incheonSubregions[i];
          subregionSelect.add(option);
      }
    
  } else if (region === "광주") {
      var gwangjuSubregions = ["광산구","남구","동구","북구","서구"];
      for (var i = 0; i < gwangjuSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = gwangjuSubregions[i];
          option.text = gwangjuSubregions[i];
          subregionSelect.add(option);
      }
    
  } else if (region === "대전") {
      var daejeonSubregions = ["대덕구","동구","서구","유성구","중구"];
      for (var i = 0; i < daejeonSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = daejeonSubregions[i];
          option.text = daejeonSubregions[i];
          subregionSelect.add(option);
      }
    
  } else if (region === "울산") {
      var ulsanSubregions = ["남구","동구","북구","울주군","중구"];
      for (var i = 0; i < ulsanSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = ulsanSubregions[i];
          option.text = ulsanSubregions[i];
          subregionSelect.add(option);
      }
    
  } else if (region === "세종") {
      var sejongSubregions = ["금남면","세종시","소정면","연서면","전동면"];
      for (var i = 0; i < sejongSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = sejongSubregions[i];
          option.text = sejongSubregions[i];
          subregionSelect.add(option);
      }
    
  } else if (region === "경기") {
      var gyeonggiSubregions = ["가평군","고양시","과천시","광명시","광주시","구리시","군포시","김포시","남양주시","동두천시","부천시","성남시","수원시","시흥시","안산시","안성시","안양시","양주시","양평군","여주시","연천군","오산시","용인시","의왕시","의정부시","이천시","파주시","평택시","포천시","하남시","화성시"];
      for (var i = 0; i < gyeonggiSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = gyeonggiSubregions[i];
          option.text = gyeonggiSubregions[i];
          subregionSelect.add(option);
      }
  } else if (region === "강원") {
      var gangwonSubregions = ["강릉시","고성군","동해시","삼척시","속초시","양구군","양양군","영월군","원주시","인제군","정선군","철원군","춘천시","태백시","평창군","홍천군","화천군","횡성군"];
      for (var i = 0; i < gangwonSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = gangwonSubregions[i];
          option.text = gangwonSubregions[i];
          subregionSelect.add(option);
      }
    
  } else if (region === "충북") {
      var chungbukSubregions = ["괴산군","단양군","보은군","영동군","옥천군","음성군","제천시","증평군","진천군","청원군","청주시","충주시"];
      for (var i = 0; i < chungbukSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = chungbukSubregions[i];
          option.text = chungbukSubregions[i];
          subregionSelect.add(option);
      }
    
  } else if (region === "충남") {
      var chungnamSubregions = ["계룡시","공주시","금산군","논산시","당진시","보령시","부여군","서산시","아산시","예산군","천안시","청양군","태안군","홍선군"];
      for (var i = 0; i < chungnamSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = chungnamSubregions[i];
          option.text = chungnamSubregions[i];
          subregionSelect.add(option);
      }
    
  } else if (region === "전북") {
      var jeonbukSubregions = ["고창군","군산시","김제시","남원시","무주군","부안군","순창군","완주군","익산시","임실군","장수군","전주시","정읍시","진안군"];
      for (var i = 0; i < jeonbukSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = jeonbukSubregions[i];
          option.text = jeonbukSubregions[i];
          subregionSelect.add(option);
      }
    
  }else if (region === "전남") {
      var jeonnamSubregions = ["강진군","고흥군","곡성군","광양시","구례군","나주시","담양군","목포시","무안군","보성군","순천시","신안군","여수시","영광군","영암군","완도군","장성군","장흥군","진도군","함평군","해남군","화순군"];
      for (var i = 0; i < jeonnamSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = jeonnamSubregions[i];
          option.text = jeonnamSubregions[i];
          subregionSelect.add(option);
      }
    
  }else if (region === "경북") {
      var gyeongbukSubregions = ["경산시","경주시","고령군","구미시","김천시","문경시","봉화군","상주시","성주군","안동시","영덕군","영양군","영주시","영천시","예천군","울릉군","울진군","의성군","청도군","청송군","칠곡군","포항시"];
      for (var i = 0; i < gyeongbukSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = gyeongbukSubregions[i];
          option.text = gyeongbukSubregions[i];
          subregionSelect.add(option);
      }
    
  }else if (region === "경남") {
      var gyeongnamSubregions = ["거제시","거창군","고성군","김해시","남해군","밀양시","사천시","산청군","양산시","의령군","진주시","창년군","창원시","통영시","하동군","함안군","함양군","합천군"];
      for (var i = 0; i < gyeongnamSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = gyeongnamSubregions[i];
          option.text = gyeongnamSubregions[i];
          subregionSelect.add(option);
      }
    
  }else if (region === "제주") {
      var jejuSubregions = ["서귀포시","제주시"];
      for (var i = 0; i < jejuSubregions.length; i++) {
          var option = document.createElement("option");
          option.value = jejuSubregions[i];
          option.text = jejuSubregions[i];
          subregionSelect.add(option);
      }
    
  }
}

// 페이지 로드시 서브지역 목록 초기화
updateSubregions();