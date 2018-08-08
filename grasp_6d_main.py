# -*- coding: utf-8 -*-
############################
#File Name: grasp_6d.py
#Author: pyni 
############################

import rospy
from gqcnn.srv import *
import numpy as np
import tf
from geometry_msgs.msg import Pose
#此处progect什么名字就是 from 名字.srv 

objectidname=['grasp_to_duck']#此处可以把id对应的名字写进去，这里只写了一个
def grasp6d_function(req ):
    print objectidname[req.obj_id]
    allthematrix= np.load(objectidname[req.obj_id]+'.npy')
    finalpose=[]
    for i in range(len(allthematrix)): 
             # print np.array(allthematrix[i]) 
             # print   tf.transformations.quaternion_from_matrix(allthematrix[i] )#quaternion
             # print    allthematrix[i][0][3],allthematrix[i][1][3],allthematrix[i][2][3]# position
             #不能写成上面这种格式，否则 return会报错
              pointpose=Pose()
              pointpose.position.x= allthematrix[i][0][3]
              pointpose.position.y= allthematrix[i][1][3]
              pointpose.position.z= allthematrix[i][2][3] 
	      quaternion=tf.transformations.quaternion_from_matrix(allthematrix[i] )
	      pointpose.orientation.x=quaternion[0]
	      pointpose.orientation.y=quaternion[1]
	      pointpose.orientation.z=quaternion[2]
	      pointpose.orientation.w=quaternion[3]
              finalpose.append(pointpose) 
    return  grasp_6dResponse( finalpose  )
 
def main():
    rospy.init_node('server_test', anonymous = True)
    rospy.Service('grasp_6d', grasp_6d, grasp6d_function)
    rospy.spin()

if __name__ == '__main__':
    main()
