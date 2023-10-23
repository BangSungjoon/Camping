DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # 엔진
        "NAME": "camping_db",  # 데이터베이스 이름
        "USER": "root",  # 사용자
        "PASSWORD": "1234",  # 비밀번호
        "HOST": "localhost",  # 호스트
        "PORT": "3306",  # 포트번호
    }
}

SECRET_KEY = 'django-insecure-^e$^ca+kv-2w%(opj)za*vec7o-6&w@eg&p^(z=$!%4$hg)34g'
