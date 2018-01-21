"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if len(intervals) < 2:
        return intervals
    intervals.sort()
    changes = False
    b = []
    i = 0
    while i < len(intervals):
        if i == len(intervals) - 1:
            b.append(intervals[i])
            i += 1
        else:
            if intervals[i][1] >= intervals[i + 1][0]:
                b.append([intervals[i][0], max(intervals[i][1], intervals[i + 1][1])])
                i += 1
                changes = True
            else:
                b.append(intervals[i])
            i += 1

    while changes:
        changes = False
        b.sort()
        intervals = b
        b = []
        i = 0
        while i < len(intervals):
            if i == len(intervals) - 1:
                b.append(intervals[i])
                i += 1
            else:
                if intervals[i][1] >= intervals[i + 1][0]:
                    b.append([intervals[i][0], max(intervals[i][1], intervals[i + 1][1])])
                    i += 1
                    changes = True
                else:
                    b.append(intervals[i])
                i += 1

    if len(b) > 0:
        return b
    else:
        return intervals

def mergeEff(intervals):
	if len(intervals) is 0:
		return []
	intervals.sort()
	res = [intervals[0]]
	for interval in intervals[1:]:
		if res[-1][1] < interval[0]:
			res.append(interval)
		else:
			res[-1][1] = max(res[-1][1], interval[1])
	return res

def main():
    print mergeEff([[1,4],[0,4]])

if __name__ == '__main__':
    main()
