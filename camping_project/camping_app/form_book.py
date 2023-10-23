from django import forms
from .models import Booking

# modelform 클래스 상속 받음
class bookcampingForm(forms.ModelForm):
    class Meta:
        model= Booking
        fields = (
            'book_no',
            'book_date',
            'stay_date',
            'camp_no',
            'id'
        )

        labels = {
            'book_no' : '예약번호',
            'book_date' : '예약한 날짜',
            'stay_date' : '거주날짜',
            'camp_no' : '캠핑장이름',
            'id' : '사용자id'
        }