from django.contrib import admin
from Bourseapp.models import Bourse
from Personapp.models import Person
from Membership.models import MemberShip
from Newsapp.models import News
from Education.models import education

admin.site.register(Bourse)
admin.site.register(Person)
admin.site.register(MemberShip)
admin.site.register(News)
admin.site.register(education)