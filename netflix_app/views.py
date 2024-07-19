import logging
from venv import logger
from django.shortcuts import render
from django.http import HttpResponse
from .models import NetflixData
from .forms import SortForm, SearchForm



def index(request):
    print("Index view called")
    sort_form = SortForm()
    search_form = SearchForm()
    result = None

    if request.method == 'POST':
        action = request.POST.get('action')
        print(f"Action: {action}")
        
        if action == 'sort':
            sort_form = SortForm(request.POST)
            if sort_form.is_valid():
                keyword = sort_form.cleaned_data['keyword']
                sort_order = sort_form.cleaned_data['sort_order'] == 'True'
                data = NetflixData.objects.all().order_by(keyword if sort_order else f'-{keyword}')
                result = data

        elif action == 'search':
            search_form = SearchForm(request.POST)
            if search_form.is_valid():
                column = search_form.cleaned_data['column']
                search_item = search_form.cleaned_data['searchItem']
                if column == 'release_year':
                    data = NetflixData.objects.filter(**{column: int(search_item)})
                else:
                    data = NetflixData.objects.filter(**{f"{column}__icontains": search_item})
                result = data

    return render(request, 'index.html', {
        'sort_form': sort_form,
        'search_form': search_form,
        'result': result
    })

