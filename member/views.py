from os import name
from django.db.models.fields import NullBooleanField
from django.db.models.query import prefetch_related_objects
from django.shortcuts import redirect, render
from .models import Prod_Categ_mid, Prod_Categ_sma, Product, User, Term, Exituser, Prod_Categ_big, Devlivery
from django.contrib import messages
import re
#from django.http import HttpResponse
# Create your views here.
def index(req): #메인 페이지 구동함수
    catbig=Prod_Categ_big.objects.order_by()
    if req.session.get('uid'):
        loggeduser=User.objects.get(UID=req.session['uid'])
        return render(req, 'main.html',{'req':req,'userexist':loggeduser,'catbig':catbig})
    else:
        return render(req, 'main.html',{'req':req,'catbig':catbig})

def login(req): #로그인 페이지 구동함수
    if req.session.get('uid'):
        messages.warning(req, '이미 로그인 되어 있습니다.')
        return redirect('/')
    else:
        return render(req, 'login.html',{'req':req})

def newjoin(req): #회원가입 페이지 구동함수
    if req.session.get('uid'):
        messages.warning(req, '이미 로그인 되어 있습니다.')
        return redirect('/')
    else:
        Termsend=Term.objects.last()
        return render(req, 'join.html',{'req':req,'Term':Termsend})

def idcheck(req): #id중복체크로 넘어온 ajax 구동함수
    checkid=User.objects.filter(UID=req.POST.get('id'))
    if checkid:
        return render(req, 'idcheck.html',{'msg':'입력하신 아이디는 이미 가입되어 있습니다.'})
    else:
        return render(req, 'idcheck.html',{'msg':'입력하신 아이디는 사용 가능합니다.'})

def bidcheck(req): #사업자번호 중복체크로 넘어온 ajax 구동함수
    checkid=User.objects.filter(Ucombid=req.POST.get('bid'))
    if checkid:
        return render(req, 'idcheck.html',{'msg':'입력하신 사업자 등록번호는 이미 가입되어 있습니다.'})
    else:
        return render(req, 'idcheck.html',{'msg':'입력하신 사업자 등록번호는 사용 가능합니다.'})

