"""
Description
中文
English
Given a set of strings which just has lower case letters and a target string, output all the strings for each the edit distance with the target no greater than k.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Have you met this question in a real interview?
Example
Given words = ["abc", "abd", "abcd", "adc"] and target = "ac", k = 1
Return ["abc", "adc"]


"""

# -*- coding: UTF-8 -*-


def getKdistanceWord( word_list, target, k):
    #生成trie树
    nodes = {}
    for word in word_list:
        node = nodes
        for i in range(len(word)):
            if word[i] not in node:
                node[word[i]] = {\
            node = node[word[i]]
            if i == len(word)-1:
                node['#'] = 1
            print nodes

    # 构建递归式
    # prev_dp 为前一列dp结果, w为当前的字母，node 当前字典树中的节点
    def helper(prev_dp, w, node, target, prev_str, result):
        print target
        print "prev_str: ", prev_str
        print "prev_dp: ", prev_dp
        # prev_
        curr_dp = [prev_dp[0] + 1]
        for i in range(len(target)):
            if target[i] == w:
                curr_dp.append(prev_dp[i])
            else:
                # prev/curr决定j
                # i决定i
                # 对于传统的edit distance: [i+1][j+1]=min([i][j+1]+1, [i+1][j]+1, [i][j]+1)
                # 分别表示delete s1[i+1], delete s2[j+1], replace
                # <x>_dp[<y>]  x=(prev|curr)=j, y=i
                # prev_dp[i]+1 = s[i][j]+1   replace
                # curr_dp[i]+1 = s[i][j+1]+1  delete s1
                # prev_dp[i+1]+1 = s[i+1][j]+1  delete s2
                min_dis = min(prev_dp[i]+1, curr_dp[i]+1, prev_dp[i+1]+1)
                # curr_dp[i+1]=s[i+1][j+1]
                curr_dp.append(min_dis)
        if curr_dp[-1] <= k and '#' in node:
            result.append(prev_str+w)
        print "repv_str+w", prev_str+w
        for nxt in node:
            if nxt != '#':
                helper(curr_dp, nxt, node[nxt], target, prev_str+w, result)
    result = []
    for key in nodes:
        # 初始化第一列
        prev_dp = [i for i in range(len(target) + 1)]
        helper(prev_dp, key, nodes[key], target, "", result)

    return result



print  getKdistanceWord(["abc", "abd", "abcd", "adc"], "ac", 1)
