import argparse
import json
import yaml
import os
import xmltodict

parser = argparse.ArgumentParser(description='Konwersja plików XML, JSON i YAML.')

parser.add_argument('input_file', type=str, help='Nazwa pliku wejściowego.')
parser.add_argument('output_file', type=str, help='Nazwa pliku wyjściowego.')
args = parser.parse_args()
