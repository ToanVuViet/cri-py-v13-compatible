"""
.. include:: ../README.md
"""


from .robot_state import (
    RobotMode,
    KinematicsState,
    OperationMode,
    RunState,
    ReplayMode,
    ErrorStates,
    RobotCartesianPosition,
    PlatformCartesianPosition,
    JointsState,
    RobotState,
    PosVariable,
    OperationInfo,
    ReferencingAxisState,
    ReferencingState,
)
from .cri_controller import CRIController
from .cri_protocol_parser import CRIProtocolParser

from .cri_errors import CRIError, CRIConnectionError, CRICommandTimeOutError
