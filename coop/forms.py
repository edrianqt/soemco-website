from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from .models import Application, ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "topic", "branch", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 5}),
                   "phone": forms.TextInput(attrs={"type": "tel", "placeholder": "09XX XXX XXXX"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["branch"].empty_label = "Any / not sure"

    def clean_phone(self):
        p = self.cleaned_data["phone"].strip()
        if p and not all(c.isdigit() or c in "+-() " for c in p):
            raise forms.ValidationError("Use numbers only, e.g. 0917 123 4567.")
        return p

    def clean_message(self):
        m = self.cleaned_data["message"].strip()
        if len(m) < 10:
            raise forms.ValidationError("Please write at least 10 characters.")
        return m


class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
                               help_text="At least 10 characters.")

    def clean_email(self):
        e = self.cleaned_data["email"].lower()
        if get_user_model().objects.filter(username=e).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return e

    def clean(self):
        data = super().clean()
        if data.get("password"):
            user = get_user_model()(username=data.get("email", ""), email=data.get("email", ""))
            try:
                validate_password(data["password"], user)
            except forms.ValidationError as e:
                self.add_error("password", e)
        return data


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["full_name", "phone", "branch", "loan_type", "amount", "term_months", "purpose"]
        widgets = {"purpose": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, kind="Membership", **kwargs):
        super().__init__(*args, **kwargs)
        self.kind = kind
        self.fields["branch"].empty_label = "Select…"
        if kind != Application.Kind.LOAN:
            for f in ("loan_type", "amount", "term_months"):
                del self.fields[f]
            self.fields["purpose"].label = "Notes (optional)"
        else:
            for f in ("loan_type", "amount", "term_months"):
                self.fields[f].required = True
            self.fields["purpose"].label = "Purpose of loan"


class EmailLoginForm(AuthenticationForm):
    """Usernames are stored as lower-case emails, so normalise what people type."""
    def clean_username(self):
        return self.cleaned_data["username"].strip().lower()
