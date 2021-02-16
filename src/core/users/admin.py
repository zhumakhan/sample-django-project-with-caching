from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email','password')}),
        (_('Personal info'), {'fields': ('avatar','phone','full_name')}),
        (_('Status'), {'fields': ('is_active','is_staff', 'is_superuser', 'groups')}),
        (_('Important dates'), {'fields': ('last_active', 'created')}),)

    list_display = (
        'id','email', 'full_name', 'is_active', 'is_staff',)
    search_fields = ('id','^email','^full_name')
    ordering = ('-created',)
    readonly_fields = ('created',)
    filter_horizontal = ('groups',)
    def save_model(self, request, obj, form, change):
        super(UserAdmin, self).save_model(request, obj, form, change)
        if 'password' in form.changed_data:
            form.instance.set_password(form.cleaned_data['password'])
        form.save()
        return form