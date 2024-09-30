from flask import Blueprint, jsonify, request

api=Blueprint("api",__name__)

#stage用のルーティングしているpyファイルのimport
from researchSupprortApp.api import routing_ct_stage
#osiro用のルーティングのimport


@api.post("/")
def index():
  return jsonify({"column":"value"}),201

@api.post("/dev")
def dev():
  a=request.data.decode("utf-8")
  return jsonify({"request":a}),201