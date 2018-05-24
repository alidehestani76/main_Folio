from django.contrib import admin
from Bourseapp.models import Bourse
from Personapp.models import Person
from Membership.models import MemberShip

admin.site.register(Bourse)
admin.site.register(Person)
admin.site.register(MemberShip)