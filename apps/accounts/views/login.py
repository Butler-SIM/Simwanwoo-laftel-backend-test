from dj_rest_auth.views import (
    LoginView,
)

from apps.accounts.schemas import (
    LoginLogoutSchema,
)


@LoginLogoutSchema.login_schema_view
class CustomLoginView(LoginView):
    """로그인"""


