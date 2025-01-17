import m5
from m5.objects import *
import random

system = System() #Created the system Object which is the parent of all other objects in our simulated system.

system.clk_domain = SrcClockDomain() #created the clock domain
system.clk_domain.clock = '1GHz' #Set the clock to 1GHz
system.clk_domain.voltage_domain = VoltageDomain() # Set the voltage domain for the clock to default option

system.mem_mode = 'timing' #Used timing mode for the memory simulation
system.mem_ranges = [AddrRange('8192MB')] #Set the single memory range to size 512MB

system.cpu = TimingSimpleCPU() #Created the CPU which executes each instruction in a single clock cycle except for the memory request

#Creases memobject SevenSegDis
system.memobj = SevenSegDis()

system.membus = SystemXBar() #Created the system wide memory bus

#since we created the memory bus, we would then connect the cache ports directly to the memory bus
system.cpu.icache_port = system.memobj.inst_port
system.cpu.dcache_port = system.memobj.data_port

system.memobj.mem_side = system.membus.slave

#Created an I/O controller on the CPU and connected it to the memory bus
system.cpu.createInterruptController()
#system.cpu.interrupts[0].pio = system.membus.master
#system.cpu.interrupts[0].int_master = system.membus.slave
#system.cpu.interrupts[0].int_slave = system.membus.master

system.system_port = system.membus.slave

#Created the memory controller to connect to the memory bus which is responsible for the entire memory range
system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

process = Process()
process.cmd = ['tests/test-progs/hello/bin/arm/linux/hello']
system.cpu.workload = process
system.cpu.createThreads()

#Created the root object for the instantiation of the system and beginning of execution
root = Root(full_system = False, system = system)

#Funbi's test
#root.svsgd = SevenSegDis()
#root.svsgd.toDisplay = "A"
#root.svsgd2 = SevenSegDis()
#root.svsgd2.toDisplay = "3"
#root.svsgd3 = SevenSegDis()
#root.svsgd3.toDisplay = "b"
#root.svsgd4 = SevenSegDis()
#root.svsgd4.toDisplay = "0"
#root.svsgd5 = SevenSegDis()
#root.svsgd5.toDisplay = "C"
#root.svsgd6 = SevenSegDis()
#root.svsgd6.toDisplay = "4"
#root.svsgd7 = SevenSegDis()
#root.svsgd7.toDisplay = "d"
#root.svsgd8 = SevenSegDis()
#root.svsgd8.toDisplay = "2"
#root.svsgd9 = SevenSegDis()
#root.svsgd9.toDisplay = "E"
#root.svsgd10 = SevenSegDis()
#root.svsgd10.toDisplay = "1"

#Funbi's test
#root.tester = Sensor()
#root.tester.curTemp = (random.randint(0, 150))
#root.tester.newTemp = (random.randint(0, 150))
#root.tester2 = Sensor()
#root.tester2.curTemp = (random.randint(0, 150))
#root.tester2.newTemp = (random.randint(0, 150))
#root.tester3 = Sensor()
#root.tester3.curTemp = (random.randint(0, 150))
#root.tester3.newTemp = (random.randint(0, 150))
#root.tester4 = Sensor()
#root.tester4.curTemp = (random.randint(0, 150))
#root.tester4.newTemp = (random.randint(0, 150))
#root.tester5 = Sensor()
#root.tester5.curTemp = (random.randint(0, 150))
#root.tester5.newTemp = (random.randint(0, 150))

#Valerie's Test 
root.svsgd = SevenSegDis()
root.svsgd.toDisplay = "0"
root.svsgd2 = SevenSegDis()
root.svsgd2.toDisplay = "1"
root.svsgd3 = SevenSegDis()
root.svsgd3.toDisplay = "2"
root.svsgd4 = SevenSegDis()
root.svsgd4.toDisplay = "3"
root.svsgd5 = SevenSegDis()
root.svsgd5.toDisplay = "4"
root.svsgd6 = SevenSegDis()
root.svsgd6.toDisplay = "A"
root.svsgd7 = SevenSegDis()
root.svsgd7.toDisplay = "b"
root.svsgd8 = SevenSegDis()
root.svsgd8.toDisplay = "C"
root.svsgd9 = SevenSegDis()
root.svsgd9.toDisplay = "d"
root.svsgd10 = SevenSegDis()
root.svsgd10.toDisplay = "E"

#Valerie's Test 
root.tester = Sensor()
root.tester.curTemp = (random.randint(0, 100))
root.tester.newTemp = (random.randint(0, 100))
root.tester2 = Sensor()
root.tester2.curTemp = (random.randint(0, 100))
root.tester2.newTemp = (random.randint(0, 100))
root.tester3 = Sensor()
root.tester3.curTemp = (random.randint(0, 100))
root.tester3.newTemp = (random.randint(0, 100))
root.tester4 = Sensor()
root.tester4.curTemp = (random.randint(0, 100))
root.tester4.newTemp = (random.randint(0, 100))
root.tester5 = Sensor()
root.tester5.curTemp = (random.randint(0, 100))
root.tester5.newTemp = (random.randint(0, 100))

m5.instantiate()


print("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'.format(m5.curTick(), exit_event.getCause()))
