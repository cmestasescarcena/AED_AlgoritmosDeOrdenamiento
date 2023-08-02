package main

// Codigo obtenido
// https://www.tutorialspoint.com/bubble-sort-in-go-lang

func BubbleSort(_array []int64) []int64 {
	for i := 0; i < len(_array)-1; i++ {
		for j := 0; j < len(_array)-i-1; j++ {
			if _array[j] > _array[j+1] {
				_array[j], _array[j+1] = _array[j+1], _array[j]
			}
		}
	}
	return _array
}
