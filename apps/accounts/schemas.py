from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from apps.accounts.serializers.login import (
    LoginSerializer,
)
from apps.accounts.serializers.signUp import (
    CustomRegisterSerializer,
)


ACCOUNT_TAG = ["api-accounts"]


class SignUpSchema:
    signUp_schema = extend_schema(
        tags=ACCOUNT_TAG,
        summary=f"회원가입 ",
        description="username은 제외하고 요청",
        request=CustomRegisterSerializer,
    )

    signUp_schema_view = extend_schema_view(post=signUp_schema)

class LoginLogoutSchema:
    login_schema = extend_schema(
        tags=ACCOUNT_TAG,
        summary=f"로그인",
        request=LoginSerializer,
    )

    login_schema_view = extend_schema_view(post=login_schema)


