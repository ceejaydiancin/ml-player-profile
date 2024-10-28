from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Player
from .forms import PlayerForm

@login_required
def player_list(request):
    players = Player.objects.all()
    return render(request, 'profiles/player_list.html', {'players': players})

@login_required
def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'profiles/add_player.html', {'form': form})

@login_required
def edit_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'profiles/edit_player.html', {'form': form})

@login_required
def delete_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        player.delete()
        return redirect('player_list')
    return render(request, 'profiles/delete_player.html', {'player': player})
