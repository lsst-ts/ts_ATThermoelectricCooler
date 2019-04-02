
import binascii

class ChillerPacketEncoder(object):
    def __init__(self)
        self.ip = "123.234.33.10"
        self.device_id = "01"


    def _checksum(self, st):
        """
        Checksum field shall be two ASCII hexadecimal bytes
        represeiting the sum of all previous bytes (8 bit 
        summation, no carry) of the command starting with SOC
        
        Parameters
        ----------
        st : ascii string to be checksummed

        Returns
        -------
        checksum : 2-character ascii string
        """
        
        total = 0x0
        for ch in st:
            total = total + int(binascii.hexlify(ch), 16)
        return hex(total)[-2:]

    def _commandwrapper(self, st):
        """
        Command packets begin with a period character and
        device ID, and end with a checksum and a carriage 
        return. This function takes a string and assembles
        the boilerplate around it. 
        
        Parameters
        ----------
        st : 10-character ascii string containing the 
             command ID followed by 8 chars of 
             descriptive text

        Returns
        -------
        string
    
        """
        if len(st) != 10:
            raise Exception

        start = "." + self.device_id + str
        cs = self._checksum(start)
        return start + cs + "\r"

        


    def watchdog(self):
        """
        Generates the ascii string that requests a watchdog
        packet from the Chiller.
        
        Parameters
        ----------
        None

        Returns
        -------
        string
    
        """
        message = "01WatchDog"
        return self._commandwrapper(message)