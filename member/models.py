import re
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.deletion import CASCADE
from django.db.models import F, Sum
from django.core.validators import RegexValidator

GENDERS =(('M','남성(Man)'),('W','여성(woman)'))

class User(models.Model): #회원테이블 정의
    Utype=models.CharField(max_length=7, verbose_name='회원유형', choices=(('normal','일반회원'),('company','기업회원')))
    UID=models.CharField(max_length=20, verbose_name='아이디', unique=True,db_index = True)
    UPW=models.CharField(max_length=20, verbose_name='비밀번호')
    Unick=models.CharField(max_length=20, verbose_name='닉네임')
    Uname=models.CharField(max_length=12, verbose_name='이름')
    Ubrith=models.DateField(verbose_name='생년월일')
    Ugender=models.CharField(max_length=1, verbose_name='성별', choices=GENDERS)
    Unation=models.CharField(max_length=3, verbose_name='국가', choices=(('KR','대한민국'),('ETC','국외')))
    Utel=models.CharField(max_length=15, verbose_name='휴대전화번호')
    Uemail=models.EmailField(max_length=60, verbose_name='이메일')
    Upostcode=models.CharField(max_length=7, verbose_name='우편번호')
    Uaddress=models.CharField(max_length=200, verbose_name='주소')
    Usmsrecive=models.BooleanField(verbose_name='SMS동의여부', default=False)
    Umailrecive=models.BooleanField(verbose_name='이메일수신동의여부', default=False)
    Ucomtype=models.CharField(max_length=1, verbose_name='회사유형', null=True, choices=(('1','개인사업자'),('2','(주)주식회사'),('3','주식회사(주)'),('4','유한회사'),('5','사단법인'),('6','재단법인'),('7','학교'),('8','공공기관'),('9','기타')))
    Ucomname=models.CharField(max_length=15, verbose_name='회사명', null=True)
    Ucombid=models.CharField(max_length=12, verbose_name='사업자등록번호', null=True, unique=True, db_index = True)
    Ufoundername=models.CharField(max_length=12, verbose_name='대표자명', null=True)
    Ucomstyle=models.CharField(max_length=20, verbose_name='업태', null=True)
    Ucomsector=models.CharField(max_length=20, verbose_name='업종', null=True)
    Ucombrith=models.DateField(verbose_name='회사설립일', null=True, blank=True)
    Ufounderbrith=models.DateField(verbose_name='창업자 생년월일', null=True ,blank=True)
    Ufoundergender=models.CharField(max_length=1, verbose_name='창업자 성별', choices=GENDERS, null=True, blank=True)
    Ufoundyear=models.CharField(max_length=1, verbose_name='창업업력', null=True, choices=(('1','예비창업자'),('2','창업초기(3년 미만)'),('3','창업도약(4년 ~ 7년)'),('4','7년 이상')))
    Ucomdepart=models.CharField(max_length=1, verbose_name='창업분야', null=True, choices=(('1','제조'),('2','IT'),('3','도소매'),('4','서비스'),('5','사회적기업')))    
    Uregisterday=models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    def __str__(self):
        return self.UID
    class Meta:
        verbose_name = "회원"
        verbose_name_plural = "회원"

class Term(models.Model): #약관 정의 최신의 것만 반영함.
    Mberterm=models.TextField(max_length=12000, verbose_name='회원가입약관')
    Privterm=models.TextField(max_length=12000, verbose_name='개인정보처리방침')
    registerday=models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    def __str__(self):
        return self.registerday.strftime('%Y-%m-%d %H:%M:%S')
    class Meta:
        verbose_name = "약관"
        verbose_name_plural = "약관"

