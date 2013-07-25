from django.db import models

class Assignment(models.Model):
	OPEN = 'Open'
	CLOSED = 'Closed'
	date_time = models.DateTimeField()
	location = models.CharField(max_length=50)
	age_group = models.CharField(max_length=50)
	center = models.CharField(max_length=50, blank=True)
	AR_1 = models.CharField(max_length=50, blank=True)	
	AR_2 = models.CharField(max_length=50, blank=True)
	status_choices = (
		(OPEN, 'Open'),
		(CLOSED, 'Closed'),
	)
	status = models.CharField(max_length=6,	
		choices = status_choices,
		default = 'Open',
	)

	list_display = ('age_group', 'location')

	def is_open(self):
		"Returns true if referee positions are not filled"
		if (self.center and self.AR_1 and self.AR_2):
			self.status == 'CLOSED'
			return False
		if (self.status == 'CLOSED'):
			return False
		else:
			return True
