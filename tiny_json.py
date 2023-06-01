#!/usr/bin/python3
import sys
import json
import urllib.parse
import argparse


parser = argparse.ArgumentParser(prog="python3 tiny_json.py")

subparsers = parser.add_subparsers(dest="command", required=True)

# Create the parser for the "encode" command
encode_parser = subparsers.add_parser('encode')
encode_parser.add_argument('--json')
encode_parser.add_argument('--show-json-template', action='store_true')

# Create the parser for the "decode" command
decode_parser = subparsers.add_parser('decode')
decode_parser.add_argument('--encoded-json')
decode_parser.add_argument('--json-template')

# Create the parser for the "decode" command
decode_parser = subparsers.add_parser('templatize')
decode_parser.add_argument('--json')

def set_value_by_path(dictionary, path, value):
    path_list = path.split('.')
    current = dictionary
    for key in path_list[:-1]:
        current = current.setdefault(key, {})
    current[path_list[-1]] = value

def key_func(path):
    if not path:
        return path
    elif path[0] == '.':
        return path[1:]
    else:
        return path

def encode(msg):
    def _encode(msg, l, path):
        for key, value in msg.items():
            if isinstance(value, dict):
                _encode(value,l, path + '.' + key)
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    if isinstance(item, dict):
                        _encode(item,l, path + '.' + key)
                    else:
                        l.append(urllib.parse.quote(item))
                        l.append(',')
            else:
                l.append(urllib.parse.quote(value))
                l.append(',')
    l = []
    _encode(msg,l,'')
    return ''.join(l)



def decode(msg_template, e):
    def _decode(msg_template, p, path, d):
        def _decode_list(list_msg,p,v):
            for index, item in enumerate(list_msg):
                if isinstance(item, dict):
                    _d = {}
                    _decode(item,p,'',_d)
                    v.append(_d)
                else:
                    v.append(urllib.parse.unquote(p.pop(0)))    
        for key, value in msg_template.items():
            if isinstance(value, dict):
                _decode(value, p, path + '.' + key, d)
            elif isinstance(value, list):
                v = []
                _decode_list(value,p,v)
                d[key_func(path + '.' + key)] = v
            else:
                _key = key_func(path + '.' + key)
                value = p.pop(0)
                set_value_by_path(d,_key,urllib.parse.unquote(value))
    d = {}
    _decode(msg_template,e.split(','),'',d)
    return d

def templatize(msg):
    for key, value in msg.items():
        if isinstance(value, dict):
            templatize(value)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    templatize(item)
                else:
                    value[index] = ""
        else:
            msg[key] = ""


if __name__=="__main__":
    args = parser.parse_args()
    if args.command == "encode":
        input_json = json.loads(args.json)
        e = encode(input_json)
        if args.show_json_template:
            templatize(input_json)
            t = json.dumps(input_json)
        else:
            t = ''
        sys.stdout.write('%s %s' % (e,t))
    elif args.command == "decode":
        decoded_json = decode(json.loads(args.json_template),args.encoded_json)
        sys.stdout.write('%s' % json.dumps(decoded_json))
    elif args.command == "templatize":
        input_json = json.loads(args.json)
        templatize(input_json)
        sys.stdout.write(json.dumps(input_json))
    else:
        print("usage: ...")
 
