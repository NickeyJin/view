#pragma once

#include "action.h"

#include <cstddef>
#include <memory>
#include <vector>

class RobotControl {
public:
    void addAction(ActionType type, const ActionParams& params);
    void runAll() const;              // 批量执行
    void clear() noexcept { actions_.clear(); }
    std::size_t size() const noexcept { return actions_.size(); }

private:
    std::vector< std::unique_ptr<Action> > actions_;
};