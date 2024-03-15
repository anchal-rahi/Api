from rest_framework import serializers
from myapiis.models import apii


class TodoSerializer(serializers.ModelSerializer):
    class Meta():
        model =apii
        fields = "__all__"