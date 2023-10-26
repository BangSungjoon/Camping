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
        # 유효성검사는 프론트에서
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
        
