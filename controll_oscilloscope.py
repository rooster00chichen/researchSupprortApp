import pyvisa as visa
from time import sleep

class Controll_osiro:
  def __init__(self):
    rm = visa.ResourceManager('')
    try:
      self.oscillo=rm.open_resource('TCPIP::<IP_ADDRESS>::1861::SOCKET')
      idn = self.oscillo.query('*IDN?')
      print(f"Connected to: {idn}")
      # Set up the oscilloscope
      self.is_op = True
    except:
      self.is_op=False