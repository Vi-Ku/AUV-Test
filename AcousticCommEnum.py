from enum import Enum

class RequestType(Enum):
    COMMUNICATION_STATUS = 10
    SYSTEM_STATUS = 20
    SENSOR_VALUE = 30
    COMMAND = 40
    GOAL = 50


class RequestId(Enum):

    class SensorStatus(Enum):
        PRESSURE =10
        DVL =20
        GPS =30
        AHRS =40
        SIDE_SCAN_SONAR =50
        FRONT_SONAR =60
        CAMERA = 70
        SBC = 80
        LATTE_PANDA =90
        MCU_1 = 100
        MCU_2 = 110
        THRUSTERS_ENCODER_1  = 200

    class GoalPosition(Enum):
        GOAL_X =10
        GOAL_Y =20
        GOAL_ROLL =30
        GOAL_YAW =40
        GOAL_PITCH =50

    class Command(Enum):
        EMERGENCY_KILL =10
        EMERGENCY_STOP =20
        START_SIDE_SCAN_SONAR =30
        STOP_SIDE_SCAN_SONAR=40
        RESTART_DVL = 50
        RESTART_AHRS =60
        RESTART_FRONT_SONAR =70
        START_CAMERA =80
        STOP_CAMERA =90
        RETURN_TO_BASE_STATION =100
        RETURN_TO_SURFACE = 110
        RESTART_SBC = 120
        RESTART_LATTE = 130

    class CommunicationStatus(Enum):
        ACOUSTIC_MODEM =10
        RF_ANTENNA =20

    class SystemParameters(Enum):
        PRESSURE =10
        VELOCITY_X =10
        VELOCITY_Y =20
        VELOCITY_Z =30
        ACCELERATION_X =40
        ACCELERATION_Y =50
        ACCELERATION_Z =60
        PITCH = 70
        ROLL = 80
        YAW = 90
        LATTITUDE = 100
        LONGITUDE = 110
        DEPTH = 120
        CURRENT_GOAL_X = 130
        CURRENT_GOAL_Y = 140
        CURRENT_GOAL_DEPTH = 150
        CURRENT_GOAL_PITCH = 160
        CURRENT_GOAL_YAW =  170
        CURRENT_GOAL_ROLL = 180
        CURRENT_GOAL_SPEED_X = 190
        CURRENT_GOAL_SPEED_Y = 200
        CURRENT_GOAL_SPEED_Z = 210
        BATTERY_STATE = 220

class FeebackCode(Enum):
    #! These codes are only used for demonstration puropose for one way communication only, the main codes to be used will be as mentioned above.
    LATTITUDE = 10
    LONGITUDE = 20
    DEPTH = 30
    VELOCITY_X =40
    YAW = 50
    BATTERY_STATE = 60
    SBC_STATUS = 70




