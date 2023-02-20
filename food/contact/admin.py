from django.contrib import admin

from contact.models import ContactModel


# Register your models here.
@admin.register(ContactModel)
class ContactAdminModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'website', 'create_at']
    list_display_links = ['name']  # поля в виде ссылок
    search_fields = ['name', 'email']  # поля поиска
    # list_filter = ('category', 'title', 'tags')
    readonly_fields = ('create_at',)  # поля только для чтения
    fields = ['name', 'email', 'website', 'message', 'create_at']  # очередность полей уже в открытом посте
    save_as = True


