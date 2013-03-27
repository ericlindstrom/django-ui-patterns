django-ui-patterns
==================

Django version of pea.rs

Install via pip:
    pip install -e git+git://github.com/ericlindstrom/django-ui-patterns.git#egg=django-ui-patterns

Add `ui_patterns` to `INSTALLED_APPS`

`settings.py`

    INSTALLED_APPS = (
        ...
        'ui_patterns',
    )

`urls.py`

    url(r'^pattern/', include('ui_patterns.urls', namespace='pattern')),
