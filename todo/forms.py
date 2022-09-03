from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['author']

    def __int__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] ='form-control'
            field.widget.attrs['placeholder'] = field_name



