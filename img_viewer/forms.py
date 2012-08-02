from django import forms

TOPIC_CHOICES = (
    ('/Users/mchen/images/expected', 'stuff1'),
    ('bug', 'Bug Report'),
)

TOPIC_CHOICES2 = (
    ('/Users/mchen/images/new', 'stuff1'),
    ('bug', 'Bug Report'),
)

class ContactForm(forms.Form):

    environment = forms.ChoiceField()
    group = forms.ChoiceField()
    version = forms.ChoiceField()
    def __init__(self, *args, **kwargs):

        env_choices = kwargs.pop('env', None)
        group_choices = kwargs.pop('group', None)
        version_choices = kwargs.pop('version', None)
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['environment'].choices = env_choices
        self.fields['group'].choices = group_choices
        self.fields['version'].choices = version_choices



    #version = forms.ChoiceField(choices=versions)
