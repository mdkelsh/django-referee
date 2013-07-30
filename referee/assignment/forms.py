from django import forms

class AssignmentForm(forms.Form):
	CENTER = 1
	AR = 2
	CHOICES = (
		(CENTER, 'Center'),
		(AR, 'Assistant Referee'),
	)
	position = forms.ChoiceField(choices=CHOICES)

	