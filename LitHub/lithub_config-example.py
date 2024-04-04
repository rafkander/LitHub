# The root directory of your this Django application
# manage.py, settings.py, lithub_config.py, etc should be
# in this directory. Don't forget the trailing slash / at 
# the end of the path.
LITHUB_ROOT = "/home/path/to/your/project/root/directory/LitHub/"

# There are various ways to test/use email. Instructions at
# https://docs.djangoproject.com/en/1.3/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/home/path/to/store/emails/for/debug/'

# To be used by django-registration for registration
ACCOUNT_ACTIVATION_DAYS = 7
DEFAULT_FROM_EMAIL="test <test@example.com>"

# For FB integration
FB_APP_ID='12345'
FB_APP_NAMESPACE='lithub-example'
FB_APP_SECRET='67890'
FB_REDIRECT_URL = "http://example.com"

# For the Google Books API - uncomment and edit 
# (Note: if you don't have one, do not uncomment)
# GOOGLE_API_KEY = "abcd"

# This allows facebook to become a valid authentication system
# Remove this if the fbconnect application is not being used
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'fbconnect.auth_backends.FBAuthentication',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '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'

# Configure the database (see Django documentation for more details)
# For testing environments, leave as is.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': LITHUB_ROOT+'database.sqlite3',   # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

