
from django.utils.safestring import mark_safe

from .models import Show, Animals, Feedback, Banner, Story, Location, SociaLinks, Partners, EndedShow, Photoreport, \
    PhotoreprtShow, AnimalImage, Image


from django.contrib import admin



class ShowAdmin(admin.ModelAdmin):
    """ Админ-панель модели выставки"""
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}



class AnimalImageInline(admin.TabularInline):
    model = AnimalImage
    verbose_name = "Фотография животного"
    verbose_name_plural = "Фотографии животного"
    extra = 1


class AnimalsAdmin(admin.ModelAdmin):
    """ Админ-панель модели животных"""
    inlines = [AnimalImageInline]
    list_display = ('name', 'get_html_image', 'description', 'category')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def get_html_image(self, object):
        if object.image_animals:
            return mark_safe(f"<img src='{object.image_animals.url}' width=50>")

    get_html_image.short_description = "Миниатюра"


class ImageAdmin(admin.ModelAdmin):
    list_display = ('get_html_image',)
    def get_html_image(self, object):
        if object.images:
            return mark_safe(f"<img src='{object.images.url}' width=50>")

    get_html_image.short_description = "Миниатюра"


class FeedbackAdmin(admin.ModelAdmin):
    """ Админ-панель модели профиля"""
    list_display = ('name', 'user_phone')
    list_display_links = ('name',)


class BannerAdmin(admin.ModelAdmin):
    """ Админ-панель модели баннера"""
    list_display = ('name', 'get_html_banner')
    list_display_links = ('name',)

    def get_html_banner(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_banner.short_description = "Миниатюра"


class StoryAdmin(admin.ModelAdmin):
    """ Админ-панель модели Счатливые истории"""
    list_display = ('name', 'story', 'get_html_photo')
    list_display_links = ('name',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


class LocationAdmin(admin.ModelAdmin):
    """ Админ-панель модели места проведения выставки"""
    list_display = ('place', 'phone', 'duration')
    list_display_links = ('place',)


class SociaLinksAdmin(admin.ModelAdmin):
    """ Админ-панель модели социальных ссылок"""
    list_display = ('name', 'social_link', 'get_html_social')
    list_display_links = ('name',)

    def get_html_social(self, object):
        if object.social_logo:
            return mark_safe(f"<img src='{object.social_logo.url}' width=50>")

    get_html_social.short_description = "Миниатюра"


class PartnersAdmin(admin.ModelAdmin):
    """ Админ-панель модели партнеров"""
    list_display = ('name', 'get_html_partners', 'partners_link')
    list_display_links = ('name',)

    def get_html_partners(self, object):
        if object.logo:
            return mark_safe(f"<img src='{object.logo.url}' width=50>")

    get_html_partners.short_description = "Миниатюра"


class PhotoreprtShowInline(admin.TabularInline):
    model = PhotoreprtShow
    verbose_name = "Фотоотчет"
    verbose_name_plural = "Фотоотчет"
    extra = 1


class EndedShowAdmin(admin.ModelAdmin):
    inlines = [PhotoreprtShowInline]
    prepopulated_fields = {'slug': ('title',)}

class PhotoreportAdmin(admin.ModelAdmin):
    list_display = ('get_html_report',)

    def get_html_report(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_report.short_description = "Миниатюра"


admin.site.register(Show, ShowAdmin)
admin.site.register(Animals, AnimalsAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(SociaLinks, SociaLinksAdmin)
admin.site.register(Partners, PartnersAdmin)
admin.site.register(EndedShow, EndedShowAdmin)
admin.site.register(Photoreport, PhotoreportAdmin)
admin.site.register(Image, ImageAdmin)

admin.site.site_title = 'Редактор выставки'
admin.site.site_header = 'Редактор выставки'



