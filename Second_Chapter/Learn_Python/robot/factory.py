from robot.actions import Action, ForwardAction, RotateAction, WaveAction, ActionType,ActionParams

_action_dict = {
    ActionType.Forward: lambda params: ForwardAction(params.distance_cm),
    ActionType.Rotate:  lambda params: RotateAction(params.angle_deg),
    ActionType.Wave:    lambda params: WaveAction(params.times),
}

def create_action(action_type: ActionType, params: ActionParams) -> Action:
    action_class = _action_dict.get(action_type)
    if action_class is not None:
        return action_class(params)
    else:
        raise ValueError(f"未知的动作类型: {action_type}")


