// Generated by gencpp from file rll_planning_project/PlanToGoalGoal.msg
// DO NOT EDIT!


#ifndef RLL_PLANNING_PROJECT_MESSAGE_PLANTOGOALGOAL_H
#define RLL_PLANNING_PROJECT_MESSAGE_PLANTOGOALGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Pose2D.h>
#include <geometry_msgs/Pose2D.h>

namespace rll_planning_project
{
template <class ContainerAllocator>
struct PlanToGoalGoal_
{
  typedef PlanToGoalGoal_<ContainerAllocator> Type;

  PlanToGoalGoal_()
    : start()
    , goal()  {
    }
  PlanToGoalGoal_(const ContainerAllocator& _alloc)
    : start(_alloc)
    , goal(_alloc)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Pose2D_<ContainerAllocator>  _start_type;
  _start_type start;

   typedef  ::geometry_msgs::Pose2D_<ContainerAllocator>  _goal_type;
  _goal_type goal;





  typedef boost::shared_ptr< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> const> ConstPtr;

}; // struct PlanToGoalGoal_

typedef ::rll_planning_project::PlanToGoalGoal_<std::allocator<void> > PlanToGoalGoal;

typedef boost::shared_ptr< ::rll_planning_project::PlanToGoalGoal > PlanToGoalGoalPtr;
typedef boost::shared_ptr< ::rll_planning_project::PlanToGoalGoal const> PlanToGoalGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace rll_planning_project

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'rll_planning_project': ['/home/phil/kuka_project/catkin_ws/devel/share/rll_planning_project/msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5e8ecd9fb61e382b8974a904baeee367";
  }

  static const char* value(const ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5e8ecd9fb61e382bULL;
  static const uint64_t static_value2 = 0x8974a904baeee367ULL;
};

template<class ContainerAllocator>
struct DataType< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rll_planning_project/PlanToGoalGoal";
  }

  static const char* value(const ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
geometry_msgs/Pose2D start\n\
geometry_msgs/Pose2D goal\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose2D\n\
# Deprecated\n\
# Please use the full 3D pose.\n\
\n\
# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.\n\
\n\
# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.\n\
\n\
\n\
# This expresses a position and orientation on a 2D manifold.\n\
\n\
float64 x\n\
float64 y\n\
float64 theta\n\
";
  }

  static const char* value(const ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.start);
      stream.next(m.goal);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PlanToGoalGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rll_planning_project::PlanToGoalGoal_<ContainerAllocator>& v)
  {
    s << indent << "start: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose2D_<ContainerAllocator> >::stream(s, indent + "  ", v.start);
    s << indent << "goal: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose2D_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RLL_PLANNING_PROJECT_MESSAGE_PLANTOGOALGOAL_H
