from . forms import students
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template import loader
from . models import Home
from . model1 import Home1
from . model2 import Home2
from . model3 import Home3
from . model4 import NOTI
from . model5 import SCHOME
from . model6 import COMP
from . model7 import Home7
from . model8 import Home8
from . model9 import Home9
from . model10 import Home10
from . model11 import Home11
from . model12 import Home12
from . model13 import Home13
from . model14 import Home14
from . model15 import Home15
from . model16 import Home16
from . model17 import Home17
from . model18 import Home18
from . forms import worker,police,insage,noti,schome,comp,woratt,salaryage,assaignwork,reportpolice,insuranceworker,paymentinsurance,cardupload
from . forms1 import login4
from . forms3 import labchating
from datetime import date,datetime
from django.db.models import F
from django.utils import timezone
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.core.exceptions import ValidationError
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageTemplate, Frame, Image,Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from django.contrib import messages
# from django.contrib.auth import authenticate, login
def no_cache(view_func):
    decorated_view=never_cache(view_func)
    return decorated_view
def reg(request):
    if request.method == 'POST':
        form = students(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registeration successfull")
            return redirect('agencreg')
    else:
        form = students()
    return render(request, 'agencyreg.html', {'fmm': form})
            
def rr(request):
    te=loader.get_template('new.html')
    return HttpResponse(te.render())
@no_cache
def agv(request):
    user_id=request.session.get('Home15_id')
    try:
        User=Home15.objects.get(id=user_id)
    except Home15.DoesNotExist:
        return redirect('new')
    stu=Home.objects.all().values()
    return render(request,'agencyview.html',{'stu':stu})
    
    # return render(request,'agencyview.html',{'stu':stu})  
@no_cache
def agencyworkerrr(request):
    stu=Home.objects.all().values()
    return render(request,'agencyworkerregistration.html',{'stu':stu})
@no_cache
def wr(request,id):
    if request.method=='POST':
        tem= worker(request.POST)
        my=Home.objects.get(id=id)
        if tem.is_valid():
            f=tem.save(commit=False)
            f.agency_id=my.id
            f.save()
            messages.success(request,"Registeration successfull")
            return redirect('workreg')
            
            
    else:
        tem=worker()
    return render(request,'workreg.html',{'fmm12':tem})    
@no_cache   
def wv(request):
    user_id=request.session.get('Home15_id')
    try:
        User=Home15.objects.get(id=user_id)
    except Home15.DoesNotExist:
        return redirect('new')
    stu=Home1.objects.all().values()
    return render(request,'workview.html',{'stu':stu})
    # stu=Home1.objects.all().values()
    # return render(request,'workview.html',{'stu':stu})
@no_cache    
def pr(request):
    if request.method=='POST':
        tem= police(request.POST)
        if tem.is_valid():
            tem.save()
            messages.success(request,"Registeration successfull")
            return redirect('policereg')
           
            
    else:
        tem=police()
    return render(request,'policereg.html',{'fmm2':tem}) 
@no_cache
def pv(request):
    user_id=request.session.get('Home15_id')
    try:
        User=Home15.objects.get(id=user_id)
    except Home15.DoesNotExist:
        return redirect('new')
    stu=Home2.objects.all().values()
    return render(request,'policeview.html',{'stu':stu})
    # stu=Home2.objects.all().values()
    # return render(request,'policeview.html',{'stu':stu}) 
@no_cache
def inr(request):
    if request.method=='POST':
        tem= insage(request.POST)
        if tem.is_valid():
            tem.save()
            messages.success(request,"Registeration successfull")
            return redirect('insreg')
           
    else:
        tem=insage()
    return render(request,'insreg.html',{'fmm3':tem})
@no_cache
def inv(request):
    user_id=request.session.get('Home15_id')
    try:
        User=Home15.objects.get(id=user_id)
    except Home15.DoesNotExist:
        return redirect('new')
    stu=Home3.objects.all().values()
    return render(request,'insview.html',{'stu':stu})
    # stu=Home3.objects.all().values()
    # return render(request,'insview.html',{'stu':stu})
@no_cache
def newadmin(request):
    user_id=request.session.get('Home15_id')
    if not user_id:
        return redirect('new')
    
    try:
        User=Home15.objects.get(id=user_id)
        
    except Home15.DoesNotExist:
        return redirect('new')
    ag=Home.objects.all().count()
    wo=Home1.objects.all().count()
    po=Home2.objects.all().count()
    ig=Home3.objects.all().count()
    return render(request,'admin1.html',{'formm':User,'aa':ag,'ab':wo,'ad':po,'ac':ig})
     

def newlogin(request,user_type):
    if user_type=="agency":
        if request.method=='POST':
            tem = login4(request.POST)
            if tem.is_valid():
                email1=tem.cleaned_data['email']
                password1=tem.cleaned_data['password']
                try:
                    User=Home.objects.get(email=email1,password=password1)
                    
                    request.session['Home_id']=User.id
                    return redirect('agencyhome')
                except Home.DoesNotExist:
                    tem.add_error(None,'Invalid username or password')
        else:
            tem=login4()
        return render(request,'logiin.html',{'formm':tem}) 
    if user_type=="police":
        if request.method=='POST':
            tem = login4(request.POST)
            if tem.is_valid():
                email1=tem.cleaned_data['email']
                password1=tem.cleaned_data['password']
                try:
                    User=Home2.objects.get(email=email1,password=password1)
                    request.session['Home2_id']=User.id
                    return redirect('policehome')
                except Home2.DoesNotExist:
                    tem.add_error(None,'Invalid username or password')
        else:
            tem=login4()
        return render(request,'logiin.html',{'formm':tem}) 
    if user_type=="worker":
        if request.method=='POST':
            tem = login4(request.POST)
            if tem.is_valid():
                email1=tem.cleaned_data['email']
                password1=tem.cleaned_data['password']
                try:
                    User=Home1.objects.get(email=email1,password=password1)
                    request.session['Home1_id']=User.id
                    return redirect('workhome')
                except Home1.DoesNotExist:
                    tem.add_error(None,'Invalid username or password')
        else:
            tem=login4()
        return render(request,'logiin.html',{'formm':tem})  
    if user_type=="insuranceagency":
        if request.method=='POST':
            tem = login4(request.POST)
            if tem.is_valid():
                email1=tem.cleaned_data['email']
                password1=tem.cleaned_data['password']
                try:
                    User=Home3.objects.get(email=email1,password=password1)
                    request.session['Home3_id']=User.id
                    return redirect('insuranceagencyhome')
                except Home3.DoesNotExist:
                    tem.add_error(None,'Invalid username or password')
        else:
            tem=login4()
        return render(request,'logiin.html',{'formm':tem})  
     
    
         
def adminlogiin(request):
    
    if request.method=='POST':
        tem = login4(request.POST)
        if tem.is_valid():
            email1=tem.cleaned_data['email']
            password1=tem.cleaned_data['password']
            try:
                User=Home15.objects.get(email=email1,password=password1)
                User1=Home15.objects.filter(email=email1,password=password1)
                if User1.exists():
                    request.session['Home15_id']=User.id
                    
                    
                    return redirect('admin1')
            except Home15.DoesNotExist:
                tem.add_error(None,'Invalid username or password')
    else:
        tem=login4()
    return render(request,'logiin.html',{'formm':tem }) 
def labourcommissionlogiin(request):
    if request.method=='POST':
        tem = login4(request.POST)
        if tem.is_valid():
            email1=tem.cleaned_data['email']
            password1=tem.cleaned_data['password']
            try:
                User=Home16.objects.get(email=email1,password=password1)
                request.session['Home16_id']=User.id
                return redirect('labourcommisionhome')
            except Home16.DoesNotExist:
                tem.add_error(None,'Invalid username or password')
    else:
        tem=login4()
    return render(request,'logiin.html',{'formm':tem}) 
@no_cache
def policehome1(request):
    user_id=request.session.get('Home2_id')
    try:
        User=Home2.objects.get(id=user_id)
    except Home2.DoesNotExist:
        return redirect('new')
    return render(request,'policehome.html',{'formm':User})
def policehomebutton(request):
    return redirect('policehome')
def adminhomebutton(request):
    return redirect('admin1')
@no_cache
def insuranceagencyhome1(request):
    user_id=request.session.get('Home3_id')
    try:
        User=Home3.objects.get(id=user_id)
    except Home3.DoesNotExist:
        return redirect('new')
    return render(request,'insuranceagencyhome.html',{'formm':User})
def insuranceagencyhomebutton(request):
    return redirect('insuranceagencyhome')
@no_cache
def labourcommisionhome1(request):
    user_id=request.session.get('Home16_id')
    # print("id",user_id)
    if not user_id:
        return redirect('new')
    try:
        User=Home16.objects.get(id=user_id)
        return render(request,'labourcommisionhome.html',{'formm':User})
    except Home16.DoesNotExist:
        return redirect('new')
    
def labourcommissionhomebutton(request):
    return redirect('labourcommisionhome')
@no_cache
def workhome1(request):
    user_id=request.session.get('Home1_id')
    try:
        User=Home1.objects.get(id=user_id)
    except Home1.DoesNotExist:
        return redirect('new')
    return render(request,'workhome.html',{'formm':User})
def workerhomebutton(request):
    return redirect('workhome')
@no_cache
def agencyhome1(request):
    user_id=request.session.get('Home_id')
    try:
        User=Home.objects.get(id=user_id)
    except Home.DoesNotExist:
        return redirect('new')
    return render(request,'agencyhome.html',{'formm':User})
def agencyhomebutton(request):
    return redirect('agencyhome')        
def base1(request):
    tmpp=loader.get_template('base.html')
    return HttpResponse(tmpp.render())
def agencybase(request):
    tmpp=loader.get_template('agencyhomebase.html')
    return HttpResponse(tmpp.render())
def insuranceagencybase(request):
    tmpp=loader.get_template('insuranceagencyhomebase.html')
    return HttpResponse(tmpp.render())
def policebase(request):
    tmpp=loader.get_template('policehomebase.html')
    return HttpResponse(tmpp.render())
def workerbase(request):
    tmpp=loader.get_template('workerhomebase.html')
    return HttpResponse(tmpp.render())
def labourbase(request):
    tmpp=loader.get_template('labourcommisionhomebase.html')
    return HttpResponse(tmpp.render())
@no_cache
def notification1(request):
    user_id=request.session.get('Home15_id')
    if not user_id:
        return redirect('new')
    try:
        if request.method=='POST':
            form = noti(request.POST)
            if form.is_valid():
                tem = form.save(commit=False)
                tem.CURRENTDATE = date.today()
                tem.save()
                return redirect('admin1')
        else:
             tem=noti()
        return render(request,'notification.html',{'stu':tem})
    except Home15.DoesNotExist:
        return redirect('new')
def notificationBACK(request): 
    return redirect('admin1')
@no_cache
def nv(request):
    user_id=request.session.get('Home15_id')
    if not user_id:
        return redirect('new')
    try:
        User=Home15.objects.get(id=user_id)
        
    except Home15.DoesNotExist:
        return redirect('new')
    stu=NOTI.objects.all().values()
    return render(request,'notiview.html',{'stu':stu})

def deleteData(request,id):
    myd=NOTI.objects.get(id=id)
    myd.delete()
    return redirect('notiview')
@no_cache      
def editnot(request,id):
    user_id=request.session.get('Home15_id')
    if not user_id:
        return redirect('new')
    try:
        User=Home15.objects.get(id=user_id)
    except Home15.DoesNotExist:
        return redirect('new')
    if request.method=='POST':
        mydata=NOTI.objects.get(id=id)
        fm=noti(request.POST,instance=mydata)
        if fm.is_valid():
            fm.save()
            return redirect('notiview')
    else:
        mydata=NOTI.objects.get(id=id)
        fm=noti(instance=mydata)
    return render(request,'editnotification.html',{'stu':fm})
def editnotificationBACK(request):
    return redirect('notiview')
@no_cache
def anv(request):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    stu=NOTI.objects.all().values()
    return render(request,'agencynotification.html',{'stu':stu})
@no_cache
def lcwv(request):
    user_id=request.session.get('Home16_id')
    # print("id",user_id)
    if not user_id:
        return redirect('new')
    try:
        User=Home16.objects.get(id=user_id)
    except Home16.DoesNotExist:
        return redirect('new')
    stu=Home1.objects.all().values()
    return render(request,'labcommworker.html',{'stu':stu})
@no_cache
def awattv(request):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    user=request.session.get('Home_id')
    User=Home.objects.get(id=user)
    stu=Home1.objects.filter(agency_id=User).values()
    return render(request,'agencyworkerattenance.html',{'stu':stu})
@no_cache
def lcav( request):
    user_id=request.session.get('Home16_id')
    # print("id",user_id)
    if not user_id:
        return redirect('new')
    try:
        User=Home16.objects.get(id=user_id)
    except Home16.DoesNotExist:
        return redirect('new')
    stu=Home.objects.all().values()
    return render(request,'labcomagen.html',{'stu':stu})
@no_cache
def insscr(request):
    userid=request.session.get('Home3_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home3.objects.get(id=userid)
    except Home3.DoesNotExist:
        return redirect('new')
    if request.method=='POST':
        tem= schome(request.POST)
        if tem.is_valid():
            tem.save()
            return redirect('insuranceagencyhome')
            # request.session['SCHOME_id']
    else:
        tem=schome()
    return render(request,'schemeinsreg.html',{'fmm123':tem})  
@no_cache
def insscv( request):
    userid=request.session.get('Home3_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home3.objects.get(id=userid)
    except Home3.DoesNotExist:
        return redirect('new')
    stu=SCHOME.objects.all().values()
    return render(request,'schemeinsview.html',{'stu':stu})  
@no_cache
def editsch(request,id):
    userid=request.session.get('Home3_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home3.objects.get(id=userid)
    except Home3.DoesNotExist:
        return redirect('new')
    if request.method=='POST':
        mydata=SCHOME.objects.get(id=id)
        fm=schome(request.POST,instance=mydata)
        if fm.is_valid():
            fm.save()
            return redirect('insuranceagencyhome')
    else:
        mydata=SCHOME.objects.get(id=id)
        fm=schome(instance=mydata)
    return render(request,'editscheme.html',{'fmm123':fm})
def editschemeBACK(request):
    return redirect('schemeinsview')
def deleteDatascheme(request,id):
    myd=SCHOME.objects.get(id=id)
    myd.delete()
    return redirect('schemeinsview')
def payment1(request):
    tmpp=loader.get_template('payment.html')
    return HttpResponse(tmpp.render())
@no_cache
def woscv( request):
    userid=request.session.get('Home1_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home1.objects.get(id=userid)
    except Home1.DoesNotExist:
        return redirect('new')
    stu=SCHOME.objects.all().values()
    return render(request,'workersinsurance.html',{'stu':stu})  
@no_cache
def comr(request):
    userid=request.session.get('Home1_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home1.objects.get(id=userid)
    except Home1.DoesNotExist:
        return redirect('new')
    if request.method=='POST':
        tem= comp(request.POST)
        if tem.is_valid():
            tem.save()
            return redirect('workhome')
    else:
        tem=comp()
    return render(request,'workcomreg.html',{'f322':tem}) 
@no_cache
def comv( request):
    userid=request.session.get('Home1_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home1.objects.get(id=userid)
    except Home1.DoesNotExist:
        return redirect('new')
    stu=COMP.objects.all().values()
    return render(request,'workcomview.html',{'stu':stu})  
def deletecomplaint(request,id):
    myd=COMP.objects.get(id=id)
    myd.delete()
    return redirect('workcomview')
@no_cache
def editcomplaint(request,id):
    userid=request.session.get('Home1_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home1.objects.get(id=userid)
    except Home1.DoesNotExist:
        return redirect('new')
    if request.method=='POST':
        mydata=COMP.objects.get(id=id)
        fm=comp(request.POST,instance=mydata)
        if fm.is_valid():
            fm.save()
            return redirect('workcomview')
    else:
        mydata=COMP.objects.get(id=id)
        fm=comp(instance=mydata)
    return render(request,'editcomplaintworker.html',{'fm123':fm})
def editcomplaintworkerBACK(request):
    return redirect('workcomview')
@no_cache
def acomv( request):
    stu=COMP.objects.all().values()
    return render(request,'workcomadmin.html',{'stu':stu})  
def chat(request):
    tmpp=loader.get_template('chat1.html')
    return HttpResponse(tmpp.render())
@no_cache
def woat(request,id):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    today = date.today()
    existing_attendance = Home7.objects.filter(WORKER_id=id, CURRENTDATE=today)

    # if existing_attendance.exists():
    #     a = 'Attendance for this worker on the same date already exists'
    #     return render(request, 'workeratt.html', {'a': a})
    if request.method=='POST':
        c=date.today()
        if not existing_attendance.exists():
            fm= woratt(request.POST)
            my=Home1.objects.get(id=id)
            if fm.is_valid():
                f=fm.save(commit=False)
                f.WORKER_id=my.id
                f.CURRENTDATE=date.today()
                f.currentmonth = datetime.now().month
                f.save()
                return redirect("agencyworkerattenance")
        else:
            a = 'Attendance for this worker on the same date already exists'
            return render(request, 'workeratt.html', {'a': a})
           
    else:
        my=Home1.objects.get(id=id)
        fm=woratt()
    return render(request,'workeratt.html',{'fm1223':fm})
def workerattBACK(request):
    return redirect('agencyworkerattenance')
@no_cache
def woatv( request,id):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    stu=Home7.objects.filter(WORKER_id=id).values()
    return render(request,'viewworkeratt.html',{'stu':stu})  
def viewworkerattBACK(request):
    return redirect('agencyworkerattenance')
@no_cache 
def lcgv(request):
    user_id=request.session.get('Home16_id')
    # print("id",user_id)
    if not user_id:
        return redirect('new')
    try:
        User=Home16.objects.get(id=user_id)
    except Home16.DoesNotExist:
        return redirect('new')
    stu=Home1.objects.all().values()
    return render(request,'cardapply.html',{'stu':stu})
@no_cache
def lcgr(request,id):
    if request.method=='POST':
        mydata=Home1.objects.get(id=id)
        fm=worker(request.POST,instance=mydata)
        if fm.is_valid():
            fm.save()
    else:
        mydata=Home1.objects.get(id=id)
        fm=worker(instance=mydata)
    return render(request,'generatecardlc.html',{'fmm12':fm})

def generate_pdf(request, id):
    # Get the Home1 instance
    mydata = get_object_or_404(Home1, id=id)

    # Create a response with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="worker_card_{mydata.workername}.pdf"'

    # Define a custom page size (adjust as needed)
    page_width, page_height = 9 * inch, 6 * inch  # 4x3 inches

    # Create a PDF document using ReportLab with custom page size
    doc = SimpleDocTemplate(response, pagesize=(page_width, page_height))
    styles = getSampleStyleSheet()

    # Customize the ID card layout
    story = []

    # Define a custom style for the header
    header_style = ParagraphStyle(
        name='HeaderStyle',
        fontSize=16,
        textColor=colors.blue,
        alignment=1,  # Center alignment
    )

    # Create a PageTemplate with a border style
    border_style = TableStyle([
        ('BOX', (0, 0), (-1, -1), 1, colors.black),  # Border around the entire page
    ])
    page_template = PageTemplate(frames=[
        Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal', showBoundary=1, topPadding=0),
    ])
    page_template.beforeDrawPage = lambda canvas, doc: canvas.saveState()
    page_template.afterDrawPage = lambda canvas, doc: canvas.restoreState()

    doc.addPageTemplates([page_template])

    # Add a header with the worker's name
    header = Paragraph(mydata.workername, header_style)
    story.append(header)

    # Add a spacer
    story.append(Spacer(1, 0.2 * inch))

    # Define a custom style for the worker's details
    details_style = ParagraphStyle(
        name='DetailsStyle',
        fontSize=10,
        textColor=colors.black,
        leftIndent=0.2 * inch,
    )

    # Add the worker's details as a table
    details_data = [
        ['Address:', mydata.address],
        ['Pincode:', str(mydata.pincode)],
        ['State:', mydata.state],
        ['District:', mydata.district],
        ['City:', mydata.city],
        ['Aadhar Number:', str(mydata.aadharnumber)],
        ['Contact Number:', str(mydata.contactnumber)],
        ['Email:', mydata.email],
    ]

    # Adjust the width of the table columns
    col_widths = [1.2 * inch, 2.8 * inch]

    details_table = Table(details_data, colWidths=col_widths)
    details_table.setStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
    ])

    # Add the details table to the story
    story.append(details_table)

    # Add an image (e.g., company logo) to the page
    # image_path = 'D:\\staticm\\Scripts\\staticproject\\home\\static\\assets\\img\\personnnn.jpg'  # Provide the path to your image
    # logo = Image(image_path, width=1.5 * inch, height=1.5 * inch)
    # story.append(logo)

    # Build the PDF document
    doc.build(story)

    return response
@no_cache
def salaryr(request):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    if request.method=='POST':
        tem= salaryage(request.POST)
        if tem.is_valid():
            tem.save()
            return redirect("agencysalaryview")
    else:
        tem=salaryage()
    return render(request,'agencysalary.html',{'f322':tem})  
@no_cache
def salaryv(request):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    stu=Home8.objects.all().values()
    return render(request,'agencysalaryview.html',{'stu':stu})
@no_cache
def editsalary(request,id):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    if request.method=='POST':
        mydata=Home8.objects.get(id=id)
        fm=salaryage(request.POST,instance=mydata)
        if fm.is_valid():
            fm.save()
            return redirect("agencysalaryview")
    else:
        mydata=Home8.objects.get(id=id)
        fm=salaryage(instance=mydata)
    return render(request,'agencysalaryedit.html',{'f322':fm})
def agencysalaryeditBACK(request):
    return redirect('agencysalaryview')
def deletesalary(request,id):
    myd=Home8.objects.get(id=id)
    myd.delete()
    return redirect('agencysalaryview')
@no_cache
def agwv(request):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    user=request.session.get('Home_id')
    User=Home.objects.get(id=user)
    stu=Home1.objects.filter(agency_id=User).values()
    return render(request,'agencyworker.html',{'stu':stu})
@no_cache
def asswoag(request,id):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    if request.method=='POST':
        existing_work = Home9.objects.filter(WORKER_id=id)
        my=Home1.objects.get(id=id)
        fm=assaignwork(request.POST)
        if not existing_work.exists():
            if fm.is_valid():
                f=fm.save(commit=False)
                f.WORKER_id=my.id
                f.save()
                return redirect('agencyworker')
        elif existing_work.exists:
            a = 'Worker already assigned'
            return render(request, 'assignworkage.html', {'a': a})
    else:
        my=Home1.objects.get(id=id)
        fm=assaignwork()
    return render(request,'assignworkage.html',{'f3221':fm})
def assignworkageBACK(request):
    return redirect('agencyworker')
@no_cache
def asswoagv(request,id):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    stu=Home9.objects.filter(WORKER_id=id).values()
    return render(request,'viewassignworkage.html',{'stu':stu})
def viewassignworkageBACK(request):
    return redirect('agencyworker')
def deletejobcategory(request,id,WORKER_id):
    myd=Home9.objects.get(id=id)
    myd.delete()
    return redirect('agencyworker')
@no_cache
def pcclabcom(request, id):
    user_id=request.session.get('Home16_id')
    # print("id",user_id)
    if not user_id:
        return redirect('new')
    try:
        User=Home16.objects.get(id=user_id)
    except Home16.DoesNotExist:
        return redirect('new')
    try:
        # Fetch the Home1 object with the given id
        stu = Home1.objects.get(id=id)
        
        # Assuming you want to access the 'id' field of 'stu'
        Worker_id = stu.id
        
        # Get the current date
        CURRENTDATE = date.today()
        
        # Create and save a Home10 instance
        Home10_instance = Home10(Worker_id=Worker_id, CURRENTDATE=CURRENTDATE)
        Home10_instance.save()
        
        # Query Home10 objects with the same Worker_id
        s = Home10.objects.filter(Worker_id=id).first()
        
        return render(request, 'pccrequestlabcom.html', {'stu': s})
    
    except Home1.DoesNotExist:
        # Handle the case where the Home1 object with the given id doesn't exist
        return render(request, 'pccrequestlabcom.html')
def pccrequestlabcomBACK(request):
    return redirect('labcommworker')
def logout(request):
    request.session.clear()
    return redirect('new')
@no_cache
def workpro(request):
    
    userid=request.session.get('Home1_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home1.objects.get(id=userid)
    except Home1.DoesNotExist:
        return redirect('new')
    user_id=request.session.get('Home1_id')
    User=Home1.objects.get(id=user_id)
    if request.method=='POST':
        mydata=Home1.objects.get(id=User.id)
        fm=worker(request.POST,instance=mydata)
        if fm.is_valid():
            fm.save()
            return redirect('workhome')
    else:
        mydata=Home1.objects.get(id=User.id)
        fm=worker(instance=mydata)
    return render(request,'workerprofile.html',{'fmm1235':fm})
@no_cache
def policepro(request):
    userid=request.session.get('Home2_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home2.objects.get(id=userid)
    except Home2.DoesNotExist:
        return redirect('new')
    user_id=request.session.get('Home2_id')
    User=Home2.objects.get(id=user_id)
    if request.method=='POST':
        mydata=Home2.objects.get(id=User.id)
        fm=police(request.POST,instance=mydata)
        if fm.is_valid():
            fm.save()
            return redirect('policehome')
    else:
        mydata=Home2.objects.get(id=User.id)
        fm=police(instance=mydata)
    return render(request,'policeprofile.html',{'fmm1235':fm})
@no_cache
def insurancepro(request):
    userid=request.session.get('Home3_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home3.objects.get(id=userid)
    except Home3.DoesNotExist:
        return redirect('new')
    user_id=request.session.get('Home3_id')
    User=Home3.objects.get(id=user_id)
    if request.method=='POST':
        mydata=Home3.objects.get(id=User.id)
        fm=insage(request.POST,instance=mydata)
        if fm.is_valid():
            fm.save()
            return redirect('insuranceagencyhome')
    else:
        mydata=Home3.objects.get(id=User.id)
        fm=insage(instance=mydata)
    return render(request,'insuranceprofile.html',{'fmm1235':fm})
@no_cache
def agencypro(request):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    user_id=request.session.get('Home_id')
    User=Home.objects.get(id=user_id)
    if request.method=='POST':
        mydata=Home.objects.get(id=User.id)
        fm=students(request.POST,instance=mydata)
        if fm.is_valid():
            fm.save()
            return redirect('agencyhome')
    else:
        mydata=Home.objects.get(id=User.id)
        fm=students(instance=mydata)
    return render(request,'agencyprofile.html',{'fmm1235':fm})
@no_cache
def applyscheme(request,id):
    user_id=request.session.get('Home1_id')
    User=Home1.objects.get(id=user_id)
    Worker_id=User.id
    stu=SCHOME.objects.filter(id=id)
    for s in stu:
        CURRENTDATE=date.today()
        Scheme_id=s.id
        Home10_instance=Home11(Worker_id=Worker_id,Scheme_id=Scheme_id,CURRENTDATE=CURRENTDATE)
        Home10_instance.save()
    
    return redirect('workersinsurance')
@no_cache
def inschview(request):
    userid=request.session.get('Home3_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home3.objects.get(id=userid)
    except Home3.DoesNotExist:
        return redirect('new')
    stu=Home11.objects.all().values()
    return render(request,'insuranceschemview.html',{'stu':stu})
def deleteDatainschemeview2(request,id):
    myd=Home11.objects.get(id=id)
    myd.delete()
    return redirect('insuranceschemview')
@no_cache
def workschdet(request):
    userid=request.session.get('Home1_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home1.objects.get(id=userid)
    except Home1.DoesNotExist:
        return redirect('new')
    user_id = request.session.get('Home1_id')
    user = Home11.objects.filter(Worker=user_id)
    schemes = [user_obj.Scheme.id for user_obj in user if user_obj.Scheme] if user.exists() else []
    user2 = SCHOME.objects.filter(id__in=schemes)

    # Retrieve the 'CURRENTDATE' field for Home11 objects matching the condition
    current_dates = {user_obj.id: user_obj.CURRENTDATE for user_obj in user}

    # Combine Home11 and SCHOME data into a single list of dictionaries
    combined_data = []
    for stu_obj in user2:
        home11_obj = user.get(Scheme=stu_obj.id)
        combined_data.append({'user': home11_obj, 'stu': stu_obj, 'current_date': current_dates.get(home11_obj.id)})

    return render(request, 'workerschemedetail.html', {'data_list': combined_data})
def deleteDatawoschemeview(request,id,Worker):
    myd=Home11.objects.get(id=id)
    myd.delete()
    return redirect('workerschemedetail')
@no_cache
def policelabourreport(request,id):
    stu=Home1.objects.get(id=id)
    stu.pass_status=1
    stu.save()
    return redirect('labcommworker')
@no_cache
def lcwpov(request):
    # stu=Home1.objects.filter(pass_status='1')
    # s=Home1.objects.get(id=stu.id)
    # s2=Home10.objects.get(Worker_id=s.id)
    # s3=s2.CURRENTDATE
    # stu = Home1.objects.filter(pass_status='1')
    # student_data = []
    userid=request.session.get('Home2_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home2.objects.get(id=userid)
    except Home2.DoesNotExist:
        return redirect('new')

    stu = Home1.objects.filter(pass_status='1')
    
    # student_data = []

    # for student in stu:
    #     try:
    #         s2 = Home10.objects.get(Worker_id=student.id)
    #         current_date = s2.CURRENTDATE
    #     except Home10.DoesNotExist:
    #         current_date = None

    #     student_data.append({'student': student, 'current_date': current_date})

    return render(request, 'policelabourworker.html', {'stu': stu})
    # stu = Home1.objects.filter(pass_status='1').select_related('Home10')
    # return render(request,'policelabourworker.html',{'stu':stu})
# def deletefilepolice(request,id):
#     my=Home12.objects.get(id=id)
#     my.file=None
#     my.save()
#     return redirect('policeuploads',id)
def deletehome12(request,id):
    my=Home12.objects.get(id=id)
    my.delete()
    return redirect('policeuploads')
@no_cache
def policeviewuploads(request):
    userid=request.session.get('Home2_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home2.objects.get(id=userid)
    except Home2.DoesNotExist:
        return redirect('new')
    my=Home12.objects.all().values()
    return render(request,'policeuploads.html',{'stu':my})
@no_cache
def policereportworker(request, id):
    userid=request.session.get('Home2_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home2.objects.get(id=userid)
    except Home2.DoesNotExist:
        return redirect('new')
    user = request.session.get('Home2_id')
    User=Home2.objects.get(id=user)
    if request.method=='POST':
        my=Home1.objects.get(id=id)
        tem= reportpolice(request.POST,request.FILES)
        if tem.is_valid():
            f=tem.save(commit=False)
            f.Worker_id=my.id
            f.police_id=User.id
            f.CURRENTDATE=date.today()
            f.save()
            return redirect('policelabourworker')
    else:
        tem=reportpolice()
    return render(request,'policerreportupload.html',{'f32243':tem})
def policerreportuploadBACK(request):
    return redirect('policelabourworker')
@no_cache
def labcomreportview(request,id):
    userid=request.session.get('Home2_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home2.objects.get(id=userid)
    except Home2.DoesNotExist:
        return redirect('new')
    stu=Home12.objects.get(Worker_id=id)
    return render(request,'policelabourreportdownload.html',{'stu':stu})
@no_cache
def lablabcomreportview(request,id):
    user_id=request.session.get('Home16_id')
    # print("id",user_id)
    if not user_id:
        return redirect('new')
    try:
        User=Home16.objects.get(id=user_id)
    except Home16.DoesNotExist:
        return redirect('new')
    stu=Home12.objects.get(Worker_id=id)
    return render(request,'labourpolicereportdownload.html',{'stu':stu})
def labourpolicereportdownloadback(request):
    return redirect('labcommworker')
def policelabourreportdownloadBACK(request):
    return redirect('policelabourworker')
@no_cache
def agencylabcomreportview(request,id):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    stu=Home12.objects.get(Worker_id=id)
    return render(request,'agencypolicelabourreportdownload.html',{'stu':stu})
def agencypolicelabourreportdownloadBACK(request):
    return redirect('agencyworker')
def BACK(request):
    return redirect('new')
def previous(request):
    return redirect('labourchat')
def previous1(request):
    return redirect('labourcommisionhome')
def previous2(request):
    return redirect('policehome')
def BACK1(request):
    return redirect('new')

def agencyhomebutton(request):
    user_id=request.session.get('Home_id')
    try:
        User=Home.objects.get(id=user_id)
    except Home.DoesNotExist:
        return redirect('new')
    return redirect('agencyhome')
@no_cache
def worattv( request):
    userid=request.session.get('Home1_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home1.objects.get(id=userid)
    except Home1.DoesNotExist:
        return redirect('new')
    user=request.session.get('Home1_id')
    User=Home1.objects.get(id=user)
    stu=Home7.objects.filter(WORKER_id=User).values()
    return render(request,'workerattendanceview.html',{'stu':stu})
@no_cache
def workinsuranceclaim(request,id,id1):
    userid=request.session.get('Home1_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home1.objects.get(id=userid)
    except Home1.DoesNotExist:
        return redirect('new')
    user=request.session.get('Home1_id')
    User=Home1.objects.get(id=user)
    if request.method=='POST':
        my=SCHOME.objects.get(id=id)
        m1=Home11.objects.get(id=id1)
        tem=insuranceworker(request.POST,request.FILES)
        if tem.is_valid():
            f=tem.save(commit=False)
            f.Worker_id=User.id
            f.Scheme_id=my.id
            f.applyscheme_id=m1.id
            f.CURRENTDATE=date.today()
            f.save()
            return redirect('workerschemedetail')
    else:
        tem=insuranceworker()
    return render(request,'workerclaiminsurance.html',{'f3223':tem})
def workerclaiminsuranceBACK(request,id):
    return redirect('workerschemedetail')
@no_cache
def workinsuranceclaimdd(request,id):
    userid=request.session.get('Home3_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home3.objects.get(id=userid)
    except Home3.DoesNotExist:
        return redirect('new')
    stu = Home13.objects.get(id=id)
    return render(request, 'viewclaimworkerinsurancedownload.html', {'stu': stu})
def viewclaimworkerinsurancedownloadBACK(request):
    return redirect('insuranceviewclaimworker')
@no_cache
def inschworkerview(request):
    userid=request.session.get('Home3_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home3.objects.get(id=userid)
    except Home3.DoesNotExist:
        return redirect('new')
    stu=Home13.objects.all().values()
    return render(request,'insuranceviewclaimworker.html',{'stu':stu})
def deleteinsuranceclaim(request,id):
    myd=Home13.objects.get(id=id)
    myd.delete()
    return redirect('insuranceviewclaimworker')
@no_cache
def insuranceagencypayment(request,id):
    userid=request.session.get('Home3_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home3.objects.get(id=userid)
    except Home3.DoesNotExist:
        return redirect('new')
    user=request.session.get('Home3_id')
    User=Home3.objects.get(id=user)
    if request.method=='POST':
        my=Home13.objects.get(id=id)
        my1=SCHOME.objects.get(id=my.Scheme.id)
        print("scheme",my.id)
        print("Insuranceagency_id",User.id)
        tem=paymentinsurance(request.POST)
        if tem.is_valid():
            f=tem.save(commit=False)
            f.Claimscheme_id=my.Scheme.id
            f.Amount=my1.SCHEME_AMOUNT
            f.Date=date.today()
            f.Insuranceagency_id=User.id
            f.save()
            my.payment_status=1
            my.save()
            return redirect('insuranceviewclaimworker')
        
    else:
        tem=paymentinsurance()
    return render(request,'viewclaimworkerinsurancepayment.html',{'f322334':tem})
def viewclaimworkerinsurancepaymentBACK(request):
    return redirect('insuranceviewclaimworker')
@no_cache
def inspaymentview(request):
    userid=request.session.get('Home3_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home3.objects.get(id=userid)
    except Home3.DoesNotExist:
        return redirect('new')
    stu=Home14.objects.all().values()
    return render(request,'insuranceviewpayment.html',{'stu':stu})
@no_cache
def lbouchat(request):
    user_id=request.session.get('Home16_id')
    # print("id",user_id)
    if not user_id:
        return redirect('new')
    try:
        User=Home16.objects.get(id=user_id)
    except Home16.DoesNotExist:
        return redirect('new')
    stu=Home2.objects.all().values()
    return render(request,'labourchat.html',{'stu':stu})
def lbouchat1(request,id):
    user_id=request.session.get('Home16_id')
    # print("id",user_id)
    if not user_id:
        return redirect('new')
    try:
        User=Home16.objects.get(id=user_id)
    except Home16.DoesNotExist:
        return redirect('new')
    stu=Home2.objects.all().values()
    s=Home2.objects.filter(id=id).values()
    s1=Home17.objects.filter(recevierid=id).values()
    s2=Home17.objects.filter(senderid=id).values()
    
    return render(request,'labourchat.html',{'s':s,'stu':stu,'s1':s1,'s2':s2})
  # Make sure to import your Home2 model

def lbouchat2(request, id):
    # Assuming you have a User model, replace it with your actual User model
    user = request.session.get('Home16_id')
    User = Home16.objects.get(id=user)
    user_id=request.session.get('Home16_id')
    # print("id",user_id)
    if not user_id:
        return redirect('new')
    try:
        User=Home16.objects.get(id=user_id)
    except Home16.DoesNotExist:
        return redirect('new')
    
    
    if request.method == 'POST':
        my = Home2.objects.get(id=id)
        message = request.POST.get('message')  # Get the message from the POST data
        
        if message:
            # Create a new Home17 object and save the message
            Home17.objects.create(
                senderid=User.id,
                recevierid=my.id,
                message=message,
                date=datetime.now()
            )
            
            return redirect('lbouchat1', id)
    
    # Handle the case when the message is not provided or the request method is not POST
    return render(request, 'labourchat.html')
def deletehome10(request,id):
    myd=Home10.objects.get(id=id)
    myd.delete()
    my1=myd.Worker.id
    return redirect('labcommworker')
@no_cache
def labviewchat(request):
    user_id=request.session.get('Home16_id')
    # print("id",user_id)
    if not user_id:
        return redirect('new')
    try:
        User=Home16.objects.get(id=user_id)
    except Home16.DoesNotExist:
        return redirect('new')
    stu=Home17.objects.all().values()
    return render(request,'labourviewchat.html',{'stu':stu})
@no_cache
def policechat(request):
    userid=request.session.get('Home2_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home2.objects.get(id=userid)
    except Home2.DoesNotExist:
        return redirect('new')
    user = request.session.get('Home2_id')
    User = Home2.objects.get(id=user)
    # stu=Home2.objects.all().values()
    # s=Home2.objects.filter(id=id).values()
    s1=Home17.objects.filter(recevierid=User.id).values()
    s3=Home2.objects.filter(id=User.id).values()
    s2=Home17.objects.filter(senderid=User.id).values()
    
    return render(request,'policemessage.html',{'s1':s1,'s3':s3,'s2':s2})
def policechat2(request,id):
    user = request.session.get('Home2_id')
    User = Home2.objects.get(id=user)
    if request.method == 'POST':
        message = request.POST.get('message')  # Get the message from the POST data
        
        if message:
            # Create a new Home17 object and save the message
            Home17.objects.create(
                senderid=User.id,
                recevierid=1,
                message=message,
                date=datetime.now()
            )
            
            return redirect('policemessage')
    return render(request,'policemessage.html')
@no_cache
def agencyaddsalaryworker(request, id):
    userid=request.session.get('Home_id')
    # print("id",user_id)
    if not userid:
        return redirect('new')
    try:
        User=Home.objects.get(id=userid)
    except Home.DoesNotExist:
        return redirect('new')
    if request.method == 'POST':
        # Get all Home7 objects for the given worker ID
        home7_instances = Home7.objects.filter(WORKER_id=id)
        
        # Initialize stu2 as a list to store unique currentmonth values
        stu2_list = []
        
        # Collect unique currentmonth values from the queryset
        for home7_instance in home7_instances:
            currentmonth = home7_instance.currentmonth
            if currentmonth not in stu2_list:
                stu2_list.append(currentmonth)
        
        # Get the Home9 object for the given worker ID
        home9_instance = Home9.objects.get(WORKER_id=id)
        
        # Get the job category from Home9
        s1 = home9_instance.JOB_CATEGORY
        
        # Get the salary per day from Home8 based on the job category
        s2 = Home8.objects.get(JOB_CATEGORY=s1)
        s3 = s2.SALARY_PER_DAY
        print("stu3:", s3)
        
        # Get the selected month from the HTML form
        month1 = request.POST.get("month")
        month_to_number = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12,
        }
        print("month1:", month_to_number.get(month1))
        totalsalary = 0
        # Check if the selected month (in numeric format) is in the list of unique currentmonth values
        if month_to_number.get(month1) in stu2_list:
            # Count the number of 'P' (present) attendances for the worker in the selected month
            selected_month_instances = home7_instances.filter(ATTENDANCE='P', currentmonth=month_to_number.get(month1))
            
            # Debugging output
            print("selected_month_instances:", selected_month_instances)
            
            present_count = selected_month_instances.count()
            
            # Debugging output
            print("present_count:", present_count)
        
            totalsalary = present_count * s3
        totalsalary = present_count * s3
        print("stu2:", stu2_list)
        print("totalsalary:", totalsalary)
        
        return render(request, 'agencyaddworkersalary.html', {'stu': totalsalary})
    
    return render(request, 'agencyaddworkersalary.html', {'stu': 0})  # Default value if not a POST request
def agencyaddworkersalaryBACK(request):
    return redirect('agencyworker')
@no_cache

def policeworkercurrentarea(request, id):
    userid = request.session.get('Home2_id')
    if not userid:
        return redirect('new')
    
    try:
        User = Home2.objects.get(id=userid)
    except Home2.DoesNotExist:
        return redirect('new')
    
    user = request.session.get('Home2_id')
    User = Home2.objects.get(id=user)

    try:
        # Retrieve the Home9 object based on the provided 'id'
        stu = Home9.objects.get(WORKER_id=id)
        stu4 = stu.Working_place

        # Retrieve a single Home2 object based on the 'pincode'
        try:
            stu2 = Home2.objects.get(pincode=stu4)
            stu2.Worker_id = stu.WORKER_id
            stu2.save()
        except Home2.DoesNotExist:
            stu2 = None

        # Now, retrieve the Home1 objects and Home9 objects based on the updated Worker_id
        stt4 = []
        stt3 = []

        if stu2 is not None:
            worker_id = stu2.Worker_id
            stt4 = Home9.objects.filter(WORKER_id=worker_id).values()
            stt3 = Home1.objects.filter(id=worker_id).values()

        return render(request, 'policeworkercurrentareajoin.html', {'stu': stt3, 'stu1': stt4})
    except Home9.DoesNotExist:
        # Redirect to 'police_labourworker' if Home9 query returns no results
        return redirect('policelabourworker')



def policeworkercurrentareajoinBACK(request):
    return redirect('policelabourworker')
def labourcardupload(request, id):
    user_id=request.session.get('Home16_id')
    # print("id",user_id)
    if not user_id:
        return redirect('new')
    try:
        User=Home16.objects.get(id=user_id)
    except Home16.DoesNotExist:
        return redirect('new')
    my=Home1.objects.get(id=id)
    if request.method=='POST':
        
        tem= cardupload(request.POST,request.FILES)
        if tem.is_valid():
            f=tem.save(commit=False)
            f.Worker_id=my.id
            f.save()
            return redirect('cardapply')
    else:
        tem=cardupload()
    return render(request,'labourcommissionuploadcard.html',{'f32243':tem})
def labourcommissionuploadcardBACK(request):
    return redirect('cardapply')
def generatecardlcBACK(request):
    return redirect('cardapply')
# def labourcarddownload
def deleteDataworker(request,id):
    myd=Home1.objects.get(id=id)
    myd.delete()
    
    return redirect('workview') 

def deleteDataagency(request,id):
    myd=Home.objects.get(id=id)
    myd.delete()
    
    return redirect('agencyview')
def deleteDatainsagency(request,id):
    myd=Home3.objects.get(id=id)
    myd.delete()
    
    return redirect('insview')
def labourcarddownload(request,id):
    user_id=request.session.get('Home_id')
    try:
        User=Home.objects.get(id=user_id)
    except Home.DoesNotExist:
        return redirect('new')
    stu=Home18.objects.filter(Worker_id=id).all()
    return render(request,'agencylabourcommissiondownloadcard.html',{'stu':stu})
def agencylabourcommissiondownloadcardBACK(request):
    return redirect('agencyworker') 

    

    
    
    
    
        
    
    
    

    
   
    
    

    
   


    
   
    
    
    
    
    
   
    
        
   
        

    

# Create your views here.
