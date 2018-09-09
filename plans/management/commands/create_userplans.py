from django.core.management import BaseCommand

from plans.models import UserPlan


class Command(BaseCommand):
    help = 'Creates UserPlans for all Users'

    def handle(self, *args, **options):
        UserPlan.create_for_users_without_plan()
