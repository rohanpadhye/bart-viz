#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import urllib.request

import google.protobuf.json_format
import gtfs_realtime_pb2 as gtfs

import cgitb
cgitb.enable()


msg = gtfs.FeedMessage()

bart_realtime_url = "http://api.bart.gov/gtfsrt/tripupdate.aspx"

with urllib.request.urlopen(bart_realtime_url) as pb:
	msg.ParseFromString(pb.read())
	for d in msg.entity:
		del d.trip_update.stop_time_update[1:] # Only keep the first update
	print("Content-Type: text/json;charset=utf-8")
	print()
	print(google.protobuf.json_format.MessageToJson(msg))