from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import JsonResponse

# Create your views here.
def app_list(request):
    context={"details":App.objects.all()}
    return render(request, "list.html", context)

def app_form(request,id=0):
    if request.method=="GET":
        if id==0:
            form=App_Form()
        else:
            try:
                # fin=App.objects.get(pk=id)
                instance = get_object_or_404(App,pk=id)
                form=App_Form(instance=instance)
            except App.DoesNotExist:
                return JsonResponse({'status':'error','Message':"Details Not Found"}, status=404)
        return render(request, "form.html", {'form':form})
    else:
        if id==0:
            form=App_Form(request.POST)
        else:
            try:
                # fin=App.objects.get(pk=id)
                instance=get_object_or_404(App, pk=id)
                form=App_Form(request.POST, instance=instance)
            except App.DoesNotExist:
                return JsonResponse({'status':'error', 'Message':"Details Not Found"}, status=404)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({"status":"success"})
            except forms.ValidationError as e:
                return JsonResponse({'status':'error',"errors":e.messages},status=400)

        # return redirect("/list")
        else:
            errors=form.errors.as_json()
            return JsonResponse({'status':"errors","errors":errors},status=400)

def app_delete(request,id=0):
    if request.method=="DELETE":
        try:
            instance=App.objects.get(pk=id)
            instance.delete()
            return JsonResponse({"status":"success"})
            # return redirect("/list")
        except App.DoesNotExist:
            return JsonResponse({"status":"error",",Message":"Details Not Found"}, status=404);
    else:
        return JsonResponse({"status":"error","Message":"Invalid Request"}, status=405)
