#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Sum
from django.utils import timezone
from .models import Album, Artist, Label
from .forms import SearchForm

def paginate(request, lists):
	paginator = Paginator(lists, 9) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		p_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		p_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		p_list = paginator.page(paginator.num_pages)


def album_list(request):
	'''
	Lista albumów
	'''

	albums_list = Album.objects.order_by('artist') # sortowanie po alfabetyczie po artyście

 	if not request.method == 'POST' and 'page' in request.GET: 
 		if 'search-albums-post' in request.session: 
 			request.POST = request.session['search-albums-post'] 
 			request.method = 'POST'


	if request.method == "POST":
		form = SearchForm(request.POST)
		request.session['search-albums-post'] = request.POST
		del request.session['search-albums-post']
		if form.is_valid():
			artist_form = form.cleaned_data['artist']
			albums_form = Album.objects.filter(artist=artist_form)
			# paginacja
			paginator = Paginator(albums_form, 9) # Show 25 contacts per page
			page = request.GET.get('page')
			try:
				albums = paginator.page(page)
			except PageNotAnInteger:
				# If page is not an integer, deliver first page.
				albums = paginator.page(1)
			except EmptyPage:
				# If page is out of range (e.g. 9999), deliver last page of results.
				albums = paginator.page(paginator.num_pages)

			return render(request, 'vinyl/album_list.html', {'albumy': albums,'form': form})
	else:
		form = SearchForm()

	# paginacja
	paginator = Paginator(albums_list, 9) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		albums = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		albums = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		albums = paginator.page(paginator.num_pages)

	return render(request, 'vinyl/album_list.html', {'albumy': albums,
													'form': form})

def album_detail(request, album_id):
	'''
	Szczegóły albumu
	'''
	album = get_object_or_404(Album, id=album_id)
	label = Label.objects.get(id=album.label_id)
	artist = Artist.objects.get(id=album.artist_id)

	return render(request, 'vinyl/album_detail.html', {'adetail': album,
														'label': label,
														'artist': artist})

def stats(request):
	'''
	Szczegóły kolekcji płyt
	'''
	albums_price = Album.objects.all().aggregate(Sum('price'), Avg('price'))
	albums_count = Album.objects.count()

	return render(request, 'vinyl/stats.html', {'suma': albums_price,
													'ilosc_albumow': albums_count})