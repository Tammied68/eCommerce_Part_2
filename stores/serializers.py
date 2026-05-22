from rest_framework import serializers
from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    """
    Serializer for Store instances.

    This serializer handles validation and transformation of Store
    model data for API requests and responses. It exposes fields such
    as vendor, name, description, and logo. The store ID and vendor
    fields are marked as read-only to prevent unauthorized changes
    through the API.
    """

    class Meta:
        model = Store
        fields = ["id", "vendor", "name", "description", "logo"]
        read_only_fields = ["id", "vendor"]
