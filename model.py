from dataclasses import dataclass
@dataclass
class UseCase:
    name:str
    monthly_tasks:int
    minutes_per_task:float
    automation_share:float
    hourly_cost_cad:float
    one_time_cost_cad:float
    annual_running_cost_cad:float
    strategic_fit:int
    data_readiness:int
    delivery_feasibility:int
    privacy_risk:int
    human_review:bool

def assess(c):
    if not 0 <= c.automation_share <= 1 or any(not 1 <= v <= 5 for v in (c.strategic_fit,c.data_readiness,c.delivery_feasibility,c.privacy_risk)):
        raise ValueError("Out-of-range assessment")
    if any(v < 0 for v in (c.monthly_tasks,c.minutes_per_task,c.hourly_cost_cad,c.one_time_cost_cad,c.annual_running_cost_cad)):
        raise ValueError("Negative values not permitted")
    hours=c.monthly_tasks*c.minutes_per_task*12/60*c.automation_share
    recurring=hours*c.hourly_cost_cad-c.annual_running_cost_cad
    score=20*(.35*c.strategic_fit+.30*c.data_readiness+.25*c.delivery_feasibility+.10*(6-c.privacy_risk))
    if c.privacy_risk>=4 and not c.human_review: decision="HOLD — governance review required"
    elif c.data_readiness<=2: decision="DISCOVER — assess data quality"
    elif score>=75 and recurring>0: decision="PILOT — controlled proof of concept"
    else: decision="EXPLORE — refine the business case"
    return dict(hours_saved=round(hours,1),year_one_net_cad=round(recurring-c.one_time_cost_cad),three_year_net_cad=round(3*recurring-c.one_time_cost_cad),score=round(score,1),decision=decision,payback_months=round(12*c.one_time_cost_cad/recurring,1) if recurring>0 else None)
