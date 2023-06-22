from django.contrib import admin
from cms.models import WebsiteSetting, Slider, Blog, FAQs,Contact,About


class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'phone']


admin.site.register(WebsiteSetting, WebsiteSettingAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ['heading', 'sub_heading', 'image', 'status']
    list_filter = ['heading']
    search_fields = ['heading']


admin.site.register(Slider, SliderAdmin)


class BlogAdmin(admin.ModelAdmin):
     prepopulated_fields = { 'slug' : ['title'] }
     list_display = ['title','author' , 'status']
     list_filter = ['title']
     search_fields = ['title']


admin.site.register(Blog, BlogAdmin)


class FAQsAdmin(admin.ModelAdmin):
    list_display = ['question']
    list_filter = ['question']
    search_fields = ['question']


admin.site.register(FAQs, FAQsAdmin)

class AboutAdmin(admin.ModelAdmin):
    '''register admin pannel for about page'''
    list_display=['title','description','imag','status']
    search_fields = ["name"]
    #actions = (active_status, inactive_status)

admin.site.register(About,AboutAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','mobile','message']
    search_fields=['name']


admin.site.register(Contact,ContactAdmin)    


