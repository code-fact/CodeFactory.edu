package main

import (
	"fmt"
	"net/http"
)

var port = ":8000"

func home(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "applphabet")
}

func index(w http.ResponseWriter, r *http.Request) {
	switch r.URL.Path {
	case "/z":
		home(w, r)
	default:
		fmt.Fprint(w, "APPleaLPHABET")
	}
}

func main() {
	http.HandleFunc("/", index)
	http.ListenAndServe(port, nil)
}
