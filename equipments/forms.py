from django import forms
from .models import Tractor, Implement, ImplementSubCategory


class TractorForm(forms.ModelForm):
    file = forms.FileField(label='Upload the Tractor pictures', widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Tractor
        exclude = ['user', 'created', 'modefied','status',]


class ImplementForm(forms.ModelForm):
    file = forms.FileField(label='Upload the Implement pictures', widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Implement
        exclude = ['user', 'created', 'modefied','status', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = ImplementSubCategory.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = ImplementSubCategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.implementsubcategory_set.order_by('name')
