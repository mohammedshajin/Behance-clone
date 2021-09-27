from re import T
from rest_framework import serializers
from work.models import Work, Tag, Comment
from users.models import Profile



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Work
        fields = '__all__'

    def get_comment(self, obj):
        comment = obj.comment_set.all()
        serializer = CommentSerializer(comment, many=True)
        return serializer.data