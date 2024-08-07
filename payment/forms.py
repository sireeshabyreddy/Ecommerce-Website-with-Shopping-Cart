from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'FullName'}),required=True)
    shipping_email=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}),required=True)
    shipping_address1=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address1'}),required=True)
    shipping_address2=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address2'}),required=False)
    shipping_city=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),required=True)
    shipping_state=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),required=True)
    shipping_pincode=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'PinCode'}),required=True)
    shipping_country=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}),required=True)
    class Meta:
        model=ShippingAddress
        fields=['shipping_full_name','shipping_email','shipping_address1','shipping_address2','shipping_city','shipping_state','shipping_pincode','shipping_country']
        exclude=['user',]

class PaymentForm(forms.Form):
    card_name=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name on card'}),required=True)
    
    card_number=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CardName'}),required=True)
    card_exp_date=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ExpirationDate'}),required=True)
    card_cvv_number=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ExpirationDate'}),required=True)
    card_address1=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing_address2'}),required=True)
    card_address2=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing_address2'}),required=True)
    card_city=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billingcity'}),required=False)
    card_state=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing State'}),required=False)
    card_pincode=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing pincode '}),required=False)
    card_country=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Billing_country'}),required=False)


    