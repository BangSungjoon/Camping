from django import forms
from .models import CampReview

# modelform 클래스 상속 받음
class campreviewform(forms.ModelForm):
    class Meta:
        model= CampReview
        fields = (
            'review_no',
            'rev_title',
            'rev_content',
            'rev_date',
            'rev_rate',
            'id',
            'camp_no'
        )

        labels = {
            'review_no' : '리뷰번호',
            'rev_title' : '제목',
            'rev_content' : '리뷰 내용',
            'rev_date' : '리뷰날짜',
            'rev_rate' : '평점',
            'id' : '사용자id',
            'camp_no' : '캠핑장이름'
        }