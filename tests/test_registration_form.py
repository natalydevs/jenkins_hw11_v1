from datetime import date

from jenkins_hw11_v1.pages.registration_page import RegistrationForm
from jenkins_hw11_v1.models.user import User, Gender, Hobby
from jenkins_hw11_v1.data import users


def test_registration_with_preset_user():
    RegistrationForm() \
        .open() \
        .register(users.student) \
        .should_have_registered(users.student)