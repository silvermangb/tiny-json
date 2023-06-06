import json
import pprint
import tiny_json

v0='{"key0":"value0","key1":"value1","key2":"False","key3":"99","key4":"F","key5":"value5","key6":{"key7":{"keyC":"value","key8":"null"},"k":"v"},"key9":"value9","keyA":"X","keyB":"00000000-0000-00000000"}'
v1='{"key0":"value0","key1":"value1","key2":"True","key3":"X","key4":"F","key5":"value5","key6":{"key7":{"name":"name","key8":"null"},"k":"v"},"key9":"value9","keyA":"X","keyB":"00000000-0000-00000000"}'
v2='{"0": "1", "1": "2", "3": "4", "l" : ["0","1","2","3", {"v2key0":"v2v0"}]}'
v3='{"key0":"value0","key1":"value1","key2":"False","key3":"X","key4":"F","key5":"value5","key6":[{"key7":{"name":"name","key8":"null"}},{"tag":{"k":"v"}}],"key9":"value9","keyA":"X","keyB":"00000000-0000-00000000"}'
v4 ='{"name": "John Doe", "age": "30", "address": { "street": "123 Main Street", "city": "Anytown", "state": "CA" } }'
test_vector = [v0,v1,v2,v3,v4]


def test(v):
    d = json.loads(v)
    e = tiny_json.encode(d)
    print('encoding',e)
    keys = tiny_json.templatize(d)
    print(keys)
    t = tiny_json.decode(d,e)
    #print(v)
    #print(json.dumps(t))
    assert json.loads(v)==t

for v in test_vector:
    test(v)
