package main

type tree struct {
	value       int64
	left, right *tree
}

// appendValues appends the elements of t to values in order
// and returns the resulting slice.
func appendValues(values []int64, t *tree) []int64 {
	if t != nil {
		values = appendValues(values, t.left)
		values = append(values, t.value)
		values = appendValues(values, t.right)
	}
	return values
}

func add(t *tree, value int64) *tree {
	if t == nil {
		// Equivalent to return &tree{value: value}.
		t = new(tree)
		t.value = value
		return t
	}
	if value < t.value {
		t.left = add(t.left, value)
	} else {
		t.right = add(t.right, value)
	}
	return t
}

// Sort sorts values in place.
func TreeSort(values []int64) []int64 {
	var root *tree
	for _, v := range values {
		root = add(root, v)
	}
	appendValues(values[:0], root)
	return values
}
