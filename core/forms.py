from django import forms

class Userform(forms.ModelForm):
    class Meta:
        model = None  # Replace with your actual model
        fields = '__all__'  # Adjust fields as necessary

    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic here if needed
        return cleaned_data