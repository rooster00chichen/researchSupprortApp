from researchSupprortApp.api import api
from researchSupprortApp.api.operate_stage import *
from flask import jsonify, request

op_stage=Operate_stage()

@api.post("/controll_stage/home",endpoint="ct_stage_op")
def cs_cheak():
  is_op=op_stage.get_op_status()
  
  if request.json['mode']=="cheak":
    return jsonify({"is_op":is_op}),201
  elif request.json['mode']=="controll":
    ct_type=request.json['type']
    if not is_op:
      return jsonify({"is_op":is_op,"type":ct_type})
    if ct_type=="up":
      move_val=op_stage.get_now_move_val()
      result = op_stage.move_pos(move_val)
    elif ct_type=="down":
      move_val=-1*op_stage.get_now_move_val()
      result=op_stage.move_pos(move_val)
    else:
      result=["none","none"]
    return jsonify({"is_op":is_op,"type":ct_type,"result":result})
  elif request.json['mode']=="shake":
    state = request.json["type"]
    if state == "start":
      op_stage.start_shake_pos()
    elif state=="stop":
      op_stage.stop_shake_pos()
    return jsonify({"is_op":is_op,"type":state})
  elif request.json['mode']=="dev":
    return jsonify({"is_op":True,})
  else:
    return jsonify({"aisatu":"hello"}),201