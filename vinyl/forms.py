#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms

from .models import Album

class SearchForm(forms.ModelForm):
	# artist_name = forms.CharField(label='Artysta', max_length=100)
	class Meta:
		model = Album
		fields = ('artist',)
