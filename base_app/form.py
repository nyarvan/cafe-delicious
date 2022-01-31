from django import forms
from .models import Reservation, Contact, Reviews

class FormReservation(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type': "text", 'name': "name", 'class': "form-control", 'id': "name",
                               'placeholder': "Your Name", 'data-rule': "minlen:4",
                               'data-msg': "Please enter at least 4 chars",
                           }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
                                                          'type': "email", 'class': "form-control", 'name': "email",
                                                        'id': "email", 'placeholder': "Your Email",
                                                        'data-rule': "email", 'data-msg': "Please enter a valid email"
    }))

    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
                                                        'type': "text", 'class': "form-control", 'name': "phone",
                                                        'id': "phone", 'placeholder': "Your Phone",
                                                        'data-rule': "minlen:4", 'data-msg': "Please enter at least 4 chars"
    }))

    date = forms.DateField(input_formats=["%d.%m.%Y", "%d/%m/%Y", "%d-%m-%Y",], widget=forms.TextInput(attrs={'type': "text", 'name': "date", 'class': "form-control", 'id': "date",
                                                         'placeholder': "Date", 'data-rule': "minlen:4",
                                                         'data-msg': "Please enter at least 4 chars"}))
    time = forms.TimeField(input_formats=["%H:%M", "%H.%M", "%H %M"], widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'name': "time", 'id': "time",
                                                         'placeholder': "Time", 'data-rule': "minlen:4",
                                                         'data-msg': "Please enter at least 4 chars"}))
    count_people = forms.DecimalField(widget=forms.TextInput(attrs={'type': "number", 'class': "form-control",
                                                                    'name': "people", 'id': "people",
                                                                    'placeholder': "# of people",
                                                                    'data-rule': "minlen:1",
                                                                    'data-msg': "Please enter at least 1 chars"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control",
                                                            'name': "message", 'rows': "5",
                                                            'placeholder': "Message"}))
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'date', 'time', 'count_people', 'message')

class FormContact(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': "text", 'name': "name",
                                                                        'class': "form-control",
                                                                        'id': "name", 'placeholder': "Your Name",
                                                                        }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': "email", 'class': "form-control",
                                                           'name': "email", 'id': "email",
                                                           'placeholder': "Your Email",}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'type': "text", 'class': "form-control",
                                                            'name': "subject", 'id': "subject",
                                                            'placeholder': "Subject",}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'name': "message", 'rows': "5",
                                                           'placeholder': "Message",}))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')


class FormReview(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type': "text", 'name': "name", 'class': "form-control", 'id': "name",
                               'placeholder': "Your Name", 'data-rule': "minlen:4",
                               'data-msg': "Please enter at least 4 chars",
                           }))
    post = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text", 'name': "post", 'class': "form-control", 'id': "post",
        'placeholder': "Your Post", 'data-rule': "minlen:4",
        'data-msg': "Please enter at least 4 chars",
    }))

    image = forms.FileField()

    rating = forms.DecimalField(widget=forms.TextInput(attrs={'type': "number", 'class': "form-control",
                                                              'name': "rating", 'id': "rating",
                                                              'placeholder': "Your rating (from 1 to 5)",
                                                              'data-rule': "minlen:1",
                                                              'data-msg': "Please enter at least 1 chars"}))

    review = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control",
                                                          'name': "message", 'rows': "5",
                                                          'placeholder': "Review"}))

    class Meta:
        model = Reviews
        fields = ('name', 'post', 'image', 'rating', 'review')