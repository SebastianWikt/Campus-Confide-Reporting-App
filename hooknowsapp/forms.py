from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = {"created_at"}
        fields = ["title", "slug", "file"]