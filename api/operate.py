from researchSupprortApp.controll_stage import *

class Operate:
  def __init__(self) -> None:
    self.op=Controll_stage()
    self.move_pos_val=2000
    self.now_pos=0

  def move_pos(self,num):
    self.move_pos_val=num
    self.now_pos=self.op.move_possition()
    return [self.move_pos_val,self.now_pos]
  
  def reset_pos(self):
    self.move_pos_val=self.op.reset_posittion()
    return self.move_pos_val

  def get_op_status(self):
    return self.op.is_op
  def get_now_move_val(self):
    return self.move_val
  def get_now_pos(self):
    return self.now_pos