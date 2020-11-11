from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя",
                           help_text="Введите своё имя"
                           )
    measure = forms.IntegerField(label="Масса",
                                 help_text="Введите свой вес",
                                 min_value=40,
                                 max_value=120
                                 )
    data = forms.DateField(label="Датка",
                           widget=forms.DateInput,
                           initial="2000-10-25",
                           help_text="Введите нужную дату",
                           )
    comment = forms.CharField(label="Комментарий",
                              widget=forms.Textarea,
                              required=False
                              )
