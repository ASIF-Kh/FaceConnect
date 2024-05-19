import os
from .settings import BASE_DIR

STATIC_URL = 'static/'
MEDIA_URL = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = '/var/www/faceConnect/static'
MEDIA_ROOT = '/var/www/faceConnect/media'

# #CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", "*")
# #CSP_FRAME_ANCESTORS = ("'self'", '*')
# #DEBUG = False
# X_FRAME_OPTIONS = 'ALLOWALL'
# SESSION_COOKIE_SAMESITE = 'None'
# SESSION_COOKIE_SECURE = True
# #SESSION_COOKIE_DOMAIN = 'localhost:9001'
# CSRF_COOKIE_SAMESITE = 'None'
# CSRF_COOKIE_SECURE = True
# #CSRF_COOKIE_DOMAIN = '.localhost'

# # REST FRAMEWORKs DEFAULT SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        # 'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'OPTIONS': {
        'context_processors': [
            'social_django.context_processors.backends',
            'social_django.context_processors.login_redirect',
        ],
    },
}


# # OAuth2 Backends
AUTHENTICATION_BACKENDS = (
    # Facebook OAuth2
    # 'social_core.backends.facebook.FacebookAppOAuth2',
    # 'social_core.backends.facebook.FacebookOAuth2',
    # Google OAuth2
    # 'social_core.backends.google.GoogleOAuth2',
    # # Apple OAuth
    # 'social_core.backends.apple.AppleIdAuth',

    # django-rest-framework-social-oauth2
    # 'rest_framework_social_oauth2.backends.DjangoOAuth2',

    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

############################################################################################################
AWS_ACCESS_KEY_ID = "" # TODO
AWS_SECRET_ACCESS_KEY = "" # TODO
AWS_STORAGE_BUCKET_NAME = "face-connect"
AWS_S3_REGION_NAME = "ap-south-1"
############################################################################################################


AWS_S3_SIGNATURE_VERSION = "s3v4"
# AWS_DEFAULT_ACL = None
# AWS_S3_VERIFY = True

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

#AWS_STATIC_LOCATION = 'static'
#STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'faceConnect.storage_backends.PublicMediaStorage'


AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
PRIVATE_FILE_STORAGE = 'faceConnect.storage_backends.PrivateMediaStorage'

############################################################################################################
DEFAULT_FROM_EMAIL = 'feignbird@gmail.com'
DEFAULT_TO_EMAIL = ""
############################################################################################################
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'feignbird@gmail.com'
EMAIL_HOST_PASSWORD = '' # TODO
EMAIL_USE_TLS = True
############################################################################################################


############################################################################################################
# For Payment purposes
STRIPE_PUBLIC_KEY = ""
STRIPE_SECRET_KEY = ""
############################################################################################################



############################################################################################################
# Facebook Social Login (OAUTH2)
SOCIAL_AUTH_FACEBOOK_KEY = ""
SOCIAL_AUTH_FACEBOOK_SECRET = ""
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
############################################################################################################


############################################################################################################
# Google Social Login (OAUTH2)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ""
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ""
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]
############################################################################################################


GOOGLE_MAPS_API_KEY = ""



############################################################################################################
# Apple Social Login (OAUTH2)
SOCIAL_AUTH_APPLE_ID_CLIENT = ""
SOCIAL_AUTH_APPLE_ID_TEAM = ""
SOCIAL_AUTH_APPLE_ID_KEY = ""
SOCIAL_AUTH_APPLE_ID_SECRET = ""
SOCIAL_AUTH_APPLE_ID_SCOPE = ['email', 'name']
SOCIAL_AUTH_APPLE_ID_EMAIL_AS_USERNAME = True
############################################################################################################



SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    # also not updating user with any new details
    # 'social_core.pipeline.user.user_details',
)


CRONJOBS = [
    # ('0 0 * * *', 'somewhere.somewhere.something')  # runs every day
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:*', ] #'https://sub-domain.domain-name.top-domain'
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST =  ['https://localhost:8000', 'http://localhost:8000']
#CSRF_TRUSTED_ORIGINS = []
#CORS_ORIGIN_WHITELIST = []

# DATE_IO_FORMAT = "%a %b %d %Y"
# OTP_TIMEOUT = 60*10 # 600 seconds or 10 minutes
# MAX_OTP_RESEND_COUNT = 3
# RESEND_EXCEED_WAIT_TIME = 60*60*2 # 7200 seconds or 2 hours
# IMAGE_CLARITY_THRESHOLD = 2900 # Threshold for image quality checking
# TESSERACT_CMD = '/usr/bin/tesseract'


