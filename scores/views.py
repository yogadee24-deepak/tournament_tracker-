from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Match

# --- AUTHENTICATION ---
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'scores/register.html', {'form': form})

# --- CRUD: READ ---
@login_required
def match_list(request):
    # Shows only the matches created by the logged-in user
    matches = Match.objects.filter(user=request.user).order_by('match_date')
    return render(request, 'scores/match_list.html', {'matches': matches})

# --- CRUD: CREATE ---
@login_required
def add_match(request):
    if request.method == 'POST':
        Match.objects.create(
            user=request.user,
            team_one=request.POST.get('team_one'),
            team_two=request.POST.get('team_two'),
            team_one_score=request.POST.get('team_one_score', 0),
            team_two_score=request.POST.get('team_two_score', 0),
            match_status=request.POST.get('match_status'),
            match_date=request.POST.get('match_date')
        )
        messages.success(request, 'Match tracked successfully!')
        return redirect('match_list')
    return render(request, 'scores/match_form.html', {'title': 'Add New Match'})

# --- CRUD: UPDATE ---
@login_required
def edit_match(request, match_id):
    match = get_object_or_404(Match, id=match_id, user=request.user)
    if request.method == 'POST':
        match.team_one = request.POST.get('team_one')
        match.team_two = request.POST.get('team_two')
        match.team_one_score = request.POST.get('team_one_score')
        match.team_two_score = request.POST.get('team_two_score')
        match.match_status = request.POST.get('match_status')
        match.match_date = request.POST.get('match_date')
        match.save()
        messages.success(request, 'Match scores updated!')
        return redirect('match_list')
    
    # Format date for the HTML datetime-local input field
    formatted_date = match.match_date.strftime('%Y-%m-%dT%H:%M')
    return render(request, 'scores/match_form.html', {'match': match, 'formatted_date': formatted_date, 'title': 'Update Scores'})

# --- CRUD: DELETE ---
@login_required
def delete_match(request, match_id):
    match = get_object_or_404(Match, id=match_id, user=request.user)
    if request.method == 'POST':
        match.delete()
        messages.success(request, 'Match removed from tracker.')
    return redirect('match_list')
