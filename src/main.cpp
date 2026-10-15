
#include "robot.h"
#include <exception>
#include <iostream>

int main() {
    try {
        RobotControl robot;

        robot.addAction(ActionType::Forward, ActionParams{.distance_cm = 100.0});
        robot.addAction(ActionType::Rotate, ActionParams{.angle_deg = 90.0});
        robot.addAction(ActionType::Wave, ActionParams{.times = 3});

        robot.runAll();
    } catch (const std::exception& e) {
        std::cerr << "错误：" << e.what() << "\n";
        return 1;
    }
    return 0;
}