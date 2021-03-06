# coding: utf-8

"""
    Grafeas API

    An API to insert and retrieve annotations on cloud artifacts.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Command(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, env=None, args=None, dir=None, id=None, wait_for=None):
        """
        Command - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'env': 'list[str]',
            'args': 'list[str]',
            'dir': 'str',
            'id': 'str',
            'wait_for': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'env': 'env',
            'args': 'args',
            'dir': 'dir',
            'id': 'id',
            'wait_for': 'waitFor'
        }

        self._name = name
        self._env = env
        self._args = args
        self._dir = dir
        self._id = id
        self._wait_for = wait_for

    @property
    def name(self):
        """
        Gets the name of this Command.
        Name of the command, as presented on the command line, or if the command is packaged as a Docker container, as presented to `docker pull`.

        :return: The name of this Command.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Command.
        Name of the command, as presented on the command line, or if the command is packaged as a Docker container, as presented to `docker pull`.

        :param name: The name of this Command.
        :type: str
        """

        self._name = name

    @property
    def env(self):
        """
        Gets the env of this Command.
        Environment variables set before running this Command.

        :return: The env of this Command.
        :rtype: list[str]
        """
        return self._env

    @env.setter
    def env(self, env):
        """
        Sets the env of this Command.
        Environment variables set before running this Command.

        :param env: The env of this Command.
        :type: list[str]
        """

        self._env = env

    @property
    def args(self):
        """
        Gets the args of this Command.
        Command-line arguments used when executing this Command.

        :return: The args of this Command.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """
        Sets the args of this Command.
        Command-line arguments used when executing this Command.

        :param args: The args of this Command.
        :type: list[str]
        """

        self._args = args

    @property
    def dir(self):
        """
        Gets the dir of this Command.
        Working directory (relative to project source root) used when running this Command.

        :return: The dir of this Command.
        :rtype: str
        """
        return self._dir

    @dir.setter
    def dir(self, dir):
        """
        Sets the dir of this Command.
        Working directory (relative to project source root) used when running this Command.

        :param dir: The dir of this Command.
        :type: str
        """

        self._dir = dir

    @property
    def id(self):
        """
        Gets the id of this Command.
        Optional unique identifier for this Command, used in wait_for to reference this Command as a dependency.

        :return: The id of this Command.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Command.
        Optional unique identifier for this Command, used in wait_for to reference this Command as a dependency.

        :param id: The id of this Command.
        :type: str
        """

        self._id = id

    @property
    def wait_for(self):
        """
        Gets the wait_for of this Command.
        The ID(s) of the Command(s) that this Command depends on.

        :return: The wait_for of this Command.
        :rtype: list[str]
        """
        return self._wait_for

    @wait_for.setter
    def wait_for(self, wait_for):
        """
        Sets the wait_for of this Command.
        The ID(s) of the Command(s) that this Command depends on.

        :param wait_for: The wait_for of this Command.
        :type: list[str]
        """

        self._wait_for = wait_for

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
