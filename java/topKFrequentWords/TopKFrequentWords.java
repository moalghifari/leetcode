// Source : https://leetcode.com/problems/top-k-frequent-words/
// Author : Mochamad Alghifari
// Date   : 2022-10-19

/***************************************************************************************************** 
 *
 * Given an array of strings words and an integer k, return the k most frequent strings.
 * 
 * Return the answer sorted by the frequency from highest to lowest. Sort the words with the same 
 * frequency by their lexicographical order.
 * 
 * Example 1:
 * 
 * Input: words = ["i","love","leetcode","i","love","coding"], k = 2
 * Output: ["i","love"]
 * Explanation: "i" and "love" are the two most frequent words.
 * Note that "i" comes before "love" due to a lower alphabetical order.
 * 
 * Example 2:
 * 
 * Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
 * Output: ["the","is","sunny","day"]
 * Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of 
 * occurrence being 4, 3, 2 and 1 respectively.
 * 
 * Constraints:
 * 
 * 	1 <= words.length <= 500
 * 	1 <= words[i].length <= 10
 * 	words[i] consists of lowercase English letters.
 * 	k is in the range [1, The number of unique words[i]]
 * 
 * Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
 ******************************************************************************************************/

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) {
            map.put(word, map.getOrDefault(word, 0)+1);
        }
        List<Map.Entry<String, Integer>> l = new LinkedList<>();
        for (Map.Entry<String, Integer> e : map.entrySet()) {
            l.add(e);
        }
        Collections.sort(l, new WordComparator());
        List<String> ans = new LinkedList<>();
        for (int i = 0; i <= k - 1; i++) {
            ans.add(l.get(i).getKey());
        }
        return ans;
    }
}

class WordComparator implements Comparator<Map.Entry<String, Integer>> {
    public int compare(Map.Entry<String, Integer> e1, Map.Entry<String, Integer> e2) {
        String word1 = e1.getKey();
        int freq1 = e1.getValue();
        String word2 = e2.getKey();
        int freq2 = e2.getValue();
        if (freq1 != freq2) {
            return freq2 - freq1;
        }
        return word1.compareTo(word2);
    }
}
