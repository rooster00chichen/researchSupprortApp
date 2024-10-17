from researchSupprortApp.controll_stage import *
import asyncio

class Operate_stage:
  def __init__(self) -> None:
    self.op=Controll_stage()
    self.move_val=2000
    self.now_pos=0

  def move_pos(self,num):
    self.op.is_op=False
    self.move_val=abs(num)
    self.now_pos=self.op.move_possition(num)
    self.op.is_op=True
    return [num,self.now_pos]
  
  def reset_pos(self):
    self.op.is_op=False
    self.move_pos_val=self.op.reset_posittion()
    self.op.is_op=True
    return self.move_pos_val

  def start_shake_pos(self):
    print("start")
    self.op.is_op=False
    self.op.is_shake=True
    self.op.move_shake_pos()

  def stop_shake_pos(self):
    self.op.is_shake=False
    self.op.is_op=True

  def get_op_status(self):
    return self.op.is_op
  def get_now_move_val(self):
    return self.move_val
  def get_now_pos(self):
    return self.now_pos