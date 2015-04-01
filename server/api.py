"""This module contains api preprocessors and the api configuration."""
from flask_restless import ProcessingException

from server.forms import RegistrationForm
from server.models import User, Keyword, Category, Event, Resource, HowTo
from server.logger import logger, logging


def log_post(data):
    """Log data of a POST."""
    logger.log(logging.INFO, data)


def validate_with_form(form_class):
    """Wrapper for form validating preprocessor."""
    def preprocessor(data=None):
        form = form_class.from_json(data)
        if not form.validate():
            raise ProcessingException

    return preprocessor


def remove_props(props):
    """Wrapper for preprocessor which removes specified props."""
    def preprocessor(data=None):
        for prop in props:
            del data[prop]

    return preprocessor


def login_required_preprocessor(data):
    """Ensure user is logged in via preprocessor."""
    if 'admin' not in data and data['admin'] == 'test':
        raise ProcessingException(
            description='Not Authorized',
            code=401
        )
    return True


api_config = [
    {
        'model': User,
        'methods': ['GET', 'POST', 'DELETE'],
        'preprocessors': {
            'POST': [
                validate_with_form(RegistrationForm),
                remove_props(['confirm'])
            ],
        }
    },
    {
        'model': Keyword,
        'methods': ['GET', 'POST', 'DELETE'],
        'preprocessors': {
            'POST': [login_required_preprocessor],
            'DELETE': [login_required_preprocessor]
        }
    },
    {
        'model': Category,
        'methods': ['GET', 'POST', 'DELETE'],
        'preprocessors': {
            'POST': [login_required_preprocessor],

        }
    },
    {
        'model': Event,
        'methods': ['GET', 'POST', 'DELETE', 'PATCH'],
        'preprocessors': {
            'PATCH_SINGLE': [
                login_required_preprocessor,
            ],
            'POST': [
                login_required_preprocessor,
            ],
            'DELETE': [
                login_required_preprocessor,
            ]

        },
        'include_columns': ['id',
                            'name',
                            'description',
                            'start',
                            'end',
                            'address',
                            'display_address',
                            'categories']
    },
    {
        'model': Resource,
        'methods': ['GET', 'POST', 'DELETE', 'PATCH'],
        'preprocessors': {
            'PATCH_SINGLE': [
                login_required_preprocessor,
            ],
            'POST': [
                login_required_preprocessor,
            ],
            'DELETE': [
                login_required_preprocessor,
            ]
        },
        'include_columns': ['id',
                            'title',
                            'resource',
                            'categories',
                            'keywords',
                            'howtos']
    },
    {
        'model': HowTo,
        'methods': ['GET', 'POST', 'DELETE', 'PATCH'],
        'preprocessors': {
            'PATCH_SINGLE': [
                login_required_preprocessor,
            ],
            'POST': [
                login_required_preprocessor,
            ],
            'DELETE': [
                login_required_preprocessor,
            ]
        },
        'include_columns': ['id',
                            'title',
                            'description',
                            'categories',
                            'steps',
                            'resources']
    }
]
