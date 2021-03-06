# -*- coding: utf-8 -*-
"""
    config
    ~~~~~~

    Configurations for the web server.

    :copyright: (c) 2017-18 by Wendell Hu.
    :license: MIT, see LICENSE for more details.
"""

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

from shared.config import PROD_DB_URI, DEV_SECRET_KEY, DEV_DB_URI, TEST_DB_URI, PROD_SECRET_KEY


class Config(object):
    #: security & authentication
    AUTH_SECRET_KEY = PROD_SECRET_KEY or DEV_SECRET_KEY
    AUTH_TOKEN_EXPIRE = 3600 * 24 * 30 * 6  #: half a year

    #: if true, all user would be recognized as authenticated
    LOGIN_DISABLED = False

    #: database
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_PROFILER_ENABLED = True

    #: error
    ERROR_404_HELP = False  #: suppress default 404 error message


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DEV_DB_URI


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = TEST_DB_URI


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = PROD_DB_URI


configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
