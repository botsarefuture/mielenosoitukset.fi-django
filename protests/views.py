from django.shortcuts import render, redirect, get_object_or_404
from .models import Protest, Participant
from .forms import ProtestForm


def protest_list(request):
    protests = Protest.objects.all()
    return render(request, "protest_list.html", {"protests": protests})


def participant_list(request):
    participants = Participant.objects.all()
    return render(request, "participant_list.html", {"participants": participants})


def protest_detail(request, protest_id):
    protest = get_object_or_404(Protest, pk=protest_id)
    return render(request, "protest_detail.html", {"protest": protest})


def create_protest(request):
    if request.method == "POST":
        form = ProtestForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            # Save the form with the current user as the organizer
            protest = form.save()
            return redirect("protest_detail", protest_id=protest.pk)
    else:
        form = ProtestForm(request.user)

    return render(request, "create_protest.html", {"form": form, "your_google_maps_api_key": "AIzaSyC-LbBEvDRjeHnjXkIZF8J8TVFS7FY_WUc"})


def edit_protest(request, pk):
    protest = get_object_or_404(Protest, pk=pk)
    if request.method == "POST":
        form = ProtestForm(request.user, request.POST, instance=protest)
        if form.is_valid():
            # Save the form with the current user as the organizer
            protest = form.save()

            return redirect("protest_detail", protest_id=protest.pk)
    else:
        form = ProtestForm(request.user, instance=protest)

    return render(request, "edit_protest.html", {"form": form, "protest": protest})


def front_page(request):
    demonstrations = Protest.upcoming_protests.all()
    return render(request, "front_page.html", {"demonstrations": demonstrations})


def delete_protest(request, pk):
    protest = get_object_or_404(Protest, pk=pk)

    if request.method == "POST":
        protest.delete()
        return redirect(
            "protest_list"
        )  # Redirect to the list of protests after deletion

    return render(request, "delete_protest.html", {"protest": protest})
