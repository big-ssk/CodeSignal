# https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso

import ipaddress


def is_ipv4_address_v1(s):
    s = s.strip('.').split('.')
    not_nums = [x for x in s if not x.isnumeric() or (len(x) > 1 and x.startswith('0'))]
    if not_nums:
        return False
    out_of_range = [x for x in s if int(x) not in range(256)]
    return False if out_of_range or len(s) != 4 else True


def is_ipv4_address_v2(s):
    s = s.split('.')
    return len(s) == 4 and all(x.isdigit() and 0 <= int(x) < 256 for x in s)


def is_ipv4_address_v3(s):
    try:
        ipaddress.ip_address(s)
    except ValueError:
        return False
    return True
