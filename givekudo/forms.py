from django import forms
from django.contrib.auth.models import User
from users.models import UserProfile

class KudoForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(KudoForm, self).__init__(*args, **kwargs)

        user_details = UserProfile.objects.get(user_id=self.request.user.id)
        org_members = UserProfile.objects.exclude(user_id=self.request.user.id).filter(
            organization_name=user_details.organization_name)
        self.fields["collegue_name"] = forms.TypedChoiceField(choices=[(member.user_id,
                                                                        User.objects.get(id=member.user_id).get_username())
                                                                       for member in org_members],
                                                              coerce=int)

    collegue_name = forms.TypedChoiceField(
        choices=(), help_text="Select colleague to whom you want to give kudo.")
    kudo_count = forms.ChoiceField(choices=[(x, x) for x in range(1, 4)])
    message = forms.CharField(
        max_length=100, help_text="Write a message for your team member.")