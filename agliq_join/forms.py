from django import forms


class UploadFileForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    projects_url = forms.URLField(max_length = 200, help_text = 'Please enter the Project URL.')
    code_url = forms.URLField(max_length = 200, help_text = 'Please enter the code URL.')
    resume = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
