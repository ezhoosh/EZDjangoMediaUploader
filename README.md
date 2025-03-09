<h1 align="center">EZDjangoMediaUploader</h1>

<p align="center">
    <img src="https://raw.githubusercontent.com/inventare/django-image-uploader-widget/main/docs/_images/behaviour_inline.gif" />
</p>

<p align="center">
    <img alt="Supported Python Versions" src="https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue" />
    <img alt="Supported Django Versions" src="https://img.shields.io/badge/Django-4.2%20|%205.0%20|%205.1-blue" />
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/django-media-uploader-widget" />
    <img alt="GitHub License" src="https://img.shields.io/github/license/ali-hv/django-media-uploader-widget" />
    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/django-media-uploader-widget" />
</p>

## Introduction

`django-media-uploader-widget` provides a beautiful media uploader widget for **django** and a multiple media file inline editor for **django-admin**. It supports images, videos, and audio files with preview capabilities in the django admin panel.

## Requirements

- Python 3.8+
- Django 4.2+

## Features

- [x] Support required and optional media fields (ImageField, FileField);
- [x] Support for media fields inside inlines **django-admin**;
- [x] Support preview modal for images, videos, and audio files;
- [x] Support custom inline for **django-admin** usage;
- [x] Support reordering inside **django-admin** inline;
- [x] Support `ArrayField` for `PostgreSQL` databases;
- [x] Support upload by dropping file;
- [x] Out of box HTMX support;
- [x] Preview support for images, videos, and audio files in django admin panel;
- [x] Media file type validation and preview.

## Installation

Install from PyPI:

```bash
pip install django-media-uploader-widget
```

Add `media_uploader_widget` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    'media_uploader_widget',
    # ...
]
```

## Basic Usage

### With Admin

The `MediaUploaderWidget` is a class that implements a custom widget for single media file uploader and can be used inside the `formfield_overrides` attribute inside the `ModelAdmin` class.

```python
# admin.py
from django.contrib import admin
from django.db import models
from media_uploader_widget.widgets import MediaUploaderWidget
from .models import YourModel


@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.FileField: {'widget': MediaUploaderWidget},
        models.ImageField: {'widget': MediaUploaderWidget},
    }
```

### With ModelForm

The `MediaUploaderWidget` can be used inside the `widgets` Meta attribute of a `Form`/`ModelForm`:

```python
# forms.py
from django import forms
from media_uploader_widget.widgets import MediaUploaderWidget


class ExampleForm(forms.ModelForm):
    class Meta:
        widgets = {
            'media': MediaUploaderWidget(),
        }
        fields = '__all__'
```

### Custom Inline Admin

The `MediaUploaderInline` is implemented with the base of the `admin.StackedInline` to create a custom **django-admin** to work with multiple media files upload using a model to store the files:

```python
# models.py

class Product(models.Model):
    # ...

class ProductMedia(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="media_files",
        on_delete=models.CASCADE
    )
    media = models.FileField("media")
    # ...
```

```python
# admin.py
from django.contrib import admin
from media_uploader_widget.admin import MediaUploaderInline
from .models import Product, ProductMedia


class ProductMediaAdmin(MediaUploaderInline):
    model = ProductMedia


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductMediaAdmin]
```

### Array Field

The ArrayField support is made by a custom field, called `MediaListField`:

```python
# models.py
from django.db import models
from media_uploader_widget.postgres import MediaListField


class TestWithArrayField(models.Model):
    media_files = MediaListField(blank=True, null=True, upload_to="admin_test")

    class Meta:
        verbose_name = "Test With Array Field"
```

## Preview

![Widget with Image in Dark Theme](https://raw.githubusercontent.com/inventare/django-image-uploader-widget/main/docs/_images/widget_image_dark.png#gh-dark-mode-only)![Widget with Image in Light Theme](https://raw.githubusercontent.com/inventare/django-image-uploader-widget/main/docs/_images/widget_image.png#gh-light-mode-only)

![Widget in Dark Theme](https://raw.githubusercontent.com/inventare/django-image-uploader-widget/main/docs/_images/widget_dark.png#gh-dark-mode-only)![Widget in Light Theme](https://raw.githubusercontent.com/inventare/django-image-uploader-widget/main/docs/_images/widget.png#gh-light-mode-only)

## Behaviour

![Widget Behaviour](https://raw.githubusercontent.com/inventare/django-image-uploader-widget/main/docs/_images/behaviour_widget.gif)

![Custom Admin Inline Behaviour](https://raw.githubusercontent.com/inventare/django-image-uploader-widget/main/docs/_images/behaviour_inline.gif)
