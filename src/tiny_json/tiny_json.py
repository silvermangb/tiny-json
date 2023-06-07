#!/usr/bin/python3
import sys
import json
import argparse
import six


parser = argparse.ArgumentParser(prog="python3 tiny_json.py")


# Check if Python version is 3.7 or higher
if sys.version_info >= (3, 7):
    subparsers = parser.add_subparsers(dest="command", required=True)
else:
    # For Python 2.x and Python 3.x < 3.7
    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

# Create the parser for the "encode" command
encode_parser = subparsers.add_parser('encode')
encode_parser.add_argument('--json')
encode_parser.add_argument('--show-json-template', action='store_true')
encode_parser.add_argument('--show-keys', action='store_true')

# Create the parser for the "decode" command
decode_parser = subparsers.add_parser('decode')
decode_parser.add_argument('--encoded-json')
decode_parser.add_argument('--json-template')

# Create the parser for the "templatize" command
templatize_parser = subparsers.add_parser('templatize')
templatize_parser.add_argument('--json')
templatize_parser.add_argument('--show-keys', action='store_true')

def set_value_by_path(dictionary, path, value):
    '''
    Given a path from root to leaf, create a key/value
    pair in the dictionary.
    '''
    path = key_func(path)
    path_list = path.split('.')
    current = dictionary
    for key in path_list[:-1]:
        current = current.setdefault(key, {})
    current[path_list[-1]] = value

def key_func(path):
    '''
    Given a path to an entry in a dictionary remove
    the leading '.' if it is present.
    '''
    if not path:
        return path
    elif path[0] == '.':
        return path[1:]
    else:
        return path

def encode(msg):
    '''
    Encode (serialize) a JSON object represented by a 
    dictionary to a comma separated values string. This
    produces a very small representation of the JSON which
    can later be decoded (deserialized) by tiny-json.
    '''
    def _encode(msg, l, path):
        for key, value in msg.items():
            if isinstance(value, dict):
                _encode(value,l, path + '.' + key)
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    if isinstance(item, dict):
                        _encode(item,l, path + '.' + key)
                    else:
                        l.append(six.moves.urllib.parse.quote(item))
                        l.append(',')
            else:
                l.append(six.moves.urllib.parse.quote(value))
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
                    v.append(six.moves.urllib.parse.unquote(p.pop(0)))    
        for key, value in msg_template.items():
            if isinstance(value, dict):
                _decode(value, p, path + '.' + key, d)
            elif isinstance(value, list):
                v = []
                _decode_list(value,p,v)
                d[key_func(path + '.' + key)] = v
            else:
                value = p.pop(0)
                set_value_by_path(d,path + '.' + key,six.moves.urllib.parse.unquote(value))
    d = {}
    _decode(msg_template,e.split(','),'',d)
    return d

def templatize(msg):
    def _templatize(msg,path,keys):
        for key, value in msg.items():
            if isinstance(value, dict):
                _templatize(value,path + '.' + key, keys)
            elif isinstance(value, list):
                keys.append(key_func(path + '.' + key))
                for index, item in enumerate(value):
                    if isinstance(item, dict):
                        _templatize(item, path + '.' + key, keys)
                    else:
                        value[index] = ""
            else:
                msg[key] = ""
                keys.append(key_func(path + '.' + key))
    keys = []
    _templatize(msg,'',keys)
    return keys

if __name__=="__main__":
    args = parser.parse_args()
    if args.command == "encode":
        input_json = json.loads(args.json)
        e = encode(input_json)
        k = ''
        t = ''
        if args.show_json_template and args.show_keys:
            k = ','.join(templatize(input_json))
            t = json.dumps(input_json)
        elif args.show_json_template:
             t = json.dumps(input_json)
        elif args.show_keys:
             k = ','.join(templatize(input_json))                      
        sys.stdout.write('%s %s %s' % (e,t,k))
    elif args.command == "decode":
        decoded_json = decode(json.loads(args.json_template),args.encoded_json)
        sys.stdout.write('%s' % json.dumps(decoded_json))
    elif args.command == "templatize":
        input_json = json.loads(args.json)
        k = ','.join(templatize(input_json))
        if not args.show_keys:
            k = ''
        sys.stdout.write('%s %s' % (json.dumps(input_json),k))
    else:
        print("usage: ...")
 