class Exituser(models.Model): #탈퇴시 유저 통계기록 테이블
    reason=models.TextField(max_length=10000, verbose_name='탈퇴사유')
    Utype=models.CharField(max_length=7, verbose_name='회원유형', choices=(('normal','일반회원'),('company','기업회원')))
    Uname=models.CharField(max_length=12, verbose_name='이름')
    Ubrith=models.DateField(verbose_name='생년월일')
    Ugender=models.CharField(max_length=1, verbose_name='성별', choices=GENDERS)
    Unation=models.CharField(max_length=3, verbose_name='국가', choices=(('KR','대한민국'),('ETC','국외')))
    Upostcode=models.CharField(max_length=7, verbose_name='우편번호')
    Uaddress=models.CharField(max_length=200, verbose_name='주소')
    Ucomtype=models.CharField(max_length=1, verbose_name='회사유형', null=True, choices=(('1','개인사업자'),('2','(주)주식회사'),('3','주식회사(주)'),('4','유한회사'),('5','사단법인'),('6','재단법인'),('7','학교'),('8','공공기관'),('9','기타')))
    Ucomname=models.CharField(max_length=15, verbose_name='회사명', null=True)
    Ufoundername=models.CharField(max_length=12, verbose_name='대표자명', null=True)
    Ucomstyle=models.CharField(max_length=20, verbose_name='업태', null=True)
    Ucomsector=models.CharField(max_length=20, verbose_name='업종', null=True)
    Ucombrith=models.DateField(verbose_name='회사설립일', null=True, blank=True)
    Ufounderbrith=models.DateField(verbose_name='창업자 생년월일', null=True, blank=True)
    Ufoundergender=models.CharField(max_length=1, verbose_name='창업자 성별', choices=GENDERS, null=True, blank=True)
    Ufoundyear=models.CharField(max_length=1, verbose_name='창업업력', null=True, choices=(('1','예비창업자'),('2','창업초기(3년 미만)'),('3','창업도약(4년 ~ 7년)'),('4','7년 이상')))
    Ucomdepart=models.CharField(max_length=1, verbose_name='창업분야', null=True, choices=(('1','제조'),('2','IT'),('3','도소매'),('4','서비스'),('5','사회적기업')))    
    Uregisterday=models.DateTimeField(verbose_name='회원가입일')
    def __str__(self):
        return self.Uname
    class Meta:
        verbose_name = "탈퇴회원"
        verbose_name_plural = "탈퇴회원"

class Prod_Categ_big(models.Model): #대분류 정의
    Code=models.CharField(max_length=20, verbose_name='대분류코드', unique=True, db_index=True)
    Name=models.CharField(max_length=50, verbose_name='대분류명', db_index=True)
    Intro=RichTextUploadingField(verbose_name='대분류소개', blank=True,null=True)
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = "대분류"
        verbose_name_plural = "대분류"

class Prod_Categ_mid(models.Model): #중분류 정의
    Big=models.ForeignKey(Prod_Categ_big,on_delete=models.CASCADE, verbose_name='대분류선택')
    Code=models.CharField(max_length=20, verbose_name='중분류코드', unique=True, db_index=True)
    Name=models.CharField(max_length=50, verbose_name='중분류명', db_index=True)
    Intro=RichTextUploadingField(verbose_name='중분류소개', blank=True,null=True)
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = "중분류"
        verbose_name_plural = "중분류"

class Prod_Categ_sma(models.Model): #소분류 정의
    Mid=models.ForeignKey(Prod_Categ_mid,on_delete=models.CASCADE, verbose_name='중분류선택')
    Code=models.CharField(max_length=20, verbose_name='소분류코드', unique=True, db_index=True)
    Name=models.CharField(max_length=50, verbose_name='소분류명', db_index=True)
    Intro=RichTextUploadingField(verbose_name='소분류소개', blank=True,null=True)
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = "소분류"
        verbose_name_plural = "소분류"

class Devlivery_com(models.Model): #택배사 정의
    Company=models.CharField(max_length=10, verbose_name='택배사', unique=True, db_index=True)
    def __str__(self):
        return self.Company
    class Meta:
        db_table = "ideafarm_Delicom"
        verbose_name = "택배사등록"
        verbose_name_plural = "택배사등록"

