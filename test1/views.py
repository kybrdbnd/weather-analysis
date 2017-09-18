from django.shortcuts import render, redirect
import urllib
import json
from datetime import datetime
from .models import StationModel
# from .forms import (WeatherForm)

# Create your views here.

def home(request):
	return render(request,'home.html',{})

def get_api_key():
	config = json.loads(open('./key.json').read())
	return config["key"]

def get_weather_form(params):
	location = params.get('location')
	start_date = params.get('start_date')
	end_date = params.get('end_date')
	data = {
	'location' : location,
	'start_date' : start_date,
	'end_date' : end_date 
	}
	return data

def get_weather_data(url):
	f = urllib.request.urlopen(url)
	json_string = f.read().decode('utf-8')
	parsed_json = json.loads(json_string)
	return parsed_json

def construct_url(api_key, url_start_date, url_end_date,location):
	url = 'http://api.wunderground.com/api/%s/planner_%s%s/q/India/%s.json' %(api_key, url_start_date, url_end_date, location)
	# url = 'http://api.wunderground.com/api/0cd57b87979dc788/planner_01010131/q/India/Delhi.json'
	return url

def weather(request):
	if request.method=='POST':
		weather_temp_data = get_weather_form(request.POST)
		url_start_date = datetime.strptime(weather_temp_data['start_date'], '%d %B').strftime('%m%d') 
		url_end_date = datetime.strptime(weather_temp_data['end_date'], '%d %B').strftime('%m%d')
		api_key = get_api_key()
		parsed_json = get_weather_data(construct_url(api_key, url_start_date, url_end_date,weather_temp_data['location']))
		error = parsed_json['trip']['error']
		if len(error) > 0:
			context = {
				'error' : error
			}
			return render(request, 'weather.html', context)
		title = parsed_json['trip']['title']
		temp_high = {
						# 'min': parsed_json['trip']['temp_high']['min']['C'],
						'max': parsed_json['trip']['temp_high']['max']['C']
					}
		temp_low = {
						# 'min': parsed_json['trip']['temp_low']['min']['C'],
						'max': parsed_json['trip']['temp_low']['max']['C']
					}
		graph_data = [{'data': [['Celcius', temp_high['max']]], 'name': 'Highest Temperature'},
 					{'data': [['Celcius', temp_low['max']]], 'name': 'Lowest Temperature'}]
		context = {
			'title': title,
			'graph_data': graph_data
		}
		# print(construct_url(api_key, url_start_date, url_end_date,weather_temp_data['location']))
		return render(request, 'weather.html',context)
	return render(request,'weather.html',{})

def construct_station_url(api_key, location):
	url = 'http://api.wunderground.com/api/%s/geolookup/q/India/%s.json' % (api_key, location)
	# url = 'http://api.wunderground.com/api/0cd57b87979dc787/geolookup/q/India/Delhi.json'
	return url

def get_weather_stations(url):
	f = urllib.request.urlopen(url)
	json_string = f.read().decode('utf-8')
	parsed_json = json.loads(json_string)
	return parsed_json

def station(request):
	if request.method=='POST':
		location = request.POST.get('location')
		api_key = get_api_key()
		parsed_json = get_weather_stations(construct_station_url(api_key, location))
		weather_stations = parsed_json['location']['nearby_weather_stations']['pws']['station']
		context = {
			'weather_stations': weather_stations
		}
		return render(request, 'station.html', context)
	return render(request,'station.html',{})


def save_stations(request):
	if request.method=='POST':
		get_stations = request.POST.getlist('stations[]')
		for station in get_stations:
			s = StationModel.objects.filter(station_name=station)
			if not s:
				StationModel.objects.create(station_name=station)
	return redirect('test1:station')