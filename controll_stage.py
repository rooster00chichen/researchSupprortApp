import pyvisa as visa
from time import sleep

class controll_stage:
  def __init__(self) -> None:
    # GPIB接続設定
    rm = visa.ResourceManager('@py')
    self.stage = rm.open_resource("GPIB0::8::INSTR")
    # initialize
    n = 201  # x movement for n times
    # move to -point
    self.stage.write("D:1S10F1000R10")
    sleep(500*10**-3)
    print("can operate stage" if self.stage.read() == "OK" else "test3")
    self.changeOfPosition = 0
    self.move_val=2000
  

  def move_signal_submit(self,move_val):
    if move_val >= 0:
        sig = "M:1+P"+str(abs(move_val))
    elif move_val <= 0:
        sig = "M:1-P"+str(abs(move_val))
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
  
  def move_positive_possition(self):
    self.changeOfPosition += self.move_signal_submit(self.move_val)
  def move_negative_possition(self):
    self.changeOfPosition += self.move_signal_submit(self.move_val*-1)
  def chage_high_move_val(self):
    self.move_val=6000
  def chage_low_move_val(self):
    self.move_val=2000
  def reset_posittion(self):
    if self.changeOfPosition != 0:
      self.changeOfPosition += self.move_signal_submit(self.changeOfPosition*-1)