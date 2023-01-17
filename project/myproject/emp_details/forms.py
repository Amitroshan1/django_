from django.forms import forms
from emp_details.models import emp_data

class emp_form(forms.Form):
    class Meta:
        model = emp_data
        fields = ('emp_id','check_in_time','check_out_time')