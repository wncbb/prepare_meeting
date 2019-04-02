from math import log,floor

def ipToVal(ip):
    ip = ip.split(".")
    val = 0
    for x in ip:
        val = (val << 8) + int(x)
    return val


def ValToIp(val):
    ip, i = ["0"] * 4, 3
    while val:
        ip[i] = str(val % (1 << 8))
        val /= (1 << 8)
        i -= 1
    return ".".join(ip)


def range2cidr(start, end):
    if not start or not end or start.count('.') != 3 or end.count('.') != 3:
        return None
    start, end = ipToVal(start), ipToVal(end)
    if start > end:
        return None
    ans = []
    while start <= end:
        firstOne = start & (-start)
        maxMask = 32 - int(log(firstOne, 2))
        maxDiff = 32 - int(floor(log(end - start + 1, 2)))
        maxMask = max(maxMask, maxDiff)
        ip = ValToIp(start)
        ans.append(ip + "/" + str(maxMask))
        start += 2 ** (32 - maxMask)
    return ans



start='10.10.10.1'
stop ='10.10.10.4'
rst=range2cidr(start, stop)
for v in rst:
    print 'rst:', v
