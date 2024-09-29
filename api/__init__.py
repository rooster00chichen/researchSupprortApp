from flask import Blueprint, jsonify, request, url_for
from researchSupprortApp.api.operate import *

api=Blueprint("api",__name__)

@api.post("/")
def index():
  return jsonify({"column":"value"}),201

@api.post("/controll_stage/op",endpoint="ct_stage_op")
def cs_cheak():
  is_op=str(op.is_op)
  if request.json['mode']=="cheak":
    return jsonify({"is_op":is_op}),201
  elif request.json['mode']=="controll":
    if op.is_op:
      return jsonify({"is_op":is_op,})
    ct_type=request.json['type']
    return jsonify({"is_op":is_op,"type":ct_type})
  elif request.json['mode']=="dev":
    return jsonify({"is_op":'True',})
  else:
    return jsonify({"aisatu":"hello"}),201

@api.post("/dev")
def dev():
  a=request.data.decode("utf-8")
  return jsonify({"request":a}),201

@api.post("/controll_stage/home")
def ccshome():
  pass