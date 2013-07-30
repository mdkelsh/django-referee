from django.contrib import admin
from assignment.models import Assignment


class RefereeAdmin(admin.ModelAdmin):
	fieldsets = (
	    (None, {
		'fields': ('date_time', 'location', 'age_group', 'status',)
	}),
	('Referees', {
		'classes': ('colapse',),
		'fields': ('center', 'AR_1', 'AR_2')
	}),
    )
admin.site.register(Assignment)

