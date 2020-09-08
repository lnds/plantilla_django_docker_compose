from crispy_forms.bootstrap import FormActions, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, Column, Row
from django import forms
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from posts.models import Post


class CrispyMixin:

    def configure_helper(self, helper):
        helper.layout = self.configure_layout()

    def configure_layout(self):
        return None

    def configure_actions(self, submit_action_label, return_action_url, returl_action_label='Volver'):
        return FormActions(
            StrictButton(submit_action_label, css_class='btn btn-warning', type='submit'),
            HTML('<a href="{}" class="btn btn-info">{}</a>'.format(return_action_url, returl_action_label)),
        )


class CrispyModelForm(forms.ModelForm, CrispyMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.configure_helper(self.helper)


class PostCreateForm(CrispyModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'tags']

    def configure_layout(self):
        return Layout(
            Row(Column('title')),
            Row(Column('text')),
            Row(Column('category'), Column('tags')),
            self.configure_buttons()
        )

    def configure_buttons(self):
        return Row(self.configure_actions(_('Crear'), reverse_lazy('home')))


class PostUpdateForm(PostCreateForm):

    def configure_buttons(self):
        return Row(self.configure_actions(_('Actualizar'), reverse_lazy('home')))
