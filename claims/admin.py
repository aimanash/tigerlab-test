from django.contrib import admin

from .models import Claim


@admin.action(description='Update status to Accepted')
def make_accepted(modeladmin, request, queryset):
    queryset.update(status='Accepted')


@admin.action(description='Update status to In Progress')
def make_in_progress(modeladmin, request, queryset):
    queryset.update(status='In Progress')


class ClaimAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'vehicle_model', 'vehicle_no', 'status']
    actions = [make_accepted, make_in_progress]


admin.site.register(Claim, ClaimAdmin)
