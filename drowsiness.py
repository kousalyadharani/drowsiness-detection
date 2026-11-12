#!/usr/bin/env python3
"""Eye-aspect-ratio drowsiness signal from facial landmark coordinates."""
import argparse,json,math
from pathlib import Path

def distance(a,b): return math.hypot(a[0]-b[0],a[1]-b[1])
def eye_aspect_ratio(points):
 """Six eye points ordered around the contour, matching common EAR definitions."""
 if len(points)!=6: raise ValueError("EAR needs six ordered points")
 return (distance(points[1],points[5])+distance(points[2],points[4]))/(2*distance(points[0],points[3]) or 1e-12)
def analyze(samples, threshold=.22, sustained_seconds=1.0):
 """Samples: timestamp and left/right six-point arrays. Alerts after sustained closure."""
 closed_since=None; alerts=[]
 for s in sorted(samples,key=lambda x:x["time"]):
  ears=[eye_aspect_ratio(s[k]) for k in ("left_eye","right_eye") if k in s]
  if not ears: continue
  closed=sum(ears)/len(ears)<threshold
  if closed and closed_since is None: closed_since=float(s["time"])
  if not closed:
   if closed_since is not None and float(s["time"])-closed_since>=sustained_seconds: alerts.append({"start":closed_since,"end":float(s["time"]),"duration":float(s["time"])-closed_since,"alert":"drowsiness_signal"})
   closed_since=None
 return alerts
def main():
 p=argparse.ArgumentParser();p.add_argument("landmarks",type=Path);p.add_argument("--threshold",type=float,default=.22);p.add_argument("--sustained-seconds",type=float,default=1);p.add_argument("--output",type=Path,default=Path("alerts.json"));a=p.parse_args()
 alerts=analyze(json.loads(a.landmarks.read_text()),a.threshold,a.sustained_seconds);a.output.write_text(json.dumps(alerts,indent=2)+"\n");print(f"{len(alerts)} drowsiness signal(s)")
if __name__=="__main__":main()
