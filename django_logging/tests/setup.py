import django
from django.conf import settings


def configure_django_settings() -> None:
    if not settings.configured:
        settings.configure(
            DEBUG=True,
            DATABASES={
                "default": {
                    "ENGINE": "django.db.backends.sqlite3",
                    "NAME": ":memory:",
                }
            },
            INSTALLED_APPS=[
                "django.contrib.contenttypes",
                "django.contrib.auth",
                "django_logging",
            ],
            MIDDLEWARE=[],
            TEMPLATES=[
                {
                    "BACKEND": "django.template.backends.django.DjangoTemplates",
                    "DIRS": [],
                    "APP_DIRS": True,
                    "OPTIONS": {
                        "context_processors": [
                            "django.template.context_processors.debug",
                            "django.template.context_processors.request",
                            "django.contrib.auth.context_processors.auth",
                            "django.contrib.messages.context_processors.messages",
                        ],
                    },
                },
            ],
            DJANGO_LOGGING={
                "AUTO_INITIALIZATION_ENABLE": True,
                "INITIALIZATION_MESSAGE_ENABLE": True,
                "LOG_FILE_LEVELS": ["DEBUG", "INFO"],
                "LOG_DIR": "logs",
                "LOG_FILE_FORMATS": {
                    "DEBUG": 1,
                    "INFO": 1,
                },
                "LOG_FILE_FORMAT_TYPES": {
                    "DEBUG": "JSON",
                },
                "EXTRA_LOG_FILES": {
                    "DEBUG": True,
                },
                "LOG_CONSOLE_LEVEL": "DEBUG",
                "LOG_CONSOLE_FORMAT": 1,
                "LOG_CONSOLE_COLORIZE": True,
                "LOG_DATE_FORMAT": "%Y-%m-%d %H:%M:%S",
                "LOG_EMAIL_NOTIFIER": {
                    "ENABLE": False,
                    "NOTIFY_ERROR": True,
                    "NOTIFY_CRITICAL": False,
                    "LOG_FORMAT": True,
                    "USE_TEMPLATE": True,
                },
            },
            EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend",
            EMAIL_HOST="smtp.example.com",
            EMAIL_PORT=587,
            EMAIL_USE_TLS=True,
            EMAIL_HOST_USER="example@test.com",
            EMAIL_HOST_PASSWORD="the_password",
            DEFAULT_FROM_EMAIL="example@test.com",
            ADMIN_EMAIL="admin@test.com",
            LANGUAGE_CODE="en-us",
            TIME_ZONE="UTC",
            USE_I18N=True,
            USE_TZ=True,
        )
        django.setup()
