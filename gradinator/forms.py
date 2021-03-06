from django import forms

from gradinator.models import UserCourseworkGrade
from gradinator.models import UserGrade
from gradinator.models import UserProfile


class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        exclude = ('user', 'GPA')


class UserGradeForm(forms.ModelForm):
    class Meta:
        model = UserGrade
        exclude = {'grade', 'sat_by', 'grade_for'}


class UserCourseworkGradeForm(forms.ModelForm):
    # grade = forms.IntegerField(help_text="Please enter what percentage you got in", required=True)
    grade = forms.ChoiceField(help_text="Please enter what band you got in ", required=True, choices=(
        (round(22 / 22 * 100, 2), "A1"), (round(21 / 22 * 100, 2), "A2"), (round(20 / 22 * 100, 2), "A3"),
        (round(19 / 22 * 100, 2), "A4"), (round(18 / 22 * 100, 2), "A5"),
        (round(17 / 22 * 100, 2), "B1"), (round(16 / 22 * 100, 2), "B2"), (round(15 / 22 * 100, 2), "B3"),
        (round(14 / 22 * 100, 2), "C1"), (round(13 / 22 * 100, 2), "C2"), (round(12 / 22 * 100, 2), "C3"),
        (round(11 / 22 * 100, 2), "D1"), (round(10 / 22 * 100, 2), "D2"), (round(9 / 22 * 100, 2), "D3"),
        (round(8 / 22 * 100, 2), "E1"), (round(7 / 22 * 100, 2), "E2"), (round(6 / 22 * 100, 2), "E3"),
        (round(5 / 22 * 100, 2), "F1"), (round(4 / 22 * 100, 2), "F2"), (round(3 / 22 * 100, 2), "F3"),
        (round(2 / 22 * 100, 2), "G1"), (round(1 / 22 * 100, 2), "G2"), (round(0 / 22 * 100, 2), "H"),

    ))
    forms.ChoiceField()

    class Meta:
        model = UserCourseworkGrade
        exclude = {'sat_by', 'grade_for'}
