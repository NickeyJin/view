from robot.actions import Action, ActionType, ActionParams
from robot.factory import create_action


class RobotController:
    def __init__(self) -> None:
        self._actions: list[Action] = []

    def add_action(self, action_type: ActionType, params: ActionParams) -> None:
        self._actions.append(create_action(action_type, params))

    def run_all(self) -> None:
        print("机器人已启动")
        for action in self._actions:
            action.execute()
        print("所有动作执行完毕")

    def clear(self) -> None:
        self._actions.clear()

    def __len__(self) -> int:
        return len(self._actions)