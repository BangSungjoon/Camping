from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import UsersAppCompanyuser
from camping_app.models import UserInquire

class CompanyUserForm(forms.ModelForm):
    class Meta:
        model = UsersAppCompanyuser  # 또는 User, CompanyUser (사용하려는 모델 선택)
        fields = ['user_ptr_id', 'company_name', 'company_tel', 'company_address']
        
    
    
class InquireForm(forms.ModelForm):
    class Meta:
        model = UserInquire  # 또는 User, CompanyUser (사용하려는 모델 선택)
        fields = ['id', 'inq_date', 'inq_title', 'inq_content']
        
    
        
    # def __init__(self, user_instance, *args, **kwargs):
    #     super(CompanyUserForm, self).__init__(*args, **kwargs)
    #     self.fields['user_instance'] = forms.ModelChoiceField(
    #         queryset=user_instance,  # user_instance로 사용자 모델 인스턴스 전달
    #         widget=forms.HiddenInput()  # 숨긴 필드로 설정하거나 필요한 형태로 렌더링 가능
    #     )
 

