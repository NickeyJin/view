import sys
from robot import ActionParams, ActionType, RobotController


def main() -> int:
    try:
        robot = RobotController()
        robot.add_action( ActionType.Forward, ActionParams(distance_cm=10.0))
        robot.add_action( ActionType.Rotate, ActionParams(angle_deg=90.0))
        robot.add_action( ActionType.Wave, ActionParams(times=3))
        robot.run_all()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit( main() )