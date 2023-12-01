package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func get_input() []string {
	flag.Parse()
	if len(flag.Args()) > 0 {
		inp_file := flag.Args()[0]
		inp_file = "./" + inp_file
		data, err := readLines(inp_file)

		check(err)
		return data

	} else {
		e := "Missing parameter \"File\", exiting..."
		fmt.Println(e)
		panic(e)
	}
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func str_to_int(inp string) int {
	i, err := strconv.Atoi(inp)
	if err != nil {
		panic(err)
	}
	return i
}

func p1(inp []string) {
	var digits []int
	for _, line := range inp {
		re := regexp.MustCompile("[0-9]")
		res := re.FindAllString(line, -1)
		first := res[0]
		last := res[len(res)-1]
		digits = append(digits, str_to_int(first+last))
	}

	res := 0
	for _, d := range digits {
		res = res + d
		fmt.Println(d)
	}
	fmt.Println(res)

}

func main() {
	inp := get_input()
	fmt.Println("INPUT:")
	fmt.Println(inp)
	//fmt.Println("Part 1:")
	//p1(inp)

}