def memberjoin(req): #회원가입 제출 서버에서 올바른지 확인 후 DB에 대입 올바르지 않을 경우 다시 회원가입으로 이동
    #print(req.POST.get('jmemtype'))
    #print(bool(re.search(r'^(normal|company)$',req.POST.get('jmemtype'))))
    # print(bool(re.search(r'KR|ETC', req.POST.get('jtelnation'))))
    # print(bool(re.search(r'^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$', req.POST.get('jemail'))))
    # print(bool(re.search(r'^[\d]{5,7}$', req.POST.get('jzipcode'))))
    # print(bool(re.search(r'.', req.POST.get('jdetailad'))))
    try:
        if bool(re.search(r'^(normal|company)$',req.POST.get('jmemtype'))) and bool(re.search(r'^[A-Za-z0-9]{4,20}$',req.POST.get('jid'))) and bool(re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[`!@#$%^&;*()-_=+\\\|\[\]\{\};:\'\";,.<>\/?`]).{5,20}$', req.POST.get('jpw'))) and bool(re.search(r'^[가-힣a-zA-Z0-9\-]{1,20}$', req.POST.get('jnick'))) and bool(re.search(r'^[가-힣]{2,12}$', req.POST.get('jname'))) and bool(re.search(r'^(19|20)\d{2}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1])$', req.POST.get('jbirth'))) and bool(re.search(r'M|W', req.POST.get('jgender'))) and bool(re.search(r'KR|ETC', req.POST.get('jtelnation'))) and bool(re.search(r'^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$', req.POST.get('jemail'))) and bool(re.search(r'^[\d]{5,7}$', req.POST.get('jzipcode'))) and bool(re.search(r'.', req.POST.get('jdetailad'))):
            if User.objects.filter(UID=req.POST.get('id')):
                return render(req, 'join.html',{'msg2':'중복된 아이디로는 회원가입이 불가능합니다.'})
            if req.POST.get('jtelnation').upper()=="KR":
                if bool(re.search(r'^[\d]{9}$', req.POST.get('jtel1') + req.POST.get('jtel2') + req.POST.get('jtel3'))):
                    Cp="01"+ str(req.POST.get('jtel1')) + "-" + str(req.POST.get('jtel2'))+ "-" + str(req.POST.get('jtel3'))
                else:
                    return render(req, 'join.html',{'msg2':'한국식 휴대전화 번호가 잘못되었습니다. '})
            else:
                if bool(re.search(r'\d{3,12}$', req.POST.get('jtel'))):
                    Cp=str(req.POST.get('jtel'))
                else:
                    return render(req, 'join.html',{'msg2':'휴대전화 번호가 잘못되었습니다. '})
            if not req.POST.getlist('Jsmsrecive'):
                smsrecive=False
            else:
                smsrecive=True
            if not req.POST.getlist('Jmailrecive'):
                mailrecive=False
            else:
                mailrecive=True
            if req.POST.get('jmemtype')=='company':
                if not (bool(re.search(r'^[1-9]{1}$', req.POST.get('jcompanytype'))) and bool(re.search(r'^[가-힣]{2,15}$', req.POST.get('jcname'))) and bool(re.search(r'\d{10}$', req.POST.get('jbid1') + req.POST.get('jbid2') + req.POST.get('jbid3'))) and bool(re.search(r'^[가-힣]{2,12}$', req.POST.get('jfoundername')))):
                    return render(req, 'join.html',{'msg2':'기업회원 필수정보가 누락되거나 잘못되었습니다. '})
            if req.POST.get('jbid1')==None:
                dcombid=None
            else:
                dcombid=str(req.POST.get('jbid1')) + "-" + str(req.POST.get('jbid2')) + "-" + str(req.POST.get('jbid3'))
            if req.POST.get('jcombirth')=="":
                dcombrith=None
            else:
                dcombrith=req.POST.get('jcombirth')
            if req.POST.get('jfounderbirth')=="":
                dfounderbrith=None
            else:
                dfounderbrith=req.POST.get('jfounderbirth')
            if req.POST.get('jfoundergender')=="":
                dfoundergender=None
            else:
                dfoundergender=req.POST.get('jfoundergender')
            detailad=re.sub(r'[,|\(|\)]'," ",req.POST.get('jdetailad'))
            Newmember=User(Utype=req.POST.get('jmemtype'),UID=req.POST.get('jid'),UPW=req.POST.get('jpw'),Unick=req.POST.get('jnick'),Uname=req.POST.get('jname'),Ubrith=req.POST.get('jbirth'),Ugender=req.POST.get('jgender').upper(),Unation=req.POST.get('jtelnation').upper(),Utel=Cp,Uemail=req.POST.get('jemail'),Upostcode=req.POST.get('jzipcode'),Uaddress=req.POST.get('jroadad')+","+detailad+req.POST.get('jextraad'),Usmsrecive=smsrecive,Umailrecive=mailrecive,Ucomtype=req.POST.get('jcompanytype'),Ucomname=req.POST.get('jcname'),Ucombid=dcombid,Ufoundername=req.POST.get('jfoundername'),Ucomstyle=req.POST.get('jcompanystyle'),Ucomsector=req.POST.get('jcomsector'),Ucombrith=dcombrith,Ufounderbrith=dfounderbrith,Ufoundergender=dfoundergender,Ufoundyear=req.POST.get('jsubcombirthyear'),Ucomdepart=req.POST.get('jcomdepartment'))
            Newmember.save()
            return render(req, 'joincomplete.html')
        else:
            return render(req, 'join.html',{'msg2':'입력된 내용에 오류가 있습니다.'})
    except TypeError:
        return render(req, 'join.html',{'msg2':'비정상적 접근입니다.'})

