from social_core.pipeline.partial import partial
from authentication.backends.odl_open_id_connect import OdlOpenIdConnectAuth
from django.db import transaction
from accounts.models import User

@partial
def sup(
    backend, details, response, *args, **kwargs
):  # pylint: disable=too-many-arguments,unused-argument
    print("sup")

@partial
def create_user_via_oidc(
    strategy,
    backend,
    user=None,
    response=None,
    flow=None,
    current_partial=None,
    *args,
    **kwargs,
):  # pylint: disable=too-many-arguments,unused-argument
    """
    Creates a new user if one does not already exist, updates an existing user's attributes.
    Args:
        strategy (social_django.strategy.DjangoStrategy): the strategy used to authenticate
        backend (social_core.backends.base.BaseAuth): the backend being used to authenticate
        user (User): the current user
        details (dict): Dict of user details
        flow (str): the type of flow (login or register)
        current_partial (Partial): the partial for the step in the pipeline
    """
    if backend.name == OdlOpenIdConnectAuth.name:
        data = response.copy()
    else:
        return {}

    if user is None:
        with transaction.atomic():
            user = User.objects.create(
                    username=data["preferred_username"],
                    email=data["email"],
                    password=None,
                    name=data["name"],
                )
        


    return {"is_new": True, "user": user, "username": user.username}