from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", required = True, max_length=100, error_messages={
        "required": "Your name must not be empty",
        "max_length": "Please enter a shorter name."
    })    #有点像models.CharField()
    # 如果在开发者模式删掉max_length=100，is_valid()函数会自动校验并报错！
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)