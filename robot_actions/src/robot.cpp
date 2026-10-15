#include "robot.h"
#include <cstdio>
void RobotControl::addAction(ActionType type, const ActionParams& params) {
    actions_.push_back( createAction(type, params) );
}
void RobotControl::runAll() const {
    printf( "机器人已启动\n" );
    for (const auto& action : actions_) action->execute();            
    printf("所有动作执行完毕\n");
}