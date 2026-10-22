#pragma once
#include <memory>
#include <stdexcept>

class Action{
    public:
        virtual ~Action() = default; //析构函数
        virtual void execute() const = 0; //纯虚函数，需要定义
    protected:
        Action() = default; //默认构造函数
        Action(const Action&) = delete; //不需要你拷贝
        Action& operator=(const Action&) = delete; //又不需要你运算
};

class ForwardAction : public Action {
    public:
        void execute() const override; //这也是虚函数
        explicit ForwardAction( double distance ); // 别想了，你只能通过其他类的构造函数来创建这个类的对象
        double getDistance() const { return distance_; };
        void setDistance( double distance ) { distance_ = distance > 0 ? distance : throw std::invalid_argument("前进距离必须大于 0，收到：" + std::to_string(distance)); };
    private:
        double distance_;
};

class RotateAction : public Action {
    public:
        void execute() const override;
        explicit RotateAction( double angle );
        double getAngle() const { return angle_; };
        void setAngle( double angle ) { angle_ = angle > 0 ? angle : throw std::invalid_argument("旋转角度必须大于 0，收到：" + std::to_string(angle)); };
    private:
        double angle_;
};

class WaveAction : public Action {
    public:
        void execute() const override;
        explicit WaveAction( int times ); 
        int getTimes() const { return times_; };
        void setTimes( int times ) { times_ = times > 0 ? times : throw std::invalid_argument("挥手次数必须大于 0，收到：" + std::to_string(times)); };
    private:
        int times_;
};


enum class ActionType {
    Forward,
    Rotate,
    Wave
}; // 枚举类，表示动作类型

struct ActionParams {// 跨过类型边界的"统一参数包"，统一安排
    double distance_cm = 0.0;
    double angle_deg   = 0.0;
    int    times       = 0;
};

std::unique_ptr<Action> createAction(ActionType type, const ActionParams& params); 
// 工厂函数，创建动作对象，从而实现动作的多态性