def loginchk(req): #로그인 시도시에 체크함수 성공시 세션을 할당
    if req.method=='POST':
        try:
            logtryuser=User.objects.get(UID=req.POST.get('eid'),UPW=req.POST.get('epw'))
            req.session['uid']=req.POST.get('eid')
            if req.POST.get('next'):
                return redirect(req.POST.get('next'))
            else:
                return redirect('/')
        except User.DoesNotExist:
            return render(req, 'login.html',{'msg':'아이디 혹은 비밀번호가 일치하지 않습니다.','req':req})
    return render(req, 'login.html',{'msg':'정상적인 로그인시도가 아닙니다.','req':req})

def logout(req): #로그아웃하고 홈으로 이동
    if req.session.get('uid'):
        req.session.pop('uid')
        return render(req, 'main.html',{'msg':'안전하게 로그아웃 되었습니다.'})
    else:
        return render(req, 'main.html',{'msg':'로그아웃할 회원이 없습니다. 올바르지 않은 접근입니다.'})

def morepw(req): #회원정보 수정 시 비밀번호 한번 더 입력하여 확인
    if req.session.get('uid'):
        loggeduser=User.objects.get(UID=req.session['uid'])
        return render(req, 'memberinfoedit.html',{'req':req, 'userexist':loggeduser})
    else:
        messages.warning(req, '정보수정할 회원정보가 없습니다.')
        return redirect('/')

def mbinfoedit(req): #회원정보 수정 창 띄우기
    if req.session.get('uid'):
        tryuser=User.objects.filter(UPW=req.POST.get('epw'))
        if tryuser:
            targetuser=User.objects.get(UID=req.session.get('uid'))
            userad=targetuser.Uaddress.split(",")
            userad1=userad[0]
            userad2=userad[1].partition("(")
            userad3=userad2[0]
            userad4=userad2[1]+userad2[2]
            return render(req, 'memberinfoedit2.html',{'req':req,'userexist':targetuser,'userad1':userad1,'userad3':userad3,'userad4':userad4})
        else:
            return render(req, 'memberinfoedit.html',{'msg':'입력한 비밀번호와 비밀번호가 일치하지 않습니다.','req':req})
    else:
        messages.warning(req, '정보수정할 회원정보가 없습니다.')
        return redirect('/')

