
from m5.objects.FUPool import *
from m5.SimObject import SimObject
from m5.params import *
from m5.objects.FuncUnit import *
from m5.objects.FuncUnitConfig import *

class VFEX0(FUDesc):
    opList = [ OpDesc(opClass='VectorIntegerArith', opLat = 1),
               # OpDesc(opClass='VectorFloatArith', opLat = 1),
               # OpDesc(opClass='VectorFloatReduce', opLat = 3),
               OpDesc(opClass='VectorMisc', opLat = 2)]
    count = 1

class VFEX1(FUDesc):
    opList = [ # OpDesc(opClass='VectorFloatArith', opLat = 1),
               OpDesc(opClass='VectorFloatConvert', opLat = 2),
               OpDesc(opClass='VectorConfig', opLat = 0),
               OpDesc(opClass='VectorIntegerReduce', opLat = 2),
               # OpDesc(opClass='VectorFloatReduce', opLat = 3),
               OpDesc(opClass='VectorMisc', opLat = 2)]
    count = 1

class VFEX2(FUDesc):
    opList = [ OpDesc(opClass='VectorIntegerArith', opLat = 1)
               # OpDesc(opClass='VectorFloatArith', opLat = 1),
               # OpDesc(opClass='VectorFloatReduce', opLat = 3)
               ]
    count = 1

class VFEX3(FUDesc):
    opList = [ # OpDesc(opClass='VectorFloatArith', opLat = 1),
               OpDesc(opClass='VectorFloatConvert', opLat = 2)
               # OpDesc(opClass='VectorFloatReduce', opLat = 3)
               ]
    count = 1

class VFEX4(FUDesc):
    opList = [ # OpDesc(opClass='VectorFloatArith', opLat = 1),
               OpDesc(opClass='VectorIntegerArith', opLat = 1)]
    count = 1

class VFEX_NEW(FUDesc):
    opList = [ OpDesc(opClass='VectorFloatArith', opLat = 1),
               OpDesc(opClass='VectorFloatReduce', opLat = 3),
               OpDesc(opClass='VectorIntegerArith', opLat = 1),
               OpDesc(opClass='VectorIntegerReduce', opLat = 2)]
    count = 1

class MyScheduler(Scheduler):
    IQs = [
        IssueQue(name='IQ_misc' , inoutPorts=1, size=1*24, fuType=[IntDiv()]),
        IssueQue(name='IQ_br', inoutPorts=2, size=2*24, fuType=[IntBRU()]),
        IssueQue(name='IQ_si', inoutPorts=2, size=2*24, fuType=[IntALU()]),
        IssueQue(name='IQ_ci', inoutPorts=2, size=2*24, fuType=[IntALU(), IntMult()]),
        IssueQue(name='IQ_stu', inoutPorts=4, size=2*24, fuType=[WritePort()]),
        IssueQue(name='IQ_ldu', inoutPorts=4, size=2*24, fuType=[ReadPort()]),
        IssueQue(name='IQ_cplx',inoutPorts=2, size=2*24,
            scheduleToExecDelay=3, fuType=[FP_MISC(), FP_SLOW(), FP_MAM(), FP_MAA()]),

        IssueQue(name='VIQ1',inoutPorts=2, size=16, fuType=[VFEX0(), VFEX1()]),
        IssueQue(name='VIQ2',inoutPorts=2, size=16, fuType=[VFEX2(), VFEX3()]),
        IssueQue(name='VIQ3',inoutPorts=1, size=10, fuType=[VFEX4()]),
        # IssueQue(name='VIQ4',inoutPorts=1, size=16, fuType=[VFEX_NEW()])
    ]
    slotNum = 12
    xbarWakeup = True