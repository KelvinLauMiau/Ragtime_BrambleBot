from controller import Robot
from pynput import keyboard

key_value = 0
robot = Robot()
timestep = int(robot.getBasicTimeStep())
motors = {}
motor_names = [
    "LF_HAA", "LF_HFE", "LF_KFE",
    "RF_HAA", "RF_HFE", "RF_KFE",
    "LH_HAA", "LH_HFE", "LH_KFE",
    "RH_HAA", "RH_HFE", "RH_KFE"
]
for name in motor_names:
    motors[name] = robot.getDevice(name)

def on_press(key):
    try:
        global key_value
        key_value = key.char
        print(f"按下了键 {key.char}")
    except AttributeError:
        print(f"特殊键 {key} 被按下")

def on_release(key):
    print(f"键 {key} 被释放")
    if key == keyboard.Key.esc:
        # 如果按下了 ESC 键，停止监听
        return False

# 创建监听器对象
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# 启动监听
listener.start()


# motors["LF_KFE"].setTorque(-1)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    if(key_value == "w"):
        motors["RH_HAA"].setPosition(0)
        motors["RH_HAA"].setVelocity(0.1)
        motors["RH_HFE"].setPosition(-1.5)
        motors["RH_HFE"].setVelocity(0.5)
        motors["RH_KFE"].setPosition(2.4)
        motors["RH_KFE"].setVelocity(0.8)

        motors["RF_HAA"].setPosition(0)
        motors["RF_HAA"].setVelocity(0.1)
        motors["RF_HFE"].setPosition(1.5)
        motors["RF_HFE"].setVelocity(0.5)
        motors["RF_KFE"].setPosition(-2.4)
        motors["RF_KFE"].setVelocity(0.8)

        motors["LH_HAA"].setPosition(0)
        motors["LH_HAA"].setVelocity(0.1)
        motors["LH_HFE"].setPosition(-1.5)
        motors["LH_HFE"].setVelocity(0.5)
        motors["LH_KFE"].setPosition(2.4)
        motors["LH_KFE"].setVelocity(0.8)

        motors["LF_HAA"].setPosition(0)
        motors["LF_HAA"].setVelocity(0.1)
        motors["LF_HFE"].setPosition(1.5)
        motors["LF_HFE"].setVelocity(0.5)
        motors["LF_KFE"].setPosition(-2.4)
        motors["LF_KFE"].setVelocity(0.8)
    elif key_value == "s":
        motors["RH_HAA"].setPosition(0)
        motors["RH_HAA"].setVelocity(0.1)
        motors["RH_HFE"].setPosition(0)
        motors["RH_HFE"].setVelocity(0.5)
        motors["RH_KFE"].setPosition(0)
        motors["RH_KFE"].setVelocity(0.8)

        motors["RF_HAA"].setPosition(0)
        motors["RF_HAA"].setVelocity(0.1)
        motors["RF_HFE"].setPosition(0)
        motors["RF_HFE"].setVelocity(0.5)
        motors["RF_KFE"].setPosition(0)
        motors["RF_KFE"].setVelocity(0.8)

        motors["LH_HAA"].setPosition(0)
        motors["LH_HAA"].setVelocity(0.1)
        motors["LH_HFE"].setPosition(0)
        motors["LH_HFE"].setVelocity(0.5)
        motors["LH_KFE"].setPosition(0)
        motors["LH_KFE"].setVelocity(0.8)

        motors["LF_HAA"].setPosition(0)
        motors["LF_HAA"].setVelocity(0.1)
        motors["LF_HFE"].setPosition(0)
        motors["LF_HFE"].setVelocity(0.5)
        motors["LF_KFE"].setPosition(0)
        motors["LF_KFE"].setVelocity(0.8)
# Enter here exit cleanup code.
