package main

import (
    "bufio"
    "os"
    "strings"
)

var filePath = "./input.txt"
var testData = []string{

}

func ReadFileToList(filePath string) ([]string) {
    file, err := os.Open(filePath)
    if err != nil {
        return nil
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, strings.TrimSpace(scanner.Text()))
    }
    return lines 
}

func GetInputDataAsString(test bool) (string) {
    if test {
        return strings.Join(testData, "\n")
    }

    data, err := os.ReadFile(filePath)
    if err != nil {
        return ""
    }
    return string(data)
}

func GetInputDataAsList(test bool) ([]string) {
    if test {
        return testData
    }
    return ReadFileToList(filePath)
}