def mbinfoeditcomp(req): #회원정보 수정 확인 및 수정완료
    if req.session.get('uid'):
        targetuser=User.objects.get(UID=req.session.get('uid'))
        userad=targetuser.Uaddress.split(",")
        userad1=userad[0]
        userad2=userad[1].partition("(")
        userad3=userad2[0]
        userad4=userad2[1]+userad2[2]
        try:
            if bool(re.search(r'^(normal|company)$',req.POST.get('jmemtype'))) and bool(re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[`!@#$%^&;*()-_=+\\\|\[\]\{\};:\'\";,.<>\/?`]).{5,20}$', req.POST.get('jpw'))) and bool(re.search(r'^[가-힣a-zA-Z0-9\-]{1,20}$', req.POST.get('jnick'))) and bool(re.search(r'^[가-힣]{2,12}$', req.POST.get('jname'))) and bool(re.search(r'^(19|20)\d{2}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1])$', req.POST.get('jbirth'))) and bool(re.search(r'M|W', req.POST.get('jgender'))) and bool(re.search(r'KR|ETC', req.POST.get('jtelnation'))) and bool(re.search(r'^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$', req.POST.get('jemail'))) and bool(re.search(r'^[\d]{5,7}$', req.POST.get('jzipcode'))) and bool(re.search(r'.', req.POST.get('jdetailad'))):
                if req.POST.get('jtelnation').upper()=="KR":
                    if bool(re.search(r'^[\d]{9}$', req.POST.get('jtel1') + req.POST.get('jtel2') + req.POST.get('jtel3'))):
                        Cp="01"+ str(req.POST.get('jtel1')) + "-" + str(req.POST.get('jtel2'))+ "-" + str(req.POST.get('jtel3'))
                    else:
                        return render(req, 'memberinfoedit2.html',{'msg':'한국식 휴대전화 번호가 잘못되었습니다.','req':req,'userexist':targetuser,'userad1':userad1,'userad3':userad3,'userad4':userad4})
                else:
                    if bool(re.search(r'\d{3,12}$', req.POST.get('jtel'))):
                        Cp=str(req.POST.get('jtel'))
                    else:
                        return render(req, 'memberinfoedit2.html',{'msg':'한국식 휴대전화 번호가 잘못되었습니다.','req':req,'userexist':targetuser,'userad1':userad1,'userad3':userad3,'userad4':userad4})
                if not req.POST.getlist('Jsmsrecive'):
                    smsrecive=False
                else:
                    smsrecive=True
                if not req.POST.getlist('Jmailrecive'):
                    mailrecive=False
                else:
                    mailrecive=True
                if req.POST.get('jmemtype')=='company':
                    if not (bool(re.search(r'^[가-힣]{2,15}$', req.POST.get('jcname'))) and bool(re.search(r'^[가-힣]{2,12}$', req.POST.get('jfoundername')))):
                        return render(req, 'memberinfoedit2.html',{'msg':'기업회원 필수정보가 누락되거나 잘못되었습니다.','req':req,'userexist':targetuser,'userad1':userad1,'userad3':userad3,'userad4':userad4})
                if req.POST.get('jcombirth')=="":
                    dcombrith=None
                else:
                    dcombrith=req.POST.get('jcombirth')
                if req.POST.get('jfounderbirth')=="":
                    dfounderbrith=None
                else:
                    dfounderbrith=req.POST.get('jfounderbirth')
                if req.POST.get('jfoundergender')=="":
                    dfoundergender=None
                else:
                    dfoundergender=req.POST.get('jfoundergender')
                detailad=re.sub(r'[,|\(|\)]'," ",req.POST.get('jdetailad'))
                targetuser.Utype=req.POST.get('jmemtype')
                targetuser.UPW=req.POST.get('jpw')
                targetuser.Unick=req.POST.get('jnick')
                targetuser.Uname=req.POST.get('jname')
                targetuser.Ugender=req.POST.get('jgender').upper()
                targetuser.Unation=req.POST.get('jtelnation').upper()
                targetuser.Utel=Cp
                targetuser.Uemail=req.POST.get('jemail')
                targetuser.Upostcode=req.POST.get('jzipcode')
                targetuser.Uaddress=req.POST.get('jroadad')+","+detailad+req.POST.get('jextraad')
                targetuser.Usmsrecive=smsrecive
                targetuser.Umailrecive=mailrecive
                targetuser.Ucomtype=req.POST.get('jcompanytype')
                targetuser.Ucomname=req.POST.get('jcname')
                targetuser.Ufoundername=req.POST.get('jfoundername')
                targetuser.Ucomstyle=req.POST.get('jcompanystyle')
                targetuser.Ucomsector=req.POST.get('jcomsector')
                targetuser.Ucombrith=dcombrith
                targetuser.Ufounderbrith=dfounderbrith
                targetuser.Ufoundergender=dfoundergender
                targetuser.Ufoundyear=req.POST.get('jsubcombirthyear')
                targetuser.Ucomdepart=req.POST.get('jcomdepartment')
                targetuser.save()
                messages.success(req, '회원정보 수정이 성공적으로 완료되었습니다.')
                if req.POST.get('next'):
                    return redirect(req.POST.get('next'))
                else:
                    return redirect('/')
            else:
                return render(req, 'memberinfoedit2.html',{'msg':'입력된 내용에 오류가 있습니다.','req':req,'userexist':targetuser,'userad1':userad1,'userad3':userad3,'userad4':userad4})
        except TypeError:
            return render(req, 'memberinfoedit2.html',{'msg':'비정상적 접근입니다.','req':req,'userexist':targetuser,'userad1':userad1,'userad3':userad3,'userad4':userad4})
    else:
        messages.warning(req, '정보수정할 회원정보가 없습니다.')
        return redirect('/')

