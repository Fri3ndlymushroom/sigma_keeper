from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.messages.flat.QuickChatSelection import QuickChatSelection
from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot.utils.game_state_util import GameState, BallState, CarState, Physics, Vector3, Rotator, GameInfoState
import math

from util.ball_prediction_analysis import find_slice_at_time
from util.boost_pad_tracker import BoostPadTracker
from util.drive import steer_toward_target
from util.sequence import Sequence, ControlStep
from util.vec import Vec3


class MyBot(BaseAgent):

    def __init__(self, name, team, index):
        super().__init__(name, team, index)
        self.active_sequence: Sequence = None
        self.boost_pad_tracker = BoostPadTracker()

    def initialize_agent(self):
        # Set up information about the boost pads now that the game is active and the info is available
        self.boost_pad_tracker.initialize_boosts(self.get_field_info())

    def resetScene(self):
         #, 
        car_state = CarState(Physics(rotation=Rotator(0, 1.57079, 0), location=Vector3(0, -5100, None)), boost_amount=100)
        ball_state = BallState(Physics(location=Vector3(0, 0, None)))

        game_state = GameState(ball=ball_state, cars={self.index: car_state})

        self.set_game_state(game_state)

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:

        my_car = packet.game_cars[self.index]
        car_location = Vec3(my_car.physics.location)
        car_velocity = Vec3(my_car.physics.velocity)
        ball_location = Vec3(packet.game_ball.physics.location)

        self.resetScene()

        controls = SimpleControllerState()

        return controls



