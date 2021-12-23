class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */
function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null,
): ListNode | null {
  let merged: ListNode | null = null;

  merged = sortList(list1, list2);

  return merged;
}

function sortList(
  list1: ListNode | null,
  list2: ListNode | null,
): ListNode | null {
  if (list1 == null) return list2;

  if (list2 == null) return list1;

  const startList1 = list1.val <= list2.val;

  // const node: ListNode = {
  //   val: startList1 ? list1.val : list2.val,
  //   next: null,
  // };

  const node = new ListNode(startList1 ? list1.val : list2.val, null);

  if (startList1) {
    list1 = list1.next;
  } else {
    list2 = list2.next;
  }

  node.next = sortList(list1, list2);

  return node;
}

export default mergeTwoLists;
