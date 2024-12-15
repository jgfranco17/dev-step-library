import time

import can
from ecu.model import MockECU


def send_mock_can_messages():
    mock_ecu = MockECU()
    while True:
        # Example CAN message for Engine RPM
        engine_rpm = can.Message(
            arbitration_id=0x0CFF00,
            data=[0x00, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            is_extended_id=True,
        )

        # Example CAN message for Vehicle Speed
        vehicle_speed = can.Message(
            arbitration_id=0x0CFF01,
            data=[0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            is_extended_id=True,
        )

        try:
            mock_ecu.send(engine_rpm, "Engine RPM")
            mock_ecu.send(vehicle_speed, "Vehicle Speed")
            time.sleep(1)

        except can.CanError as e:
            print(f"[CAN Error] {e}")

        except KeyboardInterrupt:
            print("User forced exit, shutting down...")
            break

        finally:
            mock_ecu.shutdown()


if __name__ == "__main__":
    send_mock_can_messages()
