#!/usr/bin/env python3
#
#   Copyright 2020 - The Android Open Source Project
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from l2cap.classic import facade_pb2 as l2cap_facade_pb2
from bluetooth_packets_python3 import l2cap_packets


class PyL2cap(object):

    def __init__(self, device):
        self.device = device

    def open_channel(self,
                     psm=0x33,
                     mode=l2cap_facade_pb2.RetransmissionFlowControlMode.BASIC):

        # todo, I don't understand what SetDynamicChannel means?
        self.device.l2cap.SetDynamicChannel(
            l2cap_facade_pb2.SetEnableDynamicChannelRequest(
                psm=psm, retransmission_mode=mode))
