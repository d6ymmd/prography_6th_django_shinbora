## 프로그라피 사전과제
### 1. 필수
- 게시물 목록을 반환하는 API 개발
- 게시물 상세 정보를 반환하는 API 개발
- 게시물 작성, 수정, 삭제를 수행하는 API 개발

 ### 1.1 진행
 - viewsets.ModelViewSet
 - viewsets -> ListAPIView, RetrieveAPIView로 대체
 - DestoryAPIView, CreateAPIView, UpdateAPIView 추가
 - 게시물 목록/작성, 상세/수정/삭제 기능 통합


### 2. 선택
- 과제에 대한 피드백
  - READEME.md 작성
- 사용자 권한 추가 적용
  - 게시물 작성/수정/삭제 기능 접근 권한 설정 구현
  - http://d6ymmd.pythonanywhere.com/admin 
    (admin, 1234)로그인시 게시물 작성/수정/삭제 기능 활성화 
  - 회원가입/로그인 미구현
- 서버에 배포하여 접근
  - pythonanywhere 배포
  - http://d6ymmd.pythonanywhere.com/
