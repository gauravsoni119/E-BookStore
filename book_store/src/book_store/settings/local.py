'''
Created on Jan 16, 2016

@author: Gaurav
'''
import os
from .base import *

SECRET_KEY = get_env_variable("SECRET_KEY")

DEBUG = True

TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "bookstore",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "",
        "PORT": ""
                }
             }

INSTALLED_APPS += 'rest_framework_docs', 'rest_framework_swagger',

INTERNAL_IPS = ("127.0.0.1",)

REST_FRAMEWORK_DOCS = {
    'HIDDEN': True
}