class Devlivery_term(models.Model): #배송정책 정의
    Guide=RichTextField(max_length=10000, verbose_name='배송안내')
    Refund=RichTextField(max_length=10000, verbose_name='교환 및 반품안내')
    registerday=models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    def __str__(self):
        return self.registerday.strftime('%Y-%m-%d %H:%M:%S')
    class Meta:
        db_table = "ideafarm_Deliterm"
        verbose_name = "배송정책"
        verbose_name_plural = "배송정책"

class Devlivery(models.Model): #배송비 및 방법에 대한 정의
    Method=models.CharField(max_length=20, verbose_name='배송방법', unique=True)
    Dprice=models.PositiveIntegerField(default=0,verbose_name='배송비')
    def __str__(self):
        return self.Method
    class Meta:
        db_table = "ideafarm_Deliever"
        verbose_name = "배송방법입력"
        verbose_name_plural = "배송방법입력"

class Product(models.Model): #분류를 반영한 상품 테이블 정의
    Big=models.ForeignKey(Prod_Categ_big,on_delete=models.CASCADE, verbose_name='대분류선택') #,limit_choices_to={'Name':'아이디어상품'} limit 사용은 쿼리문 연습
    Mid=models.ForeignKey(Prod_Categ_mid,on_delete=models.CASCADE, verbose_name='중분류선택')
    Sma=models.ForeignKey(Prod_Categ_sma,on_delete=models.CASCADE, verbose_name='소분류선택')
    Code=models.CharField(max_length=20, verbose_name='상품분류코드', unique=True, db_index=True)
    Name=models.CharField(max_length=50, verbose_name='상품명', db_index=True)
    SimExplanation=models.CharField(max_length=100, verbose_name='상품간단설명', db_index=True,default='')
    Descrition=models.CharField(max_length=120, verbose_name='상품태그', db_index=True)
    Detail=RichTextUploadingField(verbose_name='상품상세설명', blank=True,null=True)
    Stock=models.PositiveIntegerField(default=999999,verbose_name='재고수량')
    Seller=models.CharField(max_length=80, verbose_name='판매자', db_index=True)
    NormalPrice=models.PositiveIntegerField(verbose_name='정가(원)')
    Discount=models.FloatField(verbose_name='할인율(%)',validators=[RegexValidator(r'^((100)|(\d{1,2}(\.\d*)?))$','백분율 값을 입력해야합니다.')])
    EndPrice=models.PositiveIntegerField(verbose_name='판매가(원)',default=0)
    Option=models.CharField(max_length=5000, null=True, blank=True, verbose_name='상품옵션')
    Delicom=models.ForeignKey(Devlivery_com,on_delete=CASCADE,verbose_name='택배사 선택')
    Deliver=models.ForeignKey(Devlivery,on_delete=CASCADE,verbose_name='배송방법 선택')
    Deliverterm=models.ForeignKey(Devlivery_term,on_delete=CASCADE,verbose_name='배송정책 선택')
    ProdRelation=models.ForeignKey('self',on_delete=CASCADE,verbose_name='연관상품 선택',null=True, blank=True)
    Pregisterday=models.DateTimeField(auto_now_add=True, verbose_name='상품등록일')
    Userveiw=models.PositiveIntegerField(default=0,verbose_name='상품조회수')
    Userpurchase=models.PositiveIntegerField(default=0,verbose_name='상품구매수')
    Paytax=models.CharField(max_length=1, verbose_name='과세유형', default=1, choices=(('1','과세'),('2','면세')))
    def __str__(self):
        return self.Name
    class Meta:
        db_table = "ideafarm_Product"
        verbose_name = "상품"
        verbose_name_plural = "상품"
    def save(self,*args,**kwargs):
        self.EndPrice=self.NormalPrice - int(self.NormalPrice*self.Discount/100)
        print(self.Option)
        if self.Option==None:
            self.Option=re.sub(r'[,|\:]',"",self.Name)
        super(Product,self).save(*args, **kwargs)

