package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"time"
)

var path = "../Data/"

// var arraySizes = []int{100, 1000}
var arraySizes = []int{100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000}
var printA = false
var printB = false
var printC = false
var times = 15

// var timesN = 10
var endQ = 15

func csvToArray(_data [][]string, _size int) []int64 {
	var array []int64 = make([]int64, int(_size))
	for i := range array {
		n, err := strconv.ParseInt(_data[i][0], 10, 64)
		if err != nil {
			fmt.Printf("%d of type %T", n, n)
		}
		array[i] = n
	}
	return array
}

func readFile(_size int) []int64 {
	var pathFile = path + strconv.Itoa(_size) + ".csv"
	f, err := os.Open(pathFile)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	csvReader := csv.NewReader(f)
	data, err := csvReader.ReadAll()
	if err != nil {
		log.Fatal(err)
	}
	array := csvToArray(data, _size)
	return array
}

func average(xs []float64) float64 {
	total := 0.0
	for _, v := range xs {
		total += v
	}
	return total / float64(len(xs))
}

func standardDeviation(_num []float64) float64 {
	var mean, sd float64
	mean = average(_num)
	for i := 0; i < len(_num); i++ {
		sd += math.Pow(_num[i]-mean, 2)
	}
	sd = math.Sqrt(sd / float64(len(_num)))
	return sd
}

func sort(_algorithm string, _size int) {
	var processingTime []float64 = make([]float64, int(times))
	var durationFloat float64
	fmt.Printf(_algorithm + " " + strconv.Itoa(times) + " times " + "size " + strconv.Itoa(_size))
	for i := 0; i < times; i++ {
		//time.Sleep(250 * time.Millisecond)
		switch _algorithm {
		case "BubbleSort":
			var array = readFile(_size)
			start := time.Now()
			var newArray = BubbleSort(array)
			if printB == true {
				fmt.Print("\n")
				fmt.Print(newArray)
			}
			duration := time.Since(start)
			durationFloat = float64(duration.Nanoseconds()) / 1000000
			processingTime[i] = durationFloat

		case "TreeSort":
			var array = readFile(_size)
			start := time.Now()
			var newArray = TreeSort(array)
			if printB == true {
				fmt.Print("\n")
				fmt.Print(newArray)
			}
			duration := time.Since(start)
			durationFloat = float64(duration.Nanoseconds()) / 1000000
			processingTime[i] = durationFloat

		case "MergeSort":
			var array = readFile(_size)
			start := time.Now()
			var newArray = MergeSort(array)
			if printB == true {
				fmt.Print("\n")
				fmt.Print(newArray)
			}
			duration := time.Since(start)
			durationFloat = float64(duration.Nanoseconds()) / 1000000
			processingTime[i] = durationFloat

		}
		if printA == true {
			fmt.Print("\n\t#" + strconv.Itoa(i))
			fmt.Print("\n\tMilliseconds: ", durationFloat)
		}
	}
	fmt.Print("\n\tResult: ", processingTime)
	fmt.Print("\n\tAverage: ")
	fmt.Printf("%.5f", average(processingTime))
	fmt.Print("\n")
	fmt.Print("\tStandard Deviation: ")
	fmt.Printf("%.5f", standardDeviation(processingTime))
	fmt.Print("\n")
}

func n_queens(_n int) {
	var processingTime []float64 = make([]float64, int(times))
	var durationFloat float64
	var flag = true
	fmt.Printf("N-queens" + " " + strconv.Itoa(times) + " - " + "size " + strconv.Itoa(_n))
	for i := 0; i < times; i++ {
		board := make([][]bool, _n)
		for i := 0; i < _n; i++ {
			board[i] = make([]bool, _n)
		}
		start := time.Now()
		var outputs [][]int
		SolveN_queens(board, 0, _n, &outputs)
		duration := time.Since(start)
		durationFloat = float64(duration.Nanoseconds()) / 1000000
		processingTime[i] = durationFloat
		if printC == true && flag == true {
			fmt.Print("\n")
			for _, output := range outputs {
				fmt.Println(output)
			}
			flag = false
		}
	}
	fmt.Print("\tResult: ", processingTime)
	fmt.Print("\n\tAverage: ")
	fmt.Printf("%.5f", average(processingTime))
	fmt.Print("\n")
	fmt.Print("\tStandard Deviation: ")
	fmt.Printf("%.5f", standardDeviation(processingTime))
	fmt.Print("\n")
}

func main() {
	/*
		for i := 0; i < len(arraySizes); i++ {
			//for i := 0; i < 2; i++ {
			sort("BubbleSort", arraySizes[i])
		}

		for i := 0; i < len(arraySizes); i++ {
			sort("TreeSort", arraySizes[i])
		}

		for i := 0; i < len(arraySizes); i++ {
			sort("MergeSort", arraySizes[i])
		}
	*/

	for i := 0; i < len(arraySizes); i++ {
		sort("BubbleSort", arraySizes[i])
		sort("TreeSort", arraySizes[i])
		sort("MergeSort", arraySizes[i])
	}

	for i := 4; i <= endQ; i++ {
		n_queens(i)
	}

	/*
		a := []int64{1, 3, 6, 2, 7, 4, 5, 10, 8, 9}
		a = MergeSort(a)
		fmt.Println(a)
	*/

}
