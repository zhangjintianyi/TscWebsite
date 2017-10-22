from rest_framework import serializers

from backend.apps.tsc.models import MSO, TSC, DBS


class TSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = TSC
        fields = "__all__"


class DBSSerializer(serializers.ModelSerializer):
    class Meta:
        model = DBS
        fields = "__all__"


class MSOSerializer(serializers.ModelSerializer):
    have_tsc = TSCSerializer(many=True)
    have_dbs = DBSSerializer(many=True)

    class Meta:
        model = MSO
        fields = "__all__"
