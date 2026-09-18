# Architecture

TrajectoryGuard separates perception from reasoning.

## Detection
YOLO supplies object class, confidence, and bounding box.

## Tracking
Track IDs allow observations to be connected over time.

## Motion
The baseline computes average image-space displacement across recent frames.

## Prediction
v0.1 uses constant-velocity image-space extrapolation. This is intentionally simple and testable.

## Risk
The v0.1 risk engine combines proximity to a configurable conceptual conflict region, predicted approach, and image-space motion.

This is **not** a physical collision probability. Later versions should use camera calibration, world coordinates, vehicle geometry, predicted paths, closest approach, and time-to-collision.

## Visualization
Rendering is separate from the risk logic so UI changes cannot silently alter the safety calculation.
