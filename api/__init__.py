from flask import Blueprint, jsonify, request, url_for
from researchSupprortApp.api.operate import *

api=Blueprint("api",__name__)
op=Operate()

@api.post("/")
def index():
  return jsonify({"column":"value"}),201

@api.post("/controll_stage/op",endpoint="ct_stage_op")
def cs_cheak():
  is_op=op.get_op_status()
  if request.json['mode']=="cheak":
    return jsonify({"is_op":is_op}),201
  elif request.json['mode']=="controll":
    ct_type=request.json['type']
    if not is_op:
      return jsonify({"is_op":is_op,"type":ct_type})
    if ct_type=="up":
      move_val=op.get_now_move_val()
      result = op.move_ops(move_val)
    elif ct_type=="down":
      move_val=-1*op.get_now_move_val()
      result=op.move_ops(move_val)
    else:
      result=["none","none"]
    return jsonify({"is_op":is_op,"type":ct_type,"result":result})
  elif request.json['mode']=="dev":
    return jsonify({"is_op":True,})
  else:
    return jsonify({"aisatu":"hello"}),201

@api.post("/dev")
def dev():
  a=request.data.decode("utf-8")
  return jsonify({"request":a}),201

@api.post("/controll_stage/home")
def ccshome():
  pass