def mboutpage(req):
    if req.session.get('uid'):
        return render(req, 'memberout.html',{'req':req})
    else:
        messages.warning(req, '탈퇴할 회원이 없습니다.')
        return redirect('/')

def mboutcomp(req):
    if req.session.get('uid') and req.method=='POST':
        try:
            outuser=User.objects.get(UID=req.session.get('uid'), UPW=req.POST.get('epw'))
            useracrive=Exituser(Utype=outuser.Utype,Uname=outuser.Uname,Ubrith=outuser.Ubrith,Ugender=outuser.Ugender,Unation=outuser.Unation,Upostcode=outuser.Upostcode,Uaddress=outuser.Uaddress,Ucomtype=outuser.Ucomtype,Ucomname=outuser.Ucomname,Ufoundername=outuser.Ufoundername,Ucomstyle=outuser.Ucomstyle,Ucomsector=outuser.Ucomstyle,Ucombrith=outuser.Ucombrith,Ufounderbrith=outuser.Ufounderbrith,Ufoundergender=outuser.Ufoundergender,Ufoundyear=outuser.Ufoundyear,Ucomdepart=outuser.Ucomdepart,Uregisterday=outuser.Uregisterday,reason=req.POST.get('exitreason'))
            useracrive.save()
            req.session.pop('uid')
            outuser.delete()
            messages.info(req, '회원탈퇴처리가 완료되었습니다.')
            if req.POST.get('next'):
                return redirect(req.POST.get('next'))
            else:
                return redirect('/')
        except User.DoesNotExist:
            return render(req, 'memberout.html',{'msg':'비밀번호가 일치하지 않습니다.','req':req})
    else:
        return render(req, 'main.html',{'msg':'정상적인 접근이 아닙니다.','req':req})

def findid(req): #아이디 찾기 페이지 구동함수
    if req.session.get('uid'):
        messages.warning(req, '이미 로그인 되어 있습니다.')
        return redirect('/')
    else:
        return render(req, 'findid.html',{'req':req})

def findidchk(req): #아이디 찾기 결과 페이지 구동함수
    if req.session.get('uid'):
        messages.warning(req, '이미 로그인 되어 있습니다.')
        return redirect('/')
    elif req.method=='POST':
        if req.POST.get('etelnation').upper()=="KR":
            Cp="01"+ str(req.POST.get('etel1')) + "-" + str(req.POST.get('etel2'))+ "-" + str(req.POST.get('etel3'))
        else:
            Cp=str(req.POST.get('etel'))
        try:
            idchkuser=User.objects.get(Uname=req.POST.get('ename'),Ubrith=req.POST.get('ebirth'),Utel=Cp)
            return render(req, 'findidresult.html',{'result':idchkuser,'req':req})
        except User.DoesNotExist:
            return render(req, 'findidresult.html',{'msg':'입력한 값과 일치하는 아이디가 없습니다.','req':req})
    else:
        return render(req, 'findid.html',{'msg':'정상적인 접근이 아닙니다.','req':req})

def findpw(req): #비밀번호 찾기 페이지 구동함수
    if req.session.get('uid'):
        messages.warning(req, '이미 로그인 되어 있습니다.')
        return redirect('/')
    else:
        return render(req, 'findpw.html',{'req':req})

