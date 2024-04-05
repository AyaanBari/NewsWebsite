from rest_framework import serializers
from .models import News

#we will create a serializer class for the News model .This NLP model classifies the news into 4 categories: Business, Entertainment, Politics, and Technology.

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
# Compare this snippet from Website/today/todaytomorrownews/views.py:

