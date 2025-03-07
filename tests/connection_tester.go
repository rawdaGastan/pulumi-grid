package test

import (
	"net"
	"time"
)

const devNetwork = "dev"
const mainNetwork = "main"

func testConnection(addr string, port string) bool {
	for t := time.Now(); time.Since(t) < 3*time.Minute; {
		con, err := net.DialTimeout("tcp", net.JoinHostPort(addr, port), time.Second*12)
		if err == nil {
			con.Close()
			return true
		}
	}
	return false
}
