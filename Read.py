mport RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class RFIDReader:
        def __init__(self):
                self.reader = SimpleMFRC522()

        def read_card(self):
                try:
                        uid = self.reader.read_uid()
                        hex_id = format(int.from_bytes(uid, byteorder='big'),'X>
                        return hex_id
                finally:
                        GPIO.cleanup()
def main():
        reader = RFIDReader()
        hex_id = reader.read_card()
        print(hex_id)

if __name__=="__main__":
        main()
