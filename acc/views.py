from django.shortcuts import render, redirect
from acc.models import Operation
from main.models import Profile, Site
from django.db.models import Q


def delete_operation(request):
    if request.method == 'POST':
        operation = Operation.objects.get(id=request.POST.get('id'))
        operation.delete()
        # if not operation.operation_approval:
        #     operation.delete()

        return redirect('acc:managing_site_details' ,name=request.POST.get('site_name'))
    return redirect('acc:managing_site_details',name=request.POST.get('site_name'))


def acc_manager(request):
    prof = Profile.objects.get(user=request.user)
    if prof.job == 'رئيس مجلس ادراه':
        sites = Site.objects.all()
    else:
        sites = prof.site.all()
    return render(request, 'acc/acc_manager.html', {'sites': sites})


def managing_site_detail(request, name):
    prof = Profile.objects.get(user=request.user)
    site = Site.objects.get(name=name)
    operations = Operation.objects.filter(site=site)
    if request.method == 'POST':
        operation_status = request.POST.get('operation_status')
        site = site
        operation_name = request.POST.get('operation_name')
        operation_amount = request.POST.get('operation_amount')
        operation_document = request.FILES.get('operation_document')
        # if operation_status == 'ايداع':
        ooperation = Operation.objects.create(profile=prof, operation_status=operation_status,
                                              operation_name=operation_name,
                                              site=site,
                                              operation_amount=operation_amount,
                                              operation_document=operation_document,
                                              operation_approval=True
                                              )
        ooperation.save()
        return redirect('acc:managing_site_details', name=name)
    return render(request, 'acc/managing_site_details.html', {'site': site, 'operations': operations, })
