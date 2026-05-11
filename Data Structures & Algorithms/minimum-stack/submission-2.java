class MinStack {
    private ArrayList<Integer> stack;
    private ArrayList<Integer> minStack; 

    public MinStack() {
        this.stack = new ArrayList<>();
        this.minStack = new ArrayList<>();
    }
    // 1, 2, 0
    // 1, 1, 0
    
    public void push(int val) {
        this.stack.add(val);
        // update minStack
        if (this.minStack.isEmpty()) {
            this.minStack.add(val);
        } else {
            val = Math.min(val, this.minStack.get(this.minStack.size() - 1));
            this.minStack.add(val);
        }
    }
    
    public void pop() {
        this.stack.remove(this.stack.size() - 1);
        this.minStack.remove(this.minStack.size() - 1);
    }
    
    public int top() {
        return this.stack.get(this.stack.size() - 1);
    }
    
    public int getMin() {
        return this.minStack.get(this.minStack.size() - 1);
    }
}
