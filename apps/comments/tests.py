import json

from rest_framework.test import (
    APITestCase,
)

from apps.accounts.models import User
from apps.animations.models import Animation
from apps.comments.models import Comment
from apps.reports.models import Report


class CommentTestCase(APITestCase):

    def setUp(self):
        self.user_1 = User.objects.create_user(email="test5@test.com", password="")
        self.user_2 = User.objects.create_user(email="test6@test.com", password="")
        self.user_3 = User.objects.create_user(email="test7@test.com", password="")
        self.user_4 = User.objects.create_user(email="test8@test.com", password="")
        self.user_5 = User.objects.create_user(email="test9@test.com", password="")
        self.user_6 = User.objects.create_user(email="test10@test.com", password="")
        self.user_7 = User.objects.create_user(email="test11@test.com", password="")

        self.ani_1 = Animation.objects.create(title="ani_1")
        self.ani_2 = Animation.objects.create(title="ani_2")

    def tearDown(self):

        Comment.objects.all().delete()

    def test_댓글_목록을_조회한다(self):
        """인증된 사용자 article 댓글 목록 조회 성공"""
        self.client.force_authenticate(user=self.user_1)
        # 애니메이션 댓글 생성
        comment_1 = Comment.objects.create(user=self.user_1, animation=self.ani_1, content='댓글 내용')
        comment_2 = Comment.objects.create(user=self.user_2, animation=self.ani_1, content='신고 댓글')
        comment_3 = Comment.objects.create(user=self.user_2, animation=self.ani_1, content='스포일러 신고')

        # 일반 신고
        Report.objects.create(reason="PORN", comment_id=comment_2.id, user_id=3)
        Report.objects.create(reason="PORN", comment_id=comment_2.id, user_id=4)
        Report.objects.create(reason="PORN", comment_id=comment_2.id, user_id=5)

        # 스포일러 신고
        Report.objects.create(reason="SPOILER", comment_id=comment_3.id, user_id=3)
        Report.objects.create(reason="SPOILER", comment_id=comment_3.id, user_id=4)
        Report.objects.create(reason="SPOILER", comment_id=comment_3.id, user_id=5)
        Report.objects.create(reason="SPOILER", comment_id=comment_3.id, user_id=6)
        Report.objects.create(reason="SPOILER", comment_id=comment_3.id, user_id=7)

        # 해당 애니메이션 댓글 목록 확인
        path = f'/comments/?animation_id={self.ani_1.id}'
        response = self.client.get(path=path, content_type='application/json')

        # 애니메이션과 연결된 댓글이 2개 존재한다. (신고수가 3개 이상인 댓글은 조회 목록에서 제외)
        # 스포일러 신고 5건 이상인 댓글은 '스포일러 신고 접수된 댓글입니다.'로 표기

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['content'], '스포일러 신고 접수된 댓글입니다.')

    def test_댓글을_생성한다(self):
        # 댓글이 존재하지 않는 애니매이션을 대상으로
        self.assertFalse(Comment.objects.filter(animation=self.ani_2).exists())
        self.client.force_authenticate(user=self.user_1)
        # 댓글을 생성한다
        path = f'/comments/'
        request_data = {
            "animation": self.ani_2.id,
            "content": "애니메이션_2 댓글 내용"
        }

        response = self.client.post(path=path, data=json.dumps(request_data), content_type='application/json')

        # 댓글 생성 결과를 확인한다

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.filter(animation=self.ani_2).count(), 1)
        self.assertEqual(Comment.objects.filter(animation=self.ani_2).last().user, self.user_1)

    def test_댓글을_수정한다(self):
        # 댓글 생성
        comment = Comment.objects.create(user=self.user_1, animation=self.ani_2, content='댓글 내용')
        self.client.force_authenticate(user=self.user_1)

        # 해당 댓글을 수정한다
        path = f'/comments/{comment.id}'
        request_data = {
            'comment_id': comment.id,
            'content': '댓글 내용 수정',
        }

        response = self.client.patch(path=path, data=json.dumps(request_data), content_type='application/json')
        comment.refresh_from_db()
        print("response : ", response.data)
        # 수정 여부를 확인한다
        self.assertEqual(response.status_code, 200)
        self.assertEqual(comment.content, request_data['content'])

