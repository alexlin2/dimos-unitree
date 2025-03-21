# Copyright 2025 Dimensional Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dimos.hardware.end_effector import EndEffector

class UFactoryEndEffector(EndEffector):
    def __init__(self, model=None, **kwargs):
        super().__init__(**kwargs)
        self.model = model

    def get_model(self):
        return self.model

class UFactory7DOFArm:
    def __init__(self, arm_length=None):
        self.arm_length = arm_length

    def get_arm_length(self):
        return self.arm_length
