import argparse,json
from pathlib import Path
from datetime import datetime,timezone
from .adapters import FixtureModel
from .metrics import accuracy,psi,segment_accuracy
def main():
 p=argparse.ArgumentParser();p.add_argument("--config",required=True);a=p.parse_args()
 c=json.loads(Path(a.config).read_text());d=json.loads(Path("data/case_study.json").read_text());m,n=FixtureModel("champion"),FixtureModel("challenger")
 rows=[dict(x,expected=x["label"],predicted=m.predict(x["text"]),challenger=n.predict(x["text"])) for x in d];acc=accuracy(rows)
 robust=[m.predict(x["text"].replace("e","3",1))==x["predicted"] for x in rows];inv=sum(robust)/len(robust);seg=segment_accuracy(rows);gap=max(seg.values())-min(seg.values());drift=psi([x["label"] for x in d],[x["production_label"] for x in d]);ca=accuracy([dict(x,predicted=x["challenger"]) for x in rows])
 findings={"performance":{"value":acc,"threshold":c["min_accuracy"],"passed":acc>=c["min_accuracy"]},"robustness":{"value":1-inv,"threshold":c["max_robustness_drop"],"passed":1-inv<=c["max_robustness_drop"]},"fairness_screen":{"value":gap,"threshold":c["max_segment_gap"],"passed":gap<=c["max_segment_gap"]},"drift":{"value":drift,"threshold":c["max_psi"],"passed":drift<=c["max_psi"]},"challenger":{"value":acc-ca,"threshold":c["min_challenger_delta"],"passed":acc-ca>=c["min_challenger_delta"]}}
 run=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ");out=Path("evidence")/run;out.mkdir(parents=True)
 e={"schema_version":"0.1","run_id":run,"metrics":{"accuracy":acc,"robustness_invariance":inv,"segment_accuracy":seg,"segment_gap":gap,"psi":drift,"challenger_accuracy":ca},"findings":findings,"test_cases":rows,"limitations":["Demo adapter; not a compliance conclusion."]};(out/"validation_evidence.json").write_text(json.dumps(e,indent=2))
 lines=["# Model validation evidence","","| Control | Result |","|---|---|"]+[ "| "+k+" | "+("PASS" if v["passed"] else "FAIL")+" |" for k,v in findings.items()];(out/"validation_report.md").write_text("\n".join(lines)+"\n");print(out)
if __name__=="__main__":main()
