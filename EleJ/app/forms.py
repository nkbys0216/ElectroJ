from django import forms
from .models import Item

#データ入力画面のモデル定義

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name','age','ronbunt','ronbun','memo')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'執筆者の名前を記入してください'}),
                    'age': forms.NumberInput(attrs={'min':1}),
                    'ronbunt':forms.TextInput(attrs={'placeholder':'論文のタイトルを記入してください'}),
                    'ronbun':forms.TextInput(attrs={'placeholder':'論文のURLを記入してください'}),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }
