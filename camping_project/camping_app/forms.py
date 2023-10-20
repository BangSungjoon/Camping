from django import forms
from .models import CampInfo

class CampingForm(forms.ModelForm):
    class Meta:
        model = CampInfo
        fields = (
            'camp_name',
            'camp_s_tt',
            'camp_tag_li',
            'camp_address',
            'camp_call',
            'camp_environment',
            'camp_type',
            'camp_ope_period',
            'camp_ope_day',
            'camp_pagelink',
            'camp_book',
            'camp_itd'
            )

        labels = {
            'camp_name': '캠핑장 이름',
            'camp_s_tt': '한줄 소개',
            'camp_tag_li': '태그를 적어주세요',
            'camp_address': '주소를 적어주세요',
            'camp_call': '전화번호',
            'camp_environment': '주변 환경',
            'camp_type': '캠핑장 타입',
            'camp_ope_period': '운영 계절',
            'camp_ope_day': '운영 요일',
            'camp_pagelink': '홈페이지',
            'camp_book': '예약 방식',
            'camp_itd': '상세 소개'
        }
        