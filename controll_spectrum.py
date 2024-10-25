import pyvisa as visa 


class CT_spectrum:
  def __init__(self):
    rm = visa.ResourceManager()
    self.speana=rm.open_resource("TCPIP::あとで書くアドレス::INSTR")
    