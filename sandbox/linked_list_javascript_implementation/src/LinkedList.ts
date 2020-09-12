export class LinkedList {
  head: LinkedListNode;
  length: number;
  static fromValues: (...values: any[]) => LinkedList;

  constructor() {
    this.head = null;
    this.length = 0;
  }

  insertAtHead(payload: any): void {
    const newNode = new LinkedListNode(payload, this.head);
    this.head = newNode;
    this.length++;
  }

  insertAtIndex(index: number, value: any) {
    if (index === 0) return this.insertAtHead(value);

    const prev = this.getByIndex(index - 1);
    if (prev == null) return null;

    prev.next = new LinkedListNode(value, prev.next);
    this.length++;
  }

  getByIndex(index: number): LinkedListNode | null {
    if (index < 0 || index >= this.length) return null;

    let current = this.head;
    for (let i = 0; i < index; i++) {
      current = current.next;
    }
    return current;
  }

  removeHead(): LinkedListNode | null {
    const node = this.head;
    this.head = this.head.next;
    this.length--;
    return node;
  }

  removeAtIndex(index: number): LinkedListNode | null {
    if (index === 0) return this.removeHead();

    const prev = this.getByIndex(index - 1);
    if (prev == null) return null;

    const node = prev.next;
    prev.next = node.next;
    this.length--;
    return node;
  }

  print(): void {
    let output = "";

    let current = this.head;

    while (current) {
      output += `${current.value} -> `;
      current = current.next;
    }

    console.log(`${output}null`);
  }
}

class LinkedListNode {
  value: any;
  next?: LinkedListNode;
  constructor(value: any, next: LinkedListNode = null) {
    this.value = value;
    this.next = next;
  }
}

// Helper Functions
LinkedList.fromValues = (...values) => {
  const ll = new LinkedList();
  for (let i = values.length - 1; i >= 0; i--) {
    ll.insertAtHead(values[i]);
  }
  return ll;
};
