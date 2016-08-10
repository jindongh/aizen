#!/bin/env python

import sets
import sys

class Dicts:
	def __init__(self):
		self.appids=[]
		self.appnames={}
		self.otherids=[]
		self.othernames={}
	def add_name(self, field_type, field_name, value):
		field_key = field_type + "." + field_name
		if field_key in self.othernames:
			raise 'Duplicate name: %s' % name
		self.othernames[field_key] = value
	def add_appname(self, name, value):
		if name in self.appnames:
			raise 'Duplicate app name: %s' % name
		self.appnames[name] = value
def normalize(ds):
	dicts=Dicts()
	print '\tNormalize device'
	ds = normalize_field(ds, 'device', dicts)
	print '\tNormalize phoneinfo'
	ds = normalize_field(ds, 'phoneinfo', dicts)
	print '\tNormalize isroot'
	ds = normalize_field(ds, 'isroot', dicts, {'1':1,1:1,'0':0,0:0})
	print '\tNormalize nettype'
	ds = normalize_field(ds, 'nettype', dicts, {'1':1,1:1,'0':0,0:0})
	print '\tNormalize addr'
	ds = normalize_field(ds, 'addr', dicts)
	print '\tPrepare normalize appNames'
	appNameSet=sets.Set()
	ds['appNames'].apply(lambda x : appNameSet.update(x.split(',')))
	appId=0
	print '\tNormalize appNames'
	for appName in appNameSet:
		dicts.appnames[appName] = 'appid_%d' % appId
		ds.loc[:,'appid_%d' % appId] = map(lambda x: appName in x.split(',') and 1 or 0, ds['appNames'])
		dicts.appids.append('appid_%d' % appId)
		appId += 1
		sys.stdout.write('.')
	print '\tNormalize over'
	return ds,dicts

def normalize_field(ds, field_name, dicts, field_limits=None):
	# remove rows with bad format
	if not field_limits is None:
		rows_before = ds.shape[0]
		ds = ds.loc[ds[field_name].isin(field_limits.keys())]
		print 'Records lost for filter %s %d' % (field_name, rows_before - ds.shape[0])
		ds.loc[:, field_name + '_id'] = map(lambda x: field_limits[x], ds[field_name])
	####### normalize fields:
	else:
		field_id = 0
		for field_type in ds[field_name].unique():
			dicts.add_name(field_name, field_type, field_id)
			field_id += 1
		ds.loc[:, field_name + '_id'] = map(lambda x: dicts.othernames[field_name + "." + x], ds[field_name])
	dicts.otherids.append(field_name + '_id')
	return ds

