# from skimage import io
# Copyright 2015 gRPC authors.
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

"""The Python implementation of the GRPC face.Face client."""

from __future__ import print_function

import grpc
import tensorflow as tf
from google.protobuf import text_format
import dynamic_reload_config_pb2_grpc
import model_server_config_pb2

tf.app.flags.DEFINE_string('server', 'localhost:9000',
                           'PredictionService host:port')
tf.app.flags.DEFINE_string('config_file', 'tfserving.conf', 'path to config file ')
FLAGS = tf.app.flags.FLAGS

def main(_):
  config_file=FLAGS.config_file
  channel = grpc.insecure_channel(FLAGS.server)
  stub = dynamic_reload_config_pb2_grpc.PredictionServiceStub(channel)
  new_config = model_server_config_pb2.ModelServerConfig()
  with open(config_file, "r") as f:
      text_format.Parse(f.read(), new_config)
  stub.DynamicReload(new_config)
  print('Dynamic loading  model  successfully !')

if __name__ == '__main__':
  tf.app.run()
