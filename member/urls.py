from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ), #메인 페이지 라우팅
    path('login', views.login, name='login' ), #로그인 페이지 라우팅
    path('join', views.newjoin, name='join' ), #회원가입 페이지 라우팅
    path('idcheck', views.idcheck ), #ajax로 id 중복체크 항목
    path('bidcheck', views.bidcheck ), #ajax로 사업자번호 중복체크 항목
    path('comp', views.memberjoin ), #회원가입 제출 확인시 라우팅
    path('logincheck', views.loginchk ), #로그인 시도 확인 라우팅
    path('logout', views.logout ), #로그아웃 라우팅
    path('memmodify', views.morepw, name='mimpwneed'), #회원정보수정 라우팅
    path('mbinfoedit', views.mbinfoedit), #회원정보수정 비번입력 확인 라우팅
    path('meminfomodcomp', views.mbinfoeditcomp), #회원정보수정 제출완료 및 확인
    path('memberout', views.mboutpage), #회원탈퇴 이동
    path('memberoutcomp',views.mboutcomp), #회원탈퇴 완료 후 페이지 이동 라우팅
    path('findid',views.findid), #아이디 찾기 페이지 이동 라우팅
    path('findpw',views.findpw), #비밀번호 찾기 페이지 이동 라우팅
    path('findidcheck',views.findidchk), #아이디 찾기 결과 페이지 이동 라우팅
    path('findpwcheck',views.findpwchk), #아이디 찾기 결과 페이지 이동 라우팅
    path('mypage',views.mypagedisplay, name='mypage'), #마이 페이지 이동 라우팅
] 