from typing import Tuple

from django.utils.translation import gettext_lazy as _

# def locale_path_for_app(app: str) -> str:
#     return join(
#         dirname(dirname(dirname(abspath(__file__)))), f'{app}/locale'
#     )


DEFAULT_LOCALE_PATHS: Tuple = ()
DEFAULT_LANGUAGES: Tuple = (
    ('en', _('English')), ('ru', _('Russian')), ('kz', _('Kazakh')),
)
