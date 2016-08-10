#!/bin/env python

import sets

class Dicts:
	def __init__(self):
		self.appids=[]
		self.appnames={}
		self.otherids=[]
		self.othernames={}
	def add_name(self, name, value):
		if name in self.othernames:
			raise 'Duplicate name: %s' % name
		self.othernames[name] = value
	def add_appname(self, name, value):
		if name in self.appnames:
			raise 'Duplicate app name: %s' % name
		self.appnames[name] = value
def normalize(ds):
	dicts=Dicts()
	ds = normalize_field(ds, 'device', dicts)
	ds = normalize_field(ds, 'phoneinfo', dicts)
	ds = normalize_field(ds, 'isroot', dicts, {'1':1,1:1,'0':0,0:0})
	ds = normalize_field(ds, 'nettype', dicts, {'1':1,1:1,'0':0,0:0})
	ds = normalize_field(ds, 'addr', dicts)
	appNameSet=sets.Set()
	ds['apps'].apply(lambda x : appNameSet.update(x.split(',')))
	appId=0
	for appName in appNameSet:
		dicts.appnames[appName] = appId
		ds['appid_'+appId] = map(lambda x: appName in x.split(',') and 1 or 0, ds['appNames'])
		dicts.appnameids.append('appid_'+appId)
		appId += 1
	return ds

def normalize_field(ds, field_name, dicts, field_limits=None):
	# remove rows with bad format
	if not field_limits is None:
		ds = ds.loc[ds[field_name].isin(field_limits.keys())]
		ds[field_name + '_id'] = map(lambda x: field_limits[x], ds[field_name])
	####### normalize fields:
	else:
		field_id = 0
		for field_type in ds[field_name].unique():
			dicts.add_name(field_name, field_id)
			field_id += 1
		ds[field_name + '_id'] = map(lambda x: dicts.othernames[x], ds[field_name])
	dicts.otherids.append(field_name + '_id')
	return ds

