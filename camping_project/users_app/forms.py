from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import CompanyUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'user_name', 'user_age', 'user_gender', 'user_tel', 'user_address', 'email', 'user_subscribe_sms', 'user_subscribe_email']
        
        email = forms.EmailField(
            required=True,
            error_messages={'required': '이메일 주소를 입력해주세요.', 'invalid': '올바른 이메일 주소를 입력해주세요.'}
        )

        user_tel = forms.CharField(
            validators=[RegexValidator(
                regex=r'^[0-9]+$',
                message='숫자만 입력해주세요.'
            )]
        )
    user_address = forms.CharField(required=False)
    user_age = forms.CharField(required=False)
    
    def clean_user_age(self):
        user_age = self.cleaned_data['user_age']
        if user_age == '':
            return None
        if user_age is not None and not isinstance(user_age, int):
            try:
                user_age = int(user_age)
            except ValueError:
                raise ValidationError("생년월일을 숫자로 입력하세요.")
        return user_age



# class ChangeCompany(UserCreationForm):
  
#     class Meta:
#         model = CompanyUser
#         fields = ['company_name', 'company_tel', 'company_address']

#         company_tel = forms.CharField(
#             validators=[RegexValidator(
#                 regex=r'^[0-9]+$',
#                 message='숫자만 입력해주세요.'
#             )]
#         )
#         company_address = forms.CharField(required=False)
        

class CompanyUserForm(forms.ModelForm):
    class Meta:
        model = CompanyUser  # 또는 User, CompanyUser (사용하려는 모델 선택)
        fields = ['company_name', 'company_tel', 'company_address']

    def __init__(self, user_instance, *args, **kwargs):
        super(CompanyUserForm, self).__init__(*args, **kwargs)
        self.fields['user_instance'] = forms.ModelChoiceField(
            queryset=user_instance,  # user_instance로 사용자 모델 인스턴스 전달
            widget=forms.HiddenInput()  # 숨긴 필드로 설정하거나 필요한 형태로 렌더링 가능
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'user_age', 'user_gender', 'user_tel', 'user_address', 'email', 'user_subscribe_sms', 'user_subscribe_email']
        
        
