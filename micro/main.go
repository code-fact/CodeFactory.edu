package main

import (
	"fmt"
	"net/http"
)

var port = ":8000"

func home(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "10th will we tough")
}

func index(w http.ResponseWriter, r *http.Request) {
	switch r.URL.Path {
	case "/famg":
		home(w, r)
	default:
		fmt.Fprint(w, "11th will be practise for 12th")
	}
}

func main() {
	http.HandleFunc("/", index)
	http.ListenAndServe(port, nil)
}
