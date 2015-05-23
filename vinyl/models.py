#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from django.db import models
from PIL import Image


class Album(models.Model):
	'''
	Informacje o albumie
	'''
	CONDITION = (
		('M', 'Mint'),
		('NM', 'Near Mint'),
		('EX', 'Excelent'),
		('EX_PLUS', 'Excelent+'),
		('EX_MINUS', 'Excelent-'),
		('VG_PLUS', 'Very Good+'),
		('VG', 'Very Good'),
		('G_PLUS', 'Good+'),
		('G', 'Good'),
		('P', 'Poor'),
	)
	artist = label = models.ForeignKey('Artist', verbose_name='Artysta')
	title = models.CharField('Tytuł albumu', max_length=100)
	label = models.ForeignKey('Label', verbose_name='Label')
	catalog_number = models.CharField('Numer katalogowy', 
										max_length=50, 
										blank=True, 
										null=True)
	discog_url = models.CharField('Link do Discogs', 
										max_length=250, 
										blank=True, 
										null=True)
	disk = models.ForeignKey('Disk', verbose_name='Nośnik')
	price = models.DecimalField('Cena', max_digits=5, 
								decimal_places=2, 
								default=0)
	vinyl_condition = models.CharField('Stan nośnika', 
										max_length=15, 
										choices=CONDITION, 
										default='VG')
	cover_condition = models.CharField('Stan okładki', 
										max_length=15, 
										choices=CONDITION,
										default='VG')
	first_press = models.BooleanField('Pierwsze wydanie',
										default=False)
	source = models.CharField('Źródło zakupu', 
										max_length=50,
										default='Allegro',
										blank=True, 
										null=True)
	cover = models.ImageField('Okładka', 
								upload_to='cover',
								default='cover/no_cover.jpg', 
								blank=True, 
								null=True)
	# realease_year = models.DateField('Data wydania', blank=True, null=True)
	notes = models.CharField('Uwagi', 
							max_length=250, 
							blank=True, 
							null=True)
	publish_date = models.DateTimeField('Data wpisu')


	def __str__(self):              # __unicode__ on Python 2
		return ("%s - %s / %s") % (self.artist, self.title, self.label)

	def save(self):
		'''
		Przy zapisie zminiejsz wielkość okładki do 300px
		'''
		if not self.id and not self.cover:
			return            

		super(Album, self).save()

		image = Image.open(self.cover)
		(width, height) = image.size

		"Max width and height 800"        
		if (300 / width < 300 / height):
			factor = 300 / height
		else:
			factor = 300 / width

		size = ( int(width * factor), int(height * factor))
		image = image.resize(size, Image.ANTIALIAS)
		image.save(self.cover.path)


class Artist(models.Model):
	'''
	Informacje o artyście, strona www opcjonalna
	'''
	name = models.CharField('Artysta', max_length=100)
	url = models.CharField('Strona WWW', max_length=100, blank=True, null=True)

	def __str__(self):              # __unicode__ on Python 2
		return str(self.name)


class Disk(models.Model):
	'''
	Nosnik - stan nośnika i okladki, cena, wymiary fizyczne
	'''
	SIZE = (
		(' ', 'Brak'),
		('12', "12"),
		('7', "7"),
	)
	SPEED = (
		(' ', 'Brak'),
		('33', '33 1/3'),
		('45', '45')
		)
	FORMAT = (
		('CD', 'Compact Disk'),
		('LP', 'Vinyl')
	)
	size = models.CharField('Rozmiar nośnika',
								max_length=4,
								default=12,
								choices=SIZE)
	speed = models.CharField('Prędkość',
								max_length=6,
								default=33,
								choices=SPEED)
	format_disk = models.CharField('Format nośnika',
								max_length=12,
								default='LP',
								choices=FORMAT)
	dmm = models.BooleanField('Digital Metal Mastering', default=False)
	
	def __str__(self):              # __unicode__ on Python 2
		if self.dmm == True:
			_dmm = 'DMM'
		else:
			_dmm = ''
		if self.size != ' ':
			self.size = self.size + "''"
		return str("%s %s %s %s") % (self.format_disk, _dmm, self.size, self.speed)


class Label(models.Model):
	'''
	Label - wytwórnia, producent, rok wydania
	'''
	name = models.CharField('Wydawca', max_length=50)
	url = models.CharField('Strona WWW', max_length=100, blank=True, null=True)

	def __str__(self):              # __unicode__ on Python 2
		return str(self.name)
	