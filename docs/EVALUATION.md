# Evaluation Plan

The competition system should be evaluated rather than demonstrated only on hand-picked clips.

## Scenario groups
- pedestrian approaches conflict path
- pedestrian moves away
- fast bicycle crossing
- multiple road users
- partial occlusion
- stationary objects
- low light
- detector false positive / missed detection

## Metrics to add
- detector precision and recall on the selected dataset
- track continuity / ID switches
- trajectory displacement error
- warning lead time
- false warning rate
- missed dangerous-event rate
- runtime FPS and latency

Record model version, hardware, resolution, configuration, and dataset for every experiment.
