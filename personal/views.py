from django.shortcuts import render
from django.http import JsonResponse
from .forms import PersonalForm, ShiftForm
from django.contrib.auth.decorators import login_required

@login_required
def add_personal_and_shift(request):
    if request.method == 'POST':
        personal_form = PersonalForm(request.POST)
        shift_form = ShiftForm(request.POST)
        
        if personal_form.is_valid() and shift_form.is_valid():
            personal_form.save()
            shift_form.save()
            return JsonResponse({'success': True})
        else:
            errors = {}
            errors.update(personal_form.errors)
            errors.update(shift_form.errors)
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        personal_form = PersonalForm()
        shift_form = ShiftForm()
    
    context = {
        'personal_form': personal_form,
        'shift_form': shift_form,
    }
    return render(request, 'personal/personal.html', context)
