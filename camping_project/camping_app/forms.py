from django import forms
from .models import Camping

class CampingForm(forms.ModelForm):
    class Meta:
        model = Camping
        fields = (
            'cam_name',
            'cam_address',
            'cam_tel',
            'cam_env',
            'cam_type',
            'cam_period',
            'cam_day',
            )

        labels = {
            'cam_name': '캠핑장 이름',

            'cam_address':'주소',
            'cam_tel':"전화번호",
            'cam_env':"캠핑장 환경",
            'cam_type':"캠핑장 유형",
            'cam_period':"운영기간",
            'cam_day':"운영일"
        }
        