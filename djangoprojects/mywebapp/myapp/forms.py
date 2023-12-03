from django import forms
from .models import FinancialData

class FinancialDataForm(forms.ModelForm):
    class Meta:
        model = FinancialData
        fields = ['date', 'trade_code', 'high', 'low', 'open_price', 'close_price', 'volume']
