# 아이디어팜 프로젝트

아이디어와 관련된 물건 판매를 위한 쇼핑몰 사이트.(Django 프레임워크 기반)   
관리자에서 상품을 추가하고 사용자는 구매하며, 분류를 생성하여 그에 따라 하위 분류별 상품을 확인하고 옵션을 입력하여 주문 진행   
현재 장바구니 및 구매내역과 결제기능을 제외한 약 60% 기능 완료.      

* 현재 데모사이트 http://jyr.ideadream.co.kr:9000/ 에 구현 
* ckeditor 및 이미지 처리 pillow 모듈 사용하여 버전 확인 후 설치 필요

![ezgif com-gif-maker](https://user-images.githubusercontent.com/91244291/147218668-bc683696-c6d0-4f88-8fff-af90a1b8710c.gif)

### 메인페이지
상단(GNB), 하단(FOOTER), 댓글 부분외에 상품은 미구현으로 퍼블리싱만 되어있음.

#### 상단(GNB)
검색기능 : 등록되어 있는 상품의 제목 검색 가능

### 지식콘텐츠, 핸드메이드, 아이디어상품
* 관리자에서 지정한 대분류 목록을 나열하며, 각각 관리자에서 소개 페이지를 ckeditor로 편집하여 소개 가능함.   
* 클릭 시에 해당 분류의 상품 목록으로 이동하여 분류에 대한 소개 목록이 나오게 됨.   
* 상품분류에 대분류, 중분류, 소분류가 있으며 이에 해당하는 상품들이 목록이 출력됨.
* 분류에 해당하는 상품이 없을 경우 해당상품이 없습니다로 표시됨.
* 분류를 클릭하면 해당분류로 이동하며, 해당상품을 클릭하면 해당상품의 상세 화면으로 이동함.

### 상품 상세 페이지
* 해당상품의 등록된 이미지와 판매자, 판매가격, 할인가격, 배송방법, 배송비, 택배사, 재고 등의 정보와 옵션을 선택할 수 있음.
* 좋아요는 미구현, 공유하기는 현재 링크만 알림창으로 뜨게 설정함.
* 제품 옵션을 선택하면 재고수량에 맞게 해당옵션을 선택가능하며, 그 이상을 선택할시 오류가 발생하며 취소됨.
* 장바구니 및 구매하기를 조건을 충족시키면 결과페이지로 이동하나 아직 장바구니 및 결제가 구현되지 않아 사용불가능.
* 상품상세설명 : 관리자에서 입력한 상품에 대한 상세설명 내용이 표시되며, ckeditor로 편집하여 소개 가능함.
* 구매후기 : 해당상품에 대해서 구매한 회원의 평점을 계산하여 평균평점을 5점만점으로 표시하며 전체 구매자로 몇 명이 참여하였는지 표시됨.
* 구매문의 : 해당상품에 대해서 문의한 내역이 표시되며, 로그인하여야 문의를 작성 가능. 제목과 내용을 입력가능함. 관리자에서 답변이 없는경우 미완료로 나오며, 답변한 경우 답변이 표시됨. 
* 배송안내 : 관리자에서 DB로 입력한 배송안내 정보를 출력함.

### 구매후기
* 클릭하면 작성 후기에 대한 상세 정보가 떠야하나 아직 미구현

### 회원가입
* 관리자에서 입력한 최근 약관이 표시되며, 필수약관 동의여부 결정
* 일반회원과 기업회원으로 구분하여 회원정보를 입력하며, 각정보에 대한 기본 유효성 검사 적용(아이디 중복여부, 패스워드, 메일형식, 휴대전화번호 형식 등)
* 휴대전화번호는 국내와 국외로 나누어 적용(나름 글로벌 대비?)
* 다음 우편번호 API를 이용하여 주소 적용
* 기업회원의 경우 회사정보를 추가로 기입하며, 사업자등록번호의 경우 공공데이터 국세청 사업자등록정보 확인 API를 적용하여 유효한 사업자만 입력 가능

#### 로그인, 아이디 찾기, 비밀번호 찾기, 회원정보수정, 회원탈퇴 가능
