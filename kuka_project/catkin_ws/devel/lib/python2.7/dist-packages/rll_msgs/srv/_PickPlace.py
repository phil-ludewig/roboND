# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rll_msgs/PickPlaceRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class PickPlaceRequest(genpy.Message):
  _md5sum = "3060b6166dbcc78c572755b07312c70f"
  _type = "rll_msgs/PickPlaceRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """geometry_msgs/Pose pose_above
geometry_msgs/Pose pose_grip
bool gripper_close
string grasp_object

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['pose_above','pose_grip','gripper_close','grasp_object']
  _slot_types = ['geometry_msgs/Pose','geometry_msgs/Pose','bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pose_above,pose_grip,gripper_close,grasp_object

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PickPlaceRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.pose_above is None:
        self.pose_above = geometry_msgs.msg.Pose()
      if self.pose_grip is None:
        self.pose_grip = geometry_msgs.msg.Pose()
      if self.gripper_close is None:
        self.gripper_close = False
      if self.grasp_object is None:
        self.grasp_object = ''
    else:
      self.pose_above = geometry_msgs.msg.Pose()
      self.pose_grip = geometry_msgs.msg.Pose()
      self.gripper_close = False
      self.grasp_object = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_14dB().pack(_x.pose_above.position.x, _x.pose_above.position.y, _x.pose_above.position.z, _x.pose_above.orientation.x, _x.pose_above.orientation.y, _x.pose_above.orientation.z, _x.pose_above.orientation.w, _x.pose_grip.position.x, _x.pose_grip.position.y, _x.pose_grip.position.z, _x.pose_grip.orientation.x, _x.pose_grip.orientation.y, _x.pose_grip.orientation.z, _x.pose_grip.orientation.w, _x.gripper_close))
      _x = self.grasp_object
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.pose_above is None:
        self.pose_above = geometry_msgs.msg.Pose()
      if self.pose_grip is None:
        self.pose_grip = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 113
      (_x.pose_above.position.x, _x.pose_above.position.y, _x.pose_above.position.z, _x.pose_above.orientation.x, _x.pose_above.orientation.y, _x.pose_above.orientation.z, _x.pose_above.orientation.w, _x.pose_grip.position.x, _x.pose_grip.position.y, _x.pose_grip.position.z, _x.pose_grip.orientation.x, _x.pose_grip.orientation.y, _x.pose_grip.orientation.z, _x.pose_grip.orientation.w, _x.gripper_close,) = _get_struct_14dB().unpack(str[start:end])
      self.gripper_close = bool(self.gripper_close)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.grasp_object = str[start:end].decode('utf-8')
      else:
        self.grasp_object = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_14dB().pack(_x.pose_above.position.x, _x.pose_above.position.y, _x.pose_above.position.z, _x.pose_above.orientation.x, _x.pose_above.orientation.y, _x.pose_above.orientation.z, _x.pose_above.orientation.w, _x.pose_grip.position.x, _x.pose_grip.position.y, _x.pose_grip.position.z, _x.pose_grip.orientation.x, _x.pose_grip.orientation.y, _x.pose_grip.orientation.z, _x.pose_grip.orientation.w, _x.gripper_close))
      _x = self.grasp_object
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.pose_above is None:
        self.pose_above = geometry_msgs.msg.Pose()
      if self.pose_grip is None:
        self.pose_grip = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 113
      (_x.pose_above.position.x, _x.pose_above.position.y, _x.pose_above.position.z, _x.pose_above.orientation.x, _x.pose_above.orientation.y, _x.pose_above.orientation.z, _x.pose_above.orientation.w, _x.pose_grip.position.x, _x.pose_grip.position.y, _x.pose_grip.position.z, _x.pose_grip.orientation.x, _x.pose_grip.orientation.y, _x.pose_grip.orientation.z, _x.pose_grip.orientation.w, _x.gripper_close,) = _get_struct_14dB().unpack(str[start:end])
      self.gripper_close = bool(self.gripper_close)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.grasp_object = str[start:end].decode('utf-8')
      else:
        self.grasp_object = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_14dB = None
def _get_struct_14dB():
    global _struct_14dB
    if _struct_14dB is None:
        _struct_14dB = struct.Struct("<14dB")
    return _struct_14dB
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rll_msgs/PickPlaceResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class PickPlaceResponse(genpy.Message):
  _md5sum = "358e233cde0c8a8bcfea4ce193f8fc15"
  _type = "rll_msgs/PickPlaceResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool success

"""
  __slots__ = ['success']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PickPlaceResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
    else:
      self.success = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_B().pack(self.success))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_B().pack(self.success))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class PickPlace(object):
  _type          = 'rll_msgs/PickPlace'
  _md5sum = 'f9e1ce2e36454c554259d3461e945fff'
  _request_class  = PickPlaceRequest
  _response_class = PickPlaceResponse