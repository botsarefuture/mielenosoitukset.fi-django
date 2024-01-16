from django.shortcuts import render
from .models import Protest, Participant

def protest_list(request):
    protests = Protest.objects.all()
    return render(request, 'protest_list.html', {'protests': protests})

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'participant_list.html', {'participants': participants})

# protests/views.py
from django.shortcuts import render, get_object_or_404
from .models import Protest

def protest_detail(request, protest_id):
    protest = get_object_or_404(Protest, pk=protest_id)
    return render(request, 'protest_detail.html', {'protest': protest})

from django.shortcuts import render, redirect
from .forms import ProtestForm

def create_protest(request):
    if request.method == 'POST':
        form = ProtestForm(request.user, request.POST)
        if form.is_valid():
            # Save the form with the current user as the organizer
            protest = form.save(commit=False)
            protest.save()
            return redirect('protest_detail', protest_id=protest.pk)
    else:
        form = ProtestForm(request.user)

    return render(request, 'create_protest.html', {'form': form})

def edit_protest(request, pk):
    protest = get_object_or_404(Protest, pk=pk)
    if request.method == 'POST':
        form = ProtestForm(request.user, request.POST, instance=protest)
        if form.is_valid():
            # Save the form with the current user as the organizer
            protest = form.save(commit=False)
            protest.organizers.add(request.user.organization)  # Assuming the user has an organization attribute
            protest.save()
            return redirect('protest_detail', pk=protest.pk)
    else:
        form = ProtestForm(request.user, instance=protest)

    return render(request, 'edit_protest.html', {'form': form, 'protest': protest})

# protests/views.py
from django.shortcuts import render

def front_page(request):
    demonstrations = Protest.objects.all()
    return render(request, 'front_page.html', {'demonstrations': demonstrations})
