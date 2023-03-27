import pyvisa as visa

rm = visa.ResourceManager()
print(rm.list_resources())
keithley = rm.open_resource(rm.list_resources()[0])
keithley.write("smua.source.levelv = 0.5")
keithley.write("display.smua.measure.func = display.MEASURE_DCAMPS")
keithley.write("smua.source.output = smua.OUTPUT_ON")