from django import forms
from .models import persona, pelicula
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit




class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Iniciar sesión'))

class personaForm(forms.ModelForm):
    
    class Meta:
        model=persona
        fields=["rut","nombre","apellido"]
        

class peliculaForm(forms.ModelForm):
    
    class Meta:
        model = pelicula
        fields = ["nombrePeli", "descripcion", "credYreparto", "portada", "linkTrailer"]
        
class frmUpdatePersona(forms.ModelForm):

    class Meta:
        model=persona
        fields=["nombre"]
        #fields=["nombre","apellido","sexo"]

