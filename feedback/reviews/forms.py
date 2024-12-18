from django import forms

from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", required = True, max_length=100, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter a shorter name."
#     })    #有点像models.CharField()
#     # 如果在开发者模式删掉max_length=100，is_valid()函数会自动校验并报错！
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # fields = ['owner_comment']
        labels= {
            "user_name":"Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating",
        }
        error_messages = {
            "user_name":{
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorter name."
            }
        }