#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle nh; 
std_msgs::Int16 sensorData;
ros::Publisher pub("Topic_Sensor", &sensorData);

void setup() 
{
   pinMode(3,INPUT);
   nh.initNode();
   nh.advertise(pub);
}
 
void loop() 
{
    sensorData.data = digitalRead(3);
    pub.publish(&sensorData);
    nh.spinOnce();
    delay(10);
}
