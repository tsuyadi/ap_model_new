from rest_framework import serializers
from ap_model.agencies.models import *


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('name','address', 'phone', 'origin_id')


class LevelSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    # type = serializers.SerializerMethodField()

    class Meta:
        model = Level
        fields = ('user', 'type', 'parent', 'children')

    def get_parent(self, obj):
        parents = obj.get_ancestors(ascending=False, include_self=False)
        result = []
        for item in parents:
            result.append({
                "user": item.user.get_full_name(),
                "type": item.get_type_display()
            })
        return result

    def get_children(self, obj):
        descendants = obj.get_descendants(include_self=False)
        result = []
        for item in descendants:
            result.append({
                "id": item.user.id,
                "user": item.user.get_full_name(),
                "type": item.get_type_display()
            })
        return result

    # def get_type(self, obj):
    #     return obj.get_type_display()


class UserSerializer(serializers.ModelSerializer):
    level = LevelSerializer()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'level', 'last_login')


class PhoneSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Phone
        fields = ('id', 'type', 'number', 'is_active', 'is_default')

    def get_type(self, obj):
        return obj.get_type_display()


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address', 'zipcode', 'is_active', 'is_default')


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('id', 'name', 'account_no', 'account_holder_name', 'is_default')


class AgentSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()
    phone_set = PhoneSerializer(many=True)
    address_set = AddressSerializer(many=True)
    bank_set = BankSerializer(many=True)
    status = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    religion = serializers.SerializerMethodField()
    marital_status = serializers.SerializerMethodField()
    ptkp_status = serializers.SerializerMethodField()
    birth_date = serializers.DateTimeField(allow_null=True, default=None, format="%Y-%m-%d")
    aaji_license_date = serializers.DateTimeField(allow_null=True, default=None, format="%Y-%m-%d")
    aaji_expired_date = serializers.DateTimeField(allow_null=True, default=None, format="%Y-%m-%d")
    contract_date= serializers.DateTimeField(allow_null=True, default=None, format="%Y-%m-%d")
    fast_date = serializers.DateTimeField(allow_null=True, default=None, format="%Y-%m-%d")

    class Meta:
        model = AgentProfile
        fields = ('id', 'user', 'branch', 'code', 'status', 'gender', 'birth_date', 'religion', 'marital_status',
                  'id_number', 'npwp_number', 'ptkp_status', 'aaji_number', 'aaji_license_date', 'aaji_expired_date',
                  'origin_id', 'contract_date', 'fast_date', 'first_login', 'address_set', 'phone_set', 'bank_set')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_gender(self, obj):
        return obj.get_gender_display()

    def get_religion(self, obj):
        return obj.get_religion_display()

    def get_marital_status(self, obj):
        return obj.get_marital_status_display()

    def get_ptkp_status(self, obj):
        return obj.get_ptkp_status_display()

