from django.contrib.auth.models import User
from django.test import TestCase

from apps.animations.models import Animation
from apps.comments.models import Comment


class CommentTestCase(TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.사용자_1 = User.objects.create(username='사용자_1')
        cls.사용자_2 = User.objects.create(username='사용자_2')

        cls.애니메이션_1 = Animation.objects.create()
        cls.애니메이션_2 = Animation.objects.create()

    def test_댓글_목록을_조회한다(self):
        # 애니메이션 댓글 생성
        comment_1 = Comment.objects.create(user=self.사용자_1, animation=self.애니메이션_1, content='댓글 내용')
        Comment.objects.create(user=self.사용자_2, animation=self.애니메이션_1, content='댓글 내용', report_cnt=3)

        # 해당 애니메이션 댓글 목록 확인
        path = f'/comments/?animation_id={self.애니메이션_1.id}'
        response = self.client.get(path=path, content_type='application/json')

        # 애니메이션과 연결된 댓글이 1개 존재한다. (신고수가 3개 이상인 댓글은 조회 목록에서 제외)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], comment_1.id)

    def test_댓글을_생성한다(self):
        # 댓글이 존재하지 않는 애니매이션을 대상으로
        self.assertFalse(Comment.objects.filter(animation=self.애니메이션_2).exists())

        # 댓글을 생성한다
        path = f'/comments/create/'
        request_data = {
            'animation': self.애니메이션_2.id,
            'content': '애니메이션_2 댓글 내용'
        }
        self.client.force_login(user=self.사용자_1)
        response = self.client.post(path=path, data=request_data, content_type='application/json')

        # 댓글 생성 결과를 확인한다
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.filter(animation=self.애니메이션_2).count(), 1)
        self.assertEqual(Comment.objects.filter(animation=self.애니메이션_2).last().user, self.사용자_1)

    def test_댓글을_수정한다(self):
        # 댓글 생성
        comment = Comment.objects.create(user=self.사용자_1, animation=self.애니메이션_1, content='댓글 내용')

        # 해당 댓글을 수정한다
        path = f'/comments/update/'
        request_data = {
            'comment_id': comment.id,
            'content': '댓글 내용 수정',
            'report_cnt': 1,
        }

        response = self.client.patch(path=path, data=request_data, content_type='application/json')
        comment.refresh_from_db()

        # 수정 여부를 확인한다
        self.assertEqual(response.status_code, 200)
        self.assertEqual(comment.content, request_data['content'])
        self.assertEqual(comment.report_cnt, request_data['report_cnt'])
