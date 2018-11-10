import rospy
from geometry_msgs.msg import Twist
from math import pi
class OutAndBack():
    def __init__(self):
        #Naming the node
        rospy.init_node('out_and_back',anonymous=False)
        #Set Rospy to execute a shutdown function
        rospy.on_shutdown(self.shutdown)

        #COntrol the robot speed
        self.cmd_vel = rospy.Publisher('/cmd_vel',Twist)

        #Update speed of robot movement
        rate = 50

        #Set the ROS Rate variable
        r = rospy.Rate(rate)

        #Forward linear speed
        linear_speed = 0.2

        #Travel distance
        goal_distance = 1.0

        #Time taken
        linear_duration = goal_distance/linear_speed

        #Rotation speed
        ang_speed = 1.0

        #Rotation angle
        goal_ang = pi

        #Angular duration
        ang_dur = goal_angle/angular_speed

        #Loop through the legs of the trip
        for i in range(0,2):
            #Initialize the movement
            move_cmd = Twist()

            #Forrward speed
            move_cmd.linear.x = linear_speed

            #Time for 1 meter
            ticks = int(linear_duration * rate)

            for t in range(ticks):
                self.cmd_vel.publish(move_cmd)
                r.sleep()

            #Stop the rotation
            move_cmd = Twist()
            self.cmd_vel.publish(move_cmd)
            rospy.sleep(1)

            #Now rotate pi
            #Set the angular speed
            move_cmd.angular.z = angular_speed

            #Rotate for pi
            ticks = int(goal_angle * rate)
            for t in range(ticks):
                self.cmd_vel.publish(move_cmd)
                r.sleep()

            #stop the robot before the next leg
            move_cmd = Twist()
            self.cmd_vel.publish(move_cmd)
            rospy.sleep(1)
        #Stop the robot
        self.cmd_vel.publish(Twist())
    def shutdown(self):
        #Always stop the robot
        rospy.loginfo("Stopping the robot...")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)
if __name__ == '__main__':
    try:
        OutAndBack()
    except:
        rospy.loginfo("Out-and-Back node terminated.")
        
