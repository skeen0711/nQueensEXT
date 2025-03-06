package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os/exec"
)

type SolveResponse struct {
	Solutions [][][]string `json:"solutions"`
}

func solveHandler(w http.ResponseWriter, r *http.Request) {
	n := r.URL.Query().Get("n")
	preplaced := r.URL.Query().Get("preplaced") // e.g., "0,1"
	log.Printf("Received request: n=%s, preplaced=%s", n, preplaced)

	var args []string
	args = append(args, "../src/main.py", n)
	if preplaced != "" {
		args = append(args, preplaced) // Pass as-is, e.g., "0,1"
	}

	log.Println("Running Python solver...")
	cmd := exec.Command("python3", args...)
	output, err := cmd.CombinedOutput()
	if err != nil {
		log.Printf("Python error: %v, output: %s", err, string(output))
		http.Error(w, "Solver failed: "+err.Error()+", output: "+string(output), http.StatusInternalServerError)
		return
	}
	log.Printf("Python output: %s", string(output))

	log.Println("Parsing Python output...")
	solutions, err := parsePythonOutput(output)
	if err != nil {
		log.Printf("Parse error: %v", err)
		http.Error(w, "Failed to parse solver output: "+err.Error(), http.StatusInternalServerError)
		return
	}
	log.Printf("Returning %d solutions", len(solutions))
	json.NewEncoder(w).Encode(SolveResponse{Solutions: solutions})
}

func parsePythonOutput(output []byte) ([][][]string, error) {
	var solutions [][][]string
	err := json.Unmarshal(output, &solutions)
	return solutions, err
}

func main() {
	http.HandleFunc("/solve", solveHandler)
	srv := &http.Server{Addr: ":8080"}
	go func() {
		log.Fatal(srv.ListenAndServe())
	}()
	log.Println("Server running on :8080, press Ctrl+C to stop")
	<-make(chan struct{}) // Wait forever until interrupted
}
