from django import forms



class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(label="Phone Number", max_length=20)


class CustomerCategoryForm(forms.Form):
    category1 = forms.CharField(label="category1", max_length=20)
    category2 = forms.CharField(label="category2", max_length=20)
    category3 = forms.CharField(label="category3", max_length=20)
    category4 = forms.CharField(label="category4", max_length=20)


class GiftCategoryForm(forms.Form):
    category1 = forms.CharField(label="gift_category1", max_length=20)
    category2 = forms.CharField(label="gift_category2", max_length=20)
    category3 = forms.CharField(label="gift_category3", max_length=20)
    category4 = forms.CharField(label="gift_category4", max_length=20)
