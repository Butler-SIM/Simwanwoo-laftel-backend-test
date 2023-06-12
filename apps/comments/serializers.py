from rest_framework import serializers

from apps.comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    report_cnt = serializers.IntegerField()
    spoiler_report_cnt = serializers.IntegerField()
    content = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'user_id',
            'content',
            'report_cnt',
            'spoiler_report_cnt',
        ]

    # def get_content(self, obj):
    #     """댓글 filter"""
    #
    #     if obj.user == self.context["request"].user:
    #         return obj.content
    #
    #
    #     print("obj.self.context.user", self.context["request"].user)
    #     print("obj.content", obj.content)
    #
    #     print("obj.report cnt", obj.report_cnt)
    #     print("obj.spoiler_report_cnt", obj.spoiler_report_cnt)
    #     return obj.content

    def get_content(self, obj):
        request = self.context.get('request')
        user = request.user

        if obj.user == user:
            return obj.content

        if obj.spoiler_report_cnt >= 5:
            return "스포일러 신고 접수된 댓글입니다."

        return obj.content


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'animation',
            'content',
        ]


class CommentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
        ]
