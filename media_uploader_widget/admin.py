from django import forms
from django.contrib import admin
from django.db import models


class MediaUploaderInlineWidget(forms.ClearableFileInput):
    template_name = (
        "media_uploader_widget/admin/inline_media_uploader_preview_widget.html"
    )


class MediaUploaderInline(admin.StackedInline):
    template = "media_uploader_widget/admin/inline_media_uploader.html"
    extra = 0
    add_image_text = ""
    drop_text = ""
    empty_text = ""
    empty_icon = ""
    drop_icon = ""
    add_icon = ""
    accept = "image/*"

    formfield_overrides = {models.ImageField: {"widget": MediaUploaderInlineWidget()}}

    def get_add_image_text(self):
        return self.add_image_text

    def get_drop_text(self):
        return self.drop_text

    def get_empty_text(self):
        return self.empty_text

    def get_empty_icon(self):
        return self.empty_icon

    def get_drop_icon(self):
        return self.drop_icon

    def get_add_icon(self):
        return self.add_icon

    def get_accept(self):
        return self.accept

    def get_formset(self, request, obj=None, **kwargs):
        item = super(MediaUploaderInline, self).get_formset(request, obj, **kwargs)
        item.add_image_text = self.get_add_image_text()
        item.drop_text = self.get_drop_text()
        item.empty_text = self.get_empty_text()
        item.empty_icon = self.get_empty_icon()
        item.drop_icon = self.get_drop_icon()
        item.add_icon = self.get_add_icon()
        item.accept = self.get_accept()
        return item

    @property
    def media(self):
        return forms.Media(
            js=[
                "media_uploader_widget/js/media-uploader-modal.js",
                "media_uploader_widget/js/media-uploader-inline.js",
            ],
            css={
                "screen": [
                    "media_uploader_widget/css/media-uploader-inline.css",
                ]
            },
        )


class OrderedMediaUploaderInline(MediaUploaderInline):
    template = "media_uploader_widget/admin/ordered_inline_media_uploader.html"
    order_field = "order"

    def get_order_field(self, request):
        return self.order_field

    def get_formset(self, request, obj=None, **kwargs):
        item = super(OrderedMediaUploaderInline, self).get_formset(
            request, obj, **kwargs
        )
        item.order_field = self.get_order_field(request)
        return item

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        field = self.get_order_field(request)
        return queryset.order_by(field)

    @property
    def media(self):
        return forms.Media(
            js=[
                "media_uploader_widget/js/vendor/sortable.min.js",
                "media_uploader_widget/js/media-uploader-modal.js",
                "media_uploader_widget/js/media-uploader-inline.js",
            ],
            css={
                "screen": [
                    "media_uploader_widget/css/media-uploader-inline.css",
                ]
            },
        )
