from rest_framework import serializers
from core.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'created_by', 'rating', 'feedback_text']
