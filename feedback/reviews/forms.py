from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField()    #有点像models.CharField()