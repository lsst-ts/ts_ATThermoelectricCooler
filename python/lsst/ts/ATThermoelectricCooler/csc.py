from lsst.ts import salobj
import SALPY_ATThermoelectricCooler
import asyncio
import enum


class ChillerDetailedState(enum.IntEnum):
    CHILLER_RUNNING = 1
    CHILLER_STOPPED = 2

class ChillerCSC(salobj.BaseCsc):
    async def do_setTemperature(self,id_data):
    """ Sets the target temperature for the chiller

                Parameters
                ----------
                temperature : float

                Returns
                -------
                None
            """
        pass

    async def do_powerChillerOn(self,id_data):
        """ Powers chiller on

                Parameters
                ----------
                None

                Returns
                -------
                None
            """
        pass

    async def do_powerChillerOff(self,id_data):
        """ powers chiller off

                Parameters
                ----------
                None

                Returns
                -------
                None
            """
        pass

    def implement_simulation_mode(self,sim_mode):
        """ enables/disables simulation mode. 

                Parameters
                ----------
                sim mode: 0 for false, anything else for true

                Returns
                -------
                None
            """
        pass

    async def telemetry_loop(self):
        """ Publish Chiller Telemetry. This includes:
                    coolant temperature
                    fan speed
                    possibly other things
                    

                Parameters
                ----------
                None

                Returns
                -------
                None
            """
        pass

    async def event_loop(self):
        """ Publish Listens for chiller events, like errors and warnings.
            This uses the chiller's watchdog functionality, which returns
            a 4-digit code summarizing the status of the device. The four 
            digits represent control status, pump status, alarm status,
            and warning status, respectively. 

            control status:
                0 = auto-start
                1 = standby
                2 = run
                3 = safety
                4 = test
            pump status:
                0 = pump off
                1 = pump on
            alarm status:
                0 = no alarm
                1 = alarm present
            warning status:
                0 = no warning
                1 = warning present

            


                Parameters
                ----------
                None

                Returns
                -------
                None
            """
        pass