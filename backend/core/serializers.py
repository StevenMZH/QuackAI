from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    name = serializers.CharField()
    time_blocks = serializers.IntegerField()
    compatible_tags = serializers.ListField(
        child=serializers.CharField()
    )
    max_per_cicle = serializers.IntegerField()
    max_per_interval = serializers.IntegerField()


class ResourceSerializer(serializers.Serializer):
    name = serializers.CharField()
    tags = serializers.ListField(
        child=serializers.CharField()
    )
    max_per_cicle = serializers.IntegerField()
    max_per_interval = serializers.IntegerField()


class SchedulingProblemSerializer(serializers.Serializer):
    blocks = serializers.IntegerField()
    intervals = serializers.IntegerField()
    tasks = TaskSerializer(many=True)
    resources = ResourceSerializer(many=True)
