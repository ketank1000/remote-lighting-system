from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.template import RequestContext, loader, Context
from django.shortcuts import render_to_response
#from django.contrib.gis.utils import GeoIP
from auth.models import ledsgroup
from auth.models import leds
from auth.models import group_name

def home(request):
    user = ''
    if 'user' in request.session:
        username = request.session['user']
        """template = loader.get_template('profile/user_home.html')
        context = RequestContext(request, {'username': username})
        #context = RequestContext(request, {'username': request.COOKIES['user']})
        return HttpResponse(template.render(context))"""
        return HttpResponseRedirect('/user_home/')
    template = loader.get_template('auth/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def blog(request):
    template = loader.get_template('auth/blog.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def about(request):
    template = loader.get_template('auth/about.html')
    context = Context(request)
    return HttpResponse(template.render(context))

def contact(request):
    template = loader.get_template('auth/contact.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def register(request):
    template = loader.get_template('auth/register.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))




#profile requests


    #if 'user' in request.COOKIES:
    #    username = request.COOKIES['user']
    #context = RequestContext(request, {'username': request.COOKIES['user']})
    #template = loader.get_template('profile/user_home.html')
    #context = RequestContext(request)
    #return HttpResponse(template.render(context))
    #return HttpResponse("your name is:%s" %request.COOKIES['user'])
    #c = Context({'username': username})
    #return HttpResponse(template.render(c))
    #return render_to_response('profile/user_home.html',{'username' : request.COOKIES['user']})


def group(request):
    username = ''
    user = ''
    if 'show_leds' in request.POST:
        username = ""
        led_list = []
        group_color = ""
        
        username = request.session['user']
        groupname = request.POST.get('groupname')
        a = ledsgroup.objects.filter(groupname=groupname)
        
        for i in a:
            group_color = i.groupcolor      
        leds_main = leds.objects.filter(username=username)

        for i in a:
            for led in leds_main:
                if i.name == led.name:
                    led_list.append(led)

        led = leds.objects.filter(username=username)
        ledgroup = group_name.objects.filter(username=username)
        leds_in_group = ledsgroup.objects.filter(username=username)
        template = loader.get_template('profile/tempgr.html')
        context = RequestContext(request, {'leds_list': led_list, 'group_color':group_color, 'led':led, 'username': username,'ledgroup':ledgroup, 'leds_in_group':leds_in_group})
        return HttpResponse(template.render(context))
        #return render_to_response('profile/tempgr.html',{'leds_list': led_list, 'group_color':group_color, 'led':led,'username': username,'ledgroup':ledgroup})
        
    elif 'user' in request.session:
        username = request.session['user']
        template = loader.get_template('profile/tempgr.html')
        led = leds.objects.filter(username=username)
        #ledgroup = ledsgroup.objects.filter(username=username).values_list('groupname',flat=True).distinct()
        ledgroup = group_name.objects.filter(username=username)
        leds_in_group = ledsgroup.objects.filter(username=username)
        context = RequestContext(request, {'username': username, 'led':led, 'ledgroup':ledgroup, 'leds_in_group':leds_in_group})
        return HttpResponse(template.render(context))
    else:
        return HttpResponseRedirect('/login/')
    

def view(request):
    username = ''
    user = ''
    flag=0;
    if 'show_leds' in request.POST:
        username = ""
        led_list = []
        group_color = ""
        flag=1;
        username = request.session['user']
        groupname = request.POST.get('groupname')
        a = ledsgroup.objects.filter(groupname=groupname)
        
        for i in a:
            group_color = i.groupcolor      
        leds_main = leds.objects.filter(username=username)

        for i in a:
            for led in leds_main:
                if i.name == led.name:
                    led_list.append(led)

        led = leds.objects.all()
        ledgroup = group_name.objects.filter(username=username)
        template = loader.get_template('profile/view.html')
        context = RequestContext(request, {'leds_list': led_list, 'group_color':group_color, 'led':led,'username': username,'ledgroup':ledgroup,'flag':flag})
        return HttpResponse(template.render(context))
        #return render_to_response('profile/tempgr.html',{'leds_list': led_list, 'group_color':group_color, 'led':led,'username': username,'ledgroup':ledgroup})
        
    if 'user' in request.session:
        username = request.session['user']
        template = loader.get_template('profile/view.html')
        led = leds.objects.filter(username=username)
        #ledgroup = ledsgroup.objects.filter(username=username).values_list('groupname',flat=True).distinct()
        ledgroup = group_name.objects.filter(username=username)
        context = RequestContext(request, {'username': username, 'led':led, 'ledgroup':ledgroup,'flag':flag})
        return HttpResponse(template.render(context))
    else:
        return HttpResponseRedirect('/login/')

def user_contact(request):
    username = ''
    user = ''
    if 'user' in request.session:
        username = request.session['user']
        template = loader.get_template('profile/user_contact.html')
        context = RequestContext(request, {'username': username})
        return HttpResponse(template.render(context))
    else:
        return HttpResponseRedirect('/login/')

def settings(request):
    template = loader.get_template('profile/settings.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def temp(request):
    template = loader.get_template('profile/temp.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def temp1(request):
    template = loader.get_template('profile/temp1.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def tempgr(request):
    template = loader.get_template('profile/tempgr.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def automation(request):
    if 'user' in request.session:
        username = request.session['user']
        template = loader.get_template('profile/temp1.html')
        led = leds.objects.filter(username=username)
        #ledgroup = ledsgroup.objects.filter(username=username).values_list('groupname',flat=True).distinct()
        ledgroup = group_name.objects.filter(username=username)
        context = RequestContext(request, {'username': username, 'led':led, 'ledgroup':ledgroup})
        return HttpResponse(template.render(context))
    else:
        return HttpResponseRedirect('/login/')

def edit(request):
    if 'user' in request.session:
        username = request.session['user']
        template = loader.get_template('profile/edit.html')
        led = leds.objects.filter(username=username)
        #ledgroup = ledsgroup.objects.filter(username=username).values_list('groupname',flat=True).distinct()
        ledgroup = group_name.objects.filter(username=username)
        context = RequestContext(request, {'username': username, 'led':led, 'ledgroup':ledgroup})
        return HttpResponse(template.render(context))
    else:
        return HttpResponseRedirect('/login/')
