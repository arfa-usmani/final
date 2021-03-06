from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "first_name", "last_name"]
	form  = SignUpForm

	#class Meta:
	#	model = SignUp


admin.site.register(SignUp, SignUpAdmin)
