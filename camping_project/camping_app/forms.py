from django import forms
from .models import CampMemeberInfo

class CampingForm(forms.ModelForm):
    class Meta:
        model = CampMemeberInfo
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
            'camp_itd',
            'id',
            'approve'
            )
