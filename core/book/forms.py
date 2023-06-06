from typing import Any, Dict
from django import forms
from .models import Book
 
# class BookForm(forms.Form):
#     name =  forms.CharField()
#     author_name = forms.CharField()
#     content = forms.CharField()

# class BookForm(forms.ModelForm):

#     tax = forms.FloatField()
#     class Meta:
#         model = Book
#         fields = ("name", "author_name", "content","price")




class NewForm(forms.ModelForm):
    tax = forms.FloatField()

    class Meta:
        model = Book
        fields ="__all__"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': f'{field}form-control'})

    def clean(self):
        price=self.cleaned_data("price")
        dis_price=self.cleaned_date("dis_price",0)
        tax=self.cleaned_data("tax",0)
    
        if (price-dis_price+tax)==0:
            raise forms.ValidationError("sifirdan boyuk olsun")
        return super().clean()
    

    def save(self, commit = True):
        self.cleaned_data["name"]=self.cleaned_data["name"].upper()

        del self.cleaned_data["tax"]



        if commit:
            return Book.objects.create(
                **self.cleaned_data
            )
        return Book(**self.cleaned_data)