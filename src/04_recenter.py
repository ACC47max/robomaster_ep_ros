#!/usr/bin/env python3
# -*-coding:utf-8-*-
# Copyright (c) 2020 DJI.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import time
import robomaster
from robomaster import robot


ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

# 获取云台控制对象
ep_gimbal = ep_robot.gimbal

# 控制云台转到回正位置
ep_gimbal.recenter().wait_for_completed()

# 持续保持云台在回正位置
while True:
    ep_gimbal.recenter(pitch_speed=100, yaw_speed=100).wait_for_completed()
    time.sleep(0.1)
