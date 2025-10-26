from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import*


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class PropertyForm(forms.ModelForm):
    additional_images = forms.FileField(
        required=False,
        label="Additional Images",
        help_text="Select multiple images (hold Ctrl/Command to select multiple)"
    )

    class Meta:
        model = Property
        fields = ['property_type', 'status', 'price', 'location', 'bedrooms', 'bathrooms', 'image',
                  'additional_images']


class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image']

class PropertyFilterForm(forms.Form):
    property_status_choices = [
        ('', 'Select Status'),
        ('for_rent', 'For Rent'),
        ('for_sale', 'For Sale'),
    ]
    property_type_choices = [
        ('', 'Select Type'),
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('warehouse', 'warehouse'),
        ('land', 'Land'),
    ]

    property_status = forms.ChoiceField(choices=property_status_choices, required=False)
    property_type = forms.ChoiceField(choices=property_type_choices, required=False)
    location = forms.CharField(max_length=100, required=False)
    min_price = forms.DecimalField(required=False, min_value=0, label="Min Price")
    max_price = forms.DecimalField(required=False, min_value=0, label="Max Price")
    bedrooms = forms.IntegerField(required=False, min_value=1, label="Bedrooms")


class SearchForm(forms.Form):
    property_status = forms.ChoiceField(choices=[('for-sale', 'For Sale'), ('for-rent', 'For Rent')], required=False)
    property_type = forms.ChoiceField(choices=[('house', 'House'), ('apartment', 'Apartment'),('warehouse', 'Warehouse'),('Land', 'Land'),], required=False)
    location = forms.ChoiceField(
        choices=[(property.location, property.location) for property in Property.objects.all()],
        required=False
    )

    min_price = forms.IntegerField(required=False)
    max_price = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)