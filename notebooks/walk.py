from Servo import *
import time
import json
from enum import Enum


class SRV(Enum):
    FRONT_RIGHT_HIP = 15
    MID_RIGHT_HIP = 12
    BACK_RIGHT_HIP = 9

    FRONT_LEFT_HIP = 16
    MID_LEFT_HIP = 19
    BACK_LEFT_HIP = 22

    FRONT_RIGHT_LIFT = 14
    MID_RIGHT_LIFT = 11
    BACK_RIGHT_LIFT = 8

    FRONT_LEFT_LIFT = 17
    MID_LEFT_LIFT = 20
    BACK_LEFT_LIFT = 23

    FRONT_RIGHT_ANKLE = 13
    MID_RIGHT_ANKLE = 10
    BACK_RIGHT_ANKLE = 31

    FRONT_LEFT_ANKLE = 18
    MID_LEFT_ANKLE = 21
    BACK_LEFT_ANKLE = 27


class POS(Enum):
    TORSO = 0
    FRONT_LEFT_HIP = 1
    FRONT_LEFT_ANKLE = 2
    MID_LEFT_HIP = 3
    MID_LEFT_ANKLE = 4
    MID_RIGHT_HIP = 5
    MID_RIGHT_ANKLE = 6
    FRONT_RIGHT_HIP = 7
    FRONT_RIGHT_ANKLE = 8
    BACK_LEFT_HIP = 9
    BACK_LEFT_ANKLE = 10
    BACK_RIGHT_HIP = 11
    BACK_RIGHT_ANKLE = 12


servo = Servo()

def walk():
    for s in [
        SRV.FRONT_RIGHT_LIFT,
        SRV.MID_RIGHT_LIFT,
        SRV.BACK_RIGHT_LIFT,
        SRV.FRONT_LEFT_LIFT,
        SRV.MID_LEFT_LIFT,
        SRV.BACK_LEFT_LIFT
    ]:
        servo.setServoAngle(s.value, 90)

    for s in [
        SRV.FRONT_LEFT_HIP,
        SRV.MID_LEFT_HIP,
        SRV.BACK_LEFT_HIP,
        SRV.FRONT_RIGHT_HIP,
        SRV.MID_RIGHT_HIP,
        SRV.BACK_RIGHT_HIP,
    ]:
        servo.setServoAngle(s.value, 90)

    for s in [
        SRV.FRONT_RIGHT_ANKLE,
        SRV.MID_RIGHT_ANKLE,
        SRV.BACK_RIGHT_ANKLE
    ]:
        servo.setServoAngle(s.value, 60)

    for s in [
        SRV.FRONT_LEFT_ANKLE,
        SRV.MID_LEFT_ANKLE,
        SRV.BACK_LEFT_ANKLE
    ]:
        servo.setServoAngle(s.value, 120)

    out = json.loads(open("out.json", "r").read())

    mag_hip = 110
    mag_lift = 170
    mag_ankle = 120

    lift_offset = 50  # positive is knee up to the ceiling
    ankle_offset = -40  # positive is away from bot

    num_steps = len(out["rot"])

    for idx, r in enumerate(out["rot"]):
        progress = 100 * idx / num_steps
        print(f"step {idx}: {progress:.2f}%")

        if progress < 10:
            continue

        # FRONT LEFT
        a = mag_hip * (r[POS.FRONT_LEFT_HIP.value][3] - 0.2)
        servo.setServoAngle(SRV.FRONT_LEFT_HIP.value, 90 + a)

        a = mag_lift * (r[POS.FRONT_LEFT_ANKLE.value][1] + 0.3)
        servo.setServoAngle(SRV.FRONT_LEFT_LIFT.value, 90 - lift_offset + a)

        a = -mag_ankle * (r[POS.FRONT_LEFT_ANKLE.value][1] + 0.2)
        servo.setServoAngle(SRV.FRONT_LEFT_ANKLE.value, 90 + ankle_offset + a)
        


        # MID LEFT
        a = mag_hip * (r[POS.MID_LEFT_HIP.value][3] + 0.0)
        servo.setServoAngle(SRV.MID_LEFT_HIP.value, 90 + a)

        a = mag_lift * (r[POS.MID_LEFT_ANKLE.value][1] + 0.3)
        servo.setServoAngle(SRV.MID_LEFT_LIFT.value, 90 - lift_offset + a)

        a = -mag_ankle * (r[POS.MID_LEFT_ANKLE.value][1] + 0.2)
        servo.setServoAngle(SRV.MID_LEFT_ANKLE.value, 90 + ankle_offset)


        # BACK LEFT
        a = -mag_hip * (r[POS.BACK_LEFT_HIP.value][3] + 0.0)
        servo.setServoAngle(SRV.BACK_LEFT_HIP.value, 90 + a)

        a = 0.4 * mag_lift * (r[POS.BACK_LEFT_ANKLE.value][1] - 0.1)
        servo.setServoAngle(SRV.BACK_LEFT_LIFT.value, 90 - lift_offset + a)

        a = -0.4 * mag_ankle * (r[POS.BACK_LEFT_ANKLE.value][1] - 0.4)
        servo.setServoAngle(SRV.BACK_LEFT_ANKLE.value, 90 + ankle_offset + a)


        # FRONT RIGHT
        a = mag_hip * (r[POS.FRONT_RIGHT_HIP.value][3] + 0.0)
        servo.setServoAngle(SRV.FRONT_RIGHT_HIP.value, 90 + a)

        a = mag_lift * (r[POS.FRONT_RIGHT_ANKLE.value][1] + 0.1)
        servo.setServoAngle(SRV.FRONT_RIGHT_LIFT.value, 90 + lift_offset + a)

        a = -mag_ankle * (r[POS.FRONT_RIGHT_ANKLE.value][1] + 0.3)
        servo.setServoAngle(SRV.FRONT_RIGHT_ANKLE.value, 90 - ankle_offset + a)



        # MID RIGHT
        a = mag_hip * r[POS.MID_RIGHT_HIP.value][3]
        servo.setServoAngle(SRV.MID_RIGHT_HIP.value, 90 + a)

        a = mag_lift * (r[POS.MID_RIGHT_ANKLE.value][1] + 0.4)
        servo.setServoAngle(SRV.MID_RIGHT_LIFT.value, 90 + lift_offset + a)

        a = mag_ankle * (r[POS.MID_RIGHT_ANKLE.value][1] + 0.0)
        servo.setServoAngle(SRV.MID_RIGHT_ANKLE.value, 90 - ankle_offset + a)


        # BACK RIGHT
        a = -mag_hip * (r[POS.BACK_RIGHT_HIP.value][3] - 0.2)
        servo.setServoAngle(SRV.BACK_RIGHT_HIP.value, 90 + a)

        a = -0.4 * mag_lift * (r[POS.BACK_RIGHT_ANKLE.value][1] - 0.15)
        servo.setServoAngle(SRV.BACK_RIGHT_LIFT.value, 90 + lift_offset + a)

        a = 0.4 * mag_ankle * (r[POS.BACK_RIGHT_ANKLE.value][1] - 0.45)
        servo.setServoAngle(SRV.BACK_RIGHT_ANKLE.value, 90 - ankle_offset + a)


        time.sleep(0.05)
    

if __name__ == "__main__":
    print("Let's go for a walk!")
    walk()
