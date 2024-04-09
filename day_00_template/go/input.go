package main

import (
    "bufio"
    "os"
    "strings"
)

var filePath = "./input.txt"
var testData = []string{}

func ReadFileToList(filePath string) ([]string, error) {
    file, err := os.Open(filePath)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, strings.TrimSpace(scanner.Text()))
    }
    return lines, scanner.Err()
}

func GetInputDataAsString(test bool) (string, error) {
    if test {
        return strings.Join(testData, "\n"), nil
    }

    data, err := os.ReadFile(filePath)
    if err != nil {
        return "", err
    }
    return string(data), nil
}

func GetInputDataAsList(test bool) ([]string, error) {
    if test {
        return testData, nil
    }
    return ReadFileToList(filePath)
}