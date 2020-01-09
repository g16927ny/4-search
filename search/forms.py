from django import forms

LIBRARIES_CHOICES_DEP = (
    ('東京駅', '東京駅'),
    ('品川駅', '品川駅'),
    ('成田空港国内線ターミナル駅', '成田空港国内線ターミナル駅'),
    ('羽田空港駅', '羽田空港駅'),
)

LIBRARIES_CHOICES_DES = (
    ('東京ドーム', '東京ドーム'),
    ('幕張メッセ', '幕張メッセ'),
    ('国立競技場', '国立競技場'),
    ('武道館', '武道館'),
    ('東京国際フォーラム', '東京国際フォーラム'),
    ('両国国技館', '両国国技館'),
)

class SearchsForm(forms.Form):
    dep = forms.ChoiceField(
        label='出発地',
        widget=forms.Select,
        choices=LIBRARIES_CHOICES_DEP,
        required=True,
    )
    des = forms.ChoiceField(
        label='目的地',
        widget=forms.Select,
        choices=LIBRARIES_CHOICES_DES,
        required=True,
    )
