from rest_framework import serializers
from ap_model.agencies.models import *


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('name', 'address', 'phone', 'origin_id')