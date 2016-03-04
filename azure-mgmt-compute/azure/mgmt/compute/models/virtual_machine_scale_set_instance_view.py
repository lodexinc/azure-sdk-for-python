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


class VirtualMachineScaleSetInstanceView(Model):
    """
    The instance view of a virtual machine scale set.

    :param VirtualMachineScaleSetInstanceViewStatusesSummary virtual_machine:
     Gets the instance view status summary for the virtual machine scale set.
    :param list extensions: Gets the extensions information.
    :param list statuses: Gets or sets the resource status information.
    """ 

    _attribute_map = {
        'virtual_machine': {'key': 'virtualMachine', 'type': 'VirtualMachineScaleSetInstanceViewStatusesSummary'},
        'extensions': {'key': 'extensions', 'type': '[VirtualMachineScaleSetVMExtensionsSummary]'},
        'statuses': {'key': 'statuses', 'type': '[InstanceViewStatus]'},
    }

    def __init__(self, virtual_machine=None, extensions=None, statuses=None, **kwargs):
        self.virtual_machine = virtual_machine
        self.extensions = extensions
        self.statuses = statuses
