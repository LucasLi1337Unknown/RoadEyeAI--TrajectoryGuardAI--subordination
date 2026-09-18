import argparse
from src.core.pipeline import SafetyPipeline

def parseSource(value):
    try:
        return int(value)
    except ValueError:
        return value

def main():
    parser = argparse.ArgumentParser(description="TrajectoryGuard road-risk prototype")
    parser.add_argument("--source", default="0", help="webcam index, image, or video path")
    parser.add_argument("--config", default="configs/default.yaml")
    args = parser.parse_args()
    SafetyPipeline(args.config).run(parseSource(args.source))

if __name__ == "__main__":
    main()
