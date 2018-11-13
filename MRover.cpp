#include <string>
#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <tf/transform_broadcaster.h>

int main (int argc, char** argv)
{
ros::init(argh,argv,"state_publisher");
ros::NodeHandle n;
rod::Publisher joint_pub = n.advertise<sensor_msgs::JointState>("joint_states",1);
tf::TransformBroadcaster broadcaster;
ros::Rate loop_rate(30)

const double degree = M_PI/180;

//robot state
double inc = 0.005,base_arm_inc = 0.005,arm1_armbase_inc = 0.005

}