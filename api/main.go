package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os/exec"
	"strings"
)

type SolveResponse struct {
	Solutions [][][]string `json:"solutions"`
}

func solveHandler(w http.ResponseWriter, r *http.Request) {
	n := r.URL.Query().Get("n")
	preplaced := r.URL.Query().Get("preplaced") // e.g., "0,1"

	// Run Python solver
	cmd := exec.Command("python3", "../src/main.py", n, preplaced)
	output, err := cmd.Output()
	if err != nil {
		http.Error(w, "Solver failed: "+err.Error(), http.StatusInternalServerError)
		return
	}

	// Parse output (assuming Python prints JSON or a format you can convert)
	// For now, mock a response based on console output
	solutions := parsePythonOutput(string(output))
	json.NewEncoder(w).Encode(SolveResponse{Solutions: solutions})
}

func parsePythonOutput(output string) [][][]string {
	// Placeholder: Convert Python's printed boards to 2D arrays
	// You'll need to modify main.py to output JSON or a parseable format
	lines := strings.Split(output, "\n")
	var solutions [][][]string
	// Logic to group lines into boards and solutions (TBD based on Python output)
	return solutions
}

func main() {
	http.HandleFunc("/solve", solveHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
