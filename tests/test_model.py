from model import UseCase,assess
def test_privacy_gate():
    x=UseCase("screen",100,10,.4,35,1000,100,5,5,5,5,False)
    assert assess(x)["decision"].startswith("HOLD")
def test_hours():
    x=UseCase("triage",100,60,.5,30,1000,100,5,4,4,1,True)
    assert assess(x)["hours_saved"]==600
