# TrajectoryGuard

A software-first road-risk research prototype for detecting, tracking, predicting, and explaining dangerous interactions between road users.

## Pipeline

Video / Camera
→ YOLO detection
→ multi-object tracking
→ motion estimation
→ trajectory prediction
→ risk analysis
→ explainable warnings

## Current milestone: v0.1

This first engineering baseline intentionally does a small number of things clearly:

1. Accepts a video, webcam, or image.
2. Uses Ultralytics YOLO for road-user detection.
3. Uses YOLO's tracking interface to preserve object IDs where available.
4. Maintains short center-point histories.
5. Estimates image-space velocity.
6. Projects a short constant-velocity trajectory.
7. Computes a transparent baseline risk score.
8. Draws the reason for a warning on the output frame.
9. Logs structured detection/risk records to JSONL.

The baseline risk model is deliberately not presented as a validated real-world safety model. It is a starting point for experiments and later calibration.

## Install

Python 3.10+ recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python main.py --source 0
```

or

```bash
python main.py --source path/to/video.mp4
```

Press `q` to quit.

## Repository structure

- `src/detection` — YOLO inference/tracking adapter
- `src/tracking` — track histories and motion estimation
- `src/prediction` — trajectory projection
- `src/risk` — explainable baseline risk model
- `src/visualization` — frame rendering
- `src/core` — data models and pipeline
- `configs` — system configuration
- `tests` — unit tests for deterministic logic
- `experiments` — experiment records
- `docs` — architecture and evaluation plan
- `outputs` — generated results, ignored by Git

## Next milestones

- v0.2: evaluate tracker stability and motion smoothing
- v0.3: calibrated camera geometry / world-coordinate motion
- v0.4: vehicle-path and conflict-point prediction
- v0.5: time-to-collision / closest-approach risk model
- v1.0: evaluated end-to-end competition system

## Safety scope

This repository is a research/competition prototype. It is not certified for deployment in vehicles or safety-critical environments.
