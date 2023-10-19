$(document).ready(function(){
    $('#prdSearchFrm2').on('submit', function(){
        event.preventDefault();
        
        let formData = $(this).serialize();
        $.ajax({
            type:"post",
            // url:"/product/search2/",
            url:"http://127.0.0.1:8000/product/search2/",
            data:formData,
            datatype:'json',
            success:function(result){
                let prd_list = result.prd_list_json;
                $('#searchResultBox').empty()
                const str = `
                    <table id="prd_list">
                    <tr>
                        <th>상품번호</th>
                        <th>상품명</th>
                        <th>가격</th>
                        <th>제조회사</th>
                        <th>색상</th>
                        <th>카테고리번호</th>
                    </tr>
                `

                $('#searchResultBox').append(str);
                // 데이터 추출해서 append 
                if(prd_list.length == 0){
                    $('#prd_list').append('<tr align="center"><td colspan="6">검색결과가 없습니다</td></tr>')
                } else {
                    for(let i=0; i<prd_list.length; i++){
                        $('#prd_list').append('<tr><td>' +
                            prd_list[i].pk + '</td><td>' +
                            prd_list[i].fields.prd_name + '</td><td>' +
                            prd_list[i].fields.prd_price + '</td><td>' +
                            prd_list[i].fields.prd_maker + '</td><td>' +
                            prd_list[i].fields.prd_color + '</td><td>' +
                            prd_list[i].fields.ctg_no + '</td></tr>');                        
                    }
                }

                $('#prd_list').append('</table>');
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
