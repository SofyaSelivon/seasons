from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Season, Profile, MainVote
from django.utils.safestring import mark_safe

class CustomUserAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ()

@admin.register(MainVote)
class MainVoteAdmin(admin.ModelAdmin):
    readonly_fields = ('likes_count', 'dislikes_count')
    list_display = ('display_votes',)

    def display_votes(self, obj):
        return mark_safe(
            f'<span class="mainvote-likes" data-id="{obj.id}">{obj.likes_count}</span>\t'
            f'<span class="mainvote-dislikes" data-id="{obj.id}">{obj.dislikes_count}</span>'
        )

    display_votes.short_description = 'Голоса'

    class Media:
        js = ('js/reload.js',)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Season)
admin.site.register(Profile)