def findpwchk(req): #비밀번호 찾기 결과 페이지 구동함수
    if req.session.get('uid'):
        messages.warning(req, '이미 로그인 되어 있습니다.')
        return redirect('/')
    elif req.method=='POST':
        if req.POST.get('etelnation').upper()=="KR":
            Cp="01"+ str(req.POST.get('etel1')) + "-" + str(req.POST.get('etel2'))+ "-" + str(req.POST.get('etel3'))
        else:
            Cp=str(req.POST.get('etel'))
        try:
            pwchkuser=User.objects.get(UID=req.POST.get('eid'),Uname=req.POST.get('ename'),Ubrith=req.POST.get('ebirth'),Utel=Cp)
            return render(req, 'findpwresult.html',{'result':pwchkuser,'req':req})
        except User.DoesNotExist:
            return render(req, 'findpwresult.html',{'msg':'입력한 값과 일치하는 비밀번호를 찾을 수 없습니다.','req':req})
    else:
        return render(req, 'findpw.html',{'msg':'정상적인 접근이 아닙니다.','req':req})

def mypagedisplay(req): #로그인 되어있는 경우 마이페이지 표시
    catbig=Prod_Categ_big.objects.order_by()
    if req.session.get('uid'):
        loggeduser=User.objects.get(UID=req.session.get('uid'))
        return render(req, 'mypage.html',{'req':req,'userexist':loggeduser,'catbig':catbig})
    else:
        messages.warning(req, '마이 페이지에 표시할 정보가 없습니다. 메인페이지로 이동합니다.')
        return redirect('/')

def poductview(req, catbig,catmid="",catsma="",prodname=""):
    tester=Prod_Categ_big.objects.filter(Code=catbig)
    if tester:
        tester2=Prod_Categ_mid.objects.filter(Code=catmid)
        tester3=Prod_Categ_sma.objects.filter(Code=catsma)
        tester4=Product.objects.filter(Code=prodname)
        if req.session.get('uid'):
            viewuser=User.objects.get(UID=req.session.get('uid'))
        else:
            viewuser=''
        catbig2=Prod_Categ_big.objects.order_by()
        catbig3=Prod_Categ_big.objects.get(Code=catbig)
        catmid2=catbig3.prod_categ_mid_set.all()
        #catsma2=Prod_Categ_sma.objects.filter() #무조건 모든 해당하는 소분류를 소환함.
        #for record in catmid2:
            #print(record)
            #print(record.prod_categ_sma_set.all())
            #catsma2=catsma2 | record.prod_categ_sma_set.all()
            #catsma2.append(record.prod_categ_sma_set.all())
        #print(catsma2)
        if catmid!="" and tester2:
            obj=Prod_Categ_mid.objects.get(Code=catmid)
            catsma2=obj.prod_categ_sma_set.all()
            if catsma!="" and tester3:
                obj=Prod_Categ_sma.objects.get(Code=catsma)
                if prodname!="" and tester4:
                    obj=Product.objects.get(Code=prodname)
                    return render(req,'product.html',{'req':req,'proddetail':obj,'userexist':viewuser,'catbig':catbig2,'catmid':catmid2,'catsma':catsma2})
                fiterprod=obj.product_set.all()
                return render(req,'product.html',{'req':req,'prodsma':obj,'userexist':viewuser,'catbig':catbig2,'catmid':catmid2,'catsma':catsma2,'prodfiter':fiterprod})
            fiterprod=obj.product_set.all()
            return render(req,'product.html',{'req':req,'prodmid':obj,'userexist':viewuser,'catbig':catbig2,'catmid':catmid2,'catsma':catsma2,'prodfiter':fiterprod})
        fiterprod=catbig3.product_set.all()
        return render(req,'product.html',{'req':req,'prodbig':catbig3,'userexist':viewuser,'catbig':catbig2,'catmid':catmid2,'prodfiter':fiterprod})
    messages.warning(req, '일치하는 대상이 없습니다. 메인페이지로 돌아갑니다.')
    return redirect('/')