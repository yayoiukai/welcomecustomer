from django.shortcuts import render
from .forms import PhoneNumberForm
from .forms import CustomerCategoryForm
from .forms import GiftCategoryForm


# Create your views here.

def index(request):
    form = PhoneNumberForm()
    return render(request, 'index.html', {'form': form})


def welcome(request):
    category_form = CustomerCategoryForm
    gift_form = GiftCategoryForm
    return render(request, 'welcome.html', {'caregory_form': category_form,
                                            'gift_form': gift_form})


def location(request):
    return render(request, 'location.html')
