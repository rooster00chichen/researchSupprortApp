import pyvisa as visa
from time import sleep

class Controll_stage:
  def __init__(self) -> None:
    # GPIB接続設定
    rm = visa.ResourceManager('@py')
    try:
      self.stage = rm.open_resource("GPIB0::8::INSTR")
      # initialize
      n = 201  # x movement for n times
      # move to -point
      self.stage.write("D:1S10F1000R10")
      sleep(500*10**-3)
      print("can operate stage" if self.stage.read() == "OK" else "test3")
      self.changeOfPosition = 0
      self.is_op=True
      self.is_shake=False
    except:
      self.is_op=False
  
  def cheak_flag(self):
    self.stage.write("!:")
    judge=self.stage.read()
    if judge == "R":
      self.is_op=True
    else:
      self.is_op=False

  def move_signal_submit(self,move_val,target=1):
    if move_val >= 0:
        sig = "M:"+str(target)+"+P"+str(abs(move_val))
    elif move_val <= 0:
        sig = "M:"+str(target)+"-P"+str(abs(move_val))
    self.stage.write(sig)
    print("send the request" if self.stage.read() == "OK" else "test1")
    self.stage.write("G:")
    print("start move" if self.stage.read() == "OK" else "test2")
    while True:
        self.stage.write("!:")
        judge = self.stage.read()
        if judge == "R":
            break
        sleep(50*10**-3)
    print("can operate")
    return move_val
  
  def move_possition(self,move_val):
    self.changeOfPosition += self.move_signal_submit(move_val)
    return self.changeOfPosition
  def reset_posittion(self):
    if self.changeOfPosition != 0:
      self.changeOfPosition += self.move_signal_submit(self.changeOfPosition*-1)
    return self.changeOfPosition

  def move_shake_pos(self,move_val = 20000):
    print("start shake")
    start = self.move_signal_submit(abs(move_val)/2*-1)
    while self.is_shake:
      a=self.move_signal_submit(abs(move_val))
      b=self.move_signal_submit(-1*abs(move_val))
    stop =  start = self.move_signal_submit(abs(move_val)/2)
    print("end shake")