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

from argparse import ArgumentParser

from .common import parse_args
from ..model_collection import ModelCollection

parser = ArgumentParser(
    description="List available alleles for an MHC II model")

parser.add_argument(
    "path",
    help="Directory containing MHC II model")

def main(args_list=None):
    args = parse_args(parser, args_list)
    mc = ModelCollection(path=args.path)
    alleles = mc.alleles()
    if len(alleles) == 0:
        print("0 alleles in %s" % args.path)
    else:
        print("%d alleles in %s" % (len(alleles), args.path))
        for allele in alleles:
            print("-- %s" % allele)

