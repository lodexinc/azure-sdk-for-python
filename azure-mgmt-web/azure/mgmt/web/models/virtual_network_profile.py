# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualNetworkProfile(Model):
    """
    Specification for using a virtual network

    :param str id: Resource id of the virtual network
    :param str name: Name of the virtual network (read-only)
    :param str type: Resource type of the virtual network (read-only)
    :param str subnet: Subnet within the virtual network
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'subnet': {'key': 'subnet', 'type': 'str'},
    }

    def __init__(self, id=None, name=None, type=None, subnet=None, **kwargs):
        self.id = id
        self.name = name
        self.type = type
        self.subnet = subnet
