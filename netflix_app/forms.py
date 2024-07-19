from django import forms

class SortForm(forms.Form):
    keyword = forms.ChoiceField(choices=[
        ('title', 'Title'),
        ('type', 'Type'),
        ('country', 'Country'),
        ('release_year', 'Release Year'),
        ('duration', 'Duration'),
        ('genre', 'Genre')
    ])
    sort_order = forms.ChoiceField(choices=[
        ('True', 'Ascending'),
        ('False', 'Descending')
    ])

class SearchForm(forms.Form):
    column = forms.ChoiceField(choices=[
        ('title', 'Title'),
        ('country', 'Country'),
        ('release_year', 'Release Year'),
        ('director', 'Director')
    ])
    searchItem = forms.CharField(max_length=200)