class Product_thumb(models.Model): #상품 테이블 중 이미지 필드 연결정의
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='productimages/',verbose_name='상품이미지', blank=True,null=True)
    class Meta:
        verbose_name = "이미지업로드"
        verbose_name_plural = "이미지업로드"

class Product_qna(models.Model): #상품문의 정의
    Product=models.ForeignKey(Product,on_delete=CASCADE)
    QTitle=models.CharField(max_length=100,verbose_name='제목', db_index=True,default='')
    Question=models.TextField(max_length=10000, verbose_name='상품문의내용', db_index=True)
    Asker=models.ForeignKey(User,on_delete=CASCADE)
    Answer=models.TextField(max_length=10000, verbose_name='상품답변내용', null=True, db_index=True)
    QWriteday=models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    def __str__(self):
        return self.QTitle
    class Meta:
        verbose_name = "상품문의"
        verbose_name_plural = "상품문의"

class Product_review(models.Model): #상품후기 정의
    Product=models.ForeignKey(Product,on_delete=CASCADE)
    Evaluate=models.CharField(max_length=4,verbose_name='평점', db_index=True, validators=[RegexValidator(r'^((5)|([0-4]{1}(\.\d*)?))$','0~5점 사이를 입력하세요.')])
    ReTitle=models.CharField(max_length=100,verbose_name='제목', db_index=True,default='')
    Content=models.TextField(max_length=10000, verbose_name='내용', db_index=True)
    Reviewer=models.ForeignKey(User,on_delete=CASCADE)
    Answer=models.TextField(max_length=10000, verbose_name='후기답변내용', null=True, db_index=True)
    RWriteday=models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    class Meta:
        verbose_name = "상품후기"
        verbose_name_plural = "상품후기"

class Product_reviewimg(models.Model): #상품후기 이미지 필드 연결정의
    Product=models.ForeignKey(Product_review,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='productreviewimages/',verbose_name='사진첨부', blank=True,null=True)
    class Meta:
        verbose_name = "이미지업로드"
        verbose_name_plural = "이미지업로드"

class Like(models.Model): #좋아요 테이블 정보 정의
    User=models.ForeignKey(User,on_delete=CASCADE,verbose_name='해당사용자')
    Product=models.ForeignKey(Product,on_delete=CASCADE,verbose_name='해당제품')
    Islike=models.BooleanField(default=False, verbose_name='좋아요 여부')
    registerday=models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    class Meta:
        verbose_name = "좋아요"
        verbose_name_plural = "좋아요"

class Cart(models.Model): #장바구니 테이블 정보 정의
    User=models.ForeignKey(User,on_delete=CASCADE,verbose_name='해당사용자')
    Product=models.ForeignKey(Product,on_delete=CASCADE,verbose_name='해당제품')
    Optioninfo=models.JSONField(default=dict, verbose_name='상품옵션정보')
    registerday=models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    class Meta:
        verbose_name = "장바구니"
        verbose_name_plural = "장바구니"

class Order(models.Model): #상품주문 테이블 정보 정의
    User=models.ForeignKey(User,on_delete=CASCADE,verbose_name='해당사용자')
    Product=models.ForeignKey(Product,on_delete=CASCADE,verbose_name='해당제품')
    Optioninfo=models.JSONField(default=dict, verbose_name='상품옵션정보')
    Devliveryplace=models.CharField(max_length=200, verbose_name='배송지')
    Payment=models.CharField(max_length=50, verbose_name='결제방법')
    Devliverfee=models.PositiveIntegerField(verbose_name='배송비')
    Orderprice=models.PositiveIntegerField(verbose_name='총결제금액')
    Ordercondition=models.CharField(max_length=1, verbose_name='주문상태', default=1, choices=(('1','주문(결제)완료'),('2','입금확인'),('3','배송준비중'),('4','배송시작'),('5','배송완료'),('6','주문취소'),('7','반품처리'),('8','품절'),('9','기타')))
    registerday=models.DateTimeField(auto_now_add=True, verbose_name='주문등록일')
    class Meta:
        verbose_name = "장바구니"
        verbose_name_plural = "장바구니"