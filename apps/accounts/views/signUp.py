from dj_rest_auth.registration.views import RegisterView
from apps.accounts.schemas import SignUpSchema


@SignUpSchema.signUp_schema
class CustomRegisterView(RegisterView):
    """회원 가입"""

