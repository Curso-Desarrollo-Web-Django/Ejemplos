from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-4)md*v0ia-)r!d9pn-=0a)6k6#j!sa!+*@g7g-rwyq_y=#3ns4'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',             # App del panel de administración.
    'django.contrib.auth',              # App para manejar usuarios.
    'django.contrib.contenttypes',      # App para manejar tipos de contenido.
    'django.contrib.sessions',          # App para manejar sesiones.
    'django.contrib.messages',          # App para mensajes entre requests.
    'django.contrib.staticfiles',       # App para archivos estáticos (CSS, JS).
    
    # ✏️ MODIFICACIÓN: Agregamos nuestra primera app al proyecto.
    # ➕ AGREGADO: La app 'productos' nos va a permitir gestionar
    #   todo lo relacionado con los artículos a facturar.
    'productos',
]

# ============================================================ #
# 🧉 EXPLICACIÓN: Al incluir 'productos' en INSTALLED_APPS,
# Django reconoce oficialmente a nuestra app. Ahora cuando
# hagamos migraciones, va a buscar models.py dentro de
# la carpeta productos y creará las tablas correspondientes.
# Además, si definimos algo en admin.py, aparecerá en el panel.
# ============================================================ #


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'FACTURACION.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'FACTURACION.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ✏️MODIFICACIÓN: Cambio de idioma a Español Argentina 🧉
# Original: LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-ar'

# ✏️MODIFICACIÓN: Ajuste de zona horaria a Argentina 🕒
# Original: TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Argentina/Buenos_Aires'


USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'


# ========================================================== #
# 🧉 EXPLICACIÓN: Con estos cambios, logramos que el sistema
# hable en nuestro idioma y respete nuestro horario.
# Fundamental para un sistema de facturación argentino.
# ========================================================== #