/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode second = slow.next;
        slow.next = null;
        ListNode first = head;
        ListNode prev = null; // for reverse second part;

        while (second != null){
            ListNode tmp = second.next;
            second.next = prev;
            prev = second;
            second = tmp;
        }

        // merge reversed second and first

        while (prev != null){
            ListNode tmp1 = first.next;
            ListNode tmp2 = prev.next;

            first.next = prev;
            prev.next = tmp1;

            first = tmp1;
            prev =  tmp2;
        }
     
    }
}