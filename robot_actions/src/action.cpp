#include "action.h"

#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <cstdio>

ForwardAction::ForwardAction(double distance) : distance_(distance) {
    setDistance(distance);
}
void ForwardAction::execute() const {
    printf("执行动作：前进 前进距离：%g cm 机器人向前移动了 %g cm\n", distance_, distance_);
}

RotateAction::RotateAction(double angle) : angle_(angle) {
    setAngle(angle);
}
void RotateAction::execute() const {
    printf("执行动作：旋转 旋转角度：%g° 机器人向左旋转了 %g°\n", angle_, angle_);
}

WaveAction::WaveAction(int times) : times_(times) {
    setTimes(times);
}
void WaveAction::execute() const {
    printf("执行动作：挥手 挥手次数：%d 机器人完成了 %d 次挥手\n", times_, times_);
}

std::unique_ptr<Action> createAction(ActionType type, const ActionParams& params) {
    switch (type) {
        case ActionType::Forward:
            return std::make_unique<ForwardAction>(params.distance_cm);
        case ActionType::Rotate:
            return std::make_unique<RotateAction>(params.angle_deg);
        case ActionType::Wave:
            return std::make_unique<WaveAction>(params.times);
    }
    throw std::invalid_argument("未知的动作类型");
}