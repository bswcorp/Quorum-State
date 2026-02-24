import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CyberBSWController(Node):
    def __init__(self):
        super().__init__('cyber_bsw_controller')
        # Publisher untuk mengirim perintah kecepatan ke robot
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5  # detik
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('🦾 Project CYBER-BSW: Sistem Kendali Aktif!')

    def timer_callback(self):
        msg = Twist()
        # Perintah gerak maju (Linear X) dan putar (Angular Z)
        msg.linear.x = 0.5  # Maju 0.5 m/s
        msg.angular.z = 0.2 # Putar perlahan
        self.publisher_.publish(msg)
        self.get_logger().info('🚀 Mengirim Sinyal Pergerakan ke Robot...')

def main(args=None):
    rclpy.init(args=args)
    controller = CyberBSWController()
    try:
        rclpy.spin(controller)
    except KeyboardInterrupt:
        print("\n🛑 Emergency Stop: Kendali diputus oleh Capo.")
    finally:
        controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
