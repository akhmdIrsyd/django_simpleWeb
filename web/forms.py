from django import forms
from .models import kontak

class KontakForm(forms.ModelForm):

    class Meta:
        model = kontak
        fields = ['nama_kontak','email_kontak','isi_Kontak']