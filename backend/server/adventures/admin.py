import os
from django.contrib import admin
from django.utils.html import mark_safe
from .models import Adventure, Checklist, ChecklistItem, Collection, Transportation, Note, AdventureImage
from worldtravel.models import Country, Region, VisitedRegion


class AdventureAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'user_id', 'date', 'is_public', 'image_display')
    list_filter = ('type', 'user_id', 'is_public')

    def image_display(self, obj):
        if obj.image:
            public_url = os.environ.get('PUBLIC_URL', 'http://127.0.0.1:8000').rstrip('/')
            public_url = public_url.replace("'", "")
            return mark_safe(f'<img src="{public_url}/media/{obj.image.name}" width="100px" height="100px"')
        else:
            return

    image_display.short_description = 'Image Preview'


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_code', 'continent', 'number_of_regions')
    list_filter = ('continent', 'country_code')

    def number_of_regions(self, obj):
        return Region.objects.filter(country=obj).count()

    number_of_regions.short_description = 'Number of Regions'


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'number_of_visits')
    # list_filter = ('country', 'number_of_visits')

    def number_of_visits(self, obj):
        return VisitedRegion.objects.filter(region=obj).count()
    
    number_of_visits.short_description = 'Number of Visits'

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'uuid', 'is_active', 'image_display']
    readonly_fields = ('uuid', 'image_display')
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_pic', 'uuid', 'public_profile')}),
    )
    def image_display(self, obj):
        if obj.profile_pic:
            public_url = os.environ.get('PUBLIC_URL', 'http://127.0.0.1:8000').rstrip('/')
            public_url = public_url.replace("'", "")
            return mark_safe(f'<img src="{public_url}/media/{obj.profile_pic.name}" width="100px" height="100px"')
        else:
            return
        
class AdventureImageAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'image_display')

    def image_display(self, obj):
        if obj.image:  # Ensure this field matches your model's image field
            public_url = os.environ.get('PUBLIC_URL', 'http://127.0.0.1:8000').rstrip('/')
            public_url = public_url.replace("'", "")
            return mark_safe(f'<img src="{public_url}/media/{obj.image.name}" width="100px" height="100px"')
        else:
            return

    image_display.short_description = 'Image Preview'
                                        
        
class CollectionAdmin(admin.ModelAdmin):
    def adventure_count(self, obj):
        return obj.adventure_set.count()

    adventure_count.short_description = 'Adventure Count'

    list_display = ('name', 'user_id', 'adventure_count', 'is_public')

admin.site.register(CustomUser, CustomUserAdmin)



admin.site.register(Adventure, AdventureAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(VisitedRegion)
admin.site.register(Transportation)
admin.site.register(Note)
admin.site.register(Checklist)
admin.site.register(ChecklistItem)
admin.site.register(AdventureImage, AdventureImageAdmin)

admin.site.site_header = 'AdventureLog Admin'
admin.site.site_title = 'AdventureLog Admin Site'
admin.site.index_title = 'Welcome to AdventureLog Admin Page'
