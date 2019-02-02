from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def get_user_quota(user):
    """
    Tiny helper for getting quota dict for user
    If user has expired plan, return def plan or None
    """
    if user.is_anonymous or user.userplan.is_expired():
        from .models import Plan
        default_plan = Plan.get_default_plan()
        if default_plan is None or not default_plan.is_free():
            raise ValidationError(_('User plan has expired'))
        return default_plan.get_quota_dict()
    return user.userplan.plan.get_quota_dict()
