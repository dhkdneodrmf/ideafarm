from typing import Tuple
from django.db import models
#from django.db.models.fields import EmailField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class User(models.Model):
    Utype=models.CharField(max_length=7, verbose_name='회원유형', choices=(('normal','일반회원'),('company','기업회원')))
    UID=models.CharField(max_length=20, verbose_name='아이디', unique=True,db_index = True)
    UPW=models.CharField(max_length=20, verbose_name='비밀번호')
    Unick=models.CharField(max_length=20, verbose_name='닉네임')
    Uname=models.CharField(max_length=12, verbose_name='이름')
    Ubrith=models.DateField(verbose_name='생년월일')
    GENDERS =(('M','남성(Man)'),('W','여성(woman)'))
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
    Ucombid=models.CharField(max_length=12, verbose_name='사업자등록번호', null=True, unique=True,db_index = True)
    Ufoundername=models.CharField(max_length=12, verbose_name='대표자명', null=True)
    Ucomstyle=models.CharField(max_length=20, verbose_name='업태', null=True)
    Ucomsector=models.CharField(max_length=20, verbose_name='업종', null=True)
    Ucombrith=models.DateField(verbose_name='회사설립일', null=True,blank=True)
    Ufounderbrith=models.DateField(verbose_name='창업자 생년월일', null=True,blank=True)
    Ufoundergender=models.CharField(max_length=1, verbose_name='창업자 성별', choices=GENDERS, null=True,blank=True)
    Ufoundyear=models.CharField(max_length=1, verbose_name='창업업력', null=True, choices=(('1','예비창업자'),('2','창업초기(3년 미만)'),('3','창업도약(4년 ~ 7년)'),('4','7년 이상')))
    Ucomdepart=models.CharField(max_length=1, verbose_name='창업분야', null=True, choices=(('1','제조'),('2','IT'),('3','도소매'),('4','서비스'),('5','사회적기업')))    
    Uregisterday=models.DateTimeField(auto_now_add=True, verbose_name='등록일')

    def __str__(self):
        return self.UID

class Term(models.Model):
    Mberterm=models.TextField(max_length=12000, verbose_name='회원가입약관')
    Privterm=models.TextField(max_length=12000, verbose_name='개인정보처리방침')
    registerday=models.DateTimeField(auto_now_add=True, verbose_name='등록일')

    def __str__(self):
        return self.registerday.strftime('%Y-%m-%d %H:%M:%S')

class Exituser(models.Model):
    reason=models.TextField(max_length=10000, verbose_name='탈퇴사유')
    Utype=models.CharField(max_length=7, verbose_name='회원유형', choices=(('normal','일반회원'),('company','기업회원')))
    Uname=models.CharField(max_length=12, verbose_name='이름')
    Ubrith=models.DateField(verbose_name='생년월일')
    GENDERS =(('M','남성(Man)'),('W','여성(woman)'))
    Ugender=models.CharField(max_length=1, verbose_name='성별', choices=GENDERS)
    Unation=models.CharField(max_length=3, verbose_name='국가', choices=(('KR','대한민국'),('ETC','국외')))
    Upostcode=models.CharField(max_length=7, verbose_name='우편번호')
    Uaddress=models.CharField(max_length=200, verbose_name='주소')
    Ucomtype=models.CharField(max_length=1, verbose_name='회사유형', null=True, choices=(('1','개인사업자'),('2','(주)주식회사'),('3','주식회사(주)'),('4','유한회사'),('5','사단법인'),('6','재단법인'),('7','학교'),('8','공공기관'),('9','기타')))
    Ucomname=models.CharField(max_length=15, verbose_name='회사명', null=True)
    Ufoundername=models.CharField(max_length=12, verbose_name='대표자명', null=True)
    Ucomstyle=models.CharField(max_length=20, verbose_name='업태', null=True)
    Ucomsector=models.CharField(max_length=20, verbose_name='업종', null=True)
    Ucombrith=models.DateField(verbose_name='회사설립일', null=True,blank=True)
    Ufounderbrith=models.DateField(verbose_name='창업자 생년월일', null=True,blank=True)
    Ufoundergender=models.CharField(max_length=1, verbose_name='창업자 성별', choices=GENDERS, null=True,blank=True)
    Ufoundyear=models.CharField(max_length=1, verbose_name='창업업력', null=True, choices=(('1','예비창업자'),('2','창업초기(3년 미만)'),('3','창업도약(4년 ~ 7년)'),('4','7년 이상')))
    Ucomdepart=models.CharField(max_length=1, verbose_name='창업분야', null=True, choices=(('1','제조'),('2','IT'),('3','도소매'),('4','서비스'),('5','사회적기업')))    
    Uregisterday=models.DateTimeField(verbose_name='회원가입일')

    def __str__(self):
        return self.Uname

class Prod_Categ_big(models.Model):
    Code=models.CharField(max_length=10, verbose_name='상품분류코드', unique=True, db_index=True)
    Name=models.CharField(max_length=50, verbose_name='상품분류명', db_index=True)
    Intro=RichTextUploadingField(verbose_name='상품분류소개', blank=True,null=True)
    def __str__(self):
        return self.Name

class Prod_Categ_mid(models.Model):
    Big=models.ForeignKey(Prod_Categ_big,on_delete=models.CASCADE)
    Code=models.CharField(max_length=10, verbose_name='상품분류코드', unique=True, db_index=True)
    Name=models.CharField(max_length=50, verbose_name='상품분류명', db_index=True)
    Intro=RichTextUploadingField(verbose_name='상품분류소개', blank=True,null=True)
    def __str__(self):
        return self.Name

class Prod_Categ_sma(models.Model):
    Mid=models.ForeignKey(Prod_Categ_mid,on_delete=models.CASCADE)
    Code=models.CharField(max_length=10, verbose_name='상품분류코드', unique=True, db_index=True)
    Name=models.CharField(max_length=50, verbose_name='상품분류명', db_index=True)
    Intro=RichTextUploadingField(verbose_name='상품분류소개', blank=True,null=True)
    def __str__(self):
        return